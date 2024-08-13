# encoding: utf-8
# module renderdoc
# from D:\reverse_plugin\renderdoc_src\x64\Release\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class ShaderVariableFlags(__enum.IntFlag):
    """
    A set of flags for events that control how a shader/buffer value is interpreted and
    displayed
    
    .. data:: NoFlags
    
      No flags are specified.
    
    .. data:: RowMajorMatrix
    
      This matrix is stored in row-major order in memory, instead of column-major. In RenderDoc values
      are always provided row-major regardless, for consistency of access, but if this flag is not
      present then the original values were in column order in memory, so the data has been transposed.
    
    .. data:: HexDisplay
    
      This value should be displayed using hexadecimal where possible.
    
    .. data:: BinaryDisplay
    
      This value should be displayed using binary where possible.
    
    .. data:: RGBDisplay
    
      This value should be interpreted as an RGB colour for display where possible.
    
    .. data:: R11G11B10
    
      This value should be decoded from a 32-bit integer in R11G11B10 packing format.
    
    .. data:: R10G10B10A2
    
      This value should be decoded from a 32-bit integer in R10G10B10A2 packing format.
    
    .. data:: UNorm
    
      This value should be treated as unsigned normalised floating point values when interpreting.
    
    .. data:: SNorm
    
      This value should be treated as signed normalised floating point values when interpreting.
    
    .. data:: Truncated
    
      This value was truncated when reading - the available range was exhausted.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    BinaryDisplay = 4
    """ This value should be displayed using binary where possible. """

    HexDisplay = 2
    """ This value should be displayed using hexadecimal where possible. """

    NoFlags = 0
    """ No flags are specified. """

    R10G10B10A2 = 32
    """ This value should be decoded from a 32-bit integer in R10G10B10A2 packing format. """

    R11G11B10 = 16
    """ This value should be decoded from a 32-bit integer in R11G11B10 packing format. """

    RGBDisplay = 8
    """ This value should be interpreted as an RGB colour for display where possible. """

    RowMajorMatrix = 1
    """
    This matrix is stored in row-major order in memory, instead of column-major. In RenderDoc values
      are always provided row-major regardless, for consistency of access, but if this flag is not
      present then the original values were in column order in memory, so the data has been transposed.
    """

    SNorm = 128
    """ This value should be treated as signed normalised floating point values when interpreting. """

    Truncated = 256
    """ This value was truncated when reading - the available range was exhausted. """

    UNorm = 64
    """ This value should be treated as unsigned normalised floating point values when interpreting. """



