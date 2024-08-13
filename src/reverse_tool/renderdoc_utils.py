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
    
    # Open a capture file handle
    cap = rd.OpenCaptureFile()
    
    # Open a particular file - see also OpenBuffer to load from memory
    result = cap.OpenFile(filename, '', None)

	# Make sure the file opened successfully
    if result != rd.ResultCode.Succeeded:
        raise RuntimeError("Couldn't open file: " + str(result))

    # Make sure we can replay
    if not cap.LocalReplaySupport():
        raise RuntimeError("Capture cannot be replayed")

    # Initialise the replay
    result,controller = cap.OpenCapture(rd.ReplayOptions(), None)

    if result != rd.ResultCode.Succeeded:
        raise RuntimeError("Couldn't initialise replay: " + str(result))

    return cap, controller

def controller_traverse_action(controller: "rd.ReplayController", action: "rd.ActionDescription", isPrint: bool = False):
    '''递归遍历一个action下的所有action，打印出来所有的eventId和action的名字
    
    Args:
        controller: 用于获取各种信息
        action: 要遍历的action
        isPrint: 是否打印action的名字，默认为False
    
    参考自https://renderdoc.org/docs/python_api/examples/renderdoc/iter_actions.html
    '''
    if isPrint:
        print(f"{action.eventId}: {action.GetName(controller.GetStructuredFile())}")
        
    for event in action.children:
       controller_traverse_action(controller, event)