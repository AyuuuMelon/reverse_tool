import os
import csv
from fbx import FbxVector4, FbxLayerElement, FbxExporter, FbxVector2, FbxLayerElementNormal
from fbx import FbxManager, FbxScene, FbxMesh, FbxNode
import FbxCommon
import numpy as np


# # 检查 csv_path 是否是一个存在的 CSV 文件
# if not os.path.isfile(csv_path) or not csv_path.endswith(".csv"):
#     print("找不到这个文件：{}".format(csv_path))
# else:
#     # 以 UTF-8 编码打开 csv_path 指向的文件
#     with open(csv_path, encoding='UTF8') as f:
#         # 创建一个 CSV 阅读器来读取打开的文件
#         csv_reader = csv.reader(f)
#         # 将 CSV 阅读器读取的数据转换为一个列表
#         data_list = list(csv_reader)
#         # 打印出列表的前 100 行数据
#         for i in range(min(100, len(data_list))):
#             # print(data_list[i])
#             pass


# def setMeshPointAt(csvList, newMesh, vtxID, vertexID):
#     count = len(csvList)

#     for i in range(1, count):
#         _csv = csvList[i]
#         _vtx = _csv[vtxID]
#         pos = FbxVector4(float(_csv[vertexID]),float(_csv[vertexID+1]),float(_csv[vertexID+2]))
#         # print("第{0}顶点为:{1}".format(str(_vtx),str(pos)))

#         newMesh.SetControlPointAt(pos, i-1)

# 定义一个函数来计算4x4矩阵和向量的乘积
def multiply_matrix_and_vector(matrix, vector):
    result = np.zeros(4)
    for i in range(4):
        for j in range(4):
            result[i] += matrix[i][j] * vector[j]
    return result




# 在你的函数中，对pos进行投影矩阵的逆矩阵变换
def setMeshPointAt(csvList, newMesh, vtxID, vertexID, matrix_list):
    count = len(csvList)
    # 定义投影矩阵
    # projection_matrix = np.array([[1.13, 0, 0, 0],
    #                             [0, 2.32, 0, 0],
    #                             [0, 0, 0, 1],
    #                             [0, 0, 1, 0]])
    projection_matrix = np.array(matrix_list)

    # 计算投影矩阵的逆矩阵
    inverse_projection_matrix = np.linalg.inv(projection_matrix)

    for i in range(1, count):
        _csv = csvList[i]
        _vtx = _csv[vtxID]
        pos = np.array([float(_csv[vertexID]), float(_csv[vertexID+1]), float(_csv[vertexID+2]), 1])
        # 对pos进行投影矩阵的逆矩阵变换
        pos = np.dot(inverse_projection_matrix, pos)
        newMesh.SetControlPointAt(FbxVector4(pos[0], pos[1], pos[2]*float(_csv[vertexID+3])), i-1)

def setMeshPolygon(csvList, newMesh):
    count = len(csvList)
    for i in range(0, int(count/3)):
        # 根据顶点构建面
        newMesh.BeginPolygon(i)
        newMesh.AddPolygon(3*i)
        newMesh.AddPolygon(3*i+1)
        newMesh.AddPolygon(3*i+2)
        newMesh.EndPolygon()


def setMeshUV(csvList, newMesh, uv0ID, vtxID=1, uv1ID=None):
    count = len(csvList)
    uv_layer = newMesh.CreateElementUV("uv0")
    uv_layer.SetMappingMode(FbxCommon.FbxLayerElement.EMappingMode.eByPolygonVertex)
    uv_layer.SetReferenceMode(FbxCommon.FbxLayerElement.EReferenceMode.eIndexToDirect)
    uv_array = uv_layer.GetDirectArray()
    uv_index_array = uv_layer.GetIndexArray()
    uv_array.Resize(count-1)
    uv_index_array.Resize(count-1)
    for i in range(1, count):
        _csv = csvList[i]
        _vtx = _csv[vtxID]
        uv0 = FbxVector2(float(_csv[uv0ID]), float(_csv[uv0ID+1]))
        uv_array.SetAt(i-1, uv0)
        uv_index_array.SetAt(i-1, i-1)


def setMeshUVs(csvList, newMesh: FbxMesh, uvid_list, vtxID=1):
    count = len(csvList)
    
    # 遍历每个 UV ID
    for uv_index, uvID in enumerate(uvid_list):
        uv_layer_name = f"uv{uv_index}"
        uv_layer = newMesh.CreateElementUV(uv_layer_name)
        uv_layer.SetMappingMode(FbxCommon.FbxLayerElement.EMappingMode.eByPolygonVertex)
        uv_layer.SetReferenceMode(FbxCommon.FbxLayerElement.EReferenceMode.eIndexToDirect)
        uv_array = uv_layer.GetDirectArray()
        uv_index_array = uv_layer.GetIndexArray()
        uv_array.Resize(count - 1)
        uv_index_array.Resize(count - 1)
        
        for i in range(1, count):
            _csv = csvList[i]
            _vtx = _csv[vtxID]
            uv = FbxVector2(float(_csv[uvID]), float(_csv[uvID + 1]))
            uv_array.SetAt(i - 1, uv)
            uv_index_array.SetAt(i - 1, i - 1)

# 示例调用
# csvList = [...]  # CSV 数据列表
# newMesh = ...  # 新的网格对象
# uvid_list = [2, 4]  # UV ID 列表，例如 [2, 4] 表示两套 UV
# setMeshUV(csvList, newMesh, uvid_list)

    # Set the second UV channel
    # uv_layer1 = newMesh.CreateElementUV("uv1")
    # uv_layer1.SetMappingMode(FbxCommon.FbxLayerElement.EMappingMode.eByPolygonVertex)
    # uv_layer1.SetReferenceMode(FbxCommon.FbxLayerElement.EReferenceMode.eIndexToDirect)
    # uv_array1 = uv_layer1.GetDirectArray()
    # uv_index_array1 = uv_layer1.GetIndexArray()
    # uv_array1.Resize(count-1)
    # uv_index_array1.Resize(count-1)
    # for i in range(1, count):
    #     _csv = csvList[i]
    #     uv1 = FbxVector2(float(_csv[uv0ID+2]), float(_csv[uv0ID+3]))
    #     uv_array1.SetAt(i-1, uv1)
    #     uv_index_array1.SetAt(i-1, i-1)



def saveScene(pFilename, pFbxManager, pFbxScene, pAsASCII=False):
    exporter = FbxExporter.Create(pFbxManager, '')
    if pAsASCII:
        asciiFormatIndex = getASCIIFormatIndex(pFbxManager)
        isInitialized = exporter.Initialize(pFilename, asciiFormatIndex)
    else:
        isInitialized = exporter.Initialize(pFilename)
    if not isInitialized:
        raise Exception('Exporter failed to initialize. Error returned: ' + str(exporter.GetStatus().GetErrorString()))

    exporter.Export(pFbxScene)
    exporter.Destroy()


def getASCIIFormatIndex(pManager):
    numFormats = pManager.GetIOPluginRegistry().GetWriterFormatCount()
    formatIndex = pManager.GetIOPluginRegistry().GetNativeWriterFormat()
    for i in range(numFormats):
        if pManager.GetIOPluginRegistry().WriterIsFBX(i):
            description = pManager.GetIOPluginRegistry().GetWriterFormatDescription(i)
            if 'ascii' in description:
                formatIndex = i
                break
    return formatIndex


def setMeshNormal(csvList, newMesh, vtxID, normalID):
    count = len(csvList)
    
    normal_layer = newMesh.CreateElementNormal()
    newMesh.RemoveElementNormal(newMesh.GetElementNormal(0))
    # print(dir(FbxCommon.FbxLayerElement.EMappingMode))
    normal_layer.SetMappingMode(FbxCommon.FbxLayerElement.EMappingMode.eByControlPoint)
    normal_layer.SetReferenceMode(FbxCommon.FbxLayerElement.EReferenceMode.eDirect)
    normal_array = normal_layer.GetDirectArray()
    normal_array.Resize(count)
    for i in range(1, count):
        _csv = csvList[i]
        _vtx = _csv[vtxID]
        normal = FbxVector4(float(_csv[normalID]), float(_csv[normalID+1]), float(_csv[normalID+2]))
        newMesh.SetControlPointNormalAt(normal, int(_vtx))
        normal_array.SetAt(int(_vtx), normal)


def csv_to_fbx(csv_path, fbx_path, position_id, normal_id, uv_ids, matrix_list=[]):
    # 检查 csv_path 是否是一个存在的 CSV 文件
    if not os.path.isfile(csv_path) or not csv_path.endswith(".csv"):
        print("找不到这个文件：{}".format(csv_path))
        return

    # # 创建一个 FbxManager
    # manager = FbxManager.Create()
    # # 创建一个 FbxScene
    # scene = FbxScene.Create(manager, "MyScene")

    manager, scene = FbxCommon.InitializeSdkObjects() # 初始化
    # 创建一个 FbxMesh
    mesh = FbxMesh.Create(scene, "MyMesh")
    # 创建一个 FbxNode
    node = FbxNode.Create(scene, "MyNode")
    # 将 mesh 添加到 node
    node.SetNodeAttribute(mesh)
    # 将 node 添加到 scene
    scene.GetRootNode().AddChild(node)

    # 读取 CSV 文件
    with open(csv_path, encoding='UTF8') as f:
        csv_reader = csv.reader(f)
        data_list = list(csv_reader)
        if len(data_list) < 1:
            return

    # 设置 mesh 的顶点、面、UV 和法线
    setMeshPointAt(data_list, mesh, vtxID=1, vertexID=position_id, matrix_list=matrix_list)
    setMeshPolygon(data_list, mesh)
    setMeshUVs(data_list, mesh, uvid_list=uv_ids)
    setMeshNormal(data_list, mesh, vtxID=1, normalID=normal_id)

    # 保存 scene 到 FBX 文件
    saveScene(fbx_path, manager, scene)



# csv_path = r"D:\Projects\Dimension\rdcs\out2_in\5646_out.csv"  # 请替换为你的CSV文件路径
# fbx_path = r"D:\Projects\Dimension\rdcs\out2_in\5646_out.fbx"
# csv_to_fbx(csv_path, fbx_path)

def batch_csv_to_fbx(directory, draw_id_start, draw_id_end, position_id, normal_id, uv_ids, matrix_list=[]):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".csv"):
                file_name = int(os.path.basename(file).replace(".csv", ""))
                if file_name >= draw_id_start and file_name <= draw_id_end:
                    csv_path = os.path.join(root, file)
                    # fbx_path = os.path.splitext(csv_path)[0] + ".fbx"
                    fbx_folder = os.path.join(directory, 'outputs')
                    if not os.path.exists(fbx_folder):
                        os.makedirs(fbx_folder)

                    fbx_path = os.path.join(fbx_folder, str(file_name)+".fbx")
                    print(fbx_path)
                    
                    csv_to_fbx(csv_path, fbx_path, position_id, normal_id, uv_ids, matrix_list=matrix_list)

# 使用示例
# directory = r"D:\Projects\Dimension\rdcs\out2"  # 请替换为你的文件夹路径
# batch_csv_to_fbx(directory)