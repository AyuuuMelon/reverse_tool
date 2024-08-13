# encoding: utf-8
# module renderdoc
# from D:\reverse_plugin\renderdoc_src\x64\Release\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class ConservativeRaster(__enum.IntEnum):
    """
    The conservative rasterization mode.
    
    .. data:: Disabled
    
      No conservative rasterization, the default rasterization coverage algorithm is used.
    
    .. data:: Underestimate
    
      Fragments will only be generated if the primitive full covers all parts of the pixel, including
      edges and corners.
    
    .. data:: Overestimate
    
      Fragments will be generated if the primitive covers any part of the pixel, including edges and
      corners.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    Disabled = 0
    """ No conservative rasterization, the default rasterization coverage algorithm is used. """

    Overestimate = 2
    """
    Fragments will be generated if the primitive covers any part of the pixel, including edges and
      corners.
    """

    Underestimate = 1
    """
    Fragments will only be generated if the primitive full covers all parts of the pixel, including
      edges and corners.
    """



