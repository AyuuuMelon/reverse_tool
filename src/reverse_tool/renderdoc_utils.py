import os
import sys
import struct
import csv
from types import ModuleType
from typing import TYPE_CHECKING

def setup_renderdoc_env(pymodules_dir: str, dll_dir: str):
    '''添加正确import需要的pymodules和dll的路径
    
    参考自https://renderdoc.org/docs/python_api/examples/renderdoc_intro.html
    '''
    # 将renderdoc的python modules所在的文件夹添加到sys.path，以便正常import
    sys.path.append(pymodules_dir)

    # 提供的python modules只是python wrapper，还需要添加renderdoc的dll路径
    # python3.8以下需要将dll路径添加到系统环境变量
    os.environ["PATH"] = os.pathsep.join([os.environ["PATH"], dll_dir])

    # python3.8以上使用os.add_dll_directory函数添加dll路径
    if sys.platform == 'win32' and sys.version_info >= (3, 8):
        os.add_dll_directory(dll_dir)
        
file_path = os.path.abspath(__file__)
root_dir = file_path[:file_path.rfind("src")]

renderdoc_src_dir = os.path.join(root_dir, "renderdoc_src")
pymodules_dir = os.path.join(renderdoc_src_dir, "x64", "Release", "pymodules")
dll_dir = os.path.join(renderdoc_src_dir, "x64", "Release")

setup_renderdoc_env(pymodules_dir, dll_dir)
import renderdoc as rd

def load_capture(filename: str, rd: ModuleType):
    '''打开一个capture文件
    
    参考自https://renderdoc.org/docs/python_api/examples/renderdoc/iter_actions.html
    '''   
    # 欺骗类型检查器，使其能够正常代码跳转，实际应在使用到之前就应该调用setup_renderdoc_env并import renderdoc as rd
    if TYPE_CHECKING:
        import renderdoc as rd
    
    # 得到一个capture文件的handle
    cap = rd.OpenCaptureFile()
    
    # 打开一个特定的capture文件
    result = cap.OpenFile(filename, '', None)

	# 确保文件成功打开
    if result != rd.ResultCode.Succeeded:
        raise RuntimeError("Couldn't open file: " + str(result))

    # 确保文件可以replay，非.rdc文件不能replay
    if not cap.LocalReplaySupport():
        raise RuntimeError("Capture cannot be replayed")

    # 初始化replay，得到用于获取各种信息的replay self.controller
    result, controller = cap.OpenCapture(rd.ReplayOptions(), None)

    # 确保replay初始化成功
    if result != rd.ResultCode.Succeeded:
        raise RuntimeError("Couldn't initialise replay: " + str(result))

    return cap, controller

def traverse_print_action(action: rd.ActionDescription, structured_file: rd.SDFile, is_print: bool=True):
    '''递归遍历一个action下的所有action，打印出来所有的action的eventId和名字
    
    Args:
        action: 要遍历的action
        structured_file: 用于获取action的名字
        is_print: 是否打印action，默认为True
    
    参考自https://renderdoc.org/docs/python_api/examples/renderdoc/iter_actions.html
    '''
    if is_print:
        print(f"{action.eventId}: {action.GetName(structured_file)}")
        
    for child in action.children:
       traverse_print_action(child, structured_file, is_print)
       
def find_biggest_action(action: rd.ActionDescription):
    '''递归遍历一个action下的所有action，找到顶点数最多的action返回
    
    Args:
        action: 要遍历的action
    '''
    def traverse(action, prev_biggest):
        # 如果当前 action 的顶点数比 prev_biggest 多，更新 prev_biggest
        if prev_biggest is None or action.numIndices > prev_biggest.numIndices:
            prev_biggest = action

        # 递归遍历子 action
        for child in action.children:
            prev_biggest = traverse(child, prev_biggest)

        return prev_biggest
    # 开始递归遍历
    return traverse(action, None)

    # if prev_biggest is None or action.numIndices > prev_biggest.numIndices:
    #     prev_biggest = action
        
    # for child in action.children:
    #     child_biggest = prev_biggest = traverse_find_biggest_action(child, prev_biggest)
    #     if child_biggest.numIndices > prev_biggest.numIndices:
    #         prev_biggest = child_biggest
            
    # return prev_biggest

def traverse_find_biggest_action(prevBiggest, d):
	ret = prevBiggest
	if ret == None or d.numIndices > ret.numIndices:
		ret = d

	for c in d.children:
		biggest = traverse_find_biggest_action(ret, c)

		if biggest.numIndices > ret.numIndices:
			ret = biggest

	return ret

class MeshData(rd.MeshFormat):
    indexOffset = 0
    name = ''

class RenderdocManager():
    '''用于管理renderdoc的replay controller和相关操作，提供了保存纹理、保存mesh数据等功能'''
    def __init__(self, controller: rd.ReplayController, rd: ModuleType):
        self.controller = controller
        self.rd = rd
        self.textures = self.controller.GetTextures()
        self.root_actions = self.controller.GetRootActions()
        self.texsave = self.rd.TextureSave()
        self.structured_file = self.controller.GetStructuredFile()
        # todo: 使用字典存储action，key为eventId，value为action，这样不用都每次遍历所有action
        # self.id_to_action = {action.eventId: action for action in self.actions}
        
    def save_textures(self, begin_eid: int, end_eid: int, save_dir: str, save_inputs: bool=True, save_outputs: bool=False):
        '''保存.rdc文件中eventId在begin_eid和end_eid之间的action的输入和输出纹理(左右都是闭区间)'''
        for action in self.root_actions:
            if action.eventId >= begin_eid and action.eventId <= end_eid:
                self.controller.SetFrameEvent(action.eventId, True)
                state = self.controller.GetPipelineState()
                
                if save_inputs:
                    readonly_descs = state.GetReadOnlyResources(self.rd.ShaderStage.Fragment)
                    for readonly_desc in readonly_descs:
                        input_texture_id = readonly_desc.descriptor.resource
                        texture_desc = self._get_texture_desc_from_id(input_texture_id)
                        self._save_texture_from_desc(texture_desc, save_dir)
                        
                if save_outputs:
                    for output_texture_id in action.outputs: 
                        texture_desc = self._get_texture_desc_from_id(output_texture_id)
                        self._save_texture_from_desc(texture_desc, save_dir)
            
    def find_action_by_eid(self, eid: int):
        '''根据eventId在root actions中找到对应的action'''
        for action in self.root_actions:
            if action.eventId == eid:
                return action
        return None
    
    def _save_texture_from_desc(self, texture_desc: rd.TextureDescription | None, save_dir: str):
        '''根据texture_desc保存纹理'''
        if texture_desc is None:
            return
        texture_type = texture_desc.type.name # e.g. Texture2D
        resouce_id = str(texture_desc.resourceId).split("::")[-1] # e.g. 9360
        texture_format = texture_desc.format.Name() # e.g. BC1_UNORM
        
        file_name = f"{texture_type}_{resouce_id}_{texture_format}" # e.g. Texture2D_9360_BC1_UNORM

        self.texsave.mip = 0
        self.texsave.slice.sliceIndex = 0
        
        self.texsave.alpha = self.rd.AlphaMapping.BlendToCheckerboard
        self.texsave.destType = self.rd.FileType.JPG
        file_suffix = self.texsave.destType.name.split(".")[-1].lower() # e.g. jpg
        texture_save_path = os.path.join(save_dir, f"{file_name}.{file_suffix}")
        self.controller.SaveTexture(self.texsave, texture_save_path)
        print(f"Saving {file_name}.{file_suffix}")

    def _get_texture_desc_from_id(self, texture_resouce_id: "rd.ResourceId"):
        self.texsave.resourceId = texture_resouce_id
        if self.texsave.resourceId != self.rd.ResourceId.Null():
            for texture_desc in self.textures:
                if texture_desc.resourceId == texture_resouce_id:
                    return texture_desc

    def get_mesh_inputs(self, action: rd.ActionDescription):
        '''获取给定action的mesh input信息
        
        该方法为每个顶点的属性创建一个MeshData对象，包含了该属性的信息，如resouceid、offset(偏移)、stride(步幅)等
        '''
        state = self.controller.GetPipelineState()

        ib = state.GetIBuffer() # 索引缓冲区
        vbs = state.GetVBuffers() # 包含所有顶点缓冲区的列表，因为顶点缓冲区保存属性可以是交错式(interleaved)的也可以是分离式(separate)的
        attrs = state.GetVertexInputs() # 当前的顶点属性列表

        input_attrs: list[MeshData] = []

        for attr in attrs:
            
            # We don't handle instance attributes
            if attr.perInstance:
                raise RuntimeError("Instanced properties are not supported!")
            
            input_attr: MeshData = MeshData()
            input_attr.indexResourceId = ib.resourceId    # 索引缓冲区的resouceid，用于唯一标识该缓冲区
            input_attr.indexByteOffset = ib.byteOffset    # 索引缓冲区的偏移量，表示从缓冲区的起始位置到实际数据开始位置的偏移
            input_attr.indexByteStride = ib.byteStride    # 索引缓冲区的步幅，表示每个索引占用的字节数
            input_attr.baseVertex = action.baseVertex     # 基础偏移量，在使用索引绘制时，这个值会被加到每个索引上
            input_attr.indexOffset = action.indexOffset   # 索引的起始偏移个数，指定从哪个索引开始绘制
            input_attr.numIndices = action.numIndices     # 要绘制的索引或者顶点的数量

            # 如果这个draw没有使用索引缓冲区，那么即使绑定了索引缓冲区我们也不处理它的数据，将他的resourceid设置为Null
            if not (action.flags & rd.ActionFlags.Indexed):
                input_attr.indexResourceId = rd.ResourceId.Null()

            # 计算顶点数据在顶点缓冲区中的总字节偏移，是通过 该属性在顶点数据中的偏移量 + 该顶点缓冲区的偏移量 + 顶点偏移量乘以顶点缓冲区的步幅 得到的
            input_attr.vertexByteOffset = attr.byteOffset + vbs[attr.vertexBuffer].byteOffset + action.vertexOffset * vbs[attr.vertexBuffer].byteStride
            
            input_attr.format = attr.format          
            input_attr.vertexResourceId = vbs[attr.vertexBuffer].resourceId    # 顶点缓冲区的resouceid
            input_attr.vertexByteStride = vbs[attr.vertexBuffer].byteStride    # 顶点的步幅，表示每个顶点占用的字节数
            input_attr.name = attr.name                                        # 这个属性的名字，如POSITION、NORMAL、TANGENT0等

            input_attrs.append(input_attr)

        return input_attrs

    def get_indices(self, mesh_attr: MeshData):
        '''获取mesh的索引数据的列表，如果有索引缓冲区，那么从索引缓冲区中获取数据，否则直接返回顶点的索引'''
        # 根据索引缓冲区的步幅确定索引的格式
        indexFormat = 'B'                 # 步幅是1字节，为无符号字节
        if mesh_attr.indexByteStride == 2:
            indexFormat = 'H'             # 步幅是2字节，为无符号短整型
        elif mesh_attr.indexByteStride == 4:
            indexFormat = 'I'             # 步幅是4字节，为无符号整型

        # 把索引数量拼接到indexFormat的前面，表示要unpack的索引数量，struc.unpack_from()需要这样的格式
        indexFormat = str(mesh_attr.numIndices) + indexFormat

        if mesh_attr.indexResourceId != rd.ResourceId.Null():
            # 如果mesh有索引缓冲区，那么从index buffer中获取数据
            # 获取index buffer的数据
            ibdata = self.controller.GetBufferData(mesh_attr.indexResourceId, mesh_attr.indexByteOffset, 0)
            # 计算unpack的偏移量，通过 索引缓冲区的偏移个数 * 索引缓冲区的步幅 计算得到
            offset = mesh_attr.indexOffset * mesh_attr.indexByteStride
            # unpack这些数据，获取一个由所有单个索引数据组成的tuple
            indices = struct.unpack_from(indexFormat, ibdata, offset)
            # 对每个索引加上基础的偏移量
            return [i + mesh_attr.baseVertex for i in indices]
        else:
            # 没有索引缓冲区，那么就是直接绘制的顶点，直接返回顶点的索引即可
            return tuple(range(mesh_attr.numIndices))
        
    def save_mesh_data(self, mesh_attrs: list[MeshData] | None, action: rd.ActionDescription, save_dir: str):
        if mesh_attrs is None:
            print("No mesh data")
            return
        
        save_dir = os.path.join(save_dir, "mesh_data")
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        outPath = f"{save_dir}/{action.eventId}.csv"

        with open(outPath, "w", newline="") as csv_file:
            writer = csv.writer(csv_file)

            # 写入header
            fileheader = ["VTX", "IDX"]
            formatxyzw = [".x", ".y", ".z", ".w"]
            for attr in mesh_attrs:
                if not attr.format.Special():
                    for i in range(attr.format.compCount):
                        fileheader.append(f"{attr.name}{formatxyzw[i]}")
            writer.writerow(fileheader)

            # 写入数据，逐行写入
            indices = self.get_indices(mesh_attrs[0])
            for i, idx in enumerate(indices):
                indiceArray = [i, idx]
                for attr in mesh_attrs:
                    if not attr.format.Special():
                        offset = attr.vertexByteOffset + attr.vertexByteStride * idx
                        data = self.controller.GetBufferData(attr.vertexResourceId, offset, 0)
                        value = self.unpack_data(attr.format, data)
                        indiceArray.extend(value[:attr.format.compCount])
                writer.writerow(indiceArray)

    def print_mesh_data(self, mesh_attrs: list[MeshData] | None):
        if mesh_attrs is None:
            print("No mesh data")
            return
        
        indices = self.get_indices(mesh_attrs[0])

        print("Mesh configuration:")
        for attr in mesh_attrs:
            # e.g. POSITION, NORMAL, TANGENT0...
            print("\t%s:" % attr.name)
            # e.g. ResourceId::82428 / 12 stride, ResourceId::82428 / 4 stride, ResourceId::82428 / 4 stride...
            print("\t\t- vertex: %s / %d stride" % (attr.vertexResourceId,  attr.vertexByteStride))
            # e.g. CompType.Float x 3 @ 0, CompType.Float x 4 @ 171696, CompType.Float x 4 @ 228928...
            print("\t\t- format: %s x %s @ %d" % (attr.format.compType, attr.format.compCount, attr.vertexByteOffset))

        # We'll decode the first three indices making up a triangle
        for i in range(0, 3):
            idx = indices[i]

            print("Vertex %d is index %d:" % (i, idx))

            for attr in mesh_attrs:
                # This is the data we're reading from. This would be good to cache instead of
                # re-fetching for every attribute for every index
                offset = attr.vertexByteOffset + attr.vertexByteStride * idx # 顶点数据在顶点缓冲区中的偏移
                data = self.controller.GetBufferData(attr.vertexResourceId, offset, 0) # 从顶点缓冲区中获取数据

                # Get the value from the data
                value = self.unpack_data(attr.format, data) # 这时format.Name()是类似R8G8B8A8_UNORM这样的信息

                # We don't go into the details of semantic matching here, just print both
                print("\tAttribute '%s': %s" % (attr.name, value))

    def unpack_data(self, fmt: rd.ResourceFormat, data: bytes):
        # We don't handle 'special' formats - typically bit-packed such as 10:10:10:2
        if fmt.Special():
            print("Special!!!!!!!!!!!")
            print("fmt.Name: ", fmt.Name()) # fmt.Name:  R10G10B10A2_UNORM
            print("fmt.compType: ", fmt.compType) # fmt.compType:  CompType.UNorm
            print("fmt.type: ", fmt.type) # fmt.type:  ResourceFormatType.R10G10B10A2
            if fmt.type == rd.ResourceFormatType.R10G10B10A2:
                print("R10G10B10A2!")
                return self._unpack_r10g10b10a2(data, fmt.compType == rd.CompType.UNorm)
            
        #     raise RuntimeError("Packed formats are not supported!")

        formatChars = {}
        #                                 012345678
        formatChars[rd.CompType.UInt]  = "xBHxIxxxL"
        formatChars[rd.CompType.SInt]  = "xbhxixxxl"
        formatChars[rd.CompType.Float] = "xxexfxxxd" # only 2, 4 and 8 are valid

        # These types have identical decodes, but we might post-process them
        formatChars[rd.CompType.UNorm] = formatChars[rd.CompType.UInt]
        formatChars[rd.CompType.UScaled] = formatChars[rd.CompType.UInt]
        formatChars[rd.CompType.SNorm] = formatChars[rd.CompType.SInt]
        formatChars[rd.CompType.SScaled] = formatChars[rd.CompType.SInt]

        # We need to fetch compCount components
        vertexFormat = str(fmt.compCount) + formatChars[fmt.compType][fmt.compByteWidth]

        # Unpack the data
        value = struct.unpack_from(vertexFormat, data, 0)

        # If the format needs post-processing such as normalisation, do that now
        if fmt.compType == rd.CompType.UNorm and fmt.type != rd.ResourceFormatType.R10G10B10A2:
            divisor = float((2 ** (fmt.compByteWidth * 8)) - 1)
            value = tuple(float(i) / divisor for i in value)
        elif fmt.compType == rd.CompType.SNorm:
            maxNeg = -float(2 ** (fmt.compByteWidth * 8)) / 2
            divisor = float(-(maxNeg-1))
            value = tuple((float(i) if (i == maxNeg) else (float(i) / divisor)) for i in value)

        # If the format is BGRA, swap the two components
        if fmt.BGRAOrder():
            value = tuple(value[i] for i in [2, 1, 0, 3])

        return value
    
    def _unpack_r10g10b10a2(self, data: bytes, is_unorm: bool):
        '''解包一个R10G10B10A2格式的数据，官方示例中为了代码简洁，没有处理这种特殊格式，这里补充处理
        
        Args:
            data: 要解包的数据
            is_unorm: 是否是UNORM格式，决定是否每个通道需要归一化到0-1范围
        '''
        # 假设 data 是一个包含打包的 32 位整数的字节对象
        packed_value = int.from_bytes(data[:4], byteorder='little')

        # 使用位掩码和移位操作提取每个通道
        mask_10bit = 0x3FF  # 10 位掩码（二进制：1111111111）
        mask_2bit = 0x3    # 2 位掩码（二进制：11）
        
        r = packed_value & mask_10bit         # 取低10位（红色）
        g = (packed_value >> 10) & mask_10bit # 取中10位（绿色）
        b = (packed_value >> 20) & mask_10bit # 取高10位（蓝色）
        a = (packed_value >> 30) & mask_2bit  # 取最高2位（alpha）

        if is_unorm:
            # 归一化到 0-1 范围
            r = r / 1023.0   # 10位的最大值为1023 = 2^10 - 1
            g = g / 1023.0
            b = b / 1023.0
            a = a / 3.0      # 2位的最大值为3 = 2^2 - 1
        
        return (r, g, b, a)
    
    def get_mesh_outputs(self, postvs):
        output_attrs = []
        posidx = 0

        vs = self.controller.GetPipelineState().GetShaderReflection(rd.ShaderStage.Vertex)

        # Repeat the process, but this time sourcing the data from postvs.
        # Since these are outputs, we iterate over the list of outputs from the
        # vertex shader's reflection data
        for attr in vs.outputSignature:
            # Copy most properties from the postvs struct
            output_attr = MeshData()
            output_attr.indexResourceId = postvs.indexResourceId
            output_attr.indexByteOffset = postvs.indexByteOffset
            output_attr.indexByteStride = postvs.indexByteStride
            output_attr.baseVertex = postvs.baseVertex
            output_attr.indexOffset = 0
            output_attr.numIndices = postvs.numIndices

            # The total offset is the attribute offset from the base of the vertex,
            # as calculated by the stride per index
            output_attr.vertexByteOffset = postvs.vertexByteOffset
            output_attr.vertexResourceId = postvs.vertexResourceId
            output_attr.vertexByteStride = postvs.vertexByteStride

            # Construct a resource format for this element
            output_attr.format = rd.ResourceFormat()
            output_attr.format.compByteWidth = rd.VarTypeByteSize(attr.varType)
            output_attr.format.compCount = attr.compCount
            output_attr.format.compType = rd.VarTypeCompType(attr.varType)
            output_attr.format.type = rd.ResourceFormatType.Regular

            output_attr.name = attr.semanticIdxName if attr.varName == '' else attr.varName

            if attr.systemValue == rd.ShaderBuiltin.Position:
                posidx = len(output_attrs)

            output_attrs.append(output_attr)
            
        # Shuffle the position element to the front
        if posidx > 0:
            pos = output_attrs[posidx]
            del output_attrs[posidx]
            output_attrs.insert(0, pos)

        accumOffset = 0

        for i in range(0, len(output_attrs)):
            output_attrs[i].vertexByteOffset = accumOffset

            # Note that some APIs such as Vulkan will pad the size of the attribute here
            # while others will tightly pack
            fmt = output_attrs[i].format

            accumOffset += (8 if fmt.compByteWidth > 4 else 4) * fmt.compCount
            
        return output_attrs