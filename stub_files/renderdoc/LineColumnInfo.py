# encoding: utf-8
# module renderdoc
# from D:\reverse_plugin\renderdoc_src\x64\Release\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class LineColumnInfo(): # skipped bases: <class 'SwigPyObject'>
    """ Details the current region of code that an instruction maps to """
    def SourceEqual(self, o: LineColumnInfo) -> bool: # real signature unknown; restored from __doc__
        """
        SourceEqual(o)
        
        
        :param LineColumnInfo o: The object to compare against.
        :return: ``True`` if this object is equal to the parameter, disregarding :data:`disassemblyLine`.
        :rtype: bool
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
    def colEnd(self):
        """
The column number (starting from 1) of the end of the code on the line specified by
:data:`lineEnd`. If set to 0, no column information is available and the whole lines should be
treated as covering the code.

"""
        pass

    @colEnd.setter
    def colEnd(self, value):
        pass

    @property
    def colStart(self):
        """
The column number (starting from 1) of the start of the code on the line specified by
:data:`lineStart`. If set to 0, no column information is available and the whole lines should be
treated as covering the code.

"""
        pass

    @colStart.setter
    def colStart(self, value):
        pass

    @property
    def disassemblyLine(self):
        """The line (starting from 1) in the disassembly where this instruction is located."""
        pass

    @disassemblyLine.setter
    def disassemblyLine(self, value):
        pass

    @property
    def fileIndex(self):
        """
The current file, as an index into the list of files for this shader.

If this is negative, no source mapping is available and only :data:`disassemblyLine` is valid.

"""
        pass

    @fileIndex.setter
    def fileIndex(self, value):
        pass

    @property
    def lineEnd(self):
        """The ending line-number (starting from 1) of the source code."""
        pass

    @lineEnd.setter
    def lineEnd(self, value):
        pass

    @property
    def lineStart(self):
        """The starting line-number (starting from 1) of the source code."""
        pass

    @lineStart.setter
    def lineStart(self, value):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFE18885A90>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.LineColumnInfo' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.LineColumnInfo' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.LineColumnInfo' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.LineColumnInfo' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.LineColumnInfo' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.LineColumnInfo' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.LineColumnInfo' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.LineColumnInfo' objects>, 'SourceEqual': <method 'SourceEqual' of 'renderdoc.LineColumnInfo' objects>, 'disassemblyLine': <attribute 'disassemblyLine' of 'renderdoc.LineColumnInfo' objects>, 'fileIndex': <attribute 'fileIndex' of 'renderdoc.LineColumnInfo' objects>, 'lineEnd': <attribute 'lineEnd' of 'renderdoc.LineColumnInfo' objects>, 'lineStart': <attribute 'lineStart' of 'renderdoc.LineColumnInfo' objects>, 'colStart': <attribute 'colStart' of 'renderdoc.LineColumnInfo' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.LineColumnInfo' objects>, 'colEnd': <attribute 'colEnd' of 'renderdoc.LineColumnInfo' objects>, '__doc__': 'Details the current region of code that an instruction maps to'})"


