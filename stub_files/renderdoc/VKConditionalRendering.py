# encoding: utf-8
# module renderdoc
# from D:\reverse_plugin\renderdoc_src\x64\Release\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class VKConditionalRendering(): # skipped bases: <class 'SwigPyObject'>
    """ Contains the current conditional rendering state. """
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
    def bufferId(self):
        """The :class:`ResourceId` of the buffer containing the predicate for conditional rendering."""
        pass

    @bufferId.setter
    def bufferId(self, value):
        pass

    @property
    def byteOffset(self):
        """The byte offset into buffer where the predicate is located."""
        pass

    @byteOffset.setter
    def byteOffset(self, value):
        pass

    @property
    def isInverted(self):
        """``True`` if predicate result is inverted."""
        pass

    @isInverted.setter
    def isInverted(self, value):
        pass

    @property
    def isPassing(self):
        """``True`` if the current predicate would render."""
        pass

    @isPassing.setter
    def isPassing(self, value):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFE1887A8B0>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.VKConditionalRendering' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.VKConditionalRendering' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.VKConditionalRendering' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.VKConditionalRendering' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.VKConditionalRendering' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.VKConditionalRendering' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.VKConditionalRendering' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.VKConditionalRendering' objects>, 'isInverted': <attribute 'isInverted' of 'renderdoc.VKConditionalRendering' objects>, 'bufferId': <attribute 'bufferId' of 'renderdoc.VKConditionalRendering' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.VKConditionalRendering' objects>, 'byteOffset': <attribute 'byteOffset' of 'renderdoc.VKConditionalRendering' objects>, 'isPassing': <attribute 'isPassing' of 'renderdoc.VKConditionalRendering' objects>, '__doc__': 'Contains the current conditional rendering state.'})"


