# encoding: utf-8
# module renderdoc
# from D:\reverse_plugin\renderdoc_src\x64\Release\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class LineRaster(__enum.IntEnum):
    """
    The line rasterization mode.
    
    .. data:: Default
    
      Default line rasterization mode as defined by the API specification.
    
    .. data:: Rectangular
    
      Lines are rasterized as rectangles extruded from the line.
    
    .. data:: Bresenham
    
      Lines are rasterized according to the bresenham line algorithm.
    
    .. data:: RectangularSmooth
    
      Lines are rasterized as rectangles extruded from the line with coverage falloff being
      implementation independent.
    
    .. data:: RectangularD3D
    
      Lines are rasterized as rectangles extruded from the line, but with a width of 1.4 according to
      legacy D3D behaviour
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    Bresenham = 2
    """ Lines are rasterized according to the bresenham line algorithm. """

    Default = 0
    """ Default line rasterization mode as defined by the API specification. """

    Rectangular = 1
    """ Lines are rasterized as rectangles extruded from the line. """

    RectangularD3D = 4
    """
    Lines are rasterized as rectangles extruded from the line, but with a width of 1.4 according to
      legacy D3D behaviour
    """

    RectangularSmooth = 3
    """
    Lines are rasterized as rectangles extruded from the line with coverage falloff being
      implementation independent.
    """



