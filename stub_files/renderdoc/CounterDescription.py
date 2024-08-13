# encoding: utf-8
# module renderdoc
# from D:\reverse_plugin\renderdoc_src\x64\Release\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .Uuid import Uuid

class CounterDescription(): # skipped bases: <class 'SwigPyObject'>
    """ Describes a GPU counter's purpose and result value. """
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
    def category(self):
        """The counter category. Can be empty for uncategorized counters."""
        pass

    @category.setter
    def category(self, value):
        pass

    @property
    def counter(self):
        """
The :class:`GPUCounter` this counter represents.

.. note:: This is stored as an ``int`` not a :class:`GPUCounter` to allow for values that may not
  correspond to any of the predefined values if it's a hardware-specific counter value.

"""
        pass

    @counter.setter
    def counter(self, value):
        pass

    @property
    def description(self):
        """If available, a longer human-readable description of the value this counter measures."""
        pass

    @description.setter
    def description(self, value):
        pass

    @property
    def name(self):
        """A short human-readable name for the counter."""
        pass

    @name.setter
    def name(self, value):
        pass

    @property
    def resultByteWidth(self):
        """The number of bytes in the resulting value."""
        pass

    @resultByteWidth.setter
    def resultByteWidth(self, value):
        pass

    @property
    def resultType(self):
        """The :class:`type of value <CompType>` returned by this counter."""
        pass

    @resultType.setter
    def resultType(self, value):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    @property
    def unit(self):
        """The :class:`CounterUnit` for the result value."""
        pass

    @unit.setter
    def unit(self, value):
        pass

    @property
    def uuid(self) -> Uuid:
        """
The unique identifier for this counter that will not change across drivers or replays.

:type: Uuid

"""
        pass

    @uuid.setter
    def uuid(self, value: Uuid):
        pass


    __dict__ = None # (!) real value is 'mappingproxy({\'this\': <attribute \'this\' of \'SwigPyObject\' objects>, \'thisown\': <attribute \'thisown\' of \'SwigPyObject\' objects>, \'__new__\': <built-in method __new__ of SwigPyObjectType object at 0x00007FFE18885400>, \'__hash__\': <slot wrapper \'__hash__\' of \'renderdoc.CounterDescription\' objects>, \'__lt__\': <slot wrapper \'__lt__\' of \'renderdoc.CounterDescription\' objects>, \'__le__\': <slot wrapper \'__le__\' of \'renderdoc.CounterDescription\' objects>, \'__eq__\': <slot wrapper \'__eq__\' of \'renderdoc.CounterDescription\' objects>, \'__ne__\': <slot wrapper \'__ne__\' of \'renderdoc.CounterDescription\' objects>, \'__gt__\': <slot wrapper \'__gt__\' of \'renderdoc.CounterDescription\' objects>, \'__ge__\': <slot wrapper \'__ge__\' of \'renderdoc.CounterDescription\' objects>, \'__init__\': <slot wrapper \'__init__\' of \'renderdoc.CounterDescription\' objects>, \'uuid\': <attribute \'uuid\' of \'renderdoc.CounterDescription\' objects>, \'name\': <attribute \'name\' of \'renderdoc.CounterDescription\' objects>, \'counter\': <attribute \'counter\' of \'renderdoc.CounterDescription\' objects>, \'resultType\': <attribute \'resultType\' of \'renderdoc.CounterDescription\' objects>, \'unit\': <attribute \'unit\' of \'renderdoc.CounterDescription\' objects>, \'__dict__\': <attribute \'__dict__\' of \'renderdoc.CounterDescription\' objects>, \'category\': <attribute \'category\' of \'renderdoc.CounterDescription\' objects>, \'description\': <attribute \'description\' of \'renderdoc.CounterDescription\' objects>, \'resultByteWidth\': <attribute \'resultByteWidth\' of \'renderdoc.CounterDescription\' objects>, \'__doc__\': "Describes a GPU counter\'s purpose and result value."})'


