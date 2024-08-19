import os
import sys
import struct
import csv
from contextlib import contextmanager
from .debug_utils import timer, logger
from typing import TYPE_CHECKING

# 由于使用了比较特殊的方式导入renderdoc模块，所以这里需要使用TYPE_CHECKING来让该文件中的相关代码正常提示和跳转
if TYPE_CHECKING:
    @contextmanager
    def import_renderdoc_from(pymodules_dir: str, dll_dir: str):
        '''该上下文管理器用于导入、初始化并在结束后销毁renderdoc，需要传入renderdoc提供的python模块路径以及dll路径
        这是因为renderdoc的python模块只是一个wrapper，实际的功能是由dll提供的
        
        Args:
            pymodules_dir (str): renderdoc提供的python模块所在文件夹的路径
            dll_dir (str): renderdoc提供的dll所在文件夹的路径
        
        使用方式: with import_renderdoc_from(pymodules_dir, dll_dir) as rd:
        
        现在该管理环境的方式还不完美，虽然该函数内使用了global试图解决该问题，但是依然无法在定义该函数的文件中正常使用rd，
        比如无法在该文件中正常正常写一个继承自renderdoc模块其中的类的类，这是因为python在import一个文件时会执行其中的代码，
        而在正确import renderdoc之前rd是不存在的，所以会报错，目前的解决方式是将需要继承自renderdoc模块中的类的类放在该函数中，
        比如这里的MeshData，虽然由于python的运行机制，实际上不继承程序也能够正常运行，但是官方示例是这么做的，后续也需要找到更好的解决方案
        
        '''
        return rd
    
    import renderdoc as rd
    
    class MeshData(rd.MeshFormat):
        indexOffset = 0
        name = ''
        
if not TYPE_CHECKING:
    @contextmanager
    def import_renderdoc_from(pymodules_dir: str = None, dll_dir: str = None):
        if pymodules_dir is not None and dll_dir is None:
            dll_dir = pymodules_dir
        sys.path.append(pymodules_dir)
        os.environ["PATH"] = os.pathsep.join([os.environ["PATH"], dll_dir])
        if sys.platform == 'win32' and sys.version_info >= (3, 8):
            os.add_dll_directory(dll_dir)
        
        logger.debug("importing renderdoc from {pymodules_dir}" and {dll_dir})
        import renderdoc
        global rd, MeshData
        rd = renderdoc
        rd.InitialiseReplay(rd.GlobalEnvironment(), [])
        
        class MeshData(rd.MeshFormat):
            indexOffset = 0
            name = ''

        try:
            yield rd
        finally:
            shutdown_renderdoc()
            pass

def shutdown_renderdoc():
    rd.ShutdownReplay()

class CaptureManager:
    def __init__(self, filename: str):
        self.filename = filename
        self.cap = None
        self.controller = None
        self.texture_manager = None
        self.mesh_manager = None

    def __enter__(self):
        logger.debug(f"Initializing CaptureManager with {self.filename}")
        self.cap = rd.OpenCaptureFile()
        result = self.cap.OpenFile(self.filename, '', None)
        if result != rd.ResultCode.Succeeded:
            raise RuntimeError(f"Couldn't open file: {result}")
        if not self.cap.LocalReplaySupport():
            raise RuntimeError("Capture cannot be replayed")
        result, controller = self.cap.OpenCapture(rd.ReplayOptions(), None)
        if result != rd.ResultCode.Succeeded:
            raise RuntimeError(f"Couldn't initialize replay: {result}")
        self.controller = controller
        self.texture_manager = TextureManager(self.controller)
        self.mesh_manager = MeshManager(self.controller)
        logger.debug(f"initialized CaptureManager with {self.filename}")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.controller:
            self.controller.Shutdown()
        if self.cap:
            self.cap.Shutdown()
            
    def get_controller(self):
        return self.controller

    def save_textures(self, begin_eid: int, end_eid: int, save_dir: str, save_inputs: bool = True, save_outputs: bool = False):
        self.texture_manager.save_textures(begin_eid, end_eid, save_dir, save_inputs, save_outputs)

    def save_mesh_data(self, begin_eid: int, end_eid: int, save_dir: str, save_inputs: bool = True, save_outputs: bool = False):
        self.mesh_manager.save_mesh_data(begin_eid, end_eid, save_dir, save_inputs, save_outputs)

class TextureManager:
    def __init__(self, controller: "rd.ReplayController"):
        self.controller = controller
        self.textures = controller.GetTextures()
        self.texsave = rd.TextureSave()

    @timer
    def save_textures(self, begin_eid: int, end_eid: int, save_dir: str, save_inputs: bool = True, save_outputs: bool = False):
        for action in self.controller.GetRootActions():
            if begin_eid <= action.eventId <= end_eid:
                self.controller.SetFrameEvent(action.eventId, True)
                state = self.controller.GetPipelineState()
                eid = action.eventId
                
                if save_inputs:
                    readonly_descs = state.GetReadOnlyResources(rd.ShaderStage.Fragment)
                    for readonly_desc in readonly_descs:
                        input_texture_id = readonly_desc.descriptor.resource
                        texture_desc = self._get_texture_desc_from_id(input_texture_id)
                        self._save_texture_from_desc(texture_desc, save_dir, eid)
                        
                if save_outputs:
                    for output_texture_id in action.outputs: 
                        texture_desc = self._get_texture_desc_from_id(output_texture_id)
                        self._save_texture_from_desc(texture_desc, save_dir, eid)

    def _save_texture_from_desc(self, texture_desc: "rd.TextureDescription | None", save_dir: str, eid: int):
        if texture_desc is None:
            return
        
        texture_type = texture_desc.type.name
        resouce_id = str(texture_desc.resourceId).split("::")[-1]
        texture_format = texture_desc.format.Name()
        
        file_name = f"{texture_type}_{resouce_id}_{texture_format}"

        self.texsave.mip = 0
        # Todo: 保存所有的slice
        self.texsave.slice.sliceIndex = 0
        
        self.texsave.alpha = rd.AlphaMapping.BlendToCheckerboard
        self.texsave.destType = rd.FileType.JPG
        file_suffix = self.texsave.destType.name.split(".")[-1].lower()
        
        save_dir_with_eid = os.path.join(save_dir, str(eid))
        if not os.path.exists(save_dir_with_eid):
            os.makedirs(save_dir_with_eid)
        texture_save_path = os.path.join(save_dir_with_eid, f"{file_name}.{file_suffix}")
        
        self.controller.SaveTexture(self.texsave, texture_save_path)
        logger.debug(f"Finish saving {file_name}.{file_suffix}")

    def _get_texture_desc_from_id(self, texture_resouce_id):
        self.texsave.resourceId = texture_resouce_id
        if self.texsave.resourceId != rd.ResourceId.Null():
            for texture_desc in self.textures:
                if texture_desc.resourceId == texture_resouce_id:
                    return texture_desc

class MeshManager:
    def __init__(self, controller: "rd.ReplayController"):
        self.controller = controller
        
    def get_single_mesh_input(self, action):
        state = self.controller.GetPipelineState()
        ib = state.GetIBuffer()
        vbs = state.GetVBuffers()
        attrs = state.GetVertexInputs()
        input_attrs: "list[MeshData]" = []

        for attr in attrs:
            if attr.perInstance:
                raise RuntimeError("Instanced properties are not supported!")
            
            input_attr = MeshData()
            input_attr.indexResourceId = ib.resourceId
            input_attr.indexByteOffset = ib.byteOffset
            input_attr.indexByteStride = ib.byteStride
            input_attr.baseVertex = action.baseVertex
            input_attr.indexOffset = action.indexOffset
            input_attr.numIndices = action.numIndices

            if not (action.flags & rd.ActionFlags.Indexed):
                input_attr.indexResourceId = rd.ResourceId.Null()

            input_attr.vertexByteOffset = attr.byteOffset + vbs[attr.vertexBuffer].byteOffset + action.vertexOffset * vbs[attr.vertexBuffer].byteStride
            
            input_attr.format = attr.format          
            input_attr.vertexResourceId = vbs[attr.vertexBuffer].resourceId
            input_attr.vertexByteStride = vbs[attr.vertexBuffer].byteStride
            input_attr.name = attr.name

            input_attrs.append(input_attr)

        return input_attrs

    # @timer
    def get_single_mesh_output(self, postvs):
        output_attrs: list[MeshData] = []
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

    def get_indices(self, mesh_attr: "MeshData") -> list[int]:
        indexFormat = 'B'
        if mesh_attr.indexByteStride == 2:
            indexFormat = 'H'
        elif mesh_attr.indexByteStride == 4:
            indexFormat = 'I'

        indexFormat = str(mesh_attr.numIndices) + indexFormat

        if mesh_attr.indexResourceId != rd.ResourceId.Null():
            ibdata = self.controller.GetBufferData(mesh_attr.indexResourceId, mesh_attr.indexByteOffset, 0)
            offset = mesh_attr.indexOffset * mesh_attr.indexByteStride
            indices = struct.unpack_from(indexFormat, ibdata, offset)
            return [i + mesh_attr.baseVertex for i in indices]
        else:
            return list(range(mesh_attr.numIndices))
    
    @timer
    def save_mesh_data(self, begin_eid: int, end_eid: int, save_dir: str, save_inputs: bool = False, save_outputs: bool = True):
        for action in self.controller.GetRootActions():
            if begin_eid <= action.eventId <= end_eid:
                self.controller.SetFrameEvent(action.eventId, True)
                state = self.controller.GetPipelineState()
                eid = action.eventId
                
                if save_inputs:
                    logger.debug(f"Decoding mesh input at {eid}: {action.GetName(self.controller.GetStructuredFile())}")
                    mesh_attrs = self.get_single_mesh_input(action)
                    self.save_single_mesh_data(mesh_attrs, save_dir, eid, is_input=True)
                    logger.debug(f"finish saving mesh input at {eid}")
                    
                if save_outputs:
                    logger.debug(f"Decoding mesh output at {eid}: {action.GetName(self.controller.GetStructuredFile())}")
                    postvs = self.controller.GetPostVSData(0, 0, rd.MeshDataStage.VSOut)

                    mesh_attrs = self.get_single_mesh_output(postvs)
                    self.save_single_mesh_data(mesh_attrs, save_dir, eid, is_input=False)
                    logger.debug(f"finish saving mesh output at {eid}")
        
    @timer # 4595 46.5096s, 4600, 9.0270s, 4605, 0.3212s
    def save_single_mesh_data(self, mesh_attrs: "list[MeshData] | None", save_dir: str, eid: int, is_input: bool):
        if mesh_attrs is None:
            logger.debug(f"Mesh data is None at {eid}")
            return
        
        save_dir_with_eid = os.path.join(save_dir, str(eid))
        if not os.path.exists(save_dir_with_eid):
            os.makedirs(save_dir_with_eid)
        if is_input:
            csv_save_path = f"{save_dir_with_eid}/{eid}_input.csv"
        else:
            csv_save_path = f"{save_dir_with_eid}/{eid}_output.csv"

        with open(csv_save_path, "w", newline="") as csv_file:
            writer = csv.writer(csv_file)

            fileheader = ["VTX", "IDX"]
            formatxyzw = [".x", ".y", ".z", ".w"]
            for attr in mesh_attrs:
                if not attr.format.Special():
                    for i in range(attr.format.compCount):
                        fileheader.append(f"{attr.name}{formatxyzw[i]}")
            writer.writerow(fileheader)

            indices = self.get_indices(mesh_attrs[0])
            for i, idx in enumerate(indices):
                indiceArray = [i, idx]
                for attr in mesh_attrs:
                    if not attr.format.Special():
                        offset = attr.vertexByteOffset + attr.vertexByteStride * idx
                        # todo: 即使四位属性都是双精度浮点数( 64 bits )，大小也不会超过 32 bytes 所以这里直接取32，后续还可以优化，提前cache buffer
                        data = self.controller.GetBufferData(attr.vertexResourceId, offset, 32)
                        value = self.unpack_data(attr.format, data)

                        indiceArray.extend(value[:attr.format.compCount])
                writer.writerow(indiceArray)
    
    def unpack_data(self, fmt: "MeshData", data):
        if fmt.Special():
            if fmt.type == rd.ResourceFormatType.R10G10B10A2:
                return self._unpack_r10g10b10a2(data, fmt.compType == rd.CompType.UNorm)
            else:
                logger.debug(f"Unsupported special format: {fmt.type}")

        formatChars = {
            rd.CompType.UInt: "xBHxIxxxL",
            rd.CompType.SInt: "xbhxixxxl",
            rd.CompType.Float: "xxexfxxxd",
            rd.CompType.UNorm: "xBHxIxxxL",
            rd.CompType.UScaled: "xBHxIxxxL",
            rd.CompType.SNorm: "xbhxixxxl",
            rd.CompType.SScaled: "xbhxixxxl"
        }

        vertexFormat = str(fmt.compCount) + formatChars[fmt.compType][fmt.compByteWidth]
        value = struct.unpack_from(vertexFormat, data, 0)

        if fmt.compType == rd.CompType.UNorm and fmt.type:
            divisor = float((2 ** (fmt.compByteWidth * 8)) - 1)
            value = tuple(float(i) / divisor for i in value)
        elif fmt.compType == rd.CompType.SNorm:
            maxNeg = -float(2 ** (fmt.compByteWidth * 8)) / 2
            divisor = float(-(maxNeg-1))
            value = tuple((float(i) if (i == maxNeg) else (float(i) / divisor)) for i in value)

        if fmt.BGRAOrder():
            value = tuple(value[i] for i in [2, 1, 0, 3])

        return value
    
    def _unpack_r10g10b10a2(self, data: bytes, is_unorm: bool):
        packed_value = int.from_bytes(data[:4], byteorder='little')
        mask_10bit = 0x3FF
        mask_2bit = 0x3
        
        r = packed_value & mask_10bit
        g = (packed_value >> 10) & mask_10bit
        b = (packed_value >> 20) & mask_10bit
        a = (packed_value >> 30) & mask_2bit

        if is_unorm:
            r = r / 1023.0
            g = g / 1023.0
            b = b / 1023.0
            a = a / 3.0
        
        return (r, g, b, a)