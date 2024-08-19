import os
import csv
import numpy as np
from fbx import FbxVector4, FbxLayerElement, FbxExporter, FbxVector2
from fbx import FbxManager, FbxScene, FbxMesh, FbxNode
from reverse_tool import FbxCommon
from .debug_utils import timer, logger
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    import renderdoc as rd

def multiply_matrix_and_vector(matrix: np.ndarray, vector: np.ndarray):
    """
    计算4x4矩阵和向量的乘积
    
    Args:
        matrix: 4x4 numpy数组
        vector: 4x1 numpy数组
    
    Returns:
        4x1 numpy数组，表示矩阵和向量的乘积
    """
    return np.dot(matrix, vector)

def set_mesh_point_at(csv_list: list[list[str]], new_mesh: FbxMesh, vertex_id: int,
                      matrix_list: list[list[float]] | None = None):
    """
    设置网格的顶点位置
    
    Args:
        csv_list: CSV数据列表
        new_mesh: FBX网格对象
        vtx_id: 顶点ID在CSV中的列索引
        vertex_id: 顶点坐标在CSV中的起始列索引
        matrix_list: 4x4相机投影矩阵(MVP中的P)
    """
    count = len(csv_list) # 多少行，即多少个顶点
    projection_matrix = np.array(matrix_list)
    inverse_projection_matrix = np.linalg.inv(projection_matrix)

    for i in range(1, count):
        _csv = csv_list[i]
        pos = np.array([float(_csv[vertex_id]), float(_csv[vertex_id+1]), 1, float(_csv[vertex_id+3])])
        pos = np.dot(pos, inverse_projection_matrix)    
        new_mesh.SetControlPointAt(FbxVector4(pos[0], pos[1], pos[2]), i-1)

def set_mesh_polygon(csv_list: list[list[str]], new_mesh: FbxMesh):
    """
    设置网格的多边形
    
    Args:
        csv_list: CSV数据列表
        new_mesh: FBX网格对象
    """
    count = len(csv_list)
    for i in range(0, int(count/3)):
        new_mesh.BeginPolygon(i)
        new_mesh.AddPolygon(3*i)
        new_mesh.AddPolygon(3*i+1)
        new_mesh.AddPolygon(3*i+2)
        new_mesh.EndPolygon()

def set_mesh_uvs(csv_list: list[list[str]], new_mesh: FbxMesh, uvid_list: list[int], vtx_id: int = 1):
    """
    设置网格的UV坐标
    
    Args:
        csv_list: CSV数据列表
        new_mesh: FBX网格对象
        uvid_list: UV坐标在CSV中的列索引列表
        vtx_id: 顶点ID在CSV中的列索引
    """
    count = len(csv_list)
    
    for uv_index, uv_id in enumerate(uvid_list):
        uv_layer_name = f"uv{uv_index}"
        uv_layer = new_mesh.CreateElementUV(uv_layer_name)
        uv_layer.SetMappingMode(FbxCommon.FbxLayerElement.EMappingMode.eByPolygonVertex)
        uv_layer.SetReferenceMode(FbxCommon.FbxLayerElement.EReferenceMode.eIndexToDirect)
        uv_array = uv_layer.GetDirectArray()
        uv_index_array = uv_layer.GetIndexArray()
        uv_array.Resize(count - 1)
        uv_index_array.Resize(count - 1)
        
        for i in range(1, count):
            uv = FbxVector2(float(csv_list[i][uv_id]), float(csv_list[i][uv_id + 1]))
            uv_array.SetAt(i - 1, uv)
            uv_index_array.SetAt(i - 1, i - 1)

def save_scene(p_filename: str, p_fbx_manager: FbxManager, p_fbx_scene: FbxScene, p_as_ascii: bool = False):
    """
    保存FBX场景到文件
    
    Args:
        p_filename: 输出文件名
        p_fbx_manager: FBX管理器
        p_fbx_scene: FBX场景
        p_as_ascii: 是否保存为ASCII格式
    """
    exporter = FbxExporter.Create(p_fbx_manager, '')
    if p_as_ascii:
        ascii_format_index = get_ascii_format_index(p_fbx_manager)
        is_initialized = exporter.Initialize(p_filename, ascii_format_index)
    else:
        is_initialized = exporter.Initialize(p_filename)
    if not is_initialized:
        raise Exception('Exporter failed to initialize. Error returned: ' + str(exporter.GetStatus().GetErrorString()))

    exporter.Export(p_fbx_scene)
    exporter.Destroy()

def get_ascii_format_index(p_manager: FbxManager):
    """
    获取ASCII格式的索引
    
    Args:
        p_manager: FBX管理器
    
    Returns:
        ASCII格式的索引
    """
    num_formats = p_manager.GetIOPluginRegistry().GetWriterFormatCount()
    format_index = p_manager.GetIOPluginRegistry().GetNativeWriterFormat()
    for i in range(num_formats):
        if p_manager.GetIOPluginRegistry().WriterIsFBX(i):
            description = p_manager.GetIOPluginRegistry().GetWriterFormatDescription(i)
            if 'ascii' in description:
                format_index = i
                break
    return format_index

def set_mesh_normal(csv_list: list[list[str]], new_mesh: FbxMesh, vtx_id: int, normal_id: int | None = None):
    """
    设置网格的法线
    
    Args:
        csv_list: CSV数据列表
        new_mesh: FBX网格对象
        vtx_id: 顶点ID在CSV中的列索引
        normal_id: 法线坐标在CSV中的起始列索引
    """
    if normal_id == 0:
        logger.debug("No normal data id provided")
        return
    
    count = len(csv_list)
    
    normal_layer = new_mesh.CreateElementNormal()
    new_mesh.RemoveElementNormal(new_mesh.GetElementNormal(0))
    normal_layer.SetMappingMode(FbxCommon.FbxLayerElement.EMappingMode.eByControlPoint)
    normal_layer.SetReferenceMode(FbxCommon.FbxLayerElement.EReferenceMode.eDirect)
    normal_array = normal_layer.GetDirectArray()
    normal_array.Resize(count)
    for i in range(1, count):
        _csv = csv_list[i]
        _vtx = _csv[vtx_id]
        normal = FbxVector4(float(_csv[normal_id]), float(_csv[normal_id+1]), float(_csv[normal_id+2]))
        new_mesh.SetControlPointNormalAt(normal, int(_vtx))
        normal_array.SetAt(int(_vtx), normal)

@timer
def csv_to_fbx(csv_path: str, fbx_path: str, position_id: int, normal_id: int, uv_ids: list[int], matrix_list: list[list[float]] = []):
    """
    将CSV文件转换为FBX文件
    
    Args:
        csv_path: 输入CSV文件路径
        fbx_path: 输出FBX文件路径
        position_id: 顶点位置在CSV中的起始列索引
        normal_id: 法线在CSV中的起始列索引
        uv_ids: UV坐标在CSV中的列索引列表
        matrix_list: 4x4投影矩阵
    """
    if not os.path.isfile(csv_path) or not csv_path.endswith(".csv"):
        return

    manager, scene = FbxCommon.InitializeSdkObjects()
    mesh = FbxMesh.Create(scene, "MyMesh")
    node = FbxNode.Create(scene, "MyNode")
    node.SetNodeAttribute(mesh)
    scene.GetRootNode().AddChild(node)

    with open(csv_path, encoding='UTF8') as f:
        csv_reader = csv.reader(f)
        data_list = list(csv_reader)
        if len(data_list) < 1:
            return

    set_mesh_point_at(data_list, mesh, vertex_id=position_id, matrix_list=matrix_list)
    set_mesh_polygon(data_list, mesh)
    set_mesh_uvs(data_list, mesh, uvid_list=uv_ids)
    set_mesh_normal(data_list, mesh, vtx_id=1, normal_id=normal_id)

    save_scene(fbx_path, manager, scene)

def batch_csv_to_fbx(directory: str,
                     draw_id_start: int, draw_id_end: int,
                     position_id: int, normal_id: int, uv_ids: list[int],
                     matrix_list: list[list[float]] | None = None,
                     camera_data = None):
    """
    批量处理CSV文件并转换为FBX文件
    
    Args:
        directory: 包含CSV文件的目录
        draw_id_start: 起始绘制ID
        draw_id_end: 结束绘制ID
        position_id: 顶点位置在CSV中的起始列索引
        normal_id: 法线在CSV中的起始列索引
        uv_ids: UV坐标在CSV中的列索引列表
        matrix_list: 4x4投影矩阵
        camera_data: 猜测投影矩阵使用的相机数据
    """
    # renderdoc中还原透视投影矩阵的函数
    # Matrix4f Matrix4f::Perspective(const float degfov, const float N, const float F, const float A)
    # {
    #   const float radfov = degfov * (3.1415926535f / 180.0f);
    #   float S = 1 / tanf(radfov * 0.5f);

    #   float persp[16] = {
    #       S / A,       0.0f,        0.0f,               0.0f,
    #       0.0f,        S,           0.0f,               0.0f,
    #       0.0f,        0.0f,        F / (F - N),        1.0f,
    #       0.0f,        0.0f,        -(F * N) / (F - N), 0.0f,
    #   };

    #   return Matrix4f(persp);
    # }
    if matrix_list is None and camera_data is None:
        logger.error("Matrix list or FOV is required")
        return
    if matrix_list is None and camera_data is not None:
        radfov = camera_data.fov * (3.1415926535 / 180.0)
        S = 1 / np.tan(radfov * 0.5)
        N = camera_data.near_plane
        F = camera_data.far_plane
        A = camera_data.width / camera_data.height
        matrix_list = [
            [S / A,       0.0,        0.0,                0.0],
            [0.0,         S,          0.0,                0.0],
            [0.0,         0.0,        F / (F - N),        1.0],
            [0.0,         0.0,        -(F * N) / (F - N), 0.0]
        ]
        logger.debug(f"camera_data: {camera_data}")
        
    logger.debug(f"Matrix list: {matrix_list}")
        
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".csv"):
                file_name = os.path.basename(file).replace(".csv", "")
                fbx_file_name = ""
                for char in file_name:
                    if char.isdigit():
                        fbx_file_name += char
                if draw_id_start <= int(fbx_file_name) <= draw_id_end:
                    csv_path = os.path.join(root, file)
                    fbx_folder = os.path.join(directory, 'outputs')
                    if not os.path.exists(fbx_folder):
                        os.makedirs(fbx_folder)

                    fbx_path = os.path.join(fbx_folder, f"{fbx_file_name}.fbx")
                    logger.info(f"Converting {file} to {fbx_file_name}.fbx")
                    csv_to_fbx(csv_path, fbx_path, position_id, normal_id, uv_ids, matrix_list=matrix_list)