# encoding: utf-8
# module renderdoc
# from D:\reverse_plugin\renderdoc_src\x64\Release\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class ReplaySupport(__enum.IntEnum):
    """
    How supported a given API is on a particular replay instance.
    
    .. data:: Unsupported
    
      The API is not supported.
    
    .. data:: Supported
    
      The API is fully supported.
    
    .. data:: SuggestRemote
    
      The API is supported locally but the capture indicates it was made on a different type of machine
      so remote replay might be desired.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    SuggestRemote = 2
    """
    The API is supported locally but the capture indicates it was made on a different type of machine
      so remote replay might be desired.
    """

    Supported = 1
    """ The API is fully supported. """

    Unsupported = 0
    """ The API is not supported. """



