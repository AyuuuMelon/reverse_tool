# encoding: utf-8
# module renderdoc
# from D:\reverse_plugin\renderdoc_src\x64\Release\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class GLDepthState(): # skipped bases: <class 'SwigPyObject'>
    """ Describes the depth state. """
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
    def depthBounds(self):
        """``True`` if depth bounds tests should be applied."""
        pass

    @depthBounds.setter
    def depthBounds(self, value):
        pass

    @property
    def depthEnable(self):
        """``True`` if depth testing should be performed."""
        pass

    @depthEnable.setter
    def depthEnable(self, value):
        pass

    @property
    def depthFunction(self):
        """The :class:`CompareFunction` to use for testing depth values."""
        pass

    @depthFunction.setter
    def depthFunction(self, value):
        pass

    @property
    def depthWrites(self):
        """``True`` if depth values should be written to the depth target."""
        pass

    @depthWrites.setter
    def depthWrites(self, value):
        pass

    @property
    def farBound(self):
        """The far plane bounding value."""
        pass

    @farBound.setter
    def farBound(self, value):
        pass

    @property
    def nearBound(self):
        """The near plane bounding value."""
        pass

    @nearBound.setter
    def nearBound(self, value):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFE188B6430>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.GLDepthState' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.GLDepthState' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.GLDepthState' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.GLDepthState' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.GLDepthState' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.GLDepthState' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.GLDepthState' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.GLDepthState' objects>, 'depthFunction': <attribute 'depthFunction' of 'renderdoc.GLDepthState' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.GLDepthState' objects>, 'nearBound': <attribute 'nearBound' of 'renderdoc.GLDepthState' objects>, 'farBound': <attribute 'farBound' of 'renderdoc.GLDepthState' objects>, 'depthBounds': <attribute 'depthBounds' of 'renderdoc.GLDepthState' objects>, 'depthEnable': <attribute 'depthEnable' of 'renderdoc.GLDepthState' objects>, 'depthWrites': <attribute 'depthWrites' of 'renderdoc.GLDepthState' objects>, '__doc__': 'Describes the depth state.'})"


