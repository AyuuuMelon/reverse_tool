# encoding: utf-8
# module renderdoc
# from D:\reverse_plugin\renderdoc_src\x64\Release\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class CullMode(__enum.IntEnum):
    """
    The culling mode for polygons.
    
    .. data:: NoCull
    
      No polygon culling is performed.
    
    .. data:: Front
    
      Front-facing polygons are culled.
    
    .. data:: Back
    
      Back-facing polygons are culled.
    
    .. data:: FrontAndBack
    
      Both front-facing and back-facing polygons are culled.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    Back = 2
    """ Back-facing polygons are culled. """

    Front = 1
    """ Front-facing polygons are culled. """

    FrontAndBack = 3
    """ Both front-facing and back-facing polygons are culled. """

    NoCull = 0
    """ No polygon culling is performed. """



