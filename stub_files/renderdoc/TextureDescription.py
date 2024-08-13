# encoding: utf-8
# module renderdoc
# from D:\reverse_plugin\renderdoc_src\x64\Release\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .ResourceFormat import ResourceFormat

class TextureDescription(): # skipped bases: <class 'SwigPyObject'>
    """ A description of a texture resource. """
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
    def arraysize(self):
        """How many array elements this texture has, will be at least 1."""
        pass

    @arraysize.setter
    def arraysize(self, value):
        pass

    @property
    def byteSize(self):
        """How many bytes would be used to store this texture and all its mips/slices."""
        pass

    @byteSize.setter
    def byteSize(self, value):
        pass

    @property
    def creationFlags(self):
        """The way this texture will be used in the pipeline."""
        pass

    @creationFlags.setter
    def creationFlags(self, value):
        pass

    @property
    def cubemap(self):
        """``True`` if this texture is used as a cubemap or cubemap array."""
        pass

    @cubemap.setter
    def cubemap(self, value):
        pass

    @property
    def depth(self):
        """The depth of the texture, or 1 if not applicable."""
        pass

    @depth.setter
    def depth(self, value):
        pass

    @property
    def dimension(self):
        """The base dimension of the texture - either 1, 2, or 3."""
        pass

    @dimension.setter
    def dimension(self, value):
        pass

    @property
    def format(self) -> ResourceFormat:
        """
The format of each pixel in the texture.

:type: ResourceFormat

"""
        pass

    @format.setter
    def format(self, value: ResourceFormat):
        pass

    @property
    def height(self):
        """The height of the texture, or 1 if not applicable."""
        pass

    @height.setter
    def height(self, value):
        pass

    @property
    def mips(self):
        """How many mips this texture has, will be at least 1."""
        pass

    @mips.setter
    def mips(self, value):
        pass

    @property
    def msQual(self):
        """The quality setting of this texture, or 0 if not applicable."""
        pass

    @msQual.setter
    def msQual(self, value):
        pass

    @property
    def msSamp(self):
        """How many multisampled samples this texture has, will be at least 1."""
        pass

    @msSamp.setter
    def msSamp(self, value):
        pass

    @property
    def resourceId(self):
        """The unique :class:`ResourceId` that identifies this texture."""
        pass

    @resourceId.setter
    def resourceId(self, value):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    @property
    def type(self):
        """The :class:`TextureType` of the texture."""
        pass

    @type.setter
    def type(self, value):
        pass

    @property
    def width(self):
        """The width of the texture, or length for buffer textures."""
        pass

    @width.setter
    def width(self, value):
        pass


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFE18859090>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.TextureDescription' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.TextureDescription' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.TextureDescription' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.TextureDescription' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.TextureDescription' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.TextureDescription' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.TextureDescription' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.TextureDescription' objects>, 'cubemap': <attribute 'cubemap' of 'renderdoc.TextureDescription' objects>, 'mips': <attribute 'mips' of 'renderdoc.TextureDescription' objects>, 'msSamp': <attribute 'msSamp' of 'renderdoc.TextureDescription' objects>, 'dimension': <attribute 'dimension' of 'renderdoc.TextureDescription' objects>, 'height': <attribute 'height' of 'renderdoc.TextureDescription' objects>, 'creationFlags': <attribute 'creationFlags' of 'renderdoc.TextureDescription' objects>, 'resourceId': <attribute 'resourceId' of 'renderdoc.TextureDescription' objects>, 'format': <attribute 'format' of 'renderdoc.TextureDescription' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.TextureDescription' objects>, 'depth': <attribute 'depth' of 'renderdoc.TextureDescription' objects>, 'width': <attribute 'width' of 'renderdoc.TextureDescription' objects>, 'type': <attribute 'type' of 'renderdoc.TextureDescription' objects>, 'byteSize': <attribute 'byteSize' of 'renderdoc.TextureDescription' objects>, 'msQual': <attribute 'msQual' of 'renderdoc.TextureDescription' objects>, 'arraysize': <attribute 'arraysize' of 'renderdoc.TextureDescription' objects>, '__doc__': 'A description of a texture resource.'})"


