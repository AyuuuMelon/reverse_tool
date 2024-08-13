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

def load_capture_with_rd(filename: str, rd: ModuleType):
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

    # 初始化replay，得到用于获取各种信息的replay controller
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
    def __init__(self, controller: "rd.ReplayController"):
        self.textures = controller.GetTextures()
        
    def get_texture(self, texture_resouce_id: "rd.ResourceId"):
        for texture in self.textures:
            if texture.resourceId == texture_resouce_id:
                return texture
        return None