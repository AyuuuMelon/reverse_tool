# encoding: utf-8
# module qrenderdoc
# from D:\reverse_plugin\renderdoc_src\x64\Release\pymodules\qrenderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .RemoteHost import RemoteHost
from .BugReport import BugReport
from .ShaderProcessingTool import ShaderProcessingTool

from renderdoc.ReplayOptions import ReplayOptions

class PersistantConfig(): # skipped bases: <class 'SwigPyObject'>
    """
    A persistant config file that is automatically loaded and saved, which contains any
    settings and information that needs to be preserved from one run to the next.
    
    For more information about some of these settings that are user-facing see
    :ref:`the documentation for the settings window <settings-window>`.
    """
    def AddRemoteHost(self, host: RemoteHost): # real signature unknown; restored from __doc__
        """
        AddRemoteHost(host)
        
        Adds a new remote host.
        
        :param RemoteHost host: The remote host to add.
        """
        pass

    def Close(self): # real signature unknown; restored from __doc__
        """
        Close()
        
        Closes the config file so that subsequent calls to Save() will not write to disk at
        the file the config was loaded from.
        
        This function is rarely directly used, except in the case where RenderDoc is relaunching itself and
        wants to avoid file locking conflicts between the closing instance saving, and the loading instance
        loading. It can explicitly save and close before relaunching.
        """
        pass

    def GetRemoteHost(self, hostname: str) -> RemoteHost: # real signature unknown; restored from __doc__
        """
        GetRemoteHost(hostname)
        
        Look up a remote host by hostname.
        
        :param str hostname: The hostname to look up
        :return: The remote host for the given hostname, or an invalid ``RemoteHost`` if no such exists.
        :rtype: RemoteHost
        """
        pass

    def GetRemoteHosts(self) -> List[RemoteHost]: # real signature unknown; restored from __doc__
        """
        GetRemoteHosts()
        
        Returns a list of all remote hosts.
        
        :return: The remote host list
        :rtype: List[RemoteHost]
        """
        pass

    def Load(self, filename: str) -> bool: # real signature unknown; restored from __doc__
        """
        Load(filename)
        
        Loads the config from a given filename. This happens automatically on startup, so it's
        not recommended that you call this function manually.
        
        :param str filename: The filename to load from
        :return: A boolean status if the load was successful.
        :rtype: bool
        """
        pass

    def RemoveRemoteHost(self, host: RemoteHost): # real signature unknown; restored from __doc__
        """
        RemoveRemoteHost(host)
        
        Removes an existing remote host.
        
        :param RemoteHost host: The remote host to remove.
        """
        pass

    def Save(self) -> bool: # real signature unknown; restored from __doc__
        """
        Save()
        
        Saves the config to disk. This can happen if you want to be sure a setting has been
        propagated and will not be forgotten in the case of crash or otherwise unexpected exit.
        
        :return: A boolean status if the save was successful.
        :rtype: bool
        """
        pass

    def SetStyle(self) -> bool: # real signature unknown; restored from __doc__
        """
        SetStyle()
        
        Sets the UI style to the value in :data:`UIStyle`.
        
        Changing the style after the application has started may not properly update everything, so to be
        sure the new style is applied, the application should be restarted.
        
        :return: ``True`` if the style was set successfully, ``False`` if there was a problem e.g. the value
          of :data:`UIStyle` was unrecognised or empty.
        :rtype: bool
        """
        pass

    def SetupFormatting(self): # real signature unknown; restored from __doc__
        """
        SetupFormatting()
        
        Configures the :class:`Formatter` class with the settings from this config.
        """
        pass

    def UpdateEnumeratedProtocolDevices(self): # real signature unknown; restored from __doc__
        """
        UpdateEnumeratedProtocolDevices()
        
        If configured, queries available device protocols to update auto-configured hosts.
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
    def AllowGlobalHook(self):
        """
``True`` if global hooking is enabled. Since it has potentially problematic side-effects and is dangerous, it requires explicit opt-in.

Defaults to ``False``.
"""
        pass

    @AllowGlobalHook.setter
    def AllowGlobalHook(self, value):
        pass

    @property
    def AllowProcessInject(self):
        """
``True`` if process injection is enabled. Since it can often break and is almost always not want users want to do. New users can get confused by it being there and go to it first.

Defaults to ``False``.
"""
        pass

    @AllowProcessInject.setter
    def AllowProcessInject(self, value):
        pass

    @property
    def AlwaysLoad_Extensions(self) -> List[str]:
        """
A list of strings with extension packages to always load on startup, without needing manual enabling.

:type: List[str]
"""
        pass

    @AlwaysLoad_Extensions.setter
    def AlwaysLoad_Extensions(self, value: List[str]):
        pass

    @property
    def AlwaysReplayLocally(self):
        """
``True`` if when loading a capture that was originally captured on a remote device but uses an API that can be supported locally, should be loaded locally without prompting to switch to a remote context.

Defaults to ``False``.
"""
        pass

    @AlwaysReplayLocally.setter
    def AlwaysReplayLocally(self, value):
        pass

    @property
    def Analytics_ManualCheck(self):
        """
``True`` if the user has remained with analytics turned on, but has chosen to manually check each report that is sent out.
collection and reporting.

Defaults to ``False``.
"""
        pass

    @Analytics_ManualCheck.setter
    def Analytics_ManualCheck(self, value):
        pass

    @property
    def Analytics_TotalOptOut(self):
        """
``True`` if the user has selected to completely opt-out from and disable all analytics collection and reporting.

Defaults to ``False``.
"""
        pass

    @Analytics_TotalOptOut.setter
    def Analytics_TotalOptOut(self, value):
        pass

    @property
    def BufferFormatter_SavedFormats(self) -> List[str]:
        """
A list of strings with saved formats for the buffer formatter. The first line is the name and the rest of the contents are the formats.

:type: List[str]
"""
        pass

    @BufferFormatter_SavedFormats.setter
    def BufferFormatter_SavedFormats(self, value: List[str]):
        pass

    @property
    def CheckUpdate_AllowChecks(self):
        """
``True`` if the UI should be allowed to make update checks remotely to see if a new version is available.

Defaults to ``True``.
"""
        pass

    @CheckUpdate_AllowChecks.setter
    def CheckUpdate_AllowChecks(self, value):
        pass

    @property
    def CheckUpdate_CurrentVersion(self):
        """The current version at the time of update checks. Used to determine if a cached pending update is no longer valid because we got updated through some other method."""
        pass

    @CheckUpdate_CurrentVersion.setter
    def CheckUpdate_CurrentVersion(self, value):
        pass

    @property
    def CheckUpdate_LastUpdate(self):
        """A date containing the last time that update checks happened."""
        pass

    @CheckUpdate_LastUpdate.setter
    def CheckUpdate_LastUpdate(self, value):
        pass

    @property
    def CheckUpdate_UpdateAvailable(self):
        """
``True`` if an update to a newer version is currently available.

Defaults to ``False``.
"""
        pass

    @CheckUpdate_UpdateAvailable.setter
    def CheckUpdate_UpdateAvailable(self, value):
        pass

    @property
    def CheckUpdate_UpdateResponse(self):
        """Contains the response from the update server from the last update check, with any release notes for the new version."""
        pass

    @CheckUpdate_UpdateResponse.setter
    def CheckUpdate_UpdateResponse(self, value):
        pass

    @property
    def Comments_ShowOnLoad(self):
        """
``True`` if when loading a new capture that contains a comments section, the comment viewer will be opened and focussed.

Defaults to ``False``.
"""
        pass

    @Comments_ShowOnLoad.setter
    def Comments_ShowOnLoad(self, value):
        pass

    @property
    def CrashReport_EmailAddress(self):
        """The saved email address for pre-filling out in crash reports."""
        pass

    @CrashReport_EmailAddress.setter
    def CrashReport_EmailAddress(self, value):
        pass

    @property
    def CrashReport_EmailNagged(self):
        """
``True`` if the user has been prompted to enter their email address on a crash report. This really helps find fixes for bugs, so we prompt the user once only if they didn't enter an email. Once the prompt has happened, regardless of the answer this is set to true and remains there forever.

Defaults to ``False``.
"""
        pass

    @CrashReport_EmailNagged.setter
    def CrashReport_EmailNagged(self, value):
        pass

    @property
    def CrashReport_LastOpenedCapture(self):
        """The last opened capture, to send if any crash is encountered. This is different to the most recent opened file, because it's set before any processing happens (recent files are only added to the list when they successfully open), and it's cleared again when the capture is closed."""
        pass

    @CrashReport_LastOpenedCapture.setter
    def CrashReport_LastOpenedCapture(self, value):
        pass

    @property
    def CrashReport_ReportedBugs(self) -> List[BugReport]:
        """
A list of :class:`BugReport` detailing previously submitted bugs that we're watching for updates.

:type: List[BugReport]
"""
        pass

    @CrashReport_ReportedBugs.setter
    def CrashReport_ReportedBugs(self, value: List[BugReport]):
        pass

    @property
    def CrashReport_ShouldRememberEmail(self):
        """
``True`` if the email address entered in the crash reporter should be remembered for next time. If no email is entered then nothing happens (any previous saved email is kept).

Defaults to ``True``.
"""
        pass

    @CrashReport_ShouldRememberEmail.setter
    def CrashReport_ShouldRememberEmail(self, value):
        pass

    @property
    def DefaultCaptureSaveDirectory(self):
        """The default path to save captures in, when browsing to save a temporary capture somewhere."""
        pass

    @DefaultCaptureSaveDirectory.setter
    def DefaultCaptureSaveDirectory(self, value):
        pass

    @property
    def DefaultReplayOptions(self) -> ReplayOptions:
        """
A :class:`ReplayOptions` containing the configured default replay options to use in most scenarios when no specific options are given.

:type: renderdoc.ReplayOptions
"""
        pass

    @DefaultReplayOptions.setter
    def DefaultReplayOptions(self, value: ReplayOptions):
        pass

    @property
    def DegradedCapture_LastUpdate(self):
        """A date containing the last time that the user was warned about captures being loaded in degraded support. This prevents the user being spammed if their hardware is low spec."""
        pass

    @DegradedCapture_LastUpdate.setter
    def DegradedCapture_LastUpdate(self, value):
        pass

    @property
    def EventBrowser_AddFake(self):
        """
``True`` if fake action marker regions should be added to captures that don't have any markers, for easier browsing. The regions are identified by grouping actions that write to the same targets together.

Defaults to ``True``.
"""
        pass

    @EventBrowser_AddFake.setter
    def EventBrowser_AddFake(self, value):
        pass

    @property
    def EventBrowser_ApplyColors(self):
        """
``True`` if the :class:`EventBrowser` should apply any colors specified with API marker regions.

Defaults to ``True``.
"""
        pass

    @EventBrowser_ApplyColors.setter
    def EventBrowser_ApplyColors(self, value):
        pass

    @property
    def EventBrowser_ColorEventRow(self):
        """
``True`` if when coloring marker regions in the :class:`EventBrowser`, the whole row should be colored instead of just a side-bar.

Defaults to ``True``.
"""
        pass

    @EventBrowser_ColorEventRow.setter
    def EventBrowser_ColorEventRow(self, value):
        pass

    @property
    def EventBrowser_TimeUnit(self):
        """
The :class:`TimeUnit` to use to display the duration column in the :class:`EventBrowser`.

Defaults to microseconds.
"""
        pass

    @EventBrowser_TimeUnit.setter
    def EventBrowser_TimeUnit(self, value):
        pass

    @property
    def ExternalTool_RadeonGPUProfiler(self):
        """The path to the executable of the external Radeon GPU Profiler tool."""
        pass

    @ExternalTool_RadeonGPUProfiler.setter
    def ExternalTool_RadeonGPUProfiler(self, value):
        pass

    @property
    def Font_Family(self):
        """
The font family to use in the UI.

Defaults to an empty string which means to use the system default.
"""
        pass

    @Font_Family.setter
    def Font_Family(self, value):
        pass

    @property
    def Font_GlobalScale(self):
        """
The global scale to apply to fonts in the application, expressed as a float.

Defaults to ``1.0`` which means 100%.
"""
        pass

    @Font_GlobalScale.setter
    def Font_GlobalScale(self, value):
        pass

    @property
    def Font_MonoFamily(self):
        """
The monospaced font family to use in the UI.

Defaults to an empty string which means to use the system default.
"""
        pass

    @Font_MonoFamily.setter
    def Font_MonoFamily(self, value):
        pass

    @property
    def Font_PreferMonospaced(self):
        """
``True`` if a monospaced font should be used in all places where data is displayed, even if the data is not tabular such as names.

Defaults to ``False``.
"""
        pass

    @Font_PreferMonospaced.setter
    def Font_PreferMonospaced(self, value):
        pass

    @property
    def Formatter_MaxFigures(self):
        """
The maximum number of decimal places to show in formatted floating point values.

.. note::
  The naming of 'MaxFigures' is a historical artifact - this controls the number of   decimal places only, not the number of significant figures.

Defaults to ``5``.
"""
        pass

    @Formatter_MaxFigures.setter
    def Formatter_MaxFigures(self, value):
        pass

    @property
    def Formatter_MinFigures(self):
        """
The minimum number of decimal places to show in formatted floating point values.

.. note::
  The naming of 'MinFigures' is a historical artifact - this controls the number of   decimal places only, not the number of significant figures.

Defaults to ``2``.
"""
        pass

    @Formatter_MinFigures.setter
    def Formatter_MinFigures(self, value):
        pass

    @property
    def Formatter_NegExp(self):
        """
The cut-off on negative exponents of a normalised values to display using scientific notation.

E.g. for a value of 5, anything below 1.0e-5 will be displayed using scientific notation.

Defaults to ``5``.
"""
        pass

    @Formatter_NegExp.setter
    def Formatter_NegExp(self, value):
        pass

    @property
    def Formatter_OffsetSizeDisplayMode(self):
        """
The formatting mode to use for values marked as Offsets or Sizes.

E.g. Auto: decimal by default and hexadecimal if above a certain threshold, Decimal: always use decimal, Hexadecimal: always use hexadecimal.
Defaults to ``Auto``.
"""
        pass

    @Formatter_OffsetSizeDisplayMode.setter
    def Formatter_OffsetSizeDisplayMode(self, value):
        pass

    @property
    def Formatter_PosExp(self):
        """
The cut-off on positive exponents of a normalised values to display using scientific notation.

E.g. for a value of 7, anything below 1.0e+7 will be displayed using scientific notation.

Defaults to ``7``.
"""
        pass

    @Formatter_PosExp.setter
    def Formatter_PosExp(self, value):
        pass

    @property
    def LastCaptureExe(self):
        """The filename of the last executable that was captured, inside :data:`LastCapturePath`."""
        pass

    @LastCaptureExe.setter
    def LastCaptureExe(self, value):
        pass

    @property
    def LastCaptureFilePath(self):
        """The path to the last capture to be opened, which is useful as a default location for browsing."""
        pass

    @LastCaptureFilePath.setter
    def LastCaptureFilePath(self, value):
        pass

    @property
    def LastCapturePath(self):
        """The path containing the last executable that was captured, which is useful as a default location for browsing."""
        pass

    @LastCapturePath.setter
    def LastCapturePath(self, value):
        pass

    @property
    def LastFileBrowsePath(self):
        """The path to the last file browsed to in any dialog. Used as a default location for all file browsers without another explicit default directory (such as opening capture files - see :data:`LastCaptureFilePath`)."""
        pass

    @LastFileBrowsePath.setter
    def LastFileBrowsePath(self, value):
        pass

    @property
    def LocalProxyAPI(self):
        """
The index of the local proxy API to use when using remote context replay. ``-1`` if the default proxy should be used.

Defaults to ``-1``.
"""
        pass

    @LocalProxyAPI.setter
    def LocalProxyAPI(self, value):
        pass

    @property
    def RecentCaptureFiles(self) -> List[str]:
        """
The recently opened capture files.

:type: List[str]
"""
        pass

    @RecentCaptureFiles.setter
    def RecentCaptureFiles(self, value: List[str]):
        pass

    @property
    def RecentCaptureSettings(self) -> List[str]:
        """
The recently opened capture settings files.

:type: List[str]
"""
        pass

    @RecentCaptureSettings.setter
    def RecentCaptureSettings(self, value: List[str]):
        pass

    @property
    def ShaderProcessors(self) -> List[ShaderProcessingTool]:
        """
A list of :class:`ShaderProcessingTool` detailing shader processing programs. The list comes in priority order, with earlier processors preferred over later ones.

:type: List[ShaderProcessingTool]
"""
        pass

    @ShaderProcessors.setter
    def ShaderProcessors(self, value: List[ShaderProcessingTool]):
        pass

    @property
    def TemporaryCaptureDirectory(self):
        """The path to where temporary capture files should be stored until they're saved permanently."""
        pass

    @TemporaryCaptureDirectory.setter
    def TemporaryCaptureDirectory(self, value):
        pass

    @property
    def TextureViewer_PerTexSettings(self):
        """
``True`` if the :class:`TextureViewer` should store most visualisation settings on a per-texture basis instead of keeping it persistent across different textures.

:Defaults to ``True``.
"""
        pass

    @TextureViewer_PerTexSettings.setter
    def TextureViewer_PerTexSettings(self, value):
        pass

    @property
    def TextureViewer_PerTexYFlip(self):
        """
``True`` if the :class:`TextureViewer` should treat y-flipping as a per-texture state rather than a global toggle.

Does nothing if per-texture settings are disabled in general.

Defaults to ``False``.
"""
        pass

    @TextureViewer_PerTexYFlip.setter
    def TextureViewer_PerTexYFlip(self, value):
        pass

    @property
    def TextureViewer_ResetRange(self):
        """
``True`` if the :class:`TextureViewer` should reset the visible range when a new texture is selected.

:Defaults to ``False``.
"""
        pass

    @TextureViewer_ResetRange.setter
    def TextureViewer_ResetRange(self, value):
        pass

    @property
    def TextureViewer_ShaderDirs(self) -> List[str]:
        """
List of the directories containing custom shader files for the Texture Viewer.

:type: List[str]
"""
        pass

    @TextureViewer_ShaderDirs.setter
    def TextureViewer_ShaderDirs(self, value: List[str]):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    @property
    def Tips_HasSeenFirst(self):
        """
``True`` if the user has seen the first tip, which should always be shown first before randomising.

Defaults to ``False``.
"""
        pass

    @Tips_HasSeenFirst.setter
    def Tips_HasSeenFirst(self, value):
        pass

    @property
    def UIStyle(self):
        """The style to load for the UI. Possible values include 'Native', 'RDLight', 'RDDark'. If empty, the closest of RDLight and RDDark will be chosen, based on the overall light-on-dark or dark-on-light theme of the application native style."""
        pass

    @UIStyle.setter
    def UIStyle(self, value):
        pass

    @property
    def UnsupportedAndroid_LastUpdate(self):
        """A date containing the last time that the user was warned about an Android device being older than is generally supported. This prevents the user being spammed if they consistently use an old Android device. If it has been more than 3 weeks since the last time an old device was seen, we re-warn the user, but if it's less than 3 weeks we silently update this date so continuous use doesn't nag."""
        pass

    @UnsupportedAndroid_LastUpdate.setter
    def UnsupportedAndroid_LastUpdate(self, value):
        pass


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFE18834DC0>, '__hash__': <slot wrapper '__hash__' of 'qrenderdoc.PersistantConfig' objects>, '__lt__': <slot wrapper '__lt__' of 'qrenderdoc.PersistantConfig' objects>, '__le__': <slot wrapper '__le__' of 'qrenderdoc.PersistantConfig' objects>, '__eq__': <slot wrapper '__eq__' of 'qrenderdoc.PersistantConfig' objects>, '__ne__': <slot wrapper '__ne__' of 'qrenderdoc.PersistantConfig' objects>, '__gt__': <slot wrapper '__gt__' of 'qrenderdoc.PersistantConfig' objects>, '__ge__': <slot wrapper '__ge__' of 'qrenderdoc.PersistantConfig' objects>, '__init__': <slot wrapper '__init__' of 'qrenderdoc.PersistantConfig' objects>, 'GetRemoteHosts': <method 'GetRemoteHosts' of 'qrenderdoc.PersistantConfig' objects>, 'GetRemoteHost': <method 'GetRemoteHost' of 'qrenderdoc.PersistantConfig' objects>, 'AddRemoteHost': <method 'AddRemoteHost' of 'qrenderdoc.PersistantConfig' objects>, 'RemoveRemoteHost': <method 'RemoveRemoteHost' of 'qrenderdoc.PersistantConfig' objects>, 'UpdateEnumeratedProtocolDevices': <method 'UpdateEnumeratedProtocolDevices' of 'qrenderdoc.PersistantConfig' objects>, 'Load': <method 'Load' of 'qrenderdoc.PersistantConfig' objects>, 'Save': <method 'Save' of 'qrenderdoc.PersistantConfig' objects>, 'Close': <method 'Close' of 'qrenderdoc.PersistantConfig' objects>, 'SetupFormatting': <method 'SetupFormatting' of 'qrenderdoc.PersistantConfig' objects>, 'SetStyle': <method 'SetStyle' of 'qrenderdoc.PersistantConfig' objects>, 'CheckUpdate_AllowChecks': <attribute 'CheckUpdate_AllowChecks' of 'qrenderdoc.PersistantConfig' objects>, 'UnsupportedAndroid_LastUpdate': <attribute 'UnsupportedAndroid_LastUpdate' of 'qrenderdoc.PersistantConfig' objects>, 'CheckUpdate_LastUpdate': <attribute 'CheckUpdate_LastUpdate' of 'qrenderdoc.PersistantConfig' objects>, 'DegradedCapture_LastUpdate': <attribute 'DegradedCapture_LastUpdate' of 'qrenderdoc.PersistantConfig' objects>, 'CrashReport_EmailAddress': <attribute 'CrashReport_EmailAddress' of 'qrenderdoc.PersistantConfig' objects>, 'RecentCaptureSettings': <attribute 'RecentCaptureSettings' of 'qrenderdoc.PersistantConfig' objects>, 'TextureViewer_PerTexSettings': <attribute 'TextureViewer_PerTexSettings' of 'qrenderdoc.PersistantConfig' objects>, 'ExternalTool_RadeonGPUProfiler': <attribute 'ExternalTool_RadeonGPUProfiler' of 'qrenderdoc.PersistantConfig' objects>, 'CheckUpdate_CurrentVersion': <attribute 'CheckUpdate_CurrentVersion' of 'qrenderdoc.PersistantConfig' objects>, 'RecentCaptureFiles': <attribute 'RecentCaptureFiles' of 'qrenderdoc.PersistantConfig' objects>, 'AllowProcessInject': <attribute 'AllowProcessInject' of 'qrenderdoc.PersistantConfig' objects>, 'UIStyle': <attribute 'UIStyle' of 'qrenderdoc.PersistantConfig' objects>, 'EventBrowser_TimeUnit': <attribute 'EventBrowser_TimeUnit' of 'qrenderdoc.PersistantConfig' objects>, 'LastCapturePath': <attribute 'LastCapturePath' of 'qrenderdoc.PersistantConfig' objects>, 'Formatter_MaxFigures': <attribute 'Formatter_MaxFigures' of 'qrenderdoc.PersistantConfig' objects>, 'Formatter_MinFigures': <attribute 'Formatter_MinFigures' of 'qrenderdoc.PersistantConfig' objects>, 'LastCaptureExe': <attribute 'LastCaptureExe' of 'qrenderdoc.PersistantConfig' objects>, 'TemporaryCaptureDirectory': <attribute 'TemporaryCaptureDirectory' of 'qrenderdoc.PersistantConfig' objects>, 'DefaultCaptureSaveDirectory': <attribute 'DefaultCaptureSaveDirectory' of 'qrenderdoc.PersistantConfig' objects>, 'CrashReport_ShouldRememberEmail': <attribute 'CrashReport_ShouldRememberEmail' of 'qrenderdoc.PersistantConfig' objects>, 'Comments_ShowOnLoad': <attribute 'Comments_ShowOnLoad' of 'qrenderdoc.PersistantConfig' objects>, 'TextureViewer_ResetRange': <attribute 'TextureViewer_ResetRange' of 'qrenderdoc.PersistantConfig' objects>, 'Formatter_NegExp': <attribute 'Formatter_NegExp' of 'qrenderdoc.PersistantConfig' objects>, 'Font_PreferMonospaced': <attribute 'Font_PreferMonospaced' of 'qrenderdoc.PersistantConfig' objects>, 'Font_MonoFamily': <attribute 'Font_MonoFamily' of 'qrenderdoc.PersistantConfig' objects>, 'Font_Family': <attribute 'Font_Family' of 'qrenderdoc.PersistantConfig' objects>, '__dict__': <attribute '__dict__' of 'qrenderdoc.PersistantConfig' objects>, 'ShaderProcessors': <attribute 'ShaderProcessors' of 'qrenderdoc.PersistantConfig' objects>, 'CrashReport_ReportedBugs': <attribute 'CrashReport_ReportedBugs' of 'qrenderdoc.PersistantConfig' objects>, 'TextureViewer_ShaderDirs': <attribute 'TextureViewer_ShaderDirs' of 'qrenderdoc.PersistantConfig' objects>, 'DefaultReplayOptions': <attribute 'DefaultReplayOptions' of 'qrenderdoc.PersistantConfig' objects>, 'AlwaysReplayLocally': <attribute 'AlwaysReplayLocally' of 'qrenderdoc.PersistantConfig' objects>, 'Analytics_ManualCheck': <attribute 'Analytics_ManualCheck' of 'qrenderdoc.PersistantConfig' objects>, 'AlwaysLoad_Extensions': <attribute 'AlwaysLoad_Extensions' of 'qrenderdoc.PersistantConfig' objects>, 'EventBrowser_AddFake': <attribute 'EventBrowser_AddFake' of 'qrenderdoc.PersistantConfig' objects>, 'TextureViewer_PerTexYFlip': <attribute 'TextureViewer_PerTexYFlip' of 'qrenderdoc.PersistantConfig' objects>, 'CheckUpdate_UpdateResponse': <attribute 'CheckUpdate_UpdateResponse' of 'qrenderdoc.PersistantConfig' objects>, 'LocalProxyAPI': <attribute 'LocalProxyAPI' of 'qrenderdoc.PersistantConfig' objects>, 'Font_GlobalScale': <attribute 'Font_GlobalScale' of 'qrenderdoc.PersistantConfig' objects>, 'LastFileBrowsePath': <attribute 'LastFileBrowsePath' of 'qrenderdoc.PersistantConfig' objects>, 'EventBrowser_ApplyColors': <attribute 'EventBrowser_ApplyColors' of 'qrenderdoc.PersistantConfig' objects>, 'CrashReport_EmailNagged': <attribute 'CrashReport_EmailNagged' of 'qrenderdoc.PersistantConfig' objects>, 'BufferFormatter_SavedFormats': <attribute 'BufferFormatter_SavedFormats' of 'qrenderdoc.PersistantConfig' objects>, 'AllowGlobalHook': <attribute 'AllowGlobalHook' of 'qrenderdoc.PersistantConfig' objects>, 'Analytics_TotalOptOut': <attribute 'Analytics_TotalOptOut' of 'qrenderdoc.PersistantConfig' objects>, 'Formatter_OffsetSizeDisplayMode': <attribute 'Formatter_OffsetSizeDisplayMode' of 'qrenderdoc.PersistantConfig' objects>, 'EventBrowser_ColorEventRow': <attribute 'EventBrowser_ColorEventRow' of 'qrenderdoc.PersistantConfig' objects>, 'CheckUpdate_UpdateAvailable': <attribute 'CheckUpdate_UpdateAvailable' of 'qrenderdoc.PersistantConfig' objects>, 'Formatter_PosExp': <attribute 'Formatter_PosExp' of 'qrenderdoc.PersistantConfig' objects>, 'Tips_HasSeenFirst': <attribute 'Tips_HasSeenFirst' of 'qrenderdoc.PersistantConfig' objects>, 'CrashReport_LastOpenedCapture': <attribute 'CrashReport_LastOpenedCapture' of 'qrenderdoc.PersistantConfig' objects>, 'LastCaptureFilePath': <attribute 'LastCaptureFilePath' of 'qrenderdoc.PersistantConfig' objects>, '__doc__': '\\nA persistant config file that is automatically loaded and saved, which contains any\\nsettings and information that needs to be preserved from one run to the next.\\n\\nFor more information about some of these settings that are user-facing see\\n:ref:`the documentation for the settings window <settings-window>`.\\n\\n'})"


