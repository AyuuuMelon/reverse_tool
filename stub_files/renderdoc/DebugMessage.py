# encoding: utf-8
# module renderdoc
# from D:\reverse_plugin\renderdoc_src\x64\Release\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class DebugMessage(): # skipped bases: <class 'SwigPyObject'>
    """ A debugging message from the API validation or internal analysis and error detection. """
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
        """The :class:`category <MessageCategory>` of this debug message."""
        pass

    @category.setter
    def category(self, value):
        pass

    @property
    def description(self):
        """The string contents of the message."""
        pass

    @description.setter
    def description(self, value):
        pass

    @property
    def eventId(self):
        """The :data:`eventId <APIEvent.eventId>` where this debug message was found."""
        pass

    @eventId.setter
    def eventId(self, value):
        pass

    @property
    def messageID(self):
        """An ID that identifies this particular debug message uniquely."""
        pass

    @messageID.setter
    def messageID(self, value):
        pass

    @property
    def severity(self):
        """The :class:`severity <MessageSeverity>` of this debug message."""
        pass

    @severity.setter
    def severity(self, value):
        pass

    @property
    def source(self):
        """The :class:`source <MessageSource>` of this debug message."""
        pass

    @source.setter
    def source(self, value):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFE188AC830>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.DebugMessage' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.DebugMessage' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.DebugMessage' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.DebugMessage' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.DebugMessage' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.DebugMessage' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.DebugMessage' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.DebugMessage' objects>, 'severity': <attribute 'severity' of 'renderdoc.DebugMessage' objects>, 'messageID': <attribute 'messageID' of 'renderdoc.DebugMessage' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.DebugMessage' objects>, 'eventId': <attribute 'eventId' of 'renderdoc.DebugMessage' objects>, 'source': <attribute 'source' of 'renderdoc.DebugMessage' objects>, 'category': <attribute 'category' of 'renderdoc.DebugMessage' objects>, 'description': <attribute 'description' of 'renderdoc.DebugMessage' objects>, '__doc__': 'A debugging message from the API validation or internal analysis and error detection.'})"


