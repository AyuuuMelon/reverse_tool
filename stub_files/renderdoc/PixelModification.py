# encoding: utf-8
# module renderdoc
# from D:\reverse_plugin\renderdoc_src\x64\Release\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .ModificationValue import ModificationValue

class PixelModification(): # skipped bases: <class 'SwigPyObject'>
    """ An attempt to modify a pixel by a particular event. """
    def Passed(self) -> bool: # real signature unknown; restored from __doc__
        """
        Passed()
        
        Determine if this fragment passed all tests and wrote to the texture.
        
        :return: ``True`` if it passed all tests, ``False`` if it failed any.
        :rtype: bool
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
    def backfaceCulled(self):
        """``True`` if the backface culling test eliminated this fragment."""
        pass

    @backfaceCulled.setter
    def backfaceCulled(self, value):
        pass

    @property
    def depthBoundsFailed(self):
        """``True`` if depth bounds clipping eliminated this fragment."""
        pass

    @depthBoundsFailed.setter
    def depthBoundsFailed(self, value):
        pass

    @property
    def depthClipped(self):
        """``True`` if depth near/far clipping eliminated this fragment."""
        pass

    @depthClipped.setter
    def depthClipped(self, value):
        pass

    @property
    def depthTestFailed(self):
        """``True`` if depth testing eliminated this fragment."""
        pass

    @depthTestFailed.setter
    def depthTestFailed(self, value):
        pass

    @property
    def directShaderWrite(self):
        """``True`` if this event came as part of an arbitrary shader write."""
        pass

    @directShaderWrite.setter
    def directShaderWrite(self, value):
        pass

    @property
    def eventId(self):
        """The :data:`eventId <APIEvent.eventId>` where the modification happened."""
        pass

    @eventId.setter
    def eventId(self, value):
        pass

    @property
    def fragIndex(self):
        """
A 0-based index of which fragment this modification corresponds to, in the case that
multiple fragments from a single action wrote to a pixel.

"""
        pass

    @fragIndex.setter
    def fragIndex(self, value):
        pass

    @property
    def postMod(self) -> ModificationValue:
        """
The value of the texture after this fragment ran.

:type: ModificationValue

"""
        pass

    @postMod.setter
    def postMod(self, value: ModificationValue):
        pass

    @property
    def predicationSkipped(self):
        """``True`` if predicated rendering skipped this call."""
        pass

    @predicationSkipped.setter
    def predicationSkipped(self, value):
        pass

    @property
    def preMod(self) -> ModificationValue:
        """
The value of the texture before this fragment ran.

This is valid only for the first fragment if multiple fragments in the same event write to the same
pixel.

:type: ModificationValue

"""
        pass

    @preMod.setter
    def preMod(self, value: ModificationValue):
        pass

    @property
    def primitiveID(self):
        """The primitive that generated this fragment."""
        pass

    @primitiveID.setter
    def primitiveID(self, value):
        pass

    @property
    def sampleMasked(self):
        """``True`` if the sample mask eliminated this fragment."""
        pass

    @sampleMasked.setter
    def sampleMasked(self, value):
        pass

    @property
    def scissorClipped(self):
        """``True`` if scissor clipping eliminated this fragment."""
        pass

    @scissorClipped.setter
    def scissorClipped(self, value):
        pass

    @property
    def shaderDiscarded(self):
        """``True`` if the pixel shader executed a discard on this fragment."""
        pass

    @shaderDiscarded.setter
    def shaderDiscarded(self, value):
        pass

    @property
    def shaderOut(self) -> ModificationValue:
        """
The value that this fragment wrote from the pixel shader.

:type: ModificationValue

"""
        pass

    @shaderOut.setter
    def shaderOut(self, value: ModificationValue):
        pass

    @property
    def stencilTestFailed(self):
        """``True`` if stencil testing eliminated this fragment."""
        pass

    @stencilTestFailed.setter
    def stencilTestFailed(self, value):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    @property
    def unboundPS(self):
        """``True`` if no pixel shader was bound at this event."""
        pass

    @unboundPS.setter
    def unboundPS(self, value):
        pass

    @property
    def viewClipped(self):
        """``True`` if viewport clipping eliminated this fragment."""
        pass

    @viewClipped.setter
    def viewClipped(self, value):
        pass


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFE18870E60>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.PixelModification' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.PixelModification' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.PixelModification' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.PixelModification' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.PixelModification' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.PixelModification' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.PixelModification' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.PixelModification' objects>, 'Passed': <method 'Passed' of 'renderdoc.PixelModification' objects>, 'depthTestFailed': <attribute 'depthTestFailed' of 'renderdoc.PixelModification' objects>, 'stencilTestFailed': <attribute 'stencilTestFailed' of 'renderdoc.PixelModification' objects>, 'postMod': <attribute 'postMod' of 'renderdoc.PixelModification' objects>, 'directShaderWrite': <attribute 'directShaderWrite' of 'renderdoc.PixelModification' objects>, 'preMod': <attribute 'preMod' of 'renderdoc.PixelModification' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.PixelModification' objects>, 'eventId': <attribute 'eventId' of 'renderdoc.PixelModification' objects>, 'fragIndex': <attribute 'fragIndex' of 'renderdoc.PixelModification' objects>, 'shaderOut': <attribute 'shaderOut' of 'renderdoc.PixelModification' objects>, 'shaderDiscarded': <attribute 'shaderDiscarded' of 'renderdoc.PixelModification' objects>, 'sampleMasked': <attribute 'sampleMasked' of 'renderdoc.PixelModification' objects>, 'depthBoundsFailed': <attribute 'depthBoundsFailed' of 'renderdoc.PixelModification' objects>, 'predicationSkipped': <attribute 'predicationSkipped' of 'renderdoc.PixelModification' objects>, 'primitiveID': <attribute 'primitiveID' of 'renderdoc.PixelModification' objects>, 'backfaceCulled': <attribute 'backfaceCulled' of 'renderdoc.PixelModification' objects>, 'unboundPS': <attribute 'unboundPS' of 'renderdoc.PixelModification' objects>, 'depthClipped': <attribute 'depthClipped' of 'renderdoc.PixelModification' objects>, 'viewClipped': <attribute 'viewClipped' of 'renderdoc.PixelModification' objects>, 'scissorClipped': <attribute 'scissorClipped' of 'renderdoc.PixelModification' objects>, '__doc__': 'An attempt to modify a pixel by a particular event.'})"


