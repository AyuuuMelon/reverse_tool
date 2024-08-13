# encoding: utf-8
# module renderdoc
# from D:\reverse_plugin\renderdoc_src\x64\Release\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class DebugVariableReference(): # skipped bases: <class 'SwigPyObject'>
    """ A particular component of a debugging variable that a high-level variable component maps to """
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
    def component(self):
        """The component within the variable."""
        pass

    @component.setter
    def component(self, value):
        pass

    @property
    def name(self):
        """The name of the base debug variable."""
        pass

    @name.setter
    def name(self, value):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    @property
    def type(self):
        """The type of variable this is referring to."""
        pass

    @type.setter
    def type(self, value):
        pass


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFE18853150>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.DebugVariableReference' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.DebugVariableReference' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.DebugVariableReference' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.DebugVariableReference' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.DebugVariableReference' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.DebugVariableReference' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.DebugVariableReference' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.DebugVariableReference' objects>, 'name': <attribute 'name' of 'renderdoc.DebugVariableReference' objects>, 'component': <attribute 'component' of 'renderdoc.DebugVariableReference' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.DebugVariableReference' objects>, 'type': <attribute 'type' of 'renderdoc.DebugVariableReference' objects>, '__doc__': 'A particular component of a debugging variable that a high-level variable component maps to'})"


