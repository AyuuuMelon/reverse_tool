# encoding: utf-8
# module renderdoc
# from D:\reverse_plugin\renderdoc_src\x64\Release\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class BlendStats(): # skipped bases: <class 'SwigPyObject'>
    """ Contains the statistics for blend state binds in a frame. """
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
    def calls(self):
        """How many function calls were made."""
        pass

    @calls.setter
    def calls(self, value):
        pass

    @property
    def nulls(self):
        """How many objects were unbound."""
        pass

    @nulls.setter
    def nulls(self, value):
        pass

    @property
    def redundants(self):
        """How many calls made no change due to the existing bind being identical."""
        pass

    @redundants.setter
    def redundants(self, value):
        pass

    @property
    def sets(self):
        """How many objects were bound."""
        pass

    @sets.setter
    def sets(self, value):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFE1887BC50>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.BlendStats' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.BlendStats' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.BlendStats' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.BlendStats' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.BlendStats' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.BlendStats' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.BlendStats' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.BlendStats' objects>, 'calls': <attribute 'calls' of 'renderdoc.BlendStats' objects>, 'redundants': <attribute 'redundants' of 'renderdoc.BlendStats' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.BlendStats' objects>, 'sets': <attribute 'sets' of 'renderdoc.BlendStats' objects>, 'nulls': <attribute 'nulls' of 'renderdoc.BlendStats' objects>, '__doc__': 'Contains the statistics for blend state binds in a frame.'})"


