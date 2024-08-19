import os
import unittest
from reverse_tool.renderdoc_utils import setup_renderdoc_env, load_capture_with_rd

class TestOpenCapture(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 获取根目录（src文件夹上一次文件夹）
        file_path = os.path.abspath(__file__)
        root_dir = file_path[:file_path.rfind("src")]
        cls.resources_dir = os.path.join(root_dir, "resources")

        # 从renderdoc源码的文件夹中找到的python modules和dll路径，用于import renderdoc
        renderdoc_src_dir = os.path.join(root_dir, "renderdoc_src")
        pymodules_dir = os.path.join(renderdoc_src_dir, "x64", "Release", "pymodules")
        dll_dir = os.path.join(renderdoc_src_dir, "x64", "Release")

        setup_renderdoc_env(pymodules_dir, dll_dir)
        global rd
        import renderdoc as rd
    
    def test_open_capture(self):
        rdc_file_path = os.path.join(self.resources_dir, "rdr2_human.rdc")

        # 加载capture文件
        cap, controller =load_capture_with_rd(rdc_file_path, rd)
        self.assertEqual(len(controller.GetRootActions()), 3045)
        
    def test_save_texture(self):
        rdc_file_path = os.path.join(self.resources_dir, "rdr2_human.rdc")
