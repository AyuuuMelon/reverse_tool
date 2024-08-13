# encoding: utf-8
# module renderdoc
# from D:\reverse_plugin\renderdoc_src\x64\Release\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class GlobalEnvironment(): # skipped bases: <class 'SwigPyObject'>
    """ Structure used for initialising environment in a replay application. """
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
    def enumerateGPUs(self):
        """
Whether to enumerate available GPUs. If the replay program is only being used for
internal operation where enumerating GPUs would be too expensive or problematic, it can be disabled
here.

"""
        pass

    @enumerateGPUs.setter
    def enumerateGPUs(self, value):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    @property
    def waylandDisplay(self):
        """The handle to the wayland display to use internally. If left ``NULL``, wayland cannot be used."""
        pass

    @waylandDisplay.setter
    def waylandDisplay(self, value):
        pass

    @property
    def xlibDisplay(self):
        """The handle to the X display to use internally. If left ``NULL``, one will be opened."""
        pass

    @xlibDisplay.setter
    def xlibDisplay(self, value):
        pass


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFE18869170>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.GlobalEnvironment' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.GlobalEnvironment' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.GlobalEnvironment' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.GlobalEnvironment' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.GlobalEnvironment' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.GlobalEnvironment' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.GlobalEnvironment' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.GlobalEnvironment' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.GlobalEnvironment' objects>, 'xlibDisplay': <attribute 'xlibDisplay' of 'renderdoc.GlobalEnvironment' objects>, 'waylandDisplay': <attribute 'waylandDisplay' of 'renderdoc.GlobalEnvironment' objects>, 'enumerateGPUs': <attribute 'enumerateGPUs' of 'renderdoc.GlobalEnvironment' objects>, '__doc__': 'Structure used for initialising environment in a replay application.'})"


