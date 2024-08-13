# encoding: utf-8
# module renderdoc
# from D:\reverse_plugin\renderdoc_src\x64\Release\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .BlendEquation import BlendEquation

class ColorBlend(): # skipped bases: <class 'SwigPyObject'>
    """ Describes the blend configuration for a given output target. """
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
    def alphaBlend(self) -> BlendEquation:
        """
The blending equation for alpha values.

:type: BlendEquation

"""
        pass

    @alphaBlend.setter
    def alphaBlend(self, value: BlendEquation):
        pass

    @property
    def colorBlend(self) -> BlendEquation:
        """
The blending equation for color values.

:type: BlendEquation

"""
        pass

    @colorBlend.setter
    def colorBlend(self, value: BlendEquation):
        pass

    @property
    def enabled(self):
        """``True`` if blending is enabled for this target."""
        pass

    @enabled.setter
    def enabled(self, value):
        pass

    @property
    def logicOperation(self):
        """
The :class:`LogicOperation` to use for logic operations, if
:data:`logicOperationEnabled` is ``True``.

"""
        pass

    @logicOperation.setter
    def logicOperation(self, value):
        pass

    @property
    def logicOperationEnabled(self):
        """``True`` if the logic operation in :data:`logicOperation` should be used."""
        pass

    @logicOperationEnabled.setter
    def logicOperationEnabled(self, value):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    @property
    def writeMask(self):
        """The mask for writes to the render target."""
        pass

    @writeMask.setter
    def writeMask(self, value):
        pass


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFE188A71D0>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.ColorBlend' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.ColorBlend' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.ColorBlend' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.ColorBlend' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.ColorBlend' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.ColorBlend' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.ColorBlend' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.ColorBlend' objects>, 'colorBlend': <attribute 'colorBlend' of 'renderdoc.ColorBlend' objects>, 'enabled': <attribute 'enabled' of 'renderdoc.ColorBlend' objects>, 'logicOperationEnabled': <attribute 'logicOperationEnabled' of 'renderdoc.ColorBlend' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.ColorBlend' objects>, 'writeMask': <attribute 'writeMask' of 'renderdoc.ColorBlend' objects>, 'alphaBlend': <attribute 'alphaBlend' of 'renderdoc.ColorBlend' objects>, 'logicOperation': <attribute 'logicOperation' of 'renderdoc.ColorBlend' objects>, '__doc__': 'Describes the blend configuration for a given output target.'})"


