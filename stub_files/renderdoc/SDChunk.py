# encoding: utf-8
# module renderdoc
# from D:\reverse_plugin\renderdoc_src\x64\Release\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .SDObject import SDObject

class SDChunk(SDObject):
    """ Defines a single structured chunk, which is a :class:`SDObject`. """
    def Duplicate(self) -> 'SDChunk': # real signature unknown; restored from __doc__
        """
        Duplicate()
        
        
        :return: A new deep copy of this chunk, which the caller owns.
        :rtype: SDChunk
        """
        pass

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
    def metadata(self):
        """The :class:`SDChunkMetaData` with the metadata for this chunk."""
        pass

    @metadata.setter
    def metadata(self, value):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFE18892800>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.SDChunk' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.SDChunk' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.SDChunk' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.SDChunk' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.SDChunk' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.SDChunk' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.SDChunk' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.SDChunk' objects>, 'Duplicate': <method 'Duplicate' of 'renderdoc.SDChunk' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.SDChunk' objects>, 'metadata': <attribute 'metadata' of 'renderdoc.SDChunk' objects>, '__doc__': 'Defines a single structured chunk, which is a :class:`SDObject`.'})"


