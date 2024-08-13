# encoding: utf-8
# module renderdoc
# from D:\reverse_plugin\renderdoc_src\x64\Release\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class TextureSampleMapping(): # skipped bases: <class 'SwigPyObject'>
    """
    How to map multisampled textures for saving to non-multisampled file formats.
    
    .. data:: ResolveSamples
    
      Value for :data:`sampleIndex` if the samples should be averaged.
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
    def mapToArray(self):
        """

``True`` if the samples should be mapped to array slices. A multisampled array expands each slice
in-place, so it would be slice 0: sample 0, slice 0: sample 1, slice 1: sample 0, etc.

This then follows the mapping for array slices as with any other array texture. :data:`sampleIndex`
is ignored.

"""
        pass

    @mapToArray.setter
    def mapToArray(self, value):
        pass

    @property
    def sampleIndex(self):
        """

If :data:`mapToArray` is ``False`` this selects which sample should be extracted to treat as a
normal 2D image. If set to :data:`ResolveSamples` then instead there's a default average resolve.

"""
        pass

    @sampleIndex.setter
    def sampleIndex(self, value):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    ResolveSamples = 4294967295
    __dict__ = None # (!) real value is "mappingproxy({'ResolveSamples': 4294967295, 'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFE18852D50>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.TextureSampleMapping' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.TextureSampleMapping' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.TextureSampleMapping' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.TextureSampleMapping' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.TextureSampleMapping' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.TextureSampleMapping' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.TextureSampleMapping' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.TextureSampleMapping' objects>, 'sampleIndex': <attribute 'sampleIndex' of 'renderdoc.TextureSampleMapping' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.TextureSampleMapping' objects>, 'mapToArray': <attribute 'mapToArray' of 'renderdoc.TextureSampleMapping' objects>, '__doc__': '\\nHow to map multisampled textures for saving to non-multisampled file formats.\\n\\n.. data:: ResolveSamples\\n\\n  Value for :data:`sampleIndex` if the samples should be averaged.\\n\\n'})"


