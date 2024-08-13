# encoding: utf-8
# module renderdoc
# from D:\reverse_plugin\renderdoc_src\x64\Release\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class EventUsage(): # skipped bases: <class 'SwigPyObject'>
    """ Describes a particular use of a resource at a specific :data:`eventId <APIEvent.eventId>`. """
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
    def eventId(self):
        """The :data:`eventId <APIEvent.eventId>` where this usage happened."""
        pass

    @eventId.setter
    def eventId(self, value):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    @property
    def usage(self):
        """The :class:`ResourceUsage` in question."""
        pass

    @usage.setter
    def usage(self, value):
        pass

    @property
    def view(self):
        """An optional :class:`ResourceId` identifying the view through which the use happened."""
        pass

    @view.setter
    def view(self, value):
        pass


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFE18864000>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.EventUsage' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.EventUsage' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.EventUsage' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.EventUsage' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.EventUsage' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.EventUsage' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.EventUsage' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.EventUsage' objects>, 'view': <attribute 'view' of 'renderdoc.EventUsage' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.EventUsage' objects>, 'eventId': <attribute 'eventId' of 'renderdoc.EventUsage' objects>, 'usage': <attribute 'usage' of 'renderdoc.EventUsage' objects>, '__doc__': 'Describes a particular use of a resource at a specific :data:`eventId <APIEvent.eventId>`.'})"


