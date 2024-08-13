# encoding: utf-8
# module qrenderdoc
# from D:\reverse_plugin\renderdoc_src\x64\Release\pymodules\qrenderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class BugReport(): # skipped bases: <class 'SwigPyObject'>
    """ Describes a submitted bug report. """
    def URL(self) -> str: # real signature unknown; restored from __doc__
        """
        URL()
        
        Gets the URL for this report.
        
        :return: The URL to the report.
        :rtype: str
        """
        pass

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
    def checkDate(self):
        """The last date that we checked for updates."""
        pass

    @checkDate.setter
    def checkDate(self, value):
        pass

    @property
    def reportId(self):
        """The private ID of the bug report."""
        pass

    @reportId.setter
    def reportId(self, value):
        pass

    @property
    def submitDate(self):
        """The original date when this bug was submitted."""
        pass

    @submitDate.setter
    def submitDate(self, value):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    @property
    def unreadUpdates(self):
        """Unread updates to the bug exist"""
        pass

    @unreadUpdates.setter
    def unreadUpdates(self, value):
        pass


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFE18833500>, '__hash__': <slot wrapper '__hash__' of 'qrenderdoc.BugReport' objects>, '__lt__': <slot wrapper '__lt__' of 'qrenderdoc.BugReport' objects>, '__le__': <slot wrapper '__le__' of 'qrenderdoc.BugReport' objects>, '__eq__': <slot wrapper '__eq__' of 'qrenderdoc.BugReport' objects>, '__ne__': <slot wrapper '__ne__' of 'qrenderdoc.BugReport' objects>, '__gt__': <slot wrapper '__gt__' of 'qrenderdoc.BugReport' objects>, '__ge__': <slot wrapper '__ge__' of 'qrenderdoc.BugReport' objects>, '__init__': <slot wrapper '__init__' of 'qrenderdoc.BugReport' objects>, 'URL': <method 'URL' of 'qrenderdoc.BugReport' objects>, 'submitDate': <attribute 'submitDate' of 'qrenderdoc.BugReport' objects>, 'checkDate': <attribute 'checkDate' of 'qrenderdoc.BugReport' objects>, '__dict__': <attribute '__dict__' of 'qrenderdoc.BugReport' objects>, 'reportId': <attribute 'reportId' of 'qrenderdoc.BugReport' objects>, 'unreadUpdates': <attribute 'unreadUpdates' of 'qrenderdoc.BugReport' objects>, '__doc__': 'Describes a submitted bug report.'})"


