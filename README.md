# reverse_tool

## 使用方式

```python
    import os
    from .renderdoc_utils_refactor import import_renderdoc_from, CaptureManager
    from .fbx_utils import batch_csv_to_fbx

    renderdoc_dir = os.path.abspath(r"..\..\reverse_tool\renderdoc")
    rdc_file_path = r"your\rdc\file\path.rdc"
    export_dir = r"your\export\dir"
    begin_eid = 0
    end_eid = 1000
    position_id = 2
    normal_id = 0
    uv_ids = [6]
    proj_matrix = [[1.03466, 0.00, 0.00, 0.00],
                   [0.00, -2.41421, 0.00, 0.00],
                   [0.00, 0.00, 0.0003, -1.00],
                   [0.00, 0.00, 0.30009, 0.00]]
            
    with import_renderdoc_from(renderdoc_dir) as rd:
        with CaptureManager(rdc_file_path) as cap:
            cap.save_textures(begin_eid, end_eid, export_dir, save_inputs=True, save_outputs=False)
            cap.save_mesh_data(begin_eid, end_eid, export_dir, save_inputs=False, save_outputs=True)
            
            batch_csv_to_fbx(export_dir, begin_eid, end_eid, position_id, normal_id, uv_ids, proj_matrix)
```

其中保存fbx也可以使用相机fov值

```python
@dataclass
class CameraData:
    fov: float
    near_plane: float
    far_plane: float
    width: float
    height: float


with import_renderdoc_from(renderdoc_dir) as rd:   
    with CaptureManager(rdc_file_path) as cap:
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
```

## 从源码运行

从github下载zip解压或使用git clone该仓库

```powershell
git clone https://github.com/Ziur02/reverse_tool.git
```

### 安装相应版本的python解释器

该项目的renderdoc与fbx均为python3.10版本构建的，所以必须使用python3.10才能够运行

使用`python -V`查看当前python版本

```powershell
PS python -V
Python 3.10.14
```

如果输出为Python 3.10.x，可以正常使用该工具

如果你现在拥有python 3.8即以上的版本，但是现在没有一个合适的管理python版本的工具，可以使用[uv](https://github.com/astral-sh/uv)（这里尝试了一些版本工具，在各种管理工具中，uv是安装起来最方便的，其他或多或少都要使用到pip以外的下载方式或者修改全局变量）

使用pip安装uv

```powershell
pip install uv==0.2.37
```

使用uv安装3.10版本的python解释器

```powershell
uv python install 310
```

### 创建并使用venv

为了更好地管理不同项目的不同的依赖项，建议使用python虚拟环境，这里使用python官方支持的venv创建虚拟环境

对于全局python版本为3.10.x的用户：

```powershell
python -m venv .venv
```

对于uv用户：

```powershell
uv venv --python 310 --python-preference managed 
```

创建venv后，windows用户运行`.venv\Script\activate`即可激活该环境

```powershell
.venv\Scripts\activate
```

### 安装依赖

依赖项在`requirements.txt`，使用pip进行安装

确保该环境中有`pip`

```powershell
python -m ensurepip
```

安装依赖

```powershell
python -m pip install -r .\requirements.txt 
```

### 运行reverse_tool package中的代码

进入src文件夹

```powershell
cd src
```

使用`python -m <package>`就可以执行该`package`中`__main__.py`的代码

```powershell
python -m reverse_tool
```

### 代码提示

该项目使用vscode开发，关于vscode的配置已经放在`.vscode\settrings.json`，在vscode python插件开启的情况下即可正常获取代码提示功能，如果使用其他ide进行开发，需要将`stub_files`文件夹包含在内，这个文件夹内是renderdoc的python模块与fbx python sdk的python存根文件
