# encoding: utf-8
# module renderdoc
# from D:\reverse_plugin\renderdoc_src\x64\Release\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class BucketRecordType(__enum.IntEnum):
    """
    The type of bucketing method for recording statistics.
    
    .. data:: Linear
    
      Each bucket contains a fixed number of elements. The highest bucket also accumulates any values
      too high for any of the buckets.
    
    .. data:: Pow2
    
      Each bucket holds twice as many elements as the previous one, with the first bucket containing
      just 1 (bucket index is ``log2(value)``).
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    Linear = 0
    """
    Each bucket contains a fixed number of elements. The highest bucket also accumulates any values
      too high for any of the buckets.
    """

    Pow2 = 1
    """
    Each bucket holds twice as many elements as the previous one, with the first bucket containing
      just 1 (bucket index is ``log2(value)``).
    """



