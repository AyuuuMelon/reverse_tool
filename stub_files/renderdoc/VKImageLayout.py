# encoding: utf-8
# module renderdoc
# from D:\reverse_plugin\renderdoc_src\x64\Release\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class VKImageLayout(): # skipped bases: <class 'SwigPyObject'>
    """ Contains the layout of a range of subresources in an image. """
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
    def baseLayer(self):
        """For 3D textures and texture arrays, the first slice used in the range."""
        pass

    @baseLayer.setter
    def baseLayer(self, value):
        pass

    @property
    def baseMip(self):
        """The first mip level used in the range."""
        pass

    @baseMip.setter
    def baseMip(self, value):
        pass

    @property
    def name(self):
        """The name of the current image state."""
        pass

    @name.setter
    def name(self, value):
        pass

    @property
    def numLayer(self):
        """For 3D textures and texture arrays, the number of array slices in the range."""
        pass

    @numLayer.setter
    def numLayer(self, value):
        pass

    @property
    def numMip(self):
        """The number of mip levels in the range."""
        pass

    @numMip.setter
    def numMip(self, value):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFE18885080>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.VKImageLayout' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.VKImageLayout' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.VKImageLayout' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.VKImageLayout' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.VKImageLayout' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.VKImageLayout' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.VKImageLayout' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.VKImageLayout' objects>, 'name': <attribute 'name' of 'renderdoc.VKImageLayout' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.VKImageLayout' objects>, 'numMip': <attribute 'numMip' of 'renderdoc.VKImageLayout' objects>, 'numLayer': <attribute 'numLayer' of 'renderdoc.VKImageLayout' objects>, 'baseLayer': <attribute 'baseLayer' of 'renderdoc.VKImageLayout' objects>, 'baseMip': <attribute 'baseMip' of 'renderdoc.VKImageLayout' objects>, '__doc__': 'Contains the layout of a range of subresources in an image.'})"


