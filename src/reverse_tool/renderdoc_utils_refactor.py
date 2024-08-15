import os
import sys
import struct
import csv
from contextlib import contextmanager
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    import renderdoc as rd
    
import logging

logging.basicConfig(level=logging.DEBUG,  # 设置日志级别
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # 设置日志格式
                    datefmt='%Y-%m-%d %H:%M:%S',  # 设置日期格式
                    handlers=[
                        # logging.FileHandler('app.log'),  # 将日志输出到文件
                        logging.StreamHandler()  # 将日志输出到控制台
                    ])
logger = logging.getLogger(__name__)

@contextmanager
def import_renderdoc_from(pymodules_dir: str, dll_dir: str):
    sys.path.append(pymodules_dir)
    os.environ["PATH"] = os.pathsep.join([os.environ["PATH"], dll_dir])
    if sys.platform == 'win32' and sys.version_info >= (3, 8):
        os.add_dll_directory(dll_dir)
    
    logging.debug("importing renderdoc from {pymodules_dir}" and {dll_dir})
    import renderdoc
    global rd
    rd = renderdoc
    rd.InitialiseReplay(rd.GlobalEnvironment(), [])
    
    try:
        yield rd
    finally:
        shutdown_renderdoc()
        pass

def shutdown_renderdoc():
    rd.ShutdownReplay()

class MeshData():
    indexOffset = 0
    name = ''

class CaptureManager:
    def __init__(self, filename: str):
        self.filename = filename
        self.cap = None
        self.controller = None
        self.texture_manager = None
        self.mesh_manager = None

    def __enter__(self):
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
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.controller:
            self.controller.Shutdown()
        if self.cap:
            self.cap.Shutdown()

    def save_textures(self, begin_eid: int, end_eid: int, save_dir: str, save_inputs: bool = True, save_outputs: bool = False):
        self.texture_manager.save_textures(begin_eid, end_eid, save_dir, save_inputs, save_outputs)

    def save_mesh_data(self, begin_eid: int, end_eid: int, save_dir: str, save_inputs: bool = True, save_outputs: bool = False):
        self.mesh_manager.save_mesh_data(begin_eid, end_eid, save_dir, save_inputs, save_outputs)

class TextureManager:
    def __init__(self, controller):
        self.controller = controller
        self.textures = controller.GetTextures()
        self.texsave = rd.TextureSave()

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

    def _save_texture_from_desc(self, texture_desc: 'rd.TextureDescription | None', save_dir: str, eid: int):
        if texture_desc is None:
            return
        
        texture_type = texture_desc.type.name
        resouce_id = str(texture_desc.resourceId).split("::")[-1]
        texture_format = texture_desc.format.Name()
        
        file_name = f"{texture_type}_{resouce_id}_{texture_format}"

        self.texsave.mip = 0
        self.texsave.slice.sliceIndex = 0
        
        self.texsave.alpha = rd.AlphaMapping.BlendToCheckerboard
        self.texsave.destType = rd.FileType.JPG
        file_suffix = self.texsave.destType.name.split(".")[-1].lower()
        
        save_dir_with_eid = os.path.join(save_dir, str(eid))
        if not os.path.exists(save_dir_with_eid):
            os.makedirs(save_dir_with_eid)
        texture_save_path = os.path.join(save_dir_with_eid, f"{file_name}.{file_suffix}")
        
        self.controller.SaveTexture(self.texsave, texture_save_path)
        logging.debug(f"Finish saving {file_name}.{file_suffix}")

    def _get_texture_desc_from_id(self, texture_resouce_id):
        self.texsave.resourceId = texture_resouce_id
        if self.texsave.resourceId != rd.ResourceId.Null():
            for texture_desc in self.textures:
                if texture_desc.resourceId == texture_resouce_id:
                    return texture_desc

class MeshManager:
    def __init__(self, controller):
        self.controller = controller

    def get_mesh_inputs(self, action) -> list[MeshData]:
        state = self.controller.GetPipelineState()
        ib = state.GetIBuffer()
        vbs = state.GetVBuffers()
        attrs = state.GetVertexInputs()
        input_attrs = []

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

    def get_indices(self, mesh_attr: MeshData) -> list[int]:
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
        
    def save_mesh_data(self, begin_eid: int, end_eid: int, save_dir: str, save_inputs: bool = False, save_outputs: bool = True):
        for action in self.controller.GetRootActions():
            if begin_eid <= action.eventId <= end_eid:
                eid = action.eventId
                
                if save_inputs:
                    logging.debug(f"Decoding mesh input at {eid}: {action.GetName(self.controller.GetStructuredFile())}")
                    mesh_attrs = self.get_mesh_inputs(action)
                    self.save_single_mesh_data(mesh_attrs, save_dir, eid, is_input=True)
                    logging.debug(f"finish saving mesh input at {eid}")
                if save_outputs:
                    logging.debug(f"Decoding mesh output at {eid}: {action.GetName(self.controller.GetStructuredFile())}")
                    mesh_attrs = self.get_mesh_inputs(action)
                    self.save_single_mesh_data(mesh_attrs, save_dir, eid, is_input=False)
                    logging.debug(f"finish saving mesh output at {eid}")
        
    def save_single_mesh_data(self, mesh_attrs: list[MeshData] | None, save_dir: str, eid: int, is_input: bool):
        if mesh_attrs is None:
            logging.debug(f"Mesh data is None at {eid}")
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
                        data = self.controller.GetBufferData(attr.vertexResourceId, offset, 0)
                        value = self.unpack_data(attr.format, data)
                        indiceArray.extend(value[:attr.format.compCount])
                writer.writerow(indiceArray)

    def unpack_data(self, fmt, data):
        if fmt.Special():
            if fmt.type == rd.ResourceFormatType.R10G10B10A2:
                return self._unpack_r10g10b10a2(data, fmt.compType == rd.CompType.UNorm)

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

        if fmt.compType == rd.CompType.UNorm and fmt.type != rd.ResourceFormatType.R10G10B10A2:
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