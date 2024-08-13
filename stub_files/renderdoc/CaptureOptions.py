# encoding: utf-8
# module renderdoc
# from D:\reverse_plugin\renderdoc_src\x64\Release\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class CaptureOptions(): # skipped bases: <class 'SwigPyObject'>
    """
    Sets up configuration and options for optional features either at capture time or at API
    initialisation time that the user can enable or disable at will.
    """
    def DecodeFromString(self, encoded: str): # real signature unknown; restored from __doc__
        """
        DecodeFromString(encoded)
        
        Decode the options from a string, as returned by :meth:`EncodeAsString`. Updates this
        object in place.
        
        :param str encoded: The encoded string, as returned by :meth:`EncodeAsString`.
        """
        pass

    def EncodeAsString(self) -> str: # real signature unknown; restored from __doc__
        """
        EncodeAsString()
        
        Encode the current options to a string suitable for passing around between processes.
        
        :return: The encoded string, suitable for passing to :meth:`DecodeFromString`.
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
    def allowFullscreen(self):
        """
Allow the application to enable fullscreen.

Default - enabled

``True`` - The application can enable or disable fullscreen at will.

``False`` - fullscreen is force disabled.

"""
        pass

    @allowFullscreen.setter
    def allowFullscreen(self, value):
        pass

    @property
    def allowVSync(self):
        """
Allow the application to enable vsync.

Default - enabled

``True`` - The application can enable or disable vsync at will.

``False`` - vsync is force disabled.

"""
        pass

    @allowVSync.setter
    def allowVSync(self, value):
        pass

    @property
    def apiValidation(self):
        """
Record API debugging events and messages

Default - disabled

``True`` - Enable built-in API debugging features and records the results into
the capture logfile, which is matched up with events on replay.

``False`` - no API debugging is forcibly enabled.

"""
        pass

    @apiValidation.setter
    def apiValidation(self, value):
        pass

    @property
    def captureAllCmdLists(self):
        """
In APIs that allow for the recording of command lists to be replayed later,
RenderDoc may choose to not capture command lists before a frame capture is
triggered, to reduce overheads. This means any command lists recorded once
and replayed many times will not be available and may cause a failure to
capture.

.. note:: This is only true for APIs where multithreading is difficult or
  discouraged. Newer APIs like Vulkan and D3D12 will ignore this option
  and always capture all command lists since the API is heavily oriented
  around it and the overheads have been reduced by API design.

``True`` - All command lists are captured from the start of the application.

``False`` - Command lists are only captured if their recording begins during
the period when a frame capture is in progress.

"""
        pass

    @captureAllCmdLists.setter
    def captureAllCmdLists(self, value):
        pass

    @property
    def captureCallstacks(self):
        """
Capture CPU callstacks for API events

Default - disabled

``True`` - Enables capturing of callstacks.

``False`` - no callstacks are captured.

"""
        pass

    @captureCallstacks.setter
    def captureCallstacks(self, value):
        pass

    @property
    def captureCallstacksOnlyActions(self):
        """
When capturing CPU callstacks, only capture them from actions.
This option does nothing if :data:`captureCallstacks` is not enabled.

Default - disabled

``True`` - Only captures callstacks for actions.

``False`` - Callstacks, if enabled, are captured for every event.

"""
        pass

    @captureCallstacksOnlyActions.setter
    def captureCallstacksOnlyActions(self, value):
        pass

    @property
    def debugOutputMute(self):
        """
Mute API debugging output when the API validation mode option is enabled.

Default - enabled

``True`` - Mute any API debug messages from being displayed or passed through.

``False`` - API debugging is displayed as normal.

"""
        pass

    @debugOutputMute.setter
    def debugOutputMute(self, value):
        pass

    @property
    def delayForDebugger(self):
        """
Specify a delay in seconds to wait for a debugger to attach, after
creating or injecting into a process, before continuing to allow it to run.

``0`` indicates no delay, and the process will run immediately after injection.

Default - 0 seconds

"""
        pass

    @delayForDebugger.setter
    def delayForDebugger(self, value):
        pass

    @property
    def hookIntoChildren(self):
        """
Hooks any system API calls that create child processes, and injects
RenderDoc into them recursively with the same options.

Default - disabled

``True`` - Hooks into spawned child processes.

``False`` - Child processes are not hooked by RenderDoc.

"""
        pass

    @hookIntoChildren.setter
    def hookIntoChildren(self, value):
        pass

    @property
    def refAllResources(self):
        """
By default RenderDoc only includes resources in the final logfile necessary
for that frame, this allows you to override that behaviour.

Default - disabled

``True`` - all live resources at the time of capture are included in the log
and available for inspection.

``False`` - only the resources referenced by the captured frame are included.

"""
        pass

    @refAllResources.setter
    def refAllResources(self, value):
        pass

    @property
    def softMemoryLimit(self):
        """
Define a soft memory limit which some APIs may aim to keep overhead under where
possible. Anything above this limit will where possible be saved directly to disk during capture.
This will cause increased disk space use (which may cause a capture to fail if disk space is
exhausted) as well as slower capture times.

Not all memory allocations may be deferred like this so it is not a guarantee of a memory limit.

Units are in MBs, suggested values would range from 200MB to 1000MB.

Default - 0 Megabytes

"""
        pass

    @softMemoryLimit.setter
    def softMemoryLimit(self, value):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    @property
    def verifyBufferAccess(self):
        """
Verify buffer access. This includes checking the memory returned by a Map() call to
detect any out-of-bounds modification, as well as initialising buffers with undefined contents to
a marker value to catch use of uninitialised memory.

.. note::

  This option is only valid for OpenGL and D3D11. Explicit APIs such as D3D12 and Vulkan do not
  do the same kind of interception & checking and undefined contents are really undefined.

Default - disabled

``True`` - Verify buffer access.

``False`` - No verification is performed, and overwriting bounds may cause crashes or corruption in
RenderDoc.

"""
        pass

    @verifyBufferAccess.setter
    def verifyBufferAccess(self, value):
        pass


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFE188CF5E0>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.CaptureOptions' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.CaptureOptions' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.CaptureOptions' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.CaptureOptions' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.CaptureOptions' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.CaptureOptions' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.CaptureOptions' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.CaptureOptions' objects>, 'EncodeAsString': <method 'EncodeAsString' of 'renderdoc.CaptureOptions' objects>, 'DecodeFromString': <method 'DecodeFromString' of 'renderdoc.CaptureOptions' objects>, 'verifyBufferAccess': <attribute 'verifyBufferAccess' of 'renderdoc.CaptureOptions' objects>, 'allowVSync': <attribute 'allowVSync' of 'renderdoc.CaptureOptions' objects>, 'captureCallstacksOnlyActions': <attribute 'captureCallstacksOnlyActions' of 'renderdoc.CaptureOptions' objects>, 'captureAllCmdLists': <attribute 'captureAllCmdLists' of 'renderdoc.CaptureOptions' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.CaptureOptions' objects>, 'apiValidation': <attribute 'apiValidation' of 'renderdoc.CaptureOptions' objects>, 'softMemoryLimit': <attribute 'softMemoryLimit' of 'renderdoc.CaptureOptions' objects>, 'captureCallstacks': <attribute 'captureCallstacks' of 'renderdoc.CaptureOptions' objects>, 'delayForDebugger': <attribute 'delayForDebugger' of 'renderdoc.CaptureOptions' objects>, 'debugOutputMute': <attribute 'debugOutputMute' of 'renderdoc.CaptureOptions' objects>, 'allowFullscreen': <attribute 'allowFullscreen' of 'renderdoc.CaptureOptions' objects>, 'hookIntoChildren': <attribute 'hookIntoChildren' of 'renderdoc.CaptureOptions' objects>, 'refAllResources': <attribute 'refAllResources' of 'renderdoc.CaptureOptions' objects>, '__doc__': '\\nSets up configuration and options for optional features either at capture time or at API\\ninitialisation time that the user can enable or disable at will.\\n\\n'})"


