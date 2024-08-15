from .renderdoc_utils_refactor import (import_renderdoc_from,
                                       CaptureManager,
                                        )

from .fbx_utils import (batch_csv_to_fbx)

def main():
    rdc_file_path = r""
    export_dir = r""
            
    with import_renderdoc_from(r"D:\reverse_tool\renderdoc", r"D:\reverse_tool\renderdoc"):
        with CaptureManager(rdc_file_path) as cap:
            cap.save_textures(4595, 4655, export_dir, save_inputs=True, save_outputs=False)
            cap.save_mesh_data(4595, 4595, export_dir, save_inputs=False, save_outputs=True)

if __name__ == "__main__":
    main()