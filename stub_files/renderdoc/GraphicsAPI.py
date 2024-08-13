# encoding: utf-8
# module renderdoc
# from D:\reverse_plugin\renderdoc_src\x64\Release\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class GraphicsAPI(__enum.IntEnum):
    """
    Identifies a Graphics API.
    
    .. data:: D3D11
    
      Direct3D 11.
    
    .. data:: D3D12
    
      Direct3D 12.
    
    .. data:: OpenGL
    
      OpenGL.
    
    .. data:: Vulkan
    
      Vulkan.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    D3D11 = 0
    """ Direct3D 11. """

    D3D12 = 1
    """ Direct3D 12. """

    OpenGL = 2
    """ OpenGL. """

    Vulkan = 3
    """ Vulkan. """



