# encoding: utf-8
# module renderdoc
# from D:\reverse_plugin\renderdoc_src\x64\Release\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class ResourceUpdateStats(): # skipped bases: <class 'SwigPyObject'>
    """
    Contains the statistics for resource updates in a frame.
    
    .. data:: BucketType
    
      The type of buckets being used. See :class:`BucketRecordType`.
    
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
        """How many function calls were made."""
        pass

    @calls.setter
    def calls(self, value):
        pass

    @property
    def clients(self):
        """How many of :data:`calls` were mapped pointers written by the CPU."""
        pass

    @clients.setter
    def clients(self, value):
        pass

    @property
    def servers(self):
        """How many of :data:`calls` were batched updates written in the command queue."""
        pass

    @servers.setter
    def servers(self, value):
        pass

    @property
    def sizes(self) -> List[int]:
        """
A :class:`bucketed <BucketType>` list over the number of bytes in the update.

:type: List[int]

"""
        pass

    @sizes.setter
    def sizes(self, value: List[int]):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    @property
    def types(self) -> List[int]:
        """
A list with one element for each type in :class:`TextureType`.

The Nth element contains the number of times a resource of that type was updated.

:type: List[int]

"""
        pass

    @types.setter
    def types(self, value: List[int]):
        pass


    BucketCount = 31
    BucketType = 1
    __dict__ = None # (!) real value is "mappingproxy({'BucketType': 1, 'BucketCount': 31, 'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFE188664A0>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.ResourceUpdateStats' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.ResourceUpdateStats' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.ResourceUpdateStats' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.ResourceUpdateStats' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.ResourceUpdateStats' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.ResourceUpdateStats' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.ResourceUpdateStats' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.ResourceUpdateStats' objects>, 'calls': <attribute 'calls' of 'renderdoc.ResourceUpdateStats' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.ResourceUpdateStats' objects>, 'sizes': <attribute 'sizes' of 'renderdoc.ResourceUpdateStats' objects>, 'servers': <attribute 'servers' of 'renderdoc.ResourceUpdateStats' objects>, 'types': <attribute 'types' of 'renderdoc.ResourceUpdateStats' objects>, 'clients': <attribute 'clients' of 'renderdoc.ResourceUpdateStats' objects>, '__doc__': '\\nContains the statistics for resource updates in a frame.\\n\\n.. data:: BucketType\\n\\n  The type of buckets being used. See :class:`BucketRecordType`.\\n\\n.. data:: BucketCount\\n\\n  How many buckets there are in the arrays.\\n\\n'})"


