# encoding: utf-8
# module qrenderdoc
# from D:\reverse_plugin\renderdoc_src\x64\Release\pymodules\qrenderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class EventBookmark(): # skipped bases: <class 'SwigPyObject'>
    """ A description of a bookmark on an event """
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
        """The :data:`eventId <renderdoc.APIEvent.eventId>` at which this bookmark is placed."""
        pass

    @eventId.setter
    def eventId(self, value):
        pass

    @property
    def text(self):
        """The text associated with this bookmark - could be empty"""
        pass

    @text.setter
    def text(self, value):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFE18830C50>, '__hash__': <slot wrapper '__hash__' of 'qrenderdoc.EventBookmark' objects>, '__lt__': <slot wrapper '__lt__' of 'qrenderdoc.EventBookmark' objects>, '__le__': <slot wrapper '__le__' of 'qrenderdoc.EventBookmark' objects>, '__eq__': <slot wrapper '__eq__' of 'qrenderdoc.EventBookmark' objects>, '__ne__': <slot wrapper '__ne__' of 'qrenderdoc.EventBookmark' objects>, '__gt__': <slot wrapper '__gt__' of 'qrenderdoc.EventBookmark' objects>, '__ge__': <slot wrapper '__ge__' of 'qrenderdoc.EventBookmark' objects>, '__init__': <slot wrapper '__init__' of 'qrenderdoc.EventBookmark' objects>, '__dict__': <attribute '__dict__' of 'qrenderdoc.EventBookmark' objects>, 'text': <attribute 'text' of 'qrenderdoc.EventBookmark' objects>, 'eventId': <attribute 'eventId' of 'qrenderdoc.EventBookmark' objects>, '__doc__': 'A description of a bookmark on an event'})"


