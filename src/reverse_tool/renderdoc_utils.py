import os
import sys
from types import ModuleType
from typing import TYPE_CHECKING

# 欺骗类型检查器，使其能够正常代码跳转，实际应在使用到之前就应该调用setup_renderdoc_env并import renderdoc as rd
if TYPE_CHECKING:
    import renderdoc as rd

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

def load_capture(filename: str, rd: ModuleType):
    '''打开一个capture文件
    
    参考自https://renderdoc.org/docs/python_api/examples/renderdoc/iter_actions.html
    '''   
    
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

def traverse_print_action(action: "rd.ActionDescription", structured_file: "rd.SDFile", is_print: bool=True):
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
       
def traverse_find_biggest_action(action: "rd.ActionDescription", prev_biggest: "rd.ActionDescription"=None):
    '''递归遍历一个action下的所有action，找到顶点数最多的action返回
    
    Args:
        action: 要遍历的action
        prev_biggest: 之前找到的顶点数最多的action，默认为None，用于递归遍历时传递
    '''
    if prev_biggest is None or action.numIndices > prev_biggest.numIndices:
        prev_biggest = action
        
    for child in action.children:
        child_biggest = prev_biggest = traverse_find_biggest_action(child, prev_biggest)
        if child_biggest.numIndices > prev_biggest.numIndices:
            prev_biggest = child_biggest
            
    return prev_biggest

class TextureManager():
    '''用于保存capture文件中的texture'''
    def __init__(self, controller: "rd.ReplayController", rd: ModuleType):
        self.controller = controller
        self.rd = rd
        self.textures = self.controller.GetTextures()
        self.actions = self.controller.GetRootActions()
        self.texsave = self.rd.TextureSave()
        
    def save_textures(self, begin_eid: int, end_eid: int, save_dir: str, save_inputs: bool=True, save_outputs: bool=True):
        for action in self.actions:
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

            
    def _save_texture_from_desc(self, texture_desc: "rd.TextureDescription", save_dir: str):
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
    
    