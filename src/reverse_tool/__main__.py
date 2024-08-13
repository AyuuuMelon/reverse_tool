import os

# from renderdoc import ActionDescription

from .renderdoc_utils import (setup_renderdoc_env,
                              load_capture_with_rd,
                              traverse_print_action,
                              traverse_find_biggest_action,
                              TextureManager,
                              )

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
    import qrenderdoc as qrd
    
    # 为replay初始化renderdoc，按照示例代码应该在使用replay api之前调用
    rd.InitialiseReplay(rd.GlobalEnvironment(), [])
        
    # 加载capture文件
    resources_dir = os.path.join(root_dir, "resources")
    rdc_file_path = os.path.join(resources_dir, "rdr2_human.rdc")
    cap, controller = load_capture_with_rd(rdc_file_path, rd)
    
    # 获取capture文件的structured file，用于获取结构化过的文件信息，如action的名字
    # structured_file = controller.GetStructuredFile()
    texture_manager = TextureManager(controller)
    
    texsave = rd.TextureSave()

    # 4102 - 4133 有child的action
    # 4595 - 4655 衣服模型
    for action in controller.GetRootActions():
        if action.eventId >= 4595 and action.eventId <= 4595:
            controller.SetFrameEvent(action.eventId, True)
            state = controller.GetPipelineState()
            # state.GetReadOnlyResources(rd.ShaderStage.Fragment)
            # used_desc_list = state.GetReadWriteResources(rd.ShaderStage.Fragment)
            
            for output_id in action.outputs: 
                texsave.resourceId = output_id
                if texsave.resourceId == rd.ResourceId.Null():
                    continue
                texture_desc = texture_manager.get_texture(output_id)
                if texture_desc is None:
                    continue
                
                texture_type = texture_desc.type.name
                resouce_id = str(texture_desc.resourceId).split("::")[-1]
                texture_format = texture_desc.format.Name()
                
                filename = f"{texture_type}_{resouce_id}_{texture_format}"
                print(f"Saving images of {filename} at {action.eventId}: {action.GetName(controller.GetStructuredFile())}")

                texsave.mip = 0
                texsave.slice.sliceIndex = 0
                
                # For formats with an alpha channel, preserve it
                # texsave.alpha = rd.AlphaMapping.Preserve
                # texsave.destType = rd.FileType.PNG
                # controller.SaveTexture(texsave, os.path.join(resources_dir, f"{filename}.png"))
                
                texsave.alpha = rd.AlphaMapping.BlendToCheckerboard
                texsave.destType = rd.FileType.JPG
                controller.SaveTexture(texsave, os.path.join(resources_dir, f"{filename}.jpg"))
                

