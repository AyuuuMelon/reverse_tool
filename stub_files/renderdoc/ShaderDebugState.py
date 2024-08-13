# encoding: utf-8
# module renderdoc
# from D:\reverse_plugin\renderdoc_src\x64\Release\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .ShaderVariableChange import ShaderVariableChange

class ShaderDebugState(): # skipped bases: <class 'SwigPyObject'>
    """
    This stores the current state of shader debugging at one particular step in the shader,
    with all mutable variable contents.
    """
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
    def callstack(self) -> List[str]:
        """
The function names in the current callstack at this instruction.

The oldest/outer function is first in the list, the newest/inner function is last.

:type: List[str]

"""
        pass

    @callstack.setter
    def callstack(self, value: List[str]):
        pass

    @property
    def changes(self) -> List[ShaderVariableChange]:
        """
The changes in mutable variables for this shader. The change documents the
bidirectional change of variables, so that a single state can be updated either forwards or
backwards using the information.

:type: List[ShaderVariableChange]

"""
        pass

    @changes.setter
    def changes(self, value: List[ShaderVariableChange]):
        pass

    @property
    def flags(self):
        """A set of :class:`ShaderEvents` flags that indicate what events happened on this step."""
        pass

    @flags.setter
    def flags(self, value):
        pass

    @property
    def nextInstruction(self):
        """
The next instruction to be executed after this state. The initial state before any
shader execution happened will have ``nextInstruction == 0``.

"""
        pass

    @nextInstruction.setter
    def nextInstruction(self, value):
        pass

    @property
    def stepIndex(self):
        """
The program counter within the debug trace. The initial state will be index 0, and it
will increment linearly after that regardless of loops or branching.

"""
        pass

    @stepIndex.setter
    def stepIndex(self, value):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFE1889D650>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.ShaderDebugState' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.ShaderDebugState' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.ShaderDebugState' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.ShaderDebugState' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.ShaderDebugState' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.ShaderDebugState' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.ShaderDebugState' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.ShaderDebugState' objects>, 'callstack': <attribute 'callstack' of 'renderdoc.ShaderDebugState' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.ShaderDebugState' objects>, 'stepIndex': <attribute 'stepIndex' of 'renderdoc.ShaderDebugState' objects>, 'changes': <attribute 'changes' of 'renderdoc.ShaderDebugState' objects>, 'flags': <attribute 'flags' of 'renderdoc.ShaderDebugState' objects>, 'nextInstruction': <attribute 'nextInstruction' of 'renderdoc.ShaderDebugState' objects>, '__doc__': '\\nThis stores the current state of shader debugging at one particular step in the shader,\\nwith all mutable variable contents.\\n\\n'})"


