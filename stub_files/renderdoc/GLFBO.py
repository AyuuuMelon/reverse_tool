# encoding: utf-8
# module renderdoc
# from D:\reverse_plugin\renderdoc_src\x64\Release\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .Descriptor import Descriptor

class GLFBO(): # skipped bases: <class 'SwigPyObject'>
    """ Describes the contents of a framebuffer object. """
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
    def colorAttachments(self) -> List[Descriptor]:
        """
The framebuffer color attachments.

:type: List[Descriptor]

"""
        pass

    @colorAttachments.setter
    def colorAttachments(self, value: List[Descriptor]):
        pass

    @property
    def depthAttachment(self) -> Descriptor:
        """
The framebuffer depth attachment.

:type: Descriptor

"""
        pass

    @depthAttachment.setter
    def depthAttachment(self, value: Descriptor):
        pass

    @property
    def drawBuffers(self) -> List[int]:
        """
The draw buffer indices into the :data:`colorAttachments` attachment list.

:type: List[int]

"""
        pass

    @drawBuffers.setter
    def drawBuffers(self, value: List[int]):
        pass

    @property
    def readBuffer(self):
        """The read buffer index in the :data:`colorAttachments` attachment list."""
        pass

    @readBuffer.setter
    def readBuffer(self, value):
        pass

    @property
    def resourceId(self):
        """The :class:`ResourceId` of the framebuffer."""
        pass

    @resourceId.setter
    def resourceId(self, value):
        pass

    @property
    def stencilAttachment(self) -> Descriptor:
        """
The framebuffer stencil attachment.

:type: Descriptor

"""
        pass

    @stencilAttachment.setter
    def stencilAttachment(self, value: Descriptor):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFE18897590>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.GLFBO' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.GLFBO' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.GLFBO' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.GLFBO' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.GLFBO' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.GLFBO' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.GLFBO' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.GLFBO' objects>, 'colorAttachments': <attribute 'colorAttachments' of 'renderdoc.GLFBO' objects>, 'readBuffer': <attribute 'readBuffer' of 'renderdoc.GLFBO' objects>, 'resourceId': <attribute 'resourceId' of 'renderdoc.GLFBO' objects>, 'drawBuffers': <attribute 'drawBuffers' of 'renderdoc.GLFBO' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.GLFBO' objects>, 'depthAttachment': <attribute 'depthAttachment' of 'renderdoc.GLFBO' objects>, 'stencilAttachment': <attribute 'stencilAttachment' of 'renderdoc.GLFBO' objects>, '__doc__': 'Describes the contents of a framebuffer object.'})"


