from .renderdoc_utils_refactor import (import_renderdoc_from,
                                       CaptureManager,
                                        )

from .fbx_utils import (batch_csv_to_fbx)

def main():
    rdc_file_path = r"D:\reverse_tool\resources\DuneSpiceWars_OpenGL.rdc"
    export_dir = r"D:\reverse_tool\resources"
            
    # with import_renderdoc_from(r"D:\reverse_tool\renderdoc", r"D:\reverse_tool\renderdoc"):
    #     with CaptureManager(rdc_file_path) as cap:
    #         cap.save_textures(1543, 1674, export_dir, save_inputs=True, save_outputs=True)
    #         cap.save_mesh_data(1543, 1674, export_dir, save_inputs=False, save_outputs=True)
    
    batch_csv_to_fbx(export_dir, 1543, 1674, 2, 12, [6], [
        [1, 0, 0, 0],
        [0, 2.5, 0, 0],
        [0, 0, 0, 1],
        [0, 0, 1, 0]
    ])
    

if __name__ == "__main__":
    main()