# encoding: utf-8
# module qrenderdoc
# from D:\reverse_plugin\renderdoc_src\x64\Release\pymodules\qrenderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class ExtensionMetadata(): # skipped bases: <class 'SwigPyObject'>
    """ The metadata for an extension. """
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
    def author(self):
        """The author of the extension, optionally with an email contact"""
        pass

    @author.setter
    def author(self, value):
        pass

    @property
    def description(self):
        """A longer description of what the extension does"""
        pass

    @description.setter
    def description(self, value):
        pass

    @property
    def extensionAPI(self):
        """The version of the extension API that this extension is written against"""
        pass

    @extensionAPI.setter
    def extensionAPI(self, value):
        pass

    @property
    def extensionURL(self):
        """The URL for where the extension is fetched from"""
        pass

    @extensionURL.setter
    def extensionURL(self, value):
        pass

    @property
    def filePath(self):
        """The location of this package on disk"""
        pass

    @filePath.setter
    def filePath(self, value):
        pass

    @property
    def name(self):
        """The short friendly name for the extension"""
        pass

    @name.setter
    def name(self, value):
        pass

    @property
    def package(self):
        """The python package for this extension, e.g. foo.bar"""
        pass

    @package.setter
    def package(self, value):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    @property
    def version(self):
        """The version of the extension"""
        pass

    @version.setter
    def version(self, value):
        pass


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFE18836B00>, '__hash__': <slot wrapper '__hash__' of 'qrenderdoc.ExtensionMetadata' objects>, '__lt__': <slot wrapper '__lt__' of 'qrenderdoc.ExtensionMetadata' objects>, '__le__': <slot wrapper '__le__' of 'qrenderdoc.ExtensionMetadata' objects>, '__eq__': <slot wrapper '__eq__' of 'qrenderdoc.ExtensionMetadata' objects>, '__ne__': <slot wrapper '__ne__' of 'qrenderdoc.ExtensionMetadata' objects>, '__gt__': <slot wrapper '__gt__' of 'qrenderdoc.ExtensionMetadata' objects>, '__ge__': <slot wrapper '__ge__' of 'qrenderdoc.ExtensionMetadata' objects>, '__init__': <slot wrapper '__init__' of 'qrenderdoc.ExtensionMetadata' objects>, 'package': <attribute 'package' of 'qrenderdoc.ExtensionMetadata' objects>, 'version': <attribute 'version' of 'qrenderdoc.ExtensionMetadata' objects>, 'description': <attribute 'description' of 'qrenderdoc.ExtensionMetadata' objects>, 'extensionAPI': <attribute 'extensionAPI' of 'qrenderdoc.ExtensionMetadata' objects>, '__dict__': <attribute '__dict__' of 'qrenderdoc.ExtensionMetadata' objects>, 'author': <attribute 'author' of 'qrenderdoc.ExtensionMetadata' objects>, 'extensionURL': <attribute 'extensionURL' of 'qrenderdoc.ExtensionMetadata' objects>, 'name': <attribute 'name' of 'qrenderdoc.ExtensionMetadata' objects>, 'filePath': <attribute 'filePath' of 'qrenderdoc.ExtensionMetadata' objects>, '__doc__': 'The metadata for an extension.'})"


