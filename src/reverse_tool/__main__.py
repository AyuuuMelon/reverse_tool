import os
from .renderdoc_utils_refactor import (import_renderdoc_from,
                                       CaptureManager,
                                        )

from .fbx_utils import (batch_csv_to_fbx)

from typing import TYPE_CHECKING
from dataclasses import dataclass

@dataclass
class CameraData:
    fov: float
    near_plane: float
    far_plane: float
    width: float
    height: float

def main():
    renderdoc_dir = os.path.abspath(r"..\..\reverse_tool\renderdoc")
    rdc_file_path = r"your\rdc\file\path.rdc"
    export_dir = r"your\export\dir"
    begin_eid = 1423
    end_eid = 1757
            
    with import_renderdoc_from(renderdoc_dir) as rd:  
        if TYPE_CHECKING:
            import renderdoc as rd   
        with CaptureManager(rdc_file_path) as cap:
            cap.save_textures(begin_eid, end_eid, export_dir, save_inputs=True, save_outputs=False)
            cap.save_mesh_data(begin_eid, end_eid, export_dir, save_inputs=False, save_outputs=True)
            
            controller = cap.get_controller()
            postvs = controller.GetPostVSData(0, 0, rd.MeshDataStage.VSOut)
            viewport = controller.GetPipelineState().GetViewport(0)
            camera_data = CameraData(fov=60,
                                     near_plane=postvs.nearPlane,
                                     far_plane=postvs.farPlane,
                                     width=viewport.width,
                                     height=viewport.height
                                     )
            batch_csv_to_fbx(export_dir, begin_eid, end_eid, 2, 0, [6], camera_data=camera_data)
            # batch_csv_to_fbx(export_dir, begin_eid, end_eid, 2, 0, [6], [
            #     [1.03466, 0.00, 0.00, 0.00],
            #     [0.00, -2.41421, 0.00, 0.00],
            #     [0.00, 0.00, 0.0003, -1.00],
            #     [0.00, 0.00, 0.30009, 0.00]
            # ])
    
if __name__ == "__main__":
    main()