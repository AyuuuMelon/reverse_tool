# encoding: utf-8
# module renderdoc
# from D:\reverse_plugin\renderdoc_src\x64\Release\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class D3D12StreamOutBind(): # skipped bases: <class 'SwigPyObject'>
    """ Describes a binding on the D3D12 stream-out stage. """
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
    def byteOffset(self):
        """
The byte offset in :data:`resourceId` where the buffer view starts in the underlying
buffer.

"""
        pass

    @byteOffset.setter
    def byteOffset(self, value):
        pass

    @property
    def byteSize(self):
        """How many bytes are in this stream-out buffer view."""
        pass

    @byteSize.setter
    def byteSize(self, value):
        pass

    @property
    def resourceId(self):
        """The :class:`ResourceId` of the buffer."""
        pass

    @resourceId.setter
    def resourceId(self, value):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    @property
    def writtenCountByteOffset(self):
        """
The byte offset in :data:`writtenCountResourceId` where the stream-out count will be
written.

"""
        pass

    @writtenCountByteOffset.setter
    def writtenCountByteOffset(self, value):
        pass

    @property
    def writtenCountResourceId(self):
        """The :class:`ResourceId` of the buffer where the written count will be stored."""
        pass

    @writtenCountResourceId.setter
    def writtenCountResourceId(self, value):
        pass


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFE188BDBA0>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.D3D12StreamOutBind' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.D3D12StreamOutBind' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.D3D12StreamOutBind' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.D3D12StreamOutBind' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.D3D12StreamOutBind' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.D3D12StreamOutBind' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.D3D12StreamOutBind' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.D3D12StreamOutBind' objects>, 'resourceId': <attribute 'resourceId' of 'renderdoc.D3D12StreamOutBind' objects>, 'writtenCountResourceId': <attribute 'writtenCountResourceId' of 'renderdoc.D3D12StreamOutBind' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.D3D12StreamOutBind' objects>, 'byteOffset': <attribute 'byteOffset' of 'renderdoc.D3D12StreamOutBind' objects>, 'writtenCountByteOffset': <attribute 'writtenCountByteOffset' of 'renderdoc.D3D12StreamOutBind' objects>, 'byteSize': <attribute 'byteSize' of 'renderdoc.D3D12StreamOutBind' objects>, '__doc__': 'Describes a binding on the D3D12 stream-out stage.'})"


