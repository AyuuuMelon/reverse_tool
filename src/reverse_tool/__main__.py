import os

# from renderdoc import ActionDescription

from .renderdoc_utils import (setup_renderdoc_env,
                              load_capture,
                              traverse_print_action,
                              traverse_find_biggest_action,
                              TextureManager,
                              )

def py_dll_dirs_from_renderdoc_src(root_dir: str):
    '''从renderdoc源码文件夹中找到的python modules和dll路径
    
    Args:
        root_dir: renderdoc源码文件夹的根目录
        
    Returns:
        tuple: (pymodules_dir, dll_dir)
    '''
    renderdoc_src_dir = os.path.join(root_dir, "renderdoc_src")
    pymodules_dir = os.path.join(renderdoc_src_dir, "x64", "Release", "pymodules")
    dll_dir = os.path.join(renderdoc_src_dir, "x64", "Release")
    
    return pymodules_dir, dll_dir

if __name__ == "__main__":
    # 获取根目录（src文件夹上一层文件夹）
    file_path = os.path.abspath(__file__)
    root_dir = file_path[:file_path.rfind("src")]
    
    # 获取renderdoc源码文件夹中的python modules和dll路径
    pymodules_dir, dll_dir = py_dll_dirs_from_renderdoc_src(root_dir)

    # 设置import需要的相应环境并import renderdoc模块
    setup_renderdoc_env(pymodules_dir, dll_dir)
    import renderdoc as rd
    
    # 为replay初始化renderdoc，按照示例代码应该在使用replay api之前调用
    rd.InitialiseReplay(rd.GlobalEnvironment(), [])
        
    # 加载.rdc文件
    resources_dir = os.path.join(root_dir, "resources")
    rdc_file_path = os.path.join(resources_dir, "rdr2_human.rdc")
    cap, controller = load_capture(rdc_file_path, rd)
    
    texture_manager = TextureManager(controller, rd)

    # 4102 - 4133 有child的action
    # 4595 - 4655 衣服模型
    texture_manager.save_textures(4595, 4595, resources_dir, save_inputs=True, save_outputs=False)
    
    
    
    