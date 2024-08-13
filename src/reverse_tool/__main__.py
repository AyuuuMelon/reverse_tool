import os
import sys

# from renderdoc import ActionDescription

from .renderdoc_utils import setup_renderdoc_env, load_capture_with_rd, controller_traverse_action

if __name__ == "__main__":
    # 获取根目录（src文件夹上一层文件夹）
    file_path = os.path.abspath(__file__)
    root_dir = file_path[:file_path.rfind("src")]
    
    # 从renderdoc源码的文件夹中找到的python modules和dll路径，用于import renderdoc
    renderdoc_src_dir = os.path.join(root_dir, "renderdoc_src")
    pymodules_dir = os.path.join(renderdoc_src_dir, "x64", "Release", "pymodules")
    dll_dir = os.path.join(renderdoc_src_dir, "x64", "Release")

    # 设置import需要的相应环境并import renderdoc模块
    setup_renderdoc_env(pymodules_dir, dll_dir)
    import renderdoc as rd
    
    # 加载capture文件
    rdc_file_path = os.path.join(root_dir, "resources", "rdr2_human.rdc")
    cap, controller = load_capture_with_rd(rdc_file_path, rd)

    for action in controller.GetRootActions():
        controller_traverse_action(controller, action, isPrint=True)