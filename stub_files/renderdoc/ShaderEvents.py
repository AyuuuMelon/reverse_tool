# encoding: utf-8
# module renderdoc
# from D:\reverse_plugin\renderdoc_src\x64\Release\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class ShaderEvents(__enum.IntFlag):
    """
    A set of flags for events that may occur while debugging a shader
    
    .. data:: NoEvent
    
      No event has occurred.
    
    .. data:: SampleLoadGather
    
      A texture was sampled, loaded or gathered.
    
    .. data:: GeneratedNanOrInf
    
      A floating point operation generated a ``NaN`` or ``infinity`` result.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    GeneratedNanOrInf = 2
    """ A floating point operation generated a ``NaN`` or ``infinity`` result. """

    NoEvent = 0
    """ No event has occurred. """

    SampleLoadGather = 1
    """ A texture was sampled, loaded or gathered. """



