# encoding: utf-8
# module renderdoc
# from D:\reverse_plugin\renderdoc_src\x64\Release\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class DrawcallStats(): # skipped bases: <class 'SwigPyObject'>
    """
    Contains the statistics for draws in a frame.
    
    .. data:: BucketType
    
      The type of buckets being used. See :class:`BucketRecordType`.
    
    .. data:: BucketSize
    
      How many elements each bucket contains.
    
    .. data:: BucketCount
    
      How many buckets there are in the arrays.
    """
    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    @property
    def calls(self):
        """How many draw calls were made."""
        pass

    @calls.setter
    def calls(self, value):
        pass

    @property
    def counts(self) -> List[int]:
        """
A :class:`bucketed <BucketType>` list over the number of instances in the draw.

:type: List[int]

"""
        pass

    @counts.setter
    def counts(self, value: List[int]):
        pass

    @property
    def indirect(self):
        """How many of :data:`calls` were indirect."""
        pass

    @indirect.setter
    def indirect(self, value):
        pass

    @property
    def instanced(self):
        """How many of :data:`calls` were instanced."""
        pass

    @instanced.setter
    def instanced(self, value):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    BucketCount = 16
    BucketSize = 1
    BucketType = 0
    __dict__ = None # (!) real value is "mappingproxy({'BucketType': 0, 'BucketSize': 1, 'BucketCount': 16, 'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFE18849B50>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.DrawcallStats' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.DrawcallStats' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.DrawcallStats' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.DrawcallStats' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.DrawcallStats' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.DrawcallStats' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.DrawcallStats' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.DrawcallStats' objects>, 'calls': <attribute 'calls' of 'renderdoc.DrawcallStats' objects>, 'instanced': <attribute 'instanced' of 'renderdoc.DrawcallStats' objects>, 'indirect': <attribute 'indirect' of 'renderdoc.DrawcallStats' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.DrawcallStats' objects>, 'counts': <attribute 'counts' of 'renderdoc.DrawcallStats' objects>, '__doc__': '\\nContains the statistics for draws in a frame.\\n\\n.. data:: BucketType\\n\\n  The type of buckets being used. See :class:`BucketRecordType`.\\n\\n.. data:: BucketSize\\n\\n  How many elements each bucket contains.\\n\\n.. data:: BucketCount\\n\\n  How many buckets there are in the arrays.\\n\\n'})"


