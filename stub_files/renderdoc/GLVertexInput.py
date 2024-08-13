# encoding: utf-8
# module renderdoc
# from D:\reverse_plugin\renderdoc_src\x64\Release\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .GLVertexAttribute import GLVertexAttribute
from .GLVertexBuffer import GLVertexBuffer

class GLVertexInput(): # skipped bases: <class 'SwigPyObject'>
    """ Describes the setup for fixed-function vertex input fetch. """
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
    def attributes(self) -> List[GLVertexAttribute]:
        """
The vertex attributes.

:type: List[GLVertexAttribute]

"""
        pass

    @attributes.setter
    def attributes(self, value: List[GLVertexAttribute]):
        pass

    @property
    def indexBuffer(self):
        """The :class:`ResourceId` of the index buffer."""
        pass

    @indexBuffer.setter
    def indexBuffer(self, value):
        pass

    @property
    def indexByteStride(self):
        """
The byte width of the index buffer - typically 1, 2 or 4 bytes. It can be 0 for
non-indexed draws.

.. note::
  This does not correspond to a real GL state since the index type is specified per-action in the call
  itself. This is an implicit state derived from the last (or current) action at any given event.

"""
        pass

    @indexByteStride.setter
    def indexByteStride(self, value):
        pass

    @property
    def primitiveRestart(self):
        """``True`` if primitive restart is enabled for strip primitives."""
        pass

    @primitiveRestart.setter
    def primitiveRestart(self, value):
        pass

    @property
    def provokingVertexLast(self):
        """
``True`` if the provoking vertex is the last one in the primitive.

``False`` if the provoking vertex is the first one.

"""
        pass

    @provokingVertexLast.setter
    def provokingVertexLast(self, value):
        pass

    @property
    def restartIndex(self):
        """The index value to use to indicate a strip restart."""
        pass

    @restartIndex.setter
    def restartIndex(self, value):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    @property
    def topology(self):
        """
The byte width of the index buffer - typically 1, 2 or 4 bytes.

.. note::
  This does not correspond to a real GL state since the topology is specified per-action in the call
  itself. This is an implicit state derived from the last (or current) action at any given event.

"""
        pass

    @topology.setter
    def topology(self, value):
        pass

    @property
    def vertexArrayObject(self):
        """The :class:`ResourceId` of the vertex array object that's bound."""
        pass

    @vertexArrayObject.setter
    def vertexArrayObject(self, value):
        pass

    @property
    def vertexBuffers(self) -> List[GLVertexBuffer]:
        """
The vertex buffers.

:type: List[GLVertexBuffer]

"""
        pass

    @vertexBuffers.setter
    def vertexBuffers(self, value: List[GLVertexBuffer]):
        pass


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFE1887E7C0>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.GLVertexInput' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.GLVertexInput' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.GLVertexInput' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.GLVertexInput' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.GLVertexInput' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.GLVertexInput' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.GLVertexInput' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.GLVertexInput' objects>, 'attributes': <attribute 'attributes' of 'renderdoc.GLVertexInput' objects>, 'indexBuffer': <attribute 'indexBuffer' of 'renderdoc.GLVertexInput' objects>, 'primitiveRestart': <attribute 'primitiveRestart' of 'renderdoc.GLVertexInput' objects>, 'vertexBuffers': <attribute 'vertexBuffers' of 'renderdoc.GLVertexInput' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.GLVertexInput' objects>, 'indexByteStride': <attribute 'indexByteStride' of 'renderdoc.GLVertexInput' objects>, 'topology': <attribute 'topology' of 'renderdoc.GLVertexInput' objects>, 'provokingVertexLast': <attribute 'provokingVertexLast' of 'renderdoc.GLVertexInput' objects>, 'restartIndex': <attribute 'restartIndex' of 'renderdoc.GLVertexInput' objects>, 'vertexArrayObject': <attribute 'vertexArrayObject' of 'renderdoc.GLVertexInput' objects>, '__doc__': 'Describes the setup for fixed-function vertex input fetch.'})"


