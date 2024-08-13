# encoding: utf-8
# module qrenderdoc
# from D:\reverse_plugin\renderdoc_src\x64\Release\pymodules\qrenderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class OffsetSizeDisplayMode(__enum.IntEnum):
    """
    The formatting mode used when displaying fields marked as Offsets or Sizes.
    
    .. data:: Auto
    
      The data is displayed as decimal values by default and hexadecimal if above a certain threshold.
    
    .. data:: Decimal
    
      The data is displayed as decimal values.
    
    .. data:: Hexadecimal
    
      The data is displayed as hexadecimal values.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    Auto = 0
    """ The data is displayed as decimal values by default and hexadecimal if above a certain threshold. """

    Count = 3
    Decimal = 1
    """ The data is displayed as decimal values. """

    Hexadecimal = 2
    """ The data is displayed as hexadecimal values. """



