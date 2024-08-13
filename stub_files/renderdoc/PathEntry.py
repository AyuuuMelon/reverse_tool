# encoding: utf-8
# module renderdoc
# from D:\reverse_plugin\renderdoc_src\x64\Release\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class PathEntry(): # skipped bases: <class 'SwigPyObject'>
    """ Properties of a path on a remote filesystem. """
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
    def filename(self):
        """The filename of this path. This contains only the filename, not the full path."""
        pass

    @filename.setter
    def filename(self, value):
        pass

    @property
    def flags(self):
        """The :class:`PathProperty` flags for this path."""
        pass

    @flags.setter
    def flags(self, value):
        pass

    @property
    def lastmod(self):
        """The last modified date of this path, as a unix timestamp in UTC."""
        pass

    @lastmod.setter
    def lastmod(self, value):
        pass

    @property
    def size(self):
        """The size of the path in bytes."""
        pass

    @size.setter
    def size(self, value):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFE1889A1B0>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.PathEntry' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.PathEntry' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.PathEntry' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.PathEntry' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.PathEntry' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.PathEntry' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.PathEntry' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.PathEntry' objects>, 'lastmod': <attribute 'lastmod' of 'renderdoc.PathEntry' objects>, 'size': <attribute 'size' of 'renderdoc.PathEntry' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.PathEntry' objects>, 'filename': <attribute 'filename' of 'renderdoc.PathEntry' objects>, 'flags': <attribute 'flags' of 'renderdoc.PathEntry' objects>, '__doc__': 'Properties of a path on a remote filesystem.'})"


