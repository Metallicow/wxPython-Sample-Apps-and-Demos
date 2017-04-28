#!/usr/bin/env python
#----------------------------------------------------------------------------
# Name:         Main.py
# Purpose:      Testing lots of stuff, controls, window types, etc.
#
# Author:       Robin Dunn
#
# Created:      A long time ago, in a galaxy far, far away...
# RCS-ID:       $Id: Main.py 71772 2012-06-14 22:37:10Z RD $
# Copyright:    (c) 1999 by Total Control Software
# Licence:      wxWindows license
# Tags:         phoenix-port
#----------------------------------------------------------------------------

# TODO List:
# * UI design more professional (is the new version more professional?)
# * Update main overview

# =====================
# = EXTERNAL Packages =
# =====================
# In order to let a package (like AGW) be included in the wxPython demo,
# the package owner should create a sub-directory of the wxPython demo folder
# in which all the package's demos should live. In addition, the sub-folder
# should contain a Python file called __demo__.py which, when imported, should
# contain the following methods:
#
# * GetDemoBitmap: returns the bitmap to be used in the wxPython demo tree control
#   in a PyEmbeddedImage format;
# * GetRecentAdditions: returns a list of demos which will be displayed under the
#   "Recent Additions/Updates" tree item. This list should be a subset (or the full
#   set) of the package's demos;
# * GetDemos: returns a tuple. The first item of the tuple is the package's name
#   as will be displayed in the wxPython demo tree, right after the "Custom Controls"
#   item. The second element of the tuple is the list of demos for the external package.
# * GetOverview: returns a wx.html-ready representation of the package's documentation.
#
# Please see the __demo__.py file in the demo/agw/ folder for an example.
# Last updated: Andrea Gavana, 20 Oct 2008, 18.00 GMT


#-Imports-------------------------------------------------------------------

#--Python Imports.
import os
import sys
if sys.version_info[0] == 2:
    print('Running Python 2')
    PYTHON2 = True
    PYTHON3 = False
elif sys.version_info[0] == 3:
    print('Running Python 3')
    PYTHON2 = False
    PYTHON3 = True
import time
import traceback
import types
import imp
try:
    import cPickle as pickle
except ImportError as exc:#py3
    import pickle
try:
    from cStringIO import StringIO
except ImportError as exc:#py3
    from io import StringIO
import re
try:
    import urllib2 as urllib
except ImportError as exc:#py3
    import urllib
import shutil
from threading import Thread

# Fixing the old bird...
import py_compile  # Compile files before executing them to look for syntax errors/etc.
import subprocess  # Launch individual demos.
import site  # Locate the wx.pth file in the site-packages directory.

try:
    import six
except ImportError:
    traceback.print_exc()
    try:
        import wx.lib.six as six
    except ImportError as exc:
        raise exc

#--wxPython Imports.
try:
    import wxversion
    wxversion.select('3.0.3-msw-phoenix')  # Used to force wxPython version
except ImportError:
    traceback.print_exc()
try:
    import wx
    # print(wx.version())
except ImportError:
    import tkinter_error
    msg = ('You must install wxPython, which can be downloaded at\n'
           'http://wxpython.org/')
    tkinter_error.tkinter_error(msg)
    exit()
import wx.adv
import wx.lib.agw.aui as aui
import wx.html
import wx.lib
from wx.lib.msgpanel import MessagePanel
from wx.adv import TaskBarIcon as TaskBarIcon
from wx.adv import SplashScreen as SplashScreen
import wx.lib.mixins.inspection
import wx.lib.mixins.listctrl as listmix
import wx.lib.wxpTag
if not hasattr(wx, 'ID_HELP_CONTENTS'):
    # Used for overview wxp online link buttons.
    wx.ID_HELP_CONTENTS = wx.NewId()


#--Local Imports.
import version
# from main_globals import _demoPngsList, _treeList


from ExceptionHookDialog import ExceptionHookDialog, ExceptionStrDialog

#- Override sys.excepthook ----------------------------
# Place this bit of code in your app if you want to overide sys.excepthook.
# Otherwise sys.excepthook defaults to sys.stderr
def custom_excepthook(excType, excValue, excTrace):
    excInfo=(excType, excValue, excTrace)
    ExceptionHookDialog(excInfo=excInfo).ShowModal()

## sys.excepthook = sys.stderr # Standard procedure

# Our ExceptionHookDialog will be called every time there is an error
# while the demo is actually running.
# This includes extended demos with TestPanels.
# Ex: Sometimes a demo will need to launch a frame(ex: show a "example" button)
# and the error might not have been caught in py_compiling and was
# ran into in the frames __init__ or somewhere after.
# We want to know right away where the error occured so it can be fixed. :)
sys.excepthook = custom_excepthook

#-Debugging-----------------------------------------------------------------
DEBUG = False

def debugPrint():
    print("\n=Debug" + "="*54)
    ## wx.Trap()
    print("wx.version() = %s" %(wx.version()))
    print("wx.VERSION_STRING = %s" %(wx.VERSION_STRING))
    print("pid = %s" %(os.getpid()))
    print(sys.version_info)
    print("sys.platform = %s" %(sys.platform))
    import platform
    if sys.platform.startswith('win'):
        win32_ver = platform.win32_ver()
        print('Microsoft Windows %s %s %s %s' %(win32_ver[0], win32_ver[1], win32_ver[2], win32_ver[3]))
    elif sys.platform.startswith('linux'):
        linux_dist = platform.linux_distribution()
        print('%s %s %s' %(linux_dist[0], linux_dist[1], linux_dist[2]))
    elif sys.platform.startswith('darwin'):
        mac_ver = platform.mac_ver()
        print('Macintosh %s %s %s' %(mac_ver[0], mac_ver[1], mac_ver[2]))
    print("sys.argv = %s" %(sys.argv))
    print("="*60)
    if PYTHON2:
        raw_input("Press Enter To Continue...")
    elif PYTHON3:
        input("Press Enter To Continue...")

if DEBUG:
    debugPrint()
elif len(sys.argv) > 1:
    for i in range(1, len(sys.argv)):
        arg = sys.argv[i]
        if "-d" or "-debug" in arg:
            debugPrint()
            break

#-Globals-------------------------------------------------------------------

gAppDir = os.path.dirname(os.path.abspath(sys.argv[0]))

# print(site.getsitepackages())
# for path in site.getsitepackages():
#     if 'site-packages' in path or 'dist-packages' in path: # Windows, Unix
#         sitePackagesDir = path
#         break
#
# if os.path.exists(sitePackagesDir + os.sep + 'wx.pth'):
#     # print(site.getsitepackages())
#     # returned on windows ['C:\\Python27', 'C:\\Python27\\lib\\site-packages']
#     ('site-packages', 'dist-packages')
#     wx_pth_Path = sitePackagesDir + os.sep + 'wx.pth'
#     fileIsOpen = open(wx_pth_Path, 'r')
#     wx_pth_Path_Contents = fileIsOpen.read()
#     fileIsOpen.close()
# else:
#     wx_pth_Path = 'wx.pth could not be located'
#     print(wx_pth_Path)
#     print(site.getsitepackages())
#     wx_pth_Path_Contents = 'wx.pth could not be located'

# We won't import the images module yet, but we'll assign it to this
# global when we do.
images = None

RUN_AS_PORTABLE_APP = True
try:
    PORTABLE_PATH = os.path.dirname(os.path.abspath(__file__))
except Exception as exc:
    PORTABLE_PATH = os.path.dirname(os.path.abspath(sys.argv[0]))

USE_CUSTOMTREECTRL = False
DEFAULT_PERSPECTIVE = "Default Perspective"

_styleTable = '<h3>Window %s</h3>\n' \
              '<p>This class supports the following window %s:\n' \
              '<p><table bgcolor=\"#ffffff\" border cols=1>'

_eventTable = '<h3>Events</h3>\n' \
              '<p>Events emitted by this class:\n' \
              '<p><table bgcolor=\"#ffffff\" border cols=1>'

_appearanceTable = '<h3>Appearance</h3>\n' \
                   '<p>Control appearance on various platform:\n' \
                   '<p><table bgcolor=\"#ffffff\" cellspacing=20>'

_styleHeaders = ["Style Name", "Description"]
_eventHeaders = ["Event Name", "Description"]
_headerTable = '<td><b>%s</b></td>'
_styleTag = '<td><tt>%s</tt></td>'
_eventTag = '<td><i>%s</i></td>'
_hexValues = '<td><font color="%s"> %s </font></td>'
_description = '<td>%s</td>'
_imageTag = '<td align=center valign=middle><a href="%s"><img src="%s" alt="%s"></a></td>'
_platformTag = '<td align=center><b>%s</b></td>'

_onlineURLS = ["http://www.wxwidgets.org/",
               "http://wxpython.org/",
               "http://www.python.org/"]
_trunkURL = "http://docs.wxwidgets.org/trunk/"
_docsURL = _trunkURL + "classwx%s.html"
_platformNames = ["wxMSW", "wxGTK", "wxMac"]


_importList = ["wx.aui", "wx.calendar", "wx.html", "wx.media", "wx.wizard",
               "wx.combo", "wx.animate", "wx.gizmos", "wx.glcanvas", "wx.grid",
               "wx.richtext", "wx.stc"]

_dirWX = dir(wx)
for mod in _importList:
    try:
        module = __import__(mod)
    except ImportError as exc:
        continue

_codePagePositions = {}

# Define a translation function.
_ = wx.GetTranslation


def imp_load_source_from_filePath(filePath):
    mod_name, file_ext = os.path.splitext(os.path.split(filePath)[-1])

    if file_ext.lower() in ('.py', '.pyw'):
        py_mod = imp.load_source(mod_name, filePath)

    return py_mod

#------------------------------------------------------------------------------

def ReplaceCapitals(string):
    """
    Replaces the capital letter in a string with an underscore plus the
    corresponding lowercase character.

    **Parameters:**

    * `string`: the string to be analyzed.
    """

    newString = ""
    for char in string:
        if char.isupper():
            newString += "_%s"%char.lower()
        else:
            newString += char

    return newString


def RemoveHTMLTags(data):
    """
    Removes all the HTML tags from a string.

    **Parameters:**

    * `data`: the string to be analyzed.
    """

    p = re.compile(r'<[^<]*?>')
    return p.sub('', data)


def FormatDocs(keyword, values, num):

    names = values.keys()
    names = sorted(values.keys())

    headers = (num == 2 and [_eventHeaders] or [_styleHeaders])[0]
    table = (num == 2 and [_eventTable] or [_styleTable])[0]
    if num == 3:
        text = "<br>" + table%(keyword.lower(), keyword.lower()) + "\n<tr>\n"
    else:
        text = "<br>" + table

    for indx in range(2):
        text += _headerTable%headers[indx]

    text += "\n</tr>\n"

    for name in names:

        text += "<tr>\n"

        description = values[name].strip()
        pythonValue = name.replace("wx", "wx.")

        if num == 3:

            colour = "#ff0000"
            value = "Unavailable"
            cutValue = pythonValue[3:]

            if cutValue in _dirWX:
                try:
                    val = eval(pythonValue)
                    value = "%s"%hex(val)
                    colour = "#0000ff"
                except AttributeError as exc:
                    value = "Unavailable"
            else:
                for packages in _importList:
                    if cutValue in dir(eval(packages)):
                        val = eval("%s.%s"%(packages, cutValue))
                        value = "%s"%hex(val)
                        colour = "#0000ff"
                        pythonValue = "%s.%s"%(packages, cutValue)
                        break

            text += _styleTag%pythonValue + "\n"

        else:

            text += _eventTag%pythonValue + "\n"

        text += _description%FormatDescription(description) + "\n"
        text += "</tr>\n"

    text += "\n</table>\n\n<p>"
    return text


def FormatDescription(description):
    """
    Formats a wxWidgets C++ description in a more wxPython-based way.

    **Parameters:**

    * `description`: the string description to be formatted.
    """

    description = description.replace("wx", "wx.")
    description = description.replace("EVT_COMMAND", "wxEVT_COMMAND")
    description = description.replace("wx.Widgets", "wxWidgets")

    return description


def FormatImages(appearance):

    text = "<p><br>" + _appearanceTable

    for indx in range(2):
        text += "\n<tr>\n"
        for key in _platformNames:
            if indx == 0:
                src = appearance[key]
                alt = key + "Appearance"
                text += _imageTag%(src, src, alt)
            else:
                text += _platformTag%key

        text += "</tr>\n"

    text += "\n</table>\n\n<p>"
    return text


def FindWindowStyles(text, originalText, widgetName):
    """
    Finds the windows styles and events in the input text.

    **Parameters:**

    * `text`: the wxWidgets C++ docs for a particular widget/event, stripped
              of all HTML tags;
    * `originalText`: the wxWidgets C++ docs for a particular widget/event, with
              all HTML tags.
    """

    winStyles, winEvents, winExtra, winAppearance = {}, {}, {}, {}
    inStyle = inExtra = inEvent = False

    for line in text:
        if "following styles:" in line:
            inStyle = True
            continue

        elif "Event macros" in line:
            inEvent = True
            continue

        if "following extra styles:" in line:
            inExtra = True
            continue

        if "Appearance:" in line:
            winAppearance = FindImages(originalText, widgetName)
            continue

        elif not line.strip():
            inStyle = inEvent = inExtra = False
            continue

        if inStyle:
            start = line.index(':')
            windowStyle = line[0:start]
            styleDescription = line[start+1:]
            winStyles[windowStyle] = styleDescription
        elif inEvent:
            start = line.index(':')
            eventName = line[0:start]
            eventDescription = line[start+1:]
            winEvents[eventName] = eventDescription
        elif inExtra:
            start = line.index(':')
            styleName = line[0:start]
            styleDescription = line[start+1:]
            winExtra[styleName] = styleDescription

    return winStyles, winEvents, winExtra, winAppearance


def FindImages(text, widgetName):
    """
    When the wxWidgets docs contain a/the control appearance (a screenshot of the
    control), this method will try and download the images.

    **Parameters:**

    * `text`: the wxWidgets C++ docs for a particular widget/event, with
              all HTML tags.
    """

    winAppearance = {}
    start = text.find("class='appearance'")

    if start < 0:
        return winAppearance

    imagesDir = GetDocImagesDir()

    end = start + text.find("</table>")
    text = text[start:end]
    split = text.split()

    for indx, items in enumerate(split):

        if "src=" in items:
            possibleImage = items.replace("src=", "").strip()
            possibleImage = possibleImage.replace("'", "")
            f = urllib.urlopen(_trunkURL + possibleImage)
            stream = f.read()

        elif "alt=" in items:
            plat = items.replace("alt=", "").replace("'", "").strip()
            path = os.path.join(imagesDir, plat, widgetName + ".png")
            if not os.path.isfile(path):
                image = wx.Image(StringIO.StringIO(stream))
                image.SaveFile(path, wx.BITMAP_TYPE_PNG)

            winAppearance[plat] = path

    return winAppearance


#------------------------------------------------------------------------------
# Set up a thread that will scan the wxWidgets docs for window styles,
# events and widgets screenshots

class InternetThread(Thread):
    """ Worker thread class to attempt connection to the internet. """

    def __init__(self, notifyWindow, selectedClass):

        Thread.__init__(self)

        self.notifyWindow = notifyWindow
        self.selectedClass = selectedClass
        self.keepRunning = True
        self.setDaemon(True)

        self.start()


    def run(self):
        """ Run the worker thread. """

        # This is the code executing in the new thread. Simulation of
        # a long process as a simple urllib2/urllib call

        try:
            url = _docsURL % ReplaceCapitals(self.selectedClass)
            fid = urllib.urlopen(url)

            originalText = fid.read()
            text = RemoveHTMLTags(originalText).split("\n")
            data = FindWindowStyles(text, originalText, self.selectedClass)

            if not self.keepRunning:
                return

            wx.CallAfter(self.notifyWindow.LoadDocumentation, data)
        except (IOError, urllib.HTTPError) as exc:
            # Unable to get to the internet
            t, v = sys.exc_info()[:2]
            message = traceback.format_exception_only(t, v)
            wx.CallAfter(self.notifyWindow.StopDownload, message)
        except Exception as exc:
            # Some other strange error...
            t, v = sys.exc_info()[:2]
            message = traceback.format_exception_only(t, v)
            wx.CallAfter(self.notifyWindow.StopDownload, message)


#------------------------------------------------------------------------------
# Show how to derive a custom wxLog class

class MyLog(wx.Log):
    def __init__(self, textCtrl, logTime=0):
        wx.Log.__init__(self)
        self.tc = textCtrl
        self.logTime = logTime

    def DoLogText(self, message):
        if self.tc:
            self.tc.AppendText(message + '\n')



#------------------------------------------------------------------------------
# A class to be used to display source code in the demo.  Try using the
# wxSTC in the StyledTextCtrl_2 sample first, fall back to wxTextCtrl
# if there is an error, such as the stc module not being present.
#

try:
    ##raise ImportError  # for testing the alternate implementation
    from wx import stc
    from StyledTextCtrl_DemoCode import PythonSTC

    class DemoCodeEditor(PythonSTC):
        __doc__ = wx.stc.StyledTextCtrl.__doc__
        def __init__(self, parent, style=wx.BORDER_NONE):
            PythonSTC.__init__(self, parent, -1, style=style)
            self.parent = parent

            global gSTC
            gSTC = self

            global gStcConfig
            gStcConfig = GetStcConfig()
            self.SetUpEditorFromConfig(stcConfig=gStcConfig)

            # self.SetUpEditor()

        # Some methods to make it compatible with how the wxTextCtrl is used
        def SetValue(self, value):
            ## value = value.decode('iso8859_1')
            val = self.GetReadOnly()
            self.SetReadOnly(False)
            self.SetText(value)
            self.EmptyUndoBuffer()
            self.SetSavePoint()
            self.SetReadOnly(val)

        def SetEditable(self, val):
            self.SetReadOnly(not val)

        def IsModified(self):
            return self.GetModify()

        def Clear(self):
            self.ClearAll()

        def SetInsertionPoint(self, pos):
            self.SetCurrentPos(pos)
            self.SetAnchor(pos)

        def ShowPosition(self, pos):
            line = self.LineFromPosition(pos)
            #self.EnsureVisible(line)
            self.GotoLine(line)

        def GetLastPosition(self):
            return self.GetLength()

        def GetPositionFromLine(self, line):
            return self.PositionFromLine(line)

        def GetRange(self, start, end):
            return self.GetTextRange(start, end)

        def GetSelection(self):
            return self.GetAnchor(), self.GetCurrentPos()

        def SetSelection(self, start, end):
            self.SetSelectionStart(start)
            self.SetSelectionEnd(end)

        def SelectLine(self, line):
            start = self.PositionFromLine(line)
            end = self.GetLineEndPosition(line)
            self.SetSelection(start, end)

        def SetUpEditor(self):
            """
            This method carries out the work of setting up the demo editor.
            It's seperate so as not to clutter up the init code.
            """
            import keyword

            self.SetLexer(stc.STC_LEX_PYTHON)
            self.SetKeyWords(0, " ".join(keyword.kwlist))

            # Enable folding
            self.SetProperty("fold", "1" )

            # Highlight tab/space mixing (shouldn't be any)
            self.SetProperty("tab.timmy.whinge.level", "1")

            # Set left and right margins
            self.SetMargins(2,2)

            # Set up the numbers in the margin for margin #1
            self.SetMarginType(1, wx.stc.STC_MARGIN_NUMBER)
            # Reasonable value for, say, 4-5 digits using a mono font (40 pix)
            self.SetMarginWidth(1, 40)

            # Indentation and tab stuff
            self.SetIndent(4)               # Proscribed indent size for wx
            self.SetIndentationGuides(True) # Show indent guides
            self.SetBackSpaceUnIndents(True)# Backspace unindents rather than delete 1 space
            self.SetTabIndents(True)        # Tab key indents
            self.SetTabWidth(4)             # Proscribed tab size for wx
            self.SetUseTabs(False)          # Use spaces rather than tabs, or
                                            # TabTimmy will complain!
            # White space
            self.SetViewWhiteSpace(False)   # Don't view white space

            # EOL: Since we are loading/saving ourselves, and the
            # strings will always have \n's in them, set the STC to
            # edit them that way.
            self.SetEOLMode(wx.stc.STC_EOL_LF)
            self.SetViewEOL(False)

            # No right-edge mode indicator
            self.SetEdgeMode(stc.STC_EDGE_NONE)

            # Setup a margin to hold fold markers
            self.SetMarginType(2, stc.STC_MARGIN_SYMBOL)
            self.SetMarginMask(2, stc.STC_MASK_FOLDERS)
            self.SetMarginSensitive(2, True)
            self.SetMarginWidth(2, 12)

            # and now set up the fold markers
            self.MarkerDefine(stc.STC_MARKNUM_FOLDEREND,     stc.STC_MARK_BOXPLUSCONNECTED,  "white", "black")
            self.MarkerDefine(stc.STC_MARKNUM_FOLDEROPENMID, stc.STC_MARK_BOXMINUSCONNECTED, "white", "black")
            self.MarkerDefine(stc.STC_MARKNUM_FOLDERMIDTAIL, stc.STC_MARK_TCORNER,  "white", "black")
            self.MarkerDefine(stc.STC_MARKNUM_FOLDERTAIL,    stc.STC_MARK_LCORNER,  "white", "black")
            self.MarkerDefine(stc.STC_MARKNUM_FOLDERSUB,     stc.STC_MARK_VLINE,    "white", "black")
            self.MarkerDefine(stc.STC_MARKNUM_FOLDER,        stc.STC_MARK_BOXPLUS,  "white", "black")
            self.MarkerDefine(stc.STC_MARKNUM_FOLDEROPEN,    stc.STC_MARK_BOXMINUS, "white", "black")

            # Global default style
            if wx.Platform == '__WXMSW__':
                self.StyleSetSpec(stc.STC_STYLE_DEFAULT,
                                  'fore:#000000,back:#FFFFFF,face:Courier New')
            elif wx.Platform == '__WXMAC__':
                # TODO: if this looks fine on Linux too, remove the Mac-specific case
                # and use this whenever OS != MSW.
                self.StyleSetSpec(stc.STC_STYLE_DEFAULT,
                                  'fore:#000000,back:#FFFFFF,face:Monaco')
            else:
                defsize = wx.SystemSettings.GetFont(wx.SYS_ANSI_FIXED_FONT).GetPointSize()
                self.StyleSetSpec(stc.STC_STYLE_DEFAULT,
                                  'fore:#000000,back:#FFFFFF,face:Courier,size:%d'%defsize)

            # Clear styles and revert to default.
            self.StyleClearAll()

            # Following style specs only indicate differences from default.
            # The rest remains unchanged.

            # Line numbers in margin
            self.StyleSetSpec(wx.stc.STC_STYLE_LINENUMBER,'fore:#000000,back:#99A9C2')
            # Highlighted brace
            self.StyleSetSpec(wx.stc.STC_STYLE_BRACELIGHT,'fore:#00009D,back:#FFFF00')
            # Unmatched brace
            self.StyleSetSpec(wx.stc.STC_STYLE_BRACEBAD,'fore:#00009D,back:#FF0000')
            # Indentation guide
            self.StyleSetSpec(wx.stc.STC_STYLE_INDENTGUIDE, "fore:#CDCDCD")

            # Python styles
            self.StyleSetSpec(wx.stc.STC_P_DEFAULT, 'fore:#000000')
            # Comments
            self.StyleSetSpec(wx.stc.STC_P_COMMENTLINE,  'fore:#008000,back:#F0FFF0')
            self.StyleSetSpec(wx.stc.STC_P_COMMENTBLOCK, 'fore:#008000,back:#F0FFF0')
            # Numbers
            self.StyleSetSpec(wx.stc.STC_P_NUMBER, 'fore:#008080')
            # Strings and characters
            self.StyleSetSpec(wx.stc.STC_P_STRING, 'fore:#800080')
            self.StyleSetSpec(wx.stc.STC_P_CHARACTER, 'fore:#800080')
            # Keywords
            self.StyleSetSpec(wx.stc.STC_P_WORD, 'fore:#000080,bold')
            # Triple quotes
            self.StyleSetSpec(wx.stc.STC_P_TRIPLE, 'fore:#800080,back:#FFFFEA')
            self.StyleSetSpec(wx.stc.STC_P_TRIPLEDOUBLE, 'fore:#800080,back:#FFFFEA')
            # Class names
            self.StyleSetSpec(wx.stc.STC_P_CLASSNAME, 'fore:#0000FF,bold')
            # Function names
            self.StyleSetSpec(wx.stc.STC_P_DEFNAME, 'fore:#008080,bold')
            # Operators
            self.StyleSetSpec(wx.stc.STC_P_OPERATOR, 'fore:#800000,bold')
            # Identifiers. I leave this as not bold because everything seems
            # to be an identifier if it doesn't match the above criteria
            self.StyleSetSpec(wx.stc.STC_P_IDENTIFIER, 'fore:#000000')

            # Caret color
            self.SetCaretForeground("BLUE")
            # Selection background
            self.SetSelBackground(1, '#66CCFF')

            self.SetSelBackground(True, wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))
            self.SetSelForeground(True, wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))


        def RegisterModifiedEvent(self, eventHandler):
            self.Bind(wx.stc.EVT_STC_CHANGE, eventHandler)


except ImportError as exc:
    class DemoCodeEditor(wx.TextCtrl):
        def __init__(self, parent):
            wx.TextCtrl.__init__(self, parent, -1, style=
                                 wx.TE_MULTILINE | wx.HSCROLL | wx.TE_RICH2 | wx.TE_NOHIDESEL)

        def RegisterModifiedEvent(self, eventHandler):
            self.Bind(wx.EVT_TEXT, eventHandler)

        def SetReadOnly(self, flag):
            self.SetEditable(not flag)
            # NOTE: STC already has this method

        def GetText(self):
            return self.GetValue()

        def GetPositionFromLine(self, line):
            return self.XYToPosition(0,line)

        def GotoLine(self, line):
            pos = self.GetPositionFromLine(line)
            self.SetInsertionPoint(pos)
            self.ShowPosition(pos)

        def SelectLine(self, line):
            start = self.GetPositionFromLine(line)
            end = start + self.GetLineLength(line)
            self.SetSelection(start, end)


#------------------------------------------------------------------------------
# Constants for module versions

modOriginal = 0
modModified = 1
modDefault = modOriginal

#------------------------------------------------------------------------------

class DemoCodePanel(wx.Panel):
    """Panel for the 'Demo Code' tab"""
    __doc__ = wx.Panel.__doc__
    def __init__(self, parent, mainFrame):
        wx.Panel.__init__(self, parent, size=(1,1))
        if 'wxMSW' in wx.PlatformInfo:
            self.Hide()
        self.mainFrame = mainFrame
        self.editor = DemoCodeEditor(self)
        self.editor.RegisterModifiedEvent(self.OnCodeModified)
        self.editorStatusBar = wx.TextCtrl(self, -1, 'Ready to code :)', style=wx.TE_READONLY)

        self.btnSave = wx.Button(self, -1, "Save Changes")
        self.btnRestore = wx.Button(self, -1, "Delete Modified")
        self.btnSave.Enable(False)
        self.btnSave.Bind(wx.EVT_BUTTON, self.OnSave)
        self.btnRestore.Bind(wx.EVT_BUTTON, self.OnRestore)

        self.radioButtons = { modOriginal: wx.RadioButton(self, -1, "Original", style=wx.RB_GROUP),
                              modModified: wx.RadioButton(self, -1, "Modified") }

        self.controlBox = wx.BoxSizer(wx.HORIZONTAL)
        self.controlBox.Add(wx.StaticText(self, -1, "Active Version:"), 0,
                            wx.RIGHT | wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 5)
        for modID, radioButton in self.radioButtons.items():
            self.controlBox.Add(radioButton, 0, wx.EXPAND | wx.RIGHT, 5)
            radioButton.modID = modID # makes it easier for the event handler
            radioButton.Bind(wx.EVT_RADIOBUTTON, self.OnRadioButton)

        self.controlBox.Add(self.btnSave, 0, wx.RIGHT, 5)
        self.controlBox.Add(self.btnRestore, 0)

        self.box = wx.BoxSizer(wx.VERTICAL)
        self.box.Add(self.controlBox, 0, wx.EXPAND)
        self.box.Add(wx.StaticLine(self), 0, wx.EXPAND)
        self.box.Add(self.editor, 1, wx.EXPAND)
        self.box.Add(self.editorStatusBar, 0, wx.EXPAND)

        self.box.Fit(self)
        self.SetSizer(self.box)


    # Loads a demo from a DemoModules object
    def LoadDemo(self, demoModules):
        self.demoModules = demoModules
        if (modDefault == modModified) and demoModules.Exists(modModified):
            demoModules.SetActive(modModified)
        else:
            demoModules.SetActive(modOriginal)
        self.radioButtons[demoModules.GetActiveID()].Enable(True)
        self.ActiveModuleChanged()


    def ActiveModuleChanged(self):
        self.LoadDemoSource(self.demoModules.GetSource())
        self.UpdateControlState()
        self.mainFrame.pnl.Freeze()
        self.ReloadDemo()
        self.mainFrame.pnl.Thaw()


    def LoadDemoSource(self, source):
        self.editor.Clear()
        self.editor.SetValue(source)
        self.JumpToLine(0)
        self.btnSave.Enable(False)


    def JumpToLine(self, line, highlight=False):
        self.editor.GotoLine(line)
        self.editor.SetFocus()
        if highlight:
            self.editor.SelectLine(line)


    def UpdateControlState(self):
        active = self.demoModules.GetActiveID()
        # Update the radio/restore buttons
        for moduleID in self.radioButtons:
            btn = self.radioButtons[moduleID]
            if moduleID == active:
                btn.SetValue(True)
            else:
                btn.SetValue(False)

            if self.demoModules.Exists(moduleID):
                btn.Enable(True)
                if moduleID == modModified:
                    self.btnRestore.Enable(True)
            else:
                btn.Enable(False)
                if moduleID == modModified:
                    self.btnRestore.Enable(False)


    def OnRadioButton(self, event):
        radioSelected = event.GetEventObject()
        modSelected = radioSelected.modID
        if modSelected != self.demoModules.GetActiveID():
            busy = wx.BusyInfo("Reloading demo module...")
            self.demoModules.SetActive(modSelected)
            self.ActiveModuleChanged()


    def ReloadDemo(self):
        if self.demoModules.name != __name__:
            self.mainFrame.RunModule()


    def OnCodeModified(self, event):
        self.btnSave.Enable(self.editor.IsModified())


    def OnSave(self, event): # NOTE DEV Def for saving in the demo of original files.
        fileWrite = open(self.editor.filePath, 'w')
        try:
            fileWrite.write(u'%s' % self.editor.GetTextUTF8())
        except Exception as exc:
            fileWrite.write(u'%s' % self.editor.GetText())
        fileWrite.close()
        print('self.editor.filePath = %s' % self.editor.filePath)
        print('Saved')

        wx.CallAfter(gMainWin.tree.OnTreeSelChanged)
        # wx.CallAfter(gMainWin.LoadDemo, self.editor.filePath)

    def zOnSave(self, event):
        if self.demoModules.Exists(modModified):
            if self.demoModules.GetActiveID() == modOriginal:
                overwriteMsg = "You are about to overwrite an already existing modified copy\n" + \
                               "Do you want to continue?"
                dlg = wx.MessageDialog(self, overwriteMsg, "wxPython Demo",
                                       wx.YES_NO | wx.NO_DEFAULT| wx.ICON_EXCLAMATION)
                result = dlg.ShowModal()
                if result == wx.ID_NO:
                    return
                dlg.Destroy()

        self.demoModules.SetActive(modModified)
        modifiedFilename = GetModifiedFilename(self.demoModules.name)

        # Create the demo directory if one doesn't already exist
        if not os.path.exists(GetModifiedDirectory()):
            try:
                os.makedirs(GetModifiedDirectory())
                if not os.path.exists(GetModifiedDirectory()):
                    wx.LogMessage("BUG: Created demo directory but it still doesn't exist")
                    raise AssertionError
            except Exception as exc:
                wx.LogMessage("Error creating demo directory: %s" % GetModifiedDirectory())
                return
            else:
                wx.LogMessage("Created directory for modified demos: %s" % GetModifiedDirectory())

        # Save
        f = open(modifiedFilename, "wt")
        source = self.editor.GetText()
        try:
            f.write(source)
        finally:
            f.close()

        busy = wx.BusyInfo("Reloading demo module...")
        self.demoModules.LoadFromFile(modModified, modifiedFilename)
        self.ActiveModuleChanged()

        self.mainFrame.SetTreeModified(True)


    def OnRestore(self, event): # Handles the "Delete Modified" button
        modifiedFilename = GetModifiedFilename(self.demoModules.name)
        self.demoModules.Delete(modModified)
        os.unlink(modifiedFilename) # Delete the modified copy
        busy = wx.BusyInfo("Reloading demo module...")

        self.ActiveModuleChanged()

        self.mainFrame.SetTreeModified(False)

        gMainWin.OnTreeSelChanged() # this should fix deleting a modified file then resaving one right after.


#------------------------------------------------------------------------------

def opj(path):
    """Convert paths to the platform-specific separator"""
    st = os.path.normpath(path.replace('/', os.sep))
    # HACK: on Linux, a leading / gets lost...
    if path.startswith('/'):
        st = '/' + st
    return st


def GetDataDir():
    """
    Return the standard location on this platform for application data
    """
    if RUN_AS_PORTABLE_APP:
        return PORTABLE_PATH
    else:
        sp = wx.StandardPaths.Get()
        return sp.GetUserDataDir()

def GetConfigDirectory():
    """
    Returns the directory where configuration for the demo
    are stored
    """
    return os.path.join(GetDataDir(), "config")

def GetModifiedDirectory():
    """
    Returns the directory where modified versions of the demo files
    are stored
    """
    if RUN_AS_PORTABLE_APP:
        return PORTABLE_PATH + os.sep + "modified"
    else:
        return os.path.join(GetDataDir(), "modified")


def GetModifiedFilename(name):
    """
    Returns the filename of the modified version of the specified demo
    """
    if not name.endswith(".py"):
        name = name + ".py"
    return os.path.join(GetModifiedDirectory(), name)


def GetOriginalFilename(name):
    """
    Returns the filename of the original version of the specified demo
    """
    if not name.endswith(".py"):
        name = name + ".py"

    if os.path.isfile(name):
        return name

    originalDir = os.getcwd()
    listDir = os.listdir(originalDir)
    # Loop over the content of the demo directory
    for item in listDir:
        if not os.path.isdir(item):
            # Not a directory, continue
            continue
        dirFile = os.listdir(item)
        # See if a file called "name" is there
        if name in dirFile:
            return os.path.join(item, name)

    # We must return a string...
    return ""


def DoesModifiedExist(name):
    """Returns whether the specified demo has a modified copy"""
    if os.path.exists(GetModifiedFilename(name)):
        return True
    else:
        return False


def GetConfig():
    if not os.path.exists(GetDataDir()):
        os.makedirs(GetDataDir())

    config = wx.FileConfig(
        localFilename=os.path.join(GetDataDir(), "config", "options"))
    return config

def GetStcConfig():
    if not os.path.exists(GetDataDir()):
        os.makedirs(GetDataDir())

    configFileLoc = os.path.join(GetDataDir(),
                                 "config",
                                 "StcCodePageSettings.ini")

    config = wx.FileConfig(localFilename=configFileLoc)

    return config


def MakeDocDirs():

    docDir = os.path.join(GetDataDir(), "docs")
    if not os.path.exists(docDir):
        os.makedirs(docDir)

    for plat in _platformNames:
        imageDir = os.path.join(docDir, "images", plat)
        if not os.path.exists(imageDir):
            os.makedirs(imageDir)


def GetDocFile():

    docFile = os.path.join(GetDataDir(), "docs", "TrunkDocs.pkl")

    return docFile


def GetDocImagesDir():

    MakeDocDirs()
    return os.path.join(GetDataDir(), "docs", "images")


def SearchDemo(name, keyword):
    """ Returns whether a demo contains the search keyword or not. """
    fid = open(GetOriginalFilename(name), "rt")
    fullText = fid.read()
    fid.close()

    fullText = fullText.decode("iso-8859-1")

    if fullText.find(keyword) >= 0:
        return True

    return False


def HuntExternalDemos():
    """
    Searches for external demos (i.e. packages like AGW) in the wxPython
    demo sub-directories. In order to be found, these external packages
    must have a __demo__.py file in their directory.
    """

    externalDemos = {}
    originalDir = os.getcwd()
    listDir = os.listdir(originalDir)
    # Loop over the content of the demo directory
    for item in listDir:
        if not os.path.isdir(item):
            # Not a directory, continue
            continue
        dirFile = os.listdir(item)
        # See if a __demo__.py file is there
        if "__demo__.py" in dirFile:
            # Extend sys.path and import the external demos
            # sys.path.append(item)
            sys.path.append(os.path.abspath(item))
            hmm = __import__("__demo__")
            import importlib
            externalDemos[item] = importlib.import_module('%s.__demo__'%item)

    if not externalDemos:
        # Nothing to import...
        return {}

    # Modify the tree items and icons
    index = 0
    for category, demos in _treeList:
        # We put the external packages right before the
        # More Windows/Controls item
        if category == "More Windows/Controls":
            break
        index += 1

    # Sort and reverse the external demos keys so that they
    # come back in alphabetical order
    keys = externalDemos.keys()
    keys = sorted(externalDemos.keys())
    keys = reversed(keys)

    # Loop over all external packages
    for extern in keys:
        package = externalDemos[extern]
        # Insert a new package in the _treeList of demos
        _treeList.insert(index, package.GetDemos())
        # Get the recent additions for this package
        _treeList[0][1].extend(package.GetRecentAdditions())
        # Extend the demo bitmaps and the catalog
        _demoPngsList.insert(index+1, extern)
        images.catalog[extern] = package.GetDemoBitmap()

    # That's all folks...
    return externalDemos


def LookForExternals(externalDemos, demoName):
    """
    Checks if a demo name is in any of the external packages (like AGW) or
    if the user clicked on one of the external packages parent items in the
    tree, in which case it returns the html overview for the package.
    """

    pkg = overview = None
    # Loop over all the external demos
    for key, package in externalDemos.items():
        # Get the tree item name for the package and its demos
        treeName, treeDemos = package.GetDemos()
        # Get the overview for the package
        treeOverview = package.GetOverview()
        if treeName == demoName:
            # The user clicked on the parent tree item, return the overview
            return pkg, treeOverview
        elif demoName in treeDemos:
            # The user clicked on a real demo, return the package
            return key, overview

    # No match found, return None for both
    return pkg, overview

#------------------------------------------------------------------------------

class ModuleDictWrapper(object):
    """Emulates a module with a dynamically compiled __dict__"""
    def __init__(self, dict):
        self.dict = dict

    def __getattr__(self, name):
        if name in self.dict:
            return self.dict[name]
        else:
            raise AttributeError


class DemoModules(object):
    """
    Dynamically manages the original/modified versions of a demo
    module
    """
    def __init__(self, name):
        self.modActive = -1
        self.name = name

        #              (dict , source ,  filename , description   , error information )
        #              (  0  ,   1    ,     2     ,      3        ,          4        )
        self.modules = [[dict(),  ""    ,    ""     , "<original>"  ,        None],
                        [dict(),  ""    ,    ""     , "<modified>"  ,        None]]

        for i in [modOriginal, modModified]:
            self.modules[i][0]['__file__'] = \
                os.path.join(os.getcwd(), GetOriginalFilename(name))

        # load original module
        self.LoadFromFile(modOriginal, GetOriginalFilename(name))
        self.SetActive(modOriginal)

        # load modified module (if one exists)
        if DoesModifiedExist(name):
            self.LoadFromFile(modModified, GetModifiedFilename(name))


    def LoadFromFile(self, modID, filename):
        self.modules[modID][2] = filename
        file = open(filename, "rt")
        self.LoadFromSource(modID, file.read())
        file.close()

    def LoadFromSource(self, modID, source):
        self.modules[modID][1] = source
        self.LoadDict(modID)

    def LoadDict(self, modID):
        if self.name != __name__:
            source = self.modules[modID][1]
            description = self.modules[modID][2]
            description = description.encode(sys.getfilesystemencoding())

            try:
                code = compile(source, description, "exec")
                six.exec_(code, self.modules[modID][0])
            except Exception as exc:
                self.modules[modID][4] = DemoError(sys.exc_info())
                self.modules[modID][0] = None
            else:
                self.modules[modID][4] = None

    def SetActive(self, modID):
        if modID != modOriginal and modID != modModified:
            raise LookupError
        else:
            self.modActive = modID

    def GetActive(self):
        dict = self.modules[self.modActive][0]
        if dict is None:
            return None
        else:
            return ModuleDictWrapper(dict)

    def GetActiveID(self):
        return self.modActive

    def GetSource(self, modID = None):
        if modID is None:
            modID = self.modActive
        return self.modules[modID][1]

    def GetFilename(self, modID = None):
        if modID is None:
            modID = self.modActive
        return self.modules[self.modActive][2]

    def GetErrorInfo(self, modID = None):
        if modID is None:
            modID = self.modActive
        return self.modules[self.modActive][4]

    def Exists(self, modID):
        return self.modules[modID][1] != ""

    def UpdateFile(self, modID = None):
        """Updates the file from which a module was loaded
        with (possibly updated) source"""
        if modID is None:
            modID = self.modActive

        source = self.modules[modID][1]
        filename = self.modules[modID][2]

        try:
            file = open(filename, "wt")
            file.write(source)
        finally:
            file.close()

    def Delete(self, modID):
        if self.modActive == modID:
            self.SetActive(0)

        self.modules[modID][0] = None
        self.modules[modID][1] = ""
        self.modules[modID][2] = ""


#------------------------------------------------------------------------------

class DemoError(object):
    """Wraps and stores information about the current exception"""
    def __init__(self, exc_info):
        import copy

        excType, excValue = exc_info[:2]
        # traceback list entries: (filename, line number, function name, text)
        self.traceback = traceback.extract_tb(exc_info[2])

        # --Based on traceback.py::format_exception_only()--
        if PYTHON2:
            if type(excType) == types.ClassType:
                self.exception_type = excType.__name__
            else:
                self.exception_type = excType
        elif PYTHON3:
            if type(excType) == type:
                self.exception_type = excType.__name__
            else:
                self.exception_type = excType

        # If it's a syntax error, extra information needs
        # to be added to the traceback
        if excType is SyntaxError:
            try:
                msg, (filename, lineno, self.offset, line) = excValue
            except Exception as exc:
                pass
            else:
                if not filename:
                    filename = "<string>"
                line = line.strip()
                self.traceback.append( (filename, lineno, "", line) )
                excValue = msg
        try:
            self.exception_details = str(excValue)
        except Exception as exc:
            self.exception_details = "<unprintable %s object>" & type(excValue).__name__

        del exc_info

    def __str__(self):
        ret = "Type %s \n \
        Traceback: %s \n \
        Details  : %s" % ( str(self.exception_type), str(self.traceback), self.exception_details )
        return ret

#------------------------------------------------------------------------------

class DemoErrorPanel(wx.Panel):
    """class DemoErrorPanel(wx.Panel):
    A Panel put into the demo tab when the demo fails to run due to errors.
    """
    __doc__ = wx.Panel.__doc__
    def __init__(self, parent, codePanel, demoError, log):
        wx.Panel.__init__(self, parent, -1)#, style=wx.NO_FULL_REPAINT_ON_RESIZE)
        print('demoError = %s' % demoError)
        self.codePanel = codePanel
        self.nb = parent
        self.log = log
        self.box = wx.BoxSizer(wx.VERTICAL)

        # Main Label
        self.box.Add(wx.StaticText(self, -1,
            _(u"An error has occurred while trying to run the demo")),
            0, wx.ALIGN_CENTER | wx.TOP, 10)

        # Exception Information
        boxInfo      = wx.StaticBox(self, -1, _(u"Exception Info"))
        boxInfoSizer = wx.StaticBoxSizer(boxInfo, wx.VERTICAL) # Used to center the grid within the box
        boxInfoGrid  = wx.FlexGridSizer(cols=2)
        textFlags    = wx.ALIGN_RIGHT | wx.LEFT | wx.RIGHT | wx.TOP
        boxInfoGrid.Add(wx.StaticText(self, -1, _(u"Type:")), 0, textFlags, 5)
        boxInfoGrid.Add(wx.StaticText(self, -1, str(demoError.exception_type)), 0, textFlags, 5)
        boxInfoGrid.Add(wx.StaticText(self, -1, _(u"Details:")), 0, textFlags, 5)
        boxInfoGrid.Add(wx.StaticText(self, -1, demoError.exception_details), 0, textFlags, 5)
        boxInfoSizer.Add(boxInfoGrid, 0, wx.ALIGN_CENTRE | wx.ALL, 5)
        self.box.Add(boxInfoSizer, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        # Set up the traceback list.
        # This one automatically resizes last column to take up remaining space.
        self.list = autoWList = AutoWidthListCtrl(self, -1, style=wx.LC_REPORT | wx.SUNKEN_BORDER)
        autoWList.Bind(wx.EVT_LEFT_DCLICK, self.OnDoubleClick)
        autoWList.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnItemSelected)
        autoWList.InsertColumn(0, _(u"Filename"))
        autoWList.InsertColumn(1, _(u"Line"), wx.LIST_FORMAT_RIGHT)
        autoWList.InsertColumn(2, _(u"Function"))
        autoWList.InsertColumn(3, _(u"Code"))
        self.InsertTraceback(autoWList, demoError.traceback)
        autoWList.SetColumnWidth(0, wx.LIST_AUTOSIZE)
        autoWList.SetColumnWidth(2, wx.LIST_AUTOSIZE)
        self.box.Add(wx.StaticText(self, -1, _(u"Traceback:"))
                     , 0, wx.ALIGN_CENTER | wx.TOP, 5)
        self.box.Add(autoWList, 1, wx.GROW | wx.ALIGN_CENTER | wx.ALL, 5)
        self.box.Add(wx.StaticText(self, -1,
            _(u"Entries from the demo module are shown in blue.") + "\n" +
            _(u"Double-click on them to go to the offending line")),
            0, wx.ALIGN_CENTER | wx.BOTTOM, 5)

        self.box.Fit(self)
        self.SetSizer(self.box)


    def InsertTraceback(self, list, traceback):
        #Add the traceback data
        for x in range(len(traceback)):
            data = traceback[x]
            list.InsertItem(x, u'%s' % os.path.basename(data[0])) # Filename
            list.SetItem(x, 1, u'%s' % str(data[1]))              # Line
            list.SetItem(x, 2, u'%s' % str(data[2]))              # Function
            list.SetItem(x, 3, u'%s' % str(data[3]))              # Code

            # Check whether this entry is from the demo module
            if data[0] == "<original>" or data[0] == "<modified>": # FIXME: make more generalised
                self.list.SetItemData(x, int(data[1])) # Store line number for easy access
                # Give it a blue colour
                item = self.list.GetItem(x)
                item.SetTextColour(wx.BLUE)
                self.list.SetItem(item)
            else:
                self.list.SetItemData(x, -1) # Editor can't jump into this one's code

    def OnItemSelected(self, event):
        # This occurs before OnDoubleClick and can be used to set the
        # currentItem. OnDoubleClick doesn't get a wxListEvent....
        self.currentItem = event.Index
        event.Skip()

    def OnDoubleClick(self, event):
        # If double-clicking on a demo's entry, jump to the line number
        try:
            line = self.list.GetItemData(self.currentItem)
        except AttributeError as exc:
            return #User didn't Double click on an item
        if line != -1:
            self.nb.SetSelection(1) # Switch to the code viewer tab
            wx.CallAfter(self.codePanel.JumpToLine, line-1, True)
        event.Skip()


#------------------------------------------------------------------------------

class MainPanel(wx.Panel):
    """
    Just a simple derived panel where we override Freeze and Thaw to work
    around an issue on wxGTK.
    """
    __doc__ = wx.Panel.__doc__
    def Freeze(self):
        if 'wxMSW' in wx.PlatformInfo:
            return super(MainPanel, self).Freeze()

    def Thaw(self):
        if 'wxMSW' in wx.PlatformInfo:
            return super(MainPanel, self).Thaw()

#------------------------------------------------------------------------------

class DemoTaskBarIcon(TaskBarIcon):
    __doc__ = TaskBarIcon.__doc__
    TBMENU_RESTORE = wx.NewId()
    TBMENU_CLOSE   = wx.NewId()
    TBMENU_CHANGE  = wx.NewId()
    TBMENU_REMOVE  = wx.NewId()

    def __init__(self, frame):
        TaskBarIcon.__init__(self, wx.adv.TBI_DOCK) # wx.adv.TBI_CUSTOM_STATUSITEM
        self.frame = frame

        # Set the image
        # icon = self.MakeIcon(images.WXPdemo.GetImage())
        icon = wx.Icon(gAppDir + os.sep + 'wxpdemo.ico')
        self.SetIcon(icon, "wxPython Demo")
        self.imgidx = 1

        # bind some events
        self.Bind(wx.adv.EVT_TASKBAR_LEFT_DCLICK, self.OnTaskBarActivate)
        self.Bind(wx.EVT_MENU, self.OnTaskBarActivate, id=self.TBMENU_RESTORE)
        self.Bind(wx.EVT_MENU, self.OnTaskBarClose, id=self.TBMENU_CLOSE)
        self.Bind(wx.EVT_MENU, self.OnTaskBarChange, id=self.TBMENU_CHANGE)
        self.Bind(wx.EVT_MENU, self.OnTaskBarRemove, id=self.TBMENU_REMOVE)


    def CreatePopupMenu(self):
        """
        This method is called by the base class when it needs to popup
        the menu for the default EVT_RIGHT_DOWN event.  Just create
        the menu how you want it and return it from this function,
        the base class takes care of the rest.
        """
        menu = wx.Menu()
        menu.Append(self.TBMENU_RESTORE, "Restore wxPython Demo")
        menu.Append(self.TBMENU_CLOSE,   "Close wxPython Demo")
        menu.AppendSeparator()
        menu.Append(self.TBMENU_CHANGE, "Change the TB Icon")
        menu.Append(self.TBMENU_REMOVE, "Remove the TB Icon")
        return menu

    def MakeIcon(self, img):
        """
        The various platforms have different requirements for the
        icon size...
        """
        if "wxMSW" in wx.PlatformInfo:
            img = img.Scale(16, 16)
        elif "wxGTK" in wx.PlatformInfo:
            img = img.Scale(22, 22)
        # wxMac can be any size up to 128x128, so leave the source img alone....
        icon = wx.Icon(img.ConvertToBitmap())
        return icon

    def OnTaskBarActivate(self, evt):
        if self.frame.IsIconized():
            self.frame.Iconize(False)
        if not self.frame.IsShown():
            self.frame.Show(True)
        self.frame.Raise()

    def OnTaskBarClose(self, evt):
        wx.CallAfter(self.frame.Close)

    def OnTaskBarChange(self, evt):
        names = [ "WXPdemo", "Mondrian", "Pencil", "Carrot" ]
        name = names[self.imgidx]

        eImg = getattr(images, name)
        self.imgidx += 1
        if self.imgidx >= len(names):
            self.imgidx = 0

        icon = self.MakeIcon(eImg.Image)
        self.SetIcon(icon, "This is a new icon: " + name)

    def OnTaskBarRemove(self, evt):
        self.RemoveIcon()


#------------------------------------------------------------------------------

class AutoWidthListCtrl(wx.ListCtrl, listmix.ListCtrlAutoWidthMixin):
    __doc__ = wx.ListCtrl.__doc__
    def __init__(self, parent, ID, pos=wx.DefaultPosition,
                 size=wx.DefaultSize, style=0):
        wx.ListCtrl.__init__(self, parent, ID, pos, size, style)
        listmix.ListCtrlAutoWidthMixin.__init__(self)

#------------------------------------------------------------------------------
class TestPanel(wx.Panel):
    __doc__ = wx.Panel.__doc__
    def __init__(self, parent, log, filePath):
        self.log = log
        wx.Panel.__init__(self, parent, -1, style=wx.BORDER_SUNKEN)

        self.filePath = filePath
        self.fileName = os.path.basename(filePath)

        st = wx.StaticText(self, -1,
            u'The file has been compiled with py_compile at this point '
            u'and No syntax errors have been detected.' '\n'
            u'You can click the button to try and run the demo '
            u'normally with subprocess.Popen("python", filePath).')

        ID_RUN_DEMO = wx.NewId()
        btn1 = wx.Button(self, ID_RUN_DEMO, _(u'Run') + ' ' + '%s' % os.path.basename(filePath))
        btn1.SetToolTip(wx.ToolTip('%s' % filePath))
        btn1.Bind(wx.EVT_BUTTON, self.OnTryRunFileNormally)

        pipeCBText = (
            u'PIPE for errors\n'
            u'(This will block the wxPythonDemo GUI\n'
            u' until the process terminates\n'
            u' or show an ERROR dialog.)')
        self.pipeCB = wx.CheckBox(self, -1, pipeCBText)
        self.pipeCB.SetToolTip(wx.ToolTip(pipeCBText))

        vbSizer= wx.BoxSizer(wx.VERTICAL)
        b = 5
        vbSizer.Add(st, 1, wx.EXPAND | wx.ALL, b)
        vbSizer.Add(self.pipeCB, 0, wx.ALL, b)
        vbSizer.Add(btn1, 0, wx.ALL, b)
        if os.path.exists(GetModifiedDirectory() + os.sep + self.fileName):
            ID_RUN_MODIFIED_DEMO = wx.NewId()
            btn2 = wx.Button(self, ID_RUN_MODIFIED_DEMO, "Run %s" % os.path.basename(filePath))
            btn2.Bind(wx.EVT_BUTTON, self.OnTryRunModFileNormally)
            btn2.SetBitmap(images.catalog['custom'].GetBitmap())
            st3 = wx.StaticText(self, -1, 'filePath = %s' % GetModifiedDirectory() + os.sep + self.fileName)
            vbSizer.Add(btn2, 0, wx.ALL, b)
            vbSizer.Add(st3, 0, wx.ALL, b)
        # TODO: offer wxversion launching with a radiobox
        # wxversionSelectChoices = tuple(set(wxversion.getInstalled()))
        #PYINSTALLER_PROBLEM# st_wxpth = wx.TextCtrl(self, -1, 'Your wx.pth Path is: %s' % wx_pth_Path, style=wx.TE_READONLY)
        #PYINSTALLER_PROBLEM# st_wxpth.Enable(False)
        #PYINSTALLER_PROBLEM# st_wxpthContent = wx.TextCtrl(self, -1, '%s' % wx_pth_Path_Contents, style=wx.TE_MULTILINE | wx.TE_READONLY)
        #PYINSTALLER_PROBLEM# vbSizer.Add(st_wxpth, 0, wx.EXPAND | wx.ALL, b)
        #PYINSTALLER_PROBLEM# vbSizer.Add(st_wxpthContent, 1, wx.EXPAND | wx.ALL, b)
        self.SetSizer(vbSizer)

    def OnTryRunFileNormally(self, event=None, cmdStaysOpenAfter=False):
        # event.Skip()
        # TODO: make a way to inject wxversion and other imports into the file before running.
        # TODO: if runTest exists in source, make option to launch with it.
        # TODO: option for cmdStaysOpenAfter

        cwd = os.getcwd() # temp switch the cwd to the demo's dir
        os.chdir(os.path.dirname(self.filePath))

        if wx.Platform == '__WXMSW__': # Microsoft Windows.
            # start console in a new window.
            if cmdStaysOpenAfter or self.pipeCB.IsChecked():
                args = ['start', 'cmd', '/K', sys.executable, self.filePath]
            else:
                args = ['start', 'cmd', '/C', sys.executable, self.filePath]
            # args = [sys.executable, self.filePath]
        else: # TODO: other platforms. linux, mac. Not sure if this is sufficient.
            args = [sys.executable, self.filePath]

        if self.pipeCB.IsChecked():
            manualrun_stdout_stderr = subprocess.Popen(
                args,
                # bufsize=0, # 0=unbuffered, 1=line-buffered, else buffer-size
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                shell=True,
                )

            stdout, stderr = manualrun_stdout_stderr.communicate()
            print('STDOUT = %s' % stdout)
            print('STDERR = %s' % stderr)
            if stderr:
                ExceptionStrDialog(excStr=stderr).ShowModal()
        else:
            subprocess.Popen(
                args,
                shell=True,
                )
        os.chdir(cwd)

        # print('sys.stderr = %s' % sys.stderr)
        # # Wait until process terminates
        # while manualrun_stdout_stderr.poll() is None:
        #     # time.sleep(1)
        #     # print('sleeping...')

        # subprocess.Popen(['python', gAppDir + os.sep + 'run.py', self.filePath])

    def OnTryRunModFileNormally(self, event):
        # TODO: make a way to inject regular file path into sys.path before running so all resources are recognised.

        cwd = os.getcwd() # temp switch the cwd to the demo's dir
        os.chdir(os.path.dirname(self.filePath))
        subprocess.Popen(['python', GetModifiedDirectory() + os.sep + self.fileName])
        os.chdir(cwd)

#------------------------------------------------------------------------------
class CustomStatusBar(wx.StatusBar):
    __doc__ = wx.StatusBar.__doc__
    def __init__(self, parent, id=wx.ID_ANY, style=0, name='statusbar'):
        if not style:
            style=wx.STB_SIZEGRIP
        wx.StatusBar.__init__(self, parent, id, style, name)

        # Attibutes.
        self.sizeChanged = False

        self.SetFieldsCount(3)
        self.SetStatusWidths([-2, -1, 32])

        # Bind event handlers.
        self.Bind(wx.EVT_SIZE, self.OnStatusBarSize)
        self.Bind(wx.EVT_IDLE, self.OnStatusBarIdle)

        # Initial StatusText
        major, minor, micro, release = sys.version_info[0:-1]
        pythonVersion = u'%d.%d.%d-%s'%(major, minor, micro, release)
        statusText = ("Welcome to wxPython %s running on Python %s" %
                      (wx.version(), pythonVersion))
        self.SetStatusText(statusText, 0)

        self.whatsThisContextHelp = ContextHelpStaticBitmap(self)

        self.SetMinHeight(14) # Don't chop the lifesaver off


    def OnStatusBarSize(self, event):
        self.Reposition()  # for normal size events

        # Set a flag so the idle time handler will also do the repositioning.
        # It is done this way to get around a buglet where GetFieldRect is not
        # accurate during the EVT_SIZE resulting from a frame maximize.
        self.sizeChanged = True

    def OnStatusBarIdle(self, event):
        if self.sizeChanged:
            self.Reposition()

    # reposition the download gauge, contextHelp
    def Reposition(self):
        # rect = self.statusBar.GetFieldRect(1)
        # self.downloadGauge.SetPosition((rect.x+2, rect.y+2))
        # self.downloadGauge.SetSize((rect.width-4, rect.height-4))

        # self.whatsThisContextHelp.SetSize((16, 16))
        rect = self.GetFieldRect(2)
        rect.x += 2
        # rect.y += 2
        self.whatsThisContextHelp.SetRect(rect)

        self.sizeChanged = False


class ContextHelpStaticBitmap(wx.StaticBitmap):
    """StaticBitmap for the CustomStatusBar"""
    __doc__ = wx.StaticBitmap.__doc__
    def __init__(self, parent, id=wx.ID_CONTEXT_HELP, bitmap=wx.NullBitmap,
                 pos=wx.DefaultPosition, size=(16, 16), style=0,
                 name='staticbitmap'):
        wx.StaticBitmap.__init__(self, parent, id, bitmap, pos, size, style, name)

        self.SetBackgroundColour(parent.GetBackgroundColour())

        self.SetToolTip(wx.ToolTip(u"What's This?"))

        self.SetBitmap(wx.Bitmap('bitmaps' + os.sep + 'lifesaver_help16.png'))

        self.SetHelpText(_(u'I\'m a context help button.' + '\n' +
                           u'Click on me and then on another widget to get' + '\n' +
                           u'a more detailed message of what it does!'))

        self.Bind(wx.EVT_LEFT_UP, self.OnContextHelp)

    def OnContextHelp(self, event):
        wx.ContextHelp(window=gMainWin, doNow=True)


class ContextHelpTransientPopup(wx.PopupTransientWindow):
    """Adds a bit of text and mouse movement to the wx.PopupWindow"""
    __doc__ = wx.PopupTransientWindow.__doc__
    def __init__(self, parent, style, log, helpText):
        wx.PopupTransientWindow.__init__(self, parent, style)
        self.log = log
        self.panel = wx.Panel(self)
        # self.panel.SetBackgroundColour("#FFB6C1")

        st = wx.StaticText(self.panel, -1, helpText, style=wx.BORDER_SUNKEN)
        btn = wx.Button(self.panel, -1, "Press Me")
        spin = wx.SpinCtrl(self.panel, -1, "Hello", size=(100,-1))
        btn.Bind(wx.EVT_BUTTON, self.OnButton)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(st, 0, wx.ALL, 5)
        sizer.Add(btn, 0, wx.ALL, 5)
        sizer.Add(spin, 0, wx.ALL, 5)
        self.panel.SetSizer(sizer)

        sizer.Fit(self.panel)
        sizer.Fit(self)
        self.Layout()

        self.panel.Bind(wx.EVT_LEFT_DOWN, self.OnMouseLeftDown)
        self.panel.Bind(wx.EVT_MOTION, self.OnMouseMotion)
        self.panel.Bind(wx.EVT_LEFT_UP, self.OnMouseLeftUp)
        self.panel.Bind(wx.EVT_RIGHT_UP, self.OnRightUp)

        self.panel.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        self.panel.Bind(wx.EVT_PAINT, self.OnPaint)

        st.Bind(wx.EVT_LEFT_DOWN, self.OnMouseLeftDown)
        st.Bind(wx.EVT_MOTION, self.OnMouseMotion)
        st.Bind(wx.EVT_LEFT_UP, self.OnMouseLeftUp)
        st.Bind(wx.EVT_RIGHT_UP, self.OnRightUp)

        self.ldPos = self.panel.GetPosition()
        self.wPos = wx.Point(0, 0)

        wx.CallAfter(self.Refresh)


    def OnEraseBackground(self, event):
        pass

    def OnPaint(self, event):
        dc = wx.BufferedPaintDC(self.panel)
        dc.GradientFillLinear(self.GetClientRect(),
                              wx.WHITE,
                              wx.BLACK,
                              wx.NORTH)

    def OnMouseLeftDown(self, event):
        self.Refresh()
        self.ldPos = event.GetEventObject().ClientToScreen(event.GetPosition())
        self.wPos = self.ClientToScreen((0, 0))
        self.panel.CaptureMouse()

    def OnMouseMotion(self, event):
        if event.Dragging() and event.LeftIsDown():
            dPos = event.GetEventObject().ClientToScreen(event.GetPosition())
            nPos = (self.wPos.x + (dPos.x - self.ldPos.x),
                    self.wPos.y + (dPos.y - self.ldPos.y))
            self.Move(nPos)

    def OnMouseLeftUp(self, event):
        if self.panel.HasCapture():
            self.panel.ReleaseMouse()

    def OnRightUp(self, event):
        self.Show(False)
        self.Destroy()

    def ProcessLeftDown(self, event):
        gMainWin.log.WriteText("ProcessLeftDown: %s\n" % event.GetPosition())
        return wx.PopupTransientWindow.ProcessLeftDown(self, event)

    def OnDismiss(self):
        gMainWin.log.WriteText("OnDismiss\n")
        self.Destroy()

    def OnButton(self, event):
        btn = event.GetEventObject()
        if btn.GetLabel() == "Press Me":
            btn.SetLabel("Pressed")
        else:
            btn.SetLabel("Press Me")


class wxPythonDemo(wx.Frame):

    overviewText = "wxPython Overview"

    __doc__ = wx.Frame.__doc__
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, -1, title, size=(800, 600),
                          style=wx.DEFAULT_FRAME_STYLE |
                                wx.NO_FULL_REPAINT_ON_RESIZE)

        global gMainWin
        gMainWin = self

        self.SetMinSize((640, 480))

        self.gMainPanel = pnl = MainPanel(self)

        self.mgr = aui.AuiManager()
        self.mgr.SetManagedWindow(pnl)

        self.loaded = False
        self.cwd = os.getcwd()
        self.curOverview = ""
        self.demoPage = None
        self.codePage = None
        self.shell = None
        self.firstTime = True
        self.finddlg = None

        ##icon = images.WXPdemo.GetIcon()
        icon = wx.Icon("wxpdemo.ico", wx.BITMAP_TYPE_ICO)
        self.SetIcon(icon)

        try:
            self.tbicon = DemoTaskBarIcon(self)
        except Exception as exc:
            self.tbicon = None

        self.otherWin = None

        self.allowDocs = False
        self.downloading = False
        self.internetThread = None
        self.downloadImage = 2
        self.sendDownloadError = True
        self.downloadTimer = wx.Timer(self, wx.ID_ANY)

        self.Bind(wx.EVT_IDLE, self.OnIdle)
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)
        self.Bind(wx.EVT_ICONIZE, self.OnIconify)
        self.Bind(wx.EVT_MAXIMIZE, self.OnMaximize)
        self.Bind(wx.EVT_TIMER, self.OnDownloadTimer, self.downloadTimer)

        self.Centre(wx.BOTH)

        self.statusBar = CustomStatusBar(self)
        self.SetStatusBar(self.statusBar)

        self.downloadGauge = wx.Gauge(self.statusBar, wx.ID_ANY, 50)
        self.downloadGauge.SetToolTip("Downloading Docs...")
        self.downloadGauge.Hide()

        self.statusBar.Reposition() # Update everything immediately.

        self.dying = False
        self.skipLoad = False
        self.allowAuiFloating = False

        def EmptyHandler(event):
            pass

        self.ReadConfigurationFile()
        ###### self.externalDemos = HuntExternalDemos()

        # Create a Notebook
        self.nb = wx.Notebook(pnl, -1, style=wx.CLIP_CHILDREN)
        imgList = wx.ImageList(16, 16)
        for png in ["overview", "code", "demo"]:
            bmp = images.catalog[png].GetBitmap()
            imgList.Add(bmp)
        for indx in range(9):
            bmp = images.catalog["spinning_nb%d"%indx].GetBitmap()
            imgList.Add(bmp)

        self.nb.AssignImageList(imgList)

        self.BuildMenuBar()

        self.finddata = wx.FindReplaceData()
        self.finddata.SetFlags(wx.FR_DOWN)

        # Create a TreeCtrl
        leftPanel = wx.Panel(pnl, style=wx.TAB_TRAVERSAL|wx.CLIP_CHILDREN)
        self.treeMap = {}
        self.searchItems = {}

        self.tree = wxPythonDemoTree(leftPanel)


        self.filter = wx.SearchCtrl(leftPanel, style=wx.TE_PROCESS_ENTER)
        self.filter.ShowCancelButton(True)
        self.filter.Bind(wx.EVT_TEXT, self.tree.RecreateTree)
        self.filter.Bind(wx.EVT_SEARCHCTRL_CANCEL_BTN,
                         lambda evt: self.filter.SetValue(''))
        self.filter.Bind(wx.EVT_TEXT_ENTER, self.OnSearch)

        searchMenu = wx.Menu()
        item = searchMenu.AppendRadioItem(-1, "Sample Name")
        self.Bind(wx.EVT_MENU, self.OnSearchMenu, item)
        item = searchMenu.AppendRadioItem(-1, "Sample Content")
        self.Bind(wx.EVT_MENU, self.OnSearchMenu, item)
        self.filter.SetMenu(searchMenu)

        self.tree.RecreateTree()
        self.tree.SetExpansionState(self.expansionState)
        self.tree.BindTreeCtrlEvents()

        # Now that the full tree structure has been built for the first time,
        # lets build the Demo Menu and Insert it into the MenuBar.
        self.gMenu_Demo = self.BuildDemoMenu()
        self.gMenuBar.Insert(1, self.gMenu_Demo, '&Demo')

        # Set up a wx.html.HtmlWindow on the Overview Notebook page
        # we put it in a panel first because there seems to be a
        # refresh bug of some sort (wxGTK) when it is directly in
        # the notebook...

        if 0:  # the old way
            self.ovr = wx.html.HtmlWindow(self.nb, -1, size=(400, 400))
            self.nb.AddPage(self.ovr, self.overviewText, imageId=0)

        else:  # hopefully I can remove this hacky code soon, see SF bug #216861
            panel = wx.Panel(self.nb, -1, style=wx.CLIP_CHILDREN)
            self.ovr = wx.html.HtmlWindow(panel, -1, size=(400, 400))
            self.nb.AddPage(panel, self.overviewText, imageId=0)

            def OnOvrSize(evt, ovr=self.ovr):
                ovr.SetSize(evt.GetSize())
            panel.Bind(wx.EVT_SIZE, OnOvrSize)
            panel.Bind(wx.EVT_ERASE_BACKGROUND, EmptyHandler)

        # self.ovr.Unbind(wx.EVT_MOUSEWHEEL)
        # self.ovr.Bind(wx.EVT_MOUSEWHEEL, wx.GetApp().OnMouseWheel)

        if "gtk2" in wx.PlatformInfo:
            self.ovr.SetStandardFonts()
        self.SetOverview(self.overviewText, mainOverview)

        self.codePage = DemoCodePanel(self.nb, self)
        self.nb.AddPage(self.codePage, 'Demo Code', imageId=0)

        # Set up a log window
        self.log = wx.TextCtrl(pnl, -1,
                        style = wx.TE_MULTILINE | wx.TE_READONLY | wx.HSCROLL)

        if wx.Platform == "__WXMAC__":
            self.log.MacCheckSpelling(False)

        # Set the wxWindows log target to be this textctrl
        ## wx.Log.SetActiveTarget(wx.LogTextCtrl(self.log))

        # But instead of the above we want to show how to use our own wx.Log class
        wx.Log.SetActiveTarget(MyLog(self.log))

        # for serious debugging
        #wx.Log.SetActiveTarget(wx.LogStderr())
        #wx.Log.SetTraceMask(wx.TraceMessages)

        self.Bind(wx.EVT_ACTIVATE, self.OnActivate)
        wx.GetApp().Bind(wx.EVT_ACTIVATE_APP, self.OnAppActivate)

        # add the windows to the splitter and split it.
        leftBox = wx.BoxSizer(wx.VERTICAL)
        leftBox.Add(self.tree, 1, wx.EXPAND)
        leftBox.Add(wx.StaticText(leftPanel, label = "Filter Demos:"), 0, wx.TOP|wx.LEFT, 5)
        leftBox.Add(self.filter, 0, wx.EXPAND|wx.ALL, 5)
        if 'wxMac' in wx.PlatformInfo:
            leftBox.Add((5,5))  # Make sure there is room for the focus ring
        leftPanel.SetSizer(leftBox)

        # Select initial items.
        self.nb.SetSelection(0)
        self.tree.SelectItem(self.tree.root)

        # Load 'Main' module.
        # self.LoadDemo(self.overviewText)
        self.loaded = True

        # Select some other initial module?
        if len(sys.argv) > 1:
            for i in range(1, len(sys.argv)):
                arg = sys.argv[i]
                if arg.endswith('.py'):
                    arg = arg[:-3]
                    break
            selectedDemo = self.treeMap.get(arg, None)
            if selectedDemo:
                self.tree.SelectItem(selectedDemo)
                self.tree.EnsureVisible(selectedDemo)

        # Use the aui manager to set up everything
        self.mgr.AddPane(self.nb, aui.AuiPaneInfo().CenterPane().Name("Notebook"))
        self.mgr.AddPane(leftPanel,
                         aui.AuiPaneInfo().
                         Left().Layer(2).BestSize((240, -1)).
                         MinSize((240, -1)).
                         Floatable(self.allowAuiFloating).FloatingSize((240, 700)).
                         Caption("wxPython Demos").
                         CloseButton(False).
                         Name("DemoTree"))
        self.mgr.AddPane(self.log,
                         aui.AuiPaneInfo().
                         Bottom().BestSize((-1, 150)).
                         MinSize((-1, 140)).
                         Floatable(self.allowAuiFloating).FloatingSize((500, 160)).
                         Caption("Demo Log Messages").
                         CloseButton(False).
                         Name("LogWindow"))

        self.auiConfigurations[DEFAULT_PERSPECTIVE] = self.mgr.SavePerspective()
        self.mgr.Update()

        self.mgr.SetAGWFlags(self.mgr.GetAGWFlags() ^ aui.AUI_MGR_TRANSPARENT_DRAG)


        self.tree.SetHelpText("I'm a wx.TreeCtrl")
        self.log.SetHelpText("I'm a wx.TextCtrl")

        self.Bind(wx.EVT_HELP, self.OnHelp)
        ## self.Bind(wx.EVT_DETAILED_HELP, self.OnDetailedHelp)

        self.ovr.Bind(wx.EVT_BUTTON, self.On_wxp_ID_HELP_CONTENTS, id=wx.ID_HELP_CONTENTS)

    def On_wxp_ID_HELP_CONTENTS(self, event):
        evtObj = event.GetEventObject()
        # urlLinkStr = evtObj.GetLabel()
        urlLinkStr = evtObj.GetName()

        import urllib
        f = urllib.urlopen(urlLinkStr)
        str = f.read()

        # import urllib2
        # req = urllib2.Request(link)
        # response = urllib2.urlopen(req)
        # str = response.read()

        self.ovr.SetPage(str)

        print('wxp click')

    def OnHelp(self, event):
        evtId = event.GetId()
        print('evtId = %s' % evtId)
        win = wx.FindWindowById(evtId)
        print('win.GetHelpText() = %s' % win.GetHelpText())
        print('win.__doc__ = %s' % win.__doc__)

        self.log.WriteText(('OnHelp' + '\n'
            '    event.GetOrigin() = %s' % event.GetOrigin() + '\n' +
            '    event.GetPosition() = %s' % event.GetPosition() + '\n'
            ))

        # print('GetOrigin = %s' % event.GetOrigin()) # Returns the origin of the help event which is one of the HelpEvent.Origin values.
        # print('GetPosition = %s' % event.GetPosition()) # Returns the left-click position of the mouse, in screen coordinates.
        # print('OnHelp')

        if win.GetHelpText():
            helpText = win.GetHelpText()
        elif win.__doc__:
            helpText = win.__doc__
        else:
            try: # Maybe a Demo Subclass
                helpText = eval('%s.__doc__' % win.__class__.__name__)
            except NameError:
                helpText = '%s None' % win.__class__.__name__

        if not helpText:
            helpText = '%s None' % win.__class__.__name__

        transPopupWin = ContextHelpTransientPopup(self,
            wx.SIMPLE_BORDER, self.log, helpText)
        # Show the popup right where the mouse clicked.
        transPopupWin.Position(wx.GetMousePosition(), (0, 0))
        transPopupWin.Popup()

    def OnDetailedHelp(self, event):
        print('OnDetailedHelp')

    def ReadConfigurationFile(self):
        self.auiConfigurations = {}
        self.expansionState = [0, 1]

        config = GetConfig()
        val = config.Read('ExpansionState')
        if val:
            self.expansionState = eval(val)

        val = config.Read('AUIPerspectives')
        if val:
            self.auiConfigurations = eval(val)

        val = config.Read('AllowDownloads')
        if val:
            self.allowDocs = eval(val)

        val = config.Read('AllowAUIFloating')
        if val:
            self.allowAuiFloating = eval(val)

        MakeDocDirs()
        pickledFile = GetDocFile()

        if not os.path.isfile(pickledFile):
            self.pickledData = {}
            return

        fid = open(pickledFile, "rb")
        try:
            self.pickledData = pickle.load(fid)
        except Exception as exc:
            self.pickledData = {}

        fid.close()

    def BuildMenuBar(self):
        # Make a File menu
        self.gMenuBar = wx.MenuBar()
        menu = wx.Menu()
        item = menu.Append(-1, '&Redirect Output',
                           'Redirect print statements to a window',
                           wx.ITEM_CHECK)
        self.Bind(wx.EVT_MENU, self.OnToggleRedirect, item)

        wx.App.SetMacExitMenuItemId(9123)
        exitItem = wx.MenuItem(menu, 9123, 'E&xit\tCtrl-Q', 'Get the heck outta here!')
        exitItem.SetBitmap(images.catalog['exit'].GetBitmap())
        menu.Append(exitItem)
        self.Bind(wx.EVT_MENU, self.OnFileExit, exitItem)
        self.gMenuBar.Append(menu, '&File')

        # menu = self.BuildDemoMenu()
        # self.gMenuBar.Append(menu, '&Demo')

        # Make an Option menu

        menu = wx.Menu()
        item = wx.MenuItem(menu, -1, 'Allow download of docs', 'Docs for window styles and events from the web', wx.ITEM_CHECK)
        menu.Append(item)
        item.Check(self.allowDocs)
        self.Bind(wx.EVT_MENU, self.OnAllowDownload, item)

        item = wx.MenuItem(menu, -1, 'Delete saved docs', 'Deletes the cPickle/pickle file where docs are stored')
        item.SetBitmap(images.catalog['deletedocs'].GetBitmap())
        menu.Append(item)
        self.Bind(wx.EVT_MENU, self.OnDeleteDocs, item)

        menu.AppendSeparator()
        item = wx.MenuItem(menu, -1, 'Allow floating panes', 'Allows the demo panes to be floated using wxAUI', wx.ITEM_CHECK)
        menu.Append(item)
        item.Check(self.allowAuiFloating)
        self.Bind(wx.EVT_MENU, self.OnAllowAuiFloating, item)

        auiPerspectives = self.auiConfigurations.keys()
        auiPerspectives = sorted(self.auiConfigurations.keys())
        perspectivesMenu = wx.Menu()
        item = wx.MenuItem(perspectivesMenu, -1, DEFAULT_PERSPECTIVE, "Load startup default perspective", wx.ITEM_RADIO)
        self.Bind(wx.EVT_MENU, self.OnAUIPerspectives, item)
        perspectivesMenu.Append(item)
        for indx, key in enumerate(auiPerspectives):
            if key == DEFAULT_PERSPECTIVE:
                continue
            item = wx.MenuItem(perspectivesMenu, -1, key, "Load user perspective %d"%indx, wx.ITEM_RADIO)
            perspectivesMenu.Append(item)
            self.Bind(wx.EVT_MENU, self.OnAUIPerspectives, item)

        menu.Append(wx.ID_ANY, "&AUI Perspectives", perspectivesMenu)
        self.perspectives_menu = perspectivesMenu

        item = wx.MenuItem(menu, -1, 'Save Perspective', 'Save AUI perspective')
        item.SetBitmap(images.catalog['saveperspective'].GetBitmap())
        menu.Append(item)
        self.Bind(wx.EVT_MENU, self.OnSavePerspective, item)

        item = wx.MenuItem(menu, -1, 'Delete Perspective', 'Delete AUI perspective')
        item.SetBitmap(images.catalog['deleteperspective'].GetBitmap())
        menu.Append(item)
        self.Bind(wx.EVT_MENU, self.OnDeletePerspective, item)

        menu.AppendSeparator()

        item = wx.MenuItem(menu, -1, 'Restore Tree Expansion', 'Restore the initial tree expansion state')
        item.SetBitmap(images.catalog['expansion'].GetBitmap())
        menu.Append(item)
        self.Bind(wx.EVT_MENU, self.OnTreeExpansion, item)

        self.gMenuBar.Append(menu, '&Options')
        self.options_menu = menu

        # Make a Help menu
        menu = wx.Menu()
        findItem = wx.MenuItem(menu, -1, '&Find\tCtrl-F', 'Find in the Demo Code')
        findItem.SetBitmap(images.catalog['find'].GetBitmap())
        if 'wxMac' not in wx.PlatformInfo:
            findNextItem = wx.MenuItem(menu, -1, 'Find &Next\tF3', 'Find Next')
        else:
            findNextItem = wx.MenuItem(menu, -1, 'Find &Next\tCtrl-G', 'Find Next')
        findNextItem.SetBitmap(images.catalog['findnext'].GetBitmap())
        menu.Append(findItem)
        menu.Append(findNextItem)
        menu.AppendSeparator()

        shellItem = wx.MenuItem(menu, -1, 'Open Py&Shell Window\tF5',
                                'An interactive interpreter window with the demo app and frame objects in the namesapce')
        shellItem.SetBitmap(images.catalog['pyshell'].GetBitmap())
        menu.Append(shellItem)
        inspToolItem = wx.MenuItem(menu, -1, 'Open &Widget Inspector\tF6',
                                   'A tool that lets you browse the live widgets and sizers in an application')
        inspToolItem.SetBitmap(images.catalog['inspect'].GetBitmap())
        menu.Append(inspToolItem)
        if 'wxMac' not in wx.PlatformInfo:
            menu.AppendSeparator()
        helpItem = menu.Append(wx.ID_ABOUT, '&About wxPython Demo', 'wxPython RULES!!!')

        submenu = wx.Menu()
        for weblink in _onlineURLS:
            weblinkItem = wx.MenuItem(menu, -1, weblink, weblink)
            submenu.Append(weblinkItem)
            self.Bind(wx.EVT_MENU, self.OnLaunchWeblink, weblinkItem)
        menu.AppendSubMenu(submenu, 'Online WebLinks')

        self.Bind(wx.EVT_MENU, self.OnOpenShellWindow, shellItem)
        self.Bind(wx.EVT_MENU, self.OnOpenWidgetInspector, inspToolItem)
        self.Bind(wx.EVT_MENU, self.OnHelpAbout, helpItem)
        self.Bind(wx.EVT_MENU, self.OnHelpFind,  findItem)
        self.Bind(wx.EVT_MENU, self.OnFindNext,  findNextItem)
        self.Bind(wx.EVT_FIND, self.OnFind)
        self.Bind(wx.EVT_FIND_NEXT, self.OnFind)
        self.Bind(wx.EVT_FIND_CLOSE, self.OnFindClose)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateFindItems, findItem)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateFindItems, findNextItem)
        self.gMenuBar.Append(menu, '&Help')
        self.SetMenuBar(self.gMenuBar)

        self.EnableAUIMenu()

        if False:
            # This is another way to set Accelerators, in addition to
            # using the '\t<key>' syntax in the menu items.
            aTable = wx.AcceleratorTable([(wx.ACCEL_ALT,  ord('X'), exitItem.GetId()),
                                          (wx.ACCEL_CTRL, ord('H'), helpItem.GetId()),
                                          (wx.ACCEL_CTRL, ord('F'), findItem.GetId()),
                                          (wx.ACCEL_NORMAL, wx.WXK_F3, findNextItem.GetId()),
                                          (wx.ACCEL_NORMAL, wx.WXK_F9, shellItem.GetId()),
                                          ])
            self.SetAcceleratorTable(aTable)

    def BuildDemoMenu(self):
        """
        Make and return a Demo menu built from the wxPythonDemoTree.

        We will only show the relative path from the
        demo's application directory for the filepaths in the menu items
        long help, so as to shorten it nicely for statusbar help.
        """
        demoMenu = wx.Menu()

        ## # Will use this dict for tree popup submenu so
        ## # newIds and rebinds don't happen everytime a tree popup menu occurs.
        ## self.demoMenuIds = {}

        localRelativePath = os.path.relpath
        demoTree = self.tree
        demoTreeImageList = demoTree.treeImageList
        def iterateChildren(tree, treeItem, menu, indent=0):
            # print("  " * indent + self.tree.GetItemText(treeItem))
            # subItem = self.tree.GetFirstChild(treeItem)[0]
            # while subItem.IsOk():
            #     iterateChildren(self.tree, subItem)
            #     subItem = self.tree.GetNextSibling(subItem)

            subItem = demoTree.GetFirstChild(treeItem)[0]
            while subItem.IsOk():
                # print("  " * indent + demoTree.GetItemText(subItem))
                label = demoTree.GetItemText(subItem)
                fullpath = demoTree.GetItemData(subItem)
                relativePath = localRelativePath(fullpath, gAppDir)
                # print(fullpath)
                newId = wx.NewId()
                if os.path.isdir(fullpath):
                    menuItem = wx.MenuItem(menu, newId, label, relativePath)
                    submenu = wx.Menu()
                    menuItem.SetBitmap(demoTreeImageList.GetBitmap(demoTree.GetItemImage(subItem)))
                    menuItem.SetSubMenu(submenu)
                    menu.Append(menuItem)
                else:
                    menuItem = wx.MenuItem(menu, newId, label, relativePath)
                    menuItem.SetBitmap(demoTreeImageList.GetBitmap(demoTree.GetItemImage(subItem)))
                    menu.Append(menuItem)
                    submenu = menu

                    # menu.Bind(wx.EVT_MENU, self.OnSelectDemoFromMenuItem, id=newId)
                    self.Bind(wx.EVT_MENU, self.OnSelectDemoFromMenuItem, id=newId)

                iterateChildren(demoTree, subItem, submenu, indent+1)
                subItem = demoTree.GetNextSibling(subItem)

        iterateChildren(demoTree, demoTree.GetRootItem(), demoMenu)

        return demoMenu

    def OnSelectDemoFromMenuItem(self, event):
        evtObj = event.GetEventObject() # Menu
        menuItem = evtObj.FindItemById(event.GetId())
        relPath = menuItem.GetHelp()
        fullPath = os.path.abspath(os.path.join(gAppDir, relPath))
        self.tree.SelectItem(gMainWin.externalDemos[fullPath])
        # print('evtObj = %s' % evtObj)

    def OnLaunchWeblink(self, event):
        import webbrowser
        webbrowser.open(event.GetEventObject().GetLabel(event.GetId()))

    def PyCompileFile(self, pythonFilePath):
        """
        If python file compiled succesfully:
            return True
        else:
            return False
        """
        try: # compiling it the right way to see if it will compile.
            py_compile.compile(file=pythonFilePath,
                               cfile=None, dfile=None, doraise=True)
            # No syntax errors have been detected at this point,
            # so lets create a demoPage for running the demo(s) manually.
            return True
        except Exception as exc:
            return False

    #---------------------------------------------

    def OnSearchMenu(self, event):
        # Catch the search type (name or content)
        searchMenu = self.filter.GetMenu().GetMenuItems()
        fullSearch = searchMenu[1].IsChecked()

        if fullSearch:
            self.OnSearch()
        else:
            self.tree.RecreateTree()

    def OnSearch(self, event=None):
        value = self.filter.GetValue()
        if not value:
            self.tree.RecreateTree()
            return

        wx.BeginBusyCursor()

        for category, items in _treeList:
            self.searchItems[category] = []
            for childItem in items:
                if SearchDemo(childItem, value):
                    self.searchItems[category].append(childItem)

        wx.EndBusyCursor()
        self.tree.RecreateTree()

    def SetTreeModified(self, modified):
        item = self.tree.GetSelection()
        if modified:
            image = len(_demoPngsList)
        else:
            image = self.tree.GetItemData(item)
        self.tree.SetItemImage(item, image)

    def WriteText(self, text):
        if text[-1:] == '\n':
            text = text[:-1]
        wx.LogMessage(text)

    def write(self, txt):
        self.WriteText(txt)


    #---------------------------------------------
    def GetCompiledCodeObject(self, filePath):
        fileIsOpen = open(filePath, 'r')
        source = fileIsOpen.read()
        fileIsOpen.close()
        filename = os.path.basename(filePath)
        # filename = filePath
        code = compile(source, filename, "exec")
        return code

    def GetHtmlIzedText(self, text):
        """
        html-ize the text and return it.
        Mostly used for formating a files __doc__ for wx.html
        strip trailing spaces
        and
        reformat line breaks with html breaks.
        """
        htmlIzedText = '<br>'.join(
            [line.rstrip() for line in
                text.replace('\r\n', '\n').
                     replace('\r', '\n').
                     replace(' ', '&nbsp;').
                     split('\n')
                     ])
        return htmlIzedText

    def LoadCodePageFile(self, filePath):
        fileIsOpen = open(filePath, 'r')
        source = fileIsOpen.read()
        fileIsOpen.close()

        self.codePage.editor.SetText(u'%s' % source)
        self.codePage.editor.EmptyUndoBuffer()
        self.codePage.editor.filePath = filePath
        fileDir, basename = os.path.split(filePath)
        self.codePage.editor.fileDir = fileDir
        self.codePage.editor.fileName = basename
        self.codePage.editor.fileExt = os.path.splitext(basename)[1]

    def Load__demo__py(self, filePath):
        self.gMainPanel.Freeze()

        self.LoadCodePageFile(filePath + os.sep + '__demo__.py')

        nbTabCurrentlyOn = self.nb.FindPage(self.nb.GetCurrentPage())

        if self.nb.GetPageCount() > 2:
            self.nb.DeletePage(2)

        try:
            py_mod = imp_load_source_from_filePath(filePath + os.sep + '__demo__.py')
        except Exception as exc:
            raise exc

        self.ovr.SetPage(py_mod.GetOverview())

        if nbTabCurrentlyOn == 2: # Demo page or ERROR panel
            self.nb.SetSelection(0)
        else:
            self.nb.SetSelection(nbTabCurrentlyOn)
        self.gMainPanel.Thaw()

    def LoadDemo(self, filePath):
        print('LoadDemo filePath = %s' % filePath)

        self.gMainPanel.Freeze()

        self.LoadCodePageFile(filePath)

        # nbTabCurrentlyOn = self.nb.GetPageIndex(self.nb.GetCurrentPage())
        nbTabCurrentlyOn = self.nb.FindPage(self.nb.GetCurrentPage())

        # The third notebook page is always reserved
        # for a demo panel or error panel.
        if self.nb.GetPageCount() > 2:
            self.nb.DeletePage(2)


        if not os.path.abspath(os.path.dirname(filePath)) in sys.path:
            # sys.path.insert(0, os.path.abspath(os.path.dirname(filePath)))
            sys.path.append(os.path.abspath(os.path.dirname(filePath)))

        try:
            py_mod = imp_load_source_from_filePath(filePath)
        except Exception as exc:
            print(exc)
            if not exc:
                raise exc
            self.LoadErrorPanel()
            return

        # print(py_mod)
        # print('py_mod.__wxPyDemoPanel__ = %s' % py_mod.__wxPyDemoPanel__)

        # print(hasattr(code, '__wxPyDemoPanel__'))
        # print(hasattr(code.globals()))

        # print(dir(py_mod))

        # import inspect
        # klass = eval('py_mod.%s' %(py_mod.__wxPyDemoPanel__))
        # print(inspect.getargspec(klass))

        try:
            if hasattr(py_mod, '__wxPyDemoPanel__'): # Look for the magic attribute
                self.demoPage = eval('py_mod.%s(parent=self.nb, log=self.log)' % py_mod.__wxPyDemoPanel__)
            else:
                self.demoPage = TestPanel(self.nb, None, filePath)

            if hasattr(py_mod, 'overview'): # Look for the attribute
                self.ovr.SetPage(py_mod.overview)
            else:
                self.ovr.SetPage(self.GetHtmlIzedText('%s' % py_mod.__doc__))
            self.nb.SetPageText(0, os.path.split(filePath)[1] + ' ' + 'Overview')

        except Exception as exc:
            print(exc)
            if not exc:
                raise exc
            self.LoadErrorPanel()
            return

        self.nb.AddPage(self.demoPage, _(u'Demo'), imageId=1)

        self.nb.SetSelection(nbTabCurrentlyOn)
        self.gMainPanel.Thaw()

    def LoadErrorPanel(self, filePath=None):
        if not self.gMainPanel.IsFrozen():
            self.gMainPanel.Freeze()
        if self.nb.GetPageCount() > 2:
            self.nb.DeletePage(2)
        self.demoPage = DemoErrorPanel(self.nb, self.codePage,
                                       DemoError(sys.exc_info()), self)
        self.nb.AddPage(self.demoPage, _(u'ERROR'), imageId=-1)
        self.nb.SetSelection(2)
        self.gMainPanel.Thaw()

        # self.UpdateNotebook()

    def zLoadDemo(self, demoName):
        try:
            wx.BeginBusyCursor()
            self.gMainPanel.Freeze()

            os.chdir(self.cwd)
            try:
                # print('CodePage Pos on Load:', self.codePage.editor.GetCurrentPos())
                _codePagePositions[self.demoModules.name] = [self.codePage.editor.GetCurrentPos(),
                                                            self.codePage.editor.GetFirstVisibleLine(),
                                                            self.codePage.editor.GetSelectionStart(),
                                                            self.codePage.editor.GetSelectionEnd()]
            except AttributeError:
                pass #first time

            self.ShutdownDemoModule()

            if demoName == self.overviewText:
                # User selected the "wxPython Overview" node
                # i.e.: _this_ module
                # Changing the main window at runtime not yet supported...
                self.demoModules = DemoModules(__name__)
                self.SetOverview(self.overviewText, mainOverview)
                self.LoadDemoSource()
                self.UpdateNotebook(0)
            else:
                if os.path.exists(GetOriginalFilename(demoName)):
                    wx.LogMessage("Loading demo %s.py..." % demoName)
                    self.demoModules = DemoModules(demoName)
                    self.LoadDemoSource()

                else:

                    package, overview = LookForExternals(self.externalDemos, demoName)

                    if package:
                        wx.LogMessage("Loading demo %s.py..." % ("%s/%s"%(package, demoName)))
                        self.demoModules = DemoModules("%s/%s"%(package, demoName))
                        self.LoadDemoSource()
                    elif overview:
                        self.SetOverview(demoName, overview)
                        self.codePage = None
                        self.UpdateNotebook(0)
                    else:
                        self.SetOverview("wxPython", mainOverview)
                        self.codePage = None
                        self.UpdateNotebook(0)

        finally:
            wx.EndBusyCursor()
            self.gMainPanel.Thaw()

    #---------------------------------------------
    def LoadDemoSource(self):
        self.codePage = None
        self.codePage = DemoCodePanel(self.nb, self)
        self.codePage.LoadDemo(self.demoModules)

    #---------------------------------------------
    def RunModule(self):
        """Runs the active module"""

        module = self.demoModules.GetActive()
        self.ShutdownDemoModule()
        overviewText = ""

        # o The RunTest() for all samples must now return a window that can
        #   be placed in a tab in the main notebook.
        # o If an error occurs (or has occurred before) an error tab is created.

        if module is not None:
            wx.LogMessage("Running demo module...")
            if hasattr(module, "overview"):
                overviewText = module.overview

            try:
                self.demoPage = module.runTest(self, self.nb, self)
            except Exception as exc: # try and run normally
                print('exc = %s' % exc)
                # print(dir(module))
                # print(dir(self.demoModules))
                print(dir(self.demoModules.modules))

                # This is the path to the file we are trying to run.
                # print(self.demoModules.modules[1][0]['__file__'])
                try:
                    filePath = self.demoModules.modules[1][0]['__file__']
                except TypeError:
                    filePath = self.demoModules.modules[0][0]['__file__']

                if not exc:
                    try: # compiling it the right way to see if it will compile.

                        py_compile.compile(file=filePath, cfile=None, dfile=None, doraise=True)
                        # No syntax errors have been detected at this point,
                        # so lets create a demoPage for running the demo(s) manually.

                        self.demoPage = TestPanel(self.nb, None, filePath)

                    except Exception as exc:
                        print(exc)
                        if not exc:
                            raise exc
                        self.demoPage = DemoErrorPanel(self.nb, self.codePage,
                                                       DemoError(sys.exc_info()), self)

            bg = self.nb.GetThemeBackgroundColour()
            if bg:
                self.demoPage.SetBackgroundColour(bg)

            assert self.demoPage is not None, "runTest must return a window!"

        else:
            # There was a previous error in compiling or exec-ing

            try:
                filePath = self.demoModules.modules[1][0]['__file__']
            except TypeError:
                filePath = self.demoModules.modules[0][0]['__file__']

            # if not exc:
            try: # compiling it the right way to see if it will compile.

                py_compile.compile(file=filePath, cfile=None, dfile=None, doraise=True)
                # No syntax errors have been detected at this point,
                # so lets create a demoPage for running the demo(s) manually.

                self.demoPage = TestPanel(self.nb, None, filePath)

            except Exception as exc:
                print(exc)
                if not exc:
                    raise exc
                self.demoPage = DemoErrorPanel(self.nb, self.codePage,
                                               DemoError(sys.exc_info()), self)

        self.SetOverview(self.demoModules.name + " Overview", overviewText)

        if self.firstTime:
            # change to the demo page the first time a module is run
            self.UpdateNotebook(2)
            self.firstTime = False
        else:
            # otherwise just stay on the same tab in case the user has changed to another one
            self.UpdateNotebook()

    def OnSetCodePagePosition(self):
        try:
            # print('self.demoModules.name', self.demoModules.name)
            self.codePage.editor.GotoPos(_codePagePositions[self.demoModules.name][0])
            self.codePage.editor.SetFirstVisibleLine(_codePagePositions[self.demoModules.name][1])
            self.codePage.editor.SetSelection(_codePagePositions[self.demoModules.name][2],
                                              _codePagePositions[self.demoModules.name][3])
            self.codePage.editor.SetSTCFocus(True)
            self.codePage.editor.EnsureCaretVisible()
            # print('_codePagePositions',_codePagePositions)
        except AttributeError:
            pass #first time
        except KeyError:
            pass #first time

    #---------------------------------------------
    def ShutdownDemoModule(self):
        wx.CallAfter(self.OnSetCodePagePosition)

        if self.demoPage:
            # inform the window that it's time to quit if it cares
            if hasattr(self.demoPage, "ShutdownDemo"):
                self.demoPage.ShutdownDemo()
##            wx.YieldIfNeeded() # in case the page has pending events
            self.demoPage = None

    #---------------------------------------------
    def UpdateNotebook(self, select=-1):
        nb = self.nb
        debug = True
        self.gMainPanel.Freeze()

        def UpdatePage(page, pageText):
            pageExists = False
            pagePos = -1
            for i in range(nb.GetPageCount()):
                if nb.GetPageText(i) == pageText:
                    pageExists = True
                    pagePos = i
                    break

            if page:
                if not pageExists:
                    # Add a new page
                    nb.AddPage(page, pageText, imageId=nb.GetPageCount())
                    if debug: wx.LogMessage("DBG: ADDED %s" % pageText)
                else:
                    if nb.GetPage(pagePos) != page:
                        # Reload an existing page
                        nb.DeletePage(pagePos)
                        nb.InsertPage(pagePos, page, pageText, imageId=pagePos)
                        if debug: wx.LogMessage("DBG: RELOADED %s" % pageText)
                    else:
                        # Excellent! No redraw/flicker
                        if debug: wx.LogMessage("DBG: SAVED from reloading %s" % pageText)
            elif pageExists:
                # Delete a page
                nb.DeletePage(pagePos)
                if debug: wx.LogMessage("DBG: DELETED %s" % pageText)
            else:
                if debug: wx.LogMessage("DBG: STILL GONE - %s" % pageText)

        if select == -1:
            select = nb.GetSelection()

        UpdatePage(self.codePage, "Demo Code")
        UpdatePage(self.demoPage, "Demo")

        if select >= 0 and select < nb.GetPageCount():
            nb.SetSelection(select)

        self.gMainPanel.Thaw()

    #---------------------------------------------
    def SetOverview(self, name, text):
        self.curOverview = text
        lead = text[:6]
        if lead != '<html>' and lead != '<HTML>':
            text = '<br>'.join(text.split('\n'))
        ## text = text.decode('iso8859_1')
        self.ovr.SetPage(text)
        self.nb.SetPageText(0, os.path.split(name)[1])

    #---------------------------------------------
    def StartDownload(self):
        if self.downloading or not self.allowDocs:
            return

        item = self.tree.GetSelection()
        if self.tree.ItemHasChildren(item):
            return

        itemText = self.tree.GetItemText(item)

        if itemText in self.pickledData:
            self.LoadDocumentation(self.pickledData[itemText])
            return

        text = self.curOverview
        text += "<br><p><b>Checking for documentation on the wxWidgets website, please stand by...</b><br>"

        lead = text[:6]
        if lead != '<html>' and lead != '<HTML>':
            text = '<br>'.join(text.split('\n'))

        self.ovr.SetPage(text)

        self.downloadTimer.Start(100)
        self.downloadGauge.Show()
        self.statusBar.Reposition()
        self.downloading = True
        self.internetThread = InternetThread(self, itemText)

    #---------------------------------------------
    def StopDownload(self, error=None):
        self.downloadTimer.Stop()

        if not self.downloading:
            return

        if error:
            if self.sendDownloadError:
                self.log.WriteText("Warning: problems in downloading documentation from the wxWidgets website.\n")
                self.log.WriteText("Error message from the documentation downloader was:\n")
                self.log.WriteText("\n".join(error))
                self.sendDownloadError = False

        self.nb.SetPageImage(0, 0)

        self.internetThread.keepRunning = False
        self.internetThread = None

        self.downloading = False
        self.downloadGauge.Hide()
        self.statusBar.Reposition()

        text = self.curOverview

        lead = text[:6]
        if lead != '<html>' and lead != '<HTML>':
            text = '<br>'.join(text.split('\n'))

        self.ovr.SetPage(text)

    #---------------------------------------------
    def LoadDocumentation(self, data):
        text = self.curOverview
        addHtml = False

        if '<html>' not in text and '<HTML>' not in text:
            text = '<br>'.join(text.split('\n'))

        styles, events, extra, appearance = data

        if appearance:
            text += FormatImages(appearance)

        for names, values in zip(["Styles", "Extra Styles", "Events"], [styles, extra, events]):
            if not values:
                continue

            headers = (names == "Events" and [2] or [3])[0]
            text += "<p>" + FormatDocs(names, values, headers)

        item = self.tree.GetSelection()
        itemText = self.tree.GetItemText(item)

        self.pickledData[itemText] = data

        ## text = text.decode('iso8859_1')

        self.StopDownload()
        self.ovr.SetPage(text)
        #print("load time: ", time.time() - start)

    # Menu methods
    def OnFileExit(self, *event):
        self.Close()

    def OnToggleRedirect(self, event):
        app = wx.GetApp()
        if event.IsChecked():
            app.RedirectStdio()
            print("Print statements and other standard output will now be directed to this window.")
        else:
            app.RestoreStdio()
            print("Print statements and other standard output will now be sent to the usual location.")

    def OnAllowDownload(self, event):
        self.allowDocs = event.IsChecked()
        if self.allowDocs:
            self.StartDownload()
        else:
            self.StopDownload()

    def OnDeleteDocs(self, event):
        deleteMsg = "You are about to delete the downloaded documentation.\n" + \
                    "Do you want to continue?"
        dlg = wx.MessageDialog(self, deleteMsg, "wxPython Demo",
                               wx.YES_NO | wx.NO_DEFAULT| wx.ICON_QUESTION)
        result = dlg.ShowModal()
        if result == wx.ID_NO:
            dlg.Destroy()
            return

        dlg.Destroy()

        busy = wx.BusyInfo("Deleting downloaded data...")
        wx.SafeYield()

        pickledFile = GetDocFile()
        docDir = os.path.split(pickledFile)[0]

        if os.path.exists(docDir):
            shutil.rmtree(docDir, ignore_errors=True)

        self.pickledData = {}
        del busy
        self.sendDownloadError = True

    def OnAllowAuiFloating(self, event):
        self.allowAuiFloating = event.IsChecked()
        for pane in self.mgr.GetAllPanes():
            if pane.name != "Notebook":
                pane.Floatable(self.allowAuiFloating)

        self.EnableAUIMenu()
        self.mgr.Update()

    def EnableAUIMenu(self):
        wx.MenuItems = self.options_menu.GetMenuItems()
        for indx in range(4, len(wx.MenuItems)-1):
            item = wx.MenuItems[indx]
            item.Enable(self.allowAuiFloating)

    def OnAUIPerspectives(self, event):
        perspective = self.perspectives_menu.GetLabel(event.GetId())
        self.mgr.LoadPerspective(self.auiConfigurations[perspective])
        self.mgr.Update()

    def OnSavePerspective(self, event):
        dlg = wx.TextEntryDialog(self, "Enter a name for the new perspective:", "AUI Configuration")

        dlg.SetValue(("Perspective %d")%(len(self.auiConfigurations)+1))
        if dlg.ShowModal() != wx.ID_OK:
            return

        perspectiveName = dlg.GetValue()
        wx.MenuItems = self.perspectives_menu.GetMenuItems()
        for item in wx.MenuItems:
            if item.GetLabel() == perspectiveName:
                wx.MessageBox("The selected perspective name:\n\n%s\n\nAlready exists."%perspectiveName,
                              "Error", style=wx.ICON_ERROR)
                return

        item = wx.MenuItem(self.perspectives_menu, -1, dlg.GetValue(),
                           "Load user perspective %d"%(len(self.auiConfigurations)+1),
                           wx.ITEM_RADIO)
        self.Bind(wx.EVT_MENU, self.OnAUIPerspectives, item)
        self.perspectives_menu.Append(item)
        item.Check(True)
        self.auiConfigurations.update({dlg.GetValue(): self.mgr.SavePerspective()})

    def OnDeletePerspective(self, event):
        wx.MenuItems = self.perspectives_menu.GetMenuItems()
        lst = []
        loadDefault = False

        for indx, item in enumerate(wx.MenuItems):
            if indx > 0:
                lst.append(item.GetLabel())

        dlg = wx.MultiChoiceDialog(self,
                                   "Please select the perspectives\nyou would like to delete:",
                                   "Delete AUI Perspectives", lst)

        if dlg.ShowModal() == wx.ID_OK:
            selections = dlg.GetSelections()
            strings = [lst[x] for x in selections]
            for sel in strings:
                self.auiConfigurations.pop(sel)
                item = wx.MenuItems[lst.index(sel)+1]
                if item.IsChecked():
                    loadDefault = True
                    self.perspectives_menu.GetMenuItems()[0].Check(True)
                self.perspectives_menu.DeleteItem(item)
                lst.remove(sel)

        if loadDefault:
            self.mgr.LoadPerspective(self.auiConfigurations[DEFAULT_PERSPECTIVE])
            self.mgr.Update()

    def OnTreeExpansion(self, event):
        self.tree.SetExpansionState(self.expansionState)

    def OnHelpAbout(self, event):
        from About import MyAboutBox
        about = MyAboutBox(self)
        about.ShowModal()
        about.Destroy()

    def OnHelpFind(self, event):
        if self.finddlg != None:
            return

        self.nb.SetSelection(1)
        self.finddlg = wx.FindReplaceDialog(self, self.finddata, "Find",
                        wx.FR_NOMATCHCASE | wx.FR_NOWHOLEWORD)
        self.finddlg.Show(True)

    def OnUpdateFindItems(self, evt):
        evt.Enable(self.finddlg == None)

    def OnFind(self, event):
        editor = self.codePage.editor
        self.nb.SetSelection(1)
        end = editor.GetLastPosition()
        textstring = editor.GetRange(0, end).lower()
        findstring = self.finddata.GetFindString().lower()
        backward = not (self.finddata.GetFlags() & wx.FR_DOWN)
        if backward:
            start = editor.GetSelection()[0]
            loc = textstring.rfind(findstring, 0, start)
        else:
            start = editor.GetSelection()[1]
            loc = textstring.find(findstring, start)
        if loc == -1 and start != 0:
            # string not found, start at beginning
            if backward:
                start = end
                loc = textstring.rfind(findstring, 0, start)
            else:
                start = 0
                loc = textstring.find(findstring, start)
        if loc == -1:
            dlg = wx.MessageDialog(self, 'Find String Not Found',
                          'Find String Not Found in Demo File',
                          wx.OK | wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()
        if self.finddlg:
            if loc == -1:
                self.finddlg.SetFocus()
                return
            else:
                self.finddlg.Destroy()
                self.finddlg = None
        editor.ShowPosition(loc)
        editor.SetSelection(loc, loc + len(findstring))

    def OnFindNext(self, event):
        if self.finddata.GetFindString():
            self.OnFind(event)
        else:
            self.OnHelpFind(event)

    def OnFindClose(self, event):
        event.GetDialog().Destroy()
        self.finddlg = None

    def OnOpenShellWindow(self, evt):
        if self.shell:
            # if it already exists then just make sure it's visible
            s = self.shell
            if s.IsIconized():
                s.Iconize(False)
            s.Raise()
        else:
            # Make a PyShell window
            from wx import py
            namespace = { 'wx'    : wx,
                          'app'   : wx.GetApp(),
                          'frame' : self,
                          }
            self.shell = py.shell.ShellFrame(None, locals=namespace)
            self.shell.SetSize((640,480))
            self.shell.Show()

            # Hook the close event of the main frame window so that we
            # close the shell at the same time if it still exists
            def CloseShell(evt):
                if self.shell:
                    self.shell.Close()
                evt.Skip()
            self.Bind(wx.EVT_CLOSE, CloseShell)


    def OnOpenWidgetInspector(self, evt):
        # Activate the widget inspection tool
        from wx.lib.inspection import InspectionTool
        if not InspectionTool().initialized:
            InspectionTool().Init()

        # Find a widget to be selected in the tree.  Use either the
        # one under the cursor, if any, or this frame.
        wnd = wx.FindWindowAtPointer()
        if not wnd:
            wnd = self
        InspectionTool().Show(wnd, True)

    #---------------------------------------------
    def OnCloseWindow(self, event):
        self.mgr.UnInit()
        self.dying = True
        self.demoPage = None
        self.codePage = None
        self.gMenuBar = None
        self.StopDownload()

        if self.tbicon is not None:
            self.tbicon.Destroy()

        config = GetConfig()
        config.Write('ExpansionState', str(self.tree.GetExpansionState()))
        config.Write('AUIPerspectives', str(self.auiConfigurations))
        config.Write('AllowDownloads', str(self.allowDocs))
        config.Write('AllowDownloads', str(self.allowDocs))
        config.Write('AllowAUIFloating', str(self.allowAuiFloating))

        config.Flush()

        ## # Write the StcCodePageSettings.ini file
        ## gStcConfig.WriteInt('iIndentSize', gSTC.GetIndent())
        ## gStcConfig.WriteBool('bShowIndentationGuides', gSTC.GetIndentationGuides())
        ## gStcConfig.WriteBool('bBackSpaceUnIndents', gSTC.GetBackSpaceUnIndents())
        ## gStcConfig.WriteBool('bTabIndents', gSTC.GetTabIndents())
        ## gStcConfig.WriteInt('iTabWidth', gSTC.GetTabWidth())
        ## gStcConfig.WriteBool('bUseTabs', gSTC.GetUseTabs())
        ## gStcConfig.WriteBool('bViewWhiteSpace', gSTC.GetViewWhiteSpace())
        ## gStcConfig.WriteInt('iEOLMode', gSTC.GetEOLMode())
        ## gStcConfig.WriteBool('bViewEOL', gSTC.GetViewEOL())
        ## gStcConfig.WriteInt('iLongLineEdgeMode', gSTC.GetEdgeMode())
        ## gStcConfig.WriteInt('iLongLineEdge', gSTC.GetEdgeColumn())
        ## # gStcConfig.Write('sCaretForegroundColor', gSTC.GetCaretForeground())
        ## gStcConfig.WriteInt('iCaretSpeed', gSTC.GetCaretPeriod())
        ## gStcConfig.WriteBool('bCaretLineVisible', gSTC.GetCaretLineVisible())
        ## # gStcConfig.Write('sCaretLineBackground', gSTC.GetCaretLineBackground())
        ## #gStcConfig.WriteBool('bUseCaretLineBackgroundAlpha', 0):
        ## gStcConfig.WriteInt('iCaretLineBackgroundAlpha', gSTC.GetCaretLineBackAlpha())
        ## gStcConfig.WriteInt('iCaretPixelWidth', gSTC.GetCaretWidth())
        ##
        ## # gStcConfig.WriteBool('bUseBufferedDraw', gSTC.GetBufferedDraw())
        ## # gStcConfig.WriteBool('bScrollingPastLastLine', gSTC.GetEndAtLastLine())
        ## # self.SetMouseDwellTime(periodMilliseconds=gGlobalsDict['MouseDwellTime'])
        ## # self.SetTwoPhaseDraw(True)
        ## # self.SetWrapMode(gGlobalsDict['WordWrap'])
        ## # self.SetWrapVisualFlags(1)                                    #Set the display mode of visual flags for wrapped lines. 0 = off 1 = wraparrow at right 2 = wraparrow at left 3 = wraparrow at left and right
        ## # self.SetWrapVisualFlagsLocation(3)                            #Set the location of visual flags for wrapped lines. 3 = at where the wrap starts on the right
        ## # # self.SetWrapStartIndent(4)                                    #Set the start indent for wrapped lines.
        ##
        ## gStcConfig.Flush() # Permanently writes all changes to file.

        # Preserve the clipboard contents before the app
        # has exited, so it can still be used afterwards.
        wx.TheClipboard.Flush()

        MakeDocDirs()
        pickledFile = GetDocFile()
        fid = open(pickledFile, "wb")
        pickle.dump(self.pickledData, fid, pickle.HIGHEST_PROTOCOL)
        fid.close()

        self.Destroy()

    #---------------------------------------------
    def OnIdle(self, event):
        if self.otherWin:
            self.otherWin.Raise()
            self.demoPage = self.otherWin
            self.otherWin = None

    #---------------------------------------------
    def OnDownloadTimer(self, event):

        self.downloadGauge.Pulse()

        self.downloadImage += 1
        if self.downloadImage > 9:
            self.downloadImage = 3

        self.nb.SetPageImage(0, self.downloadImage)
##        wx.SafeYield()

    #---------------------------------------------
    def ShowTip(self):
        config = GetConfig()
        showTipText = config.Read("tips")
        if showTipText:
            showTip, index = eval(showTipText)
        else:
            showTip, index = (1, 0)

        # if showTip:
            # tp = wx.CreateFileTipProvider(opj("data/tips.txt"), index)
            # showTip = wx.ShowTip(self, tp)
            # index = tp.GetCurrentTip()
            # config.Write("tips", str( (showTip, index) ))
            # config.Flush()

    #---------------------------------------------
    def OnDemoMenu(self, event):
        try:
            selectedDemo = self.treeMap[event.GetEventObject().GetLabel(event.GetId())]
        except Exception as exc:
            selectedDemo = None
        if selectedDemo:
            self.tree.SelectItem(selectedDemo)
            self.tree.EnsureVisible(selectedDemo)

    #---------------------------------------------
    def OnIconify(self, evt):
        wx.LogMessage("OnIconify: %s" % evt.Iconized())
        evt.Skip()

    #---------------------------------------------
    def OnMaximize(self, evt):
        wx.LogMessage("OnMaximize")
        evt.Skip()

    #---------------------------------------------
    def OnActivate(self, evt):
        wx.LogMessage("OnActivate: %s" % evt.GetActive())
        evt.Skip()

    #---------------------------------------------
    def OnAppActivate(self, evt):
        wx.LogMessage("OnAppActivate: %s" % evt.GetActive())
        evt.Skip()

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

class MySplashScreen(SplashScreen):
    __doc__ = SplashScreen.__doc__
    def __init__(self):
        bmp = wx.Bitmap(opj("bitmaps/splash.png"))
        SplashScreen.__init__(self, bmp,
                              wx.adv.SPLASH_CENTRE_ON_SCREEN | wx.adv.SPLASH_TIMEOUT,
                              5000, None, -1)
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.fc = wx.CallLater(2000, self.ShowMain)


    def OnClose(self, evt):
        # Make sure the default handler runs too so this window gets
        # destroyed
        evt.Skip()
        self.Hide()

        # if the timer is still running then go ahead and show the
        # main frame now
        if self.fc.IsRunning():
            self.fc.Stop()
            self.ShowMain()

    def ShowMain(self):
        frame = wxPythonDemo(None, "wxPython: (A Demonstration)")
        frame.Show()
        if self.fc.IsRunning():
            self.Raise()
        wx.CallAfter(frame.ShowTip)


#------------------------------------------------------------------------------

from wx.lib.mixins.treemixin import ExpansionState
if USE_CUSTOMTREECTRL:
    import wx.lib.agw.customtreectrl as CT
    TreeBaseClass = CT.CustomTreeCtrl
else:
    TreeBaseClass = wx.TreeCtrl


class wxPythonDemoTree(ExpansionState, TreeBaseClass):
    """class wxPythonDemoTree(ExpansionState, TreeBaseClass):
    \"\"\"
    TreeBaseClass that shows the wxPython Demo's included packages
    according to the __demo__.py package structure.
    \"\"\""""
    if USE_CUSTOMTREECTRL:
        __doc__ = CT.CustomTreeCtrl.__doc__
    else:
        __doc__ = wx.TreeCtrl.__doc__
    def __init__(self, parent):
        """Default class constructor."""
        TreeBaseClass.__init__(self, parent, style=wx.TR_DEFAULT_STYLE|
                               wx.TR_HAS_VARIABLE_ROW_HEIGHT)
        ## self.BuildTreeImageList() # TODO: refactor
        if USE_CUSTOMTREECTRL:
            self.SetSpacing(10)
            self.SetWindowStyle(self.GetWindowStyle() & ~wx.TR_LINES_AT_ROOT)

        self.SetInitialSize((100, 80))

        self.SetTreeBackForeColors(wx.WHITE, wx.BLACK)
        # self.SetTreeBackForeColors(wx.BLACK, wx.WHITE)


    def BindTreeCtrlEvents(self):
        self.Bind(wx.EVT_TREE_ITEM_MENU, self.OnTreeContextMenu)
        self.Bind(wx.EVT_TREE_ITEM_EXPANDED, self.OnTreeItemExpanded)
        self.Bind(wx.EVT_TREE_ITEM_COLLAPSED, self.OnTreeItemCollapsed)
        self.Bind(wx.EVT_TREE_SEL_CHANGED, self.OnTreeSelChanged)
        self.Bind(wx.EVT_LEFT_DOWN, self.OnTreeLeftDown)

    def RecreateTree(self, event=None):
        # Catch the search type (name or content)
        searchMenu = gMainWin.filter.GetMenu().GetMenuItems()
        fullSearch = searchMenu[1].IsChecked()

        if event:
            if fullSearch:
                # Do not scan all the demo files for every char
                # the user input, use wx.EVT_TEXT_ENTER instead
                return

        expansionState = self.GetExpansionState()

        current = None
        item = self.GetSelection()
        if item:
            itemParent = self.GetItemParent(item)
            if itemParent:
                current = (self.GetItemText(item),
                           self.GetItemText(itemParent))

        self.Freeze()
        self.DeleteAllItems()
        self.root = self.AddRoot("wxPython Overview")
        self.SetItemImage(self.root, 0)
        self.SetItemData(self.root, 0)

        treeFont = self.GetFont()
        catFont = self.GetFont()

        # The native treectrl on MSW has a bug where it doesn't draw
        # all of the text for an item if the font is larger than the
        # default.  It seems to be clipping the item's label as if it
        # was the size of the same label in the default font.
        if USE_CUSTOMTREECTRL or 'wxMSW' not in wx.PlatformInfo:
            treeFont.SetPointSize(treeFont.GetPointSize()+2)

        treeFont.SetWeight(wx.FONTWEIGHT_BOLD)
        catFont.SetWeight(wx.FONTWEIGHT_BOLD)
        self.SetItemFont(self.root, treeFont)

        firstChild = None
        selectItem = None
        filter = gMainWin.filter.GetValue()
        count = 0


        def dirHasDemoFile(dirPath):
            # print('called dirHasDemoFile')
            return os.path.exists(dirPath + os.sep + "__demo__.py")

        # Building the new framework tree imageList

        self.treeImageList = treeImageList = wx.ImageList(width=16, height=16, mask=True, initialCount=0)
        self.treeImageList.Add(images.overview.GetBitmap())
        self.SetImageList(treeImageList)


        local_imp_load_source_from_filePath = imp_load_source_from_filePath
        # Building the new framework tree
        osSep = os.sep
        pyFilesInDemoRoot = [f for f in os.listdir(gAppDir) if f.lower().endswith('.py')]
        root = gAppDir
        externalDemos = {root : self.GetRootItem()}
        demoPackageInfos = {}
        # showTheseDemos = []
        treeItemDirBGColor = '#FFFFFF'
        treeItemFileBGColor = '#FFFFFF'
        treeItemDirTextColor = '#000000'
        treeItemFileTextColor = '#000000'
        treeItemDirFont = wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False)
        treeItemFileFont = wx.Font(8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False)
        treeDirItems = []
        self_SetItemTextColour = self.SetItemTextColour
        self_SetItemBold = self.SetItemBold
        self_SetItemData = self.SetItemData
        self_SetItemImage = self.SetItemImage
        self_SetItemBackgroundColour = self.SetItemBackgroundColour
        self_SetItemFont = self.SetItemFont
        self_AppendItem = self.AppendItem
        treeImageList_Add = treeImageList.Add
        treeImageList_GetImageCount = treeImageList.GetImageCount
        for (path, dirs, files) in os.walk(gAppDir):
            for dirname in sorted(dirs):
                if dirHasDemoFile(path + osSep + dirname):
                    fullpath = os.path.join(path, dirname)
                    demoPackageInfos[fullpath] = local_imp_load_source_from_filePath(fullpath + osSep + "__demo__.py")
                    treeImageList_Add(demoPackageInfos[fullpath].GetDemoBitmap().GetBitmap())
                    treeItemName = demoPackageInfos[fullpath].GetDemos()[0]
                    treeItemDir = self_AppendItem(externalDemos[path], treeItemName)
                    treeDirItems.append(treeItemDir)
                    self_SetItemBold(treeItemDir) # Bold catagory name/directory text
                    # self.SetItemFont(treeItemDir, treeItemDirFont)
                    self_SetItemTextColour(treeItemDir, treeItemDirTextColor)
                    self_SetItemData(treeItemDir, fullpath)
                    self_SetItemImage(treeItemDir, treeImageList_GetImageCount() - 1)
                    self_SetItemBackgroundColour(treeItemDir, treeItemDirBGColor)
                    externalDemos[fullpath] = treeItemDir
                else:
                    continue

            # try:
                # showTheseDemos = demoPackageInfos[path].GetDemos()[1]
                # print(showTheseDemos)
            # except KeyError:
                # print('KeyError', path)
                # continue

            for filename in sorted(files):
                fn = filename.lower()
                if fn.endswith('.py'):
                    # Don't show demo specific files or the actual demo app files in the head directory.
                    if not fn in ('__init__.py', '__demo__.py') and filename not in pyFilesInDemoRoot:
                        fullpath = path + osSep + filename

                        if filter and not filter in filename:
                            continue

                        if path in externalDemos:
                            treeItemFile = self_AppendItem(externalDemos[path], filename)
                            self_SetItemData(treeItemFile, fullpath)
                            self_SetItemImage(treeItemFile, self.GetItemImage(self.GetItemParent(treeItemFile)))
                            self_SetItemFont(treeItemFile, treeItemFileFont)
                            self_SetItemTextColour(treeItemDir, treeItemFileTextColor)
                            self_SetItemBackgroundColour(treeItemFile, treeItemFileBGColor)
                            externalDemos[fullpath] = treeItemFile

            # try:
                # if not filterCountFound:
                    # self.Delete(treeItemDir)
            # except UnboundLocalError:
                # pass

        def zprintChildren(tree, treeItem, indent=0):
            print("  " * indent + tree.GetItemText(treeItem))
            subItem = tree.GetFirstChild(treeItem)[0]
            while subItem.IsOk():
                printChildren(tree, subItem, indent+1)
                subItem = tree.GetNextSibling(subItem)

        def printChildren(tree, treeItem, indent=0):
            subItem = tree.GetFirstChild(treeItem)[0]
            while subItem.IsOk():
                print("  " * indent + tree.GetItemText(subItem))
                printChildren(tree, subItem, indent+1)
                subItem = tree.GetNextSibling(subItem)

        if filter:
            # We need to take care of the empty tree folder items clutter also,
            # so we will work our way backwards through the tree items.
            treeDirItems.reverse()
            [self.Delete(item) for item in treeDirItems
                if not self.GetChildrenCount(item, recursively=False)]



        # result = self.GetItemFromLabel(self, 'Window Layout', self.GetRootItem())
        # result = self.GetItemFromLabel(self, 'MyCoolDemo.py', self.GetRootItem())
        # if result.IsOk():
        #     self.SetItemBackgroundColour(result, '#FF0000')
        #     print('We have a match!')

        gMainWin.externalDemos = externalDemos
        # print(externalDemos)


        ## # Build the tree.
        ## for category, items in _treeList:
        ##     count += 1
        ##     if filter:
        ##         if fullSearch:
        ##             items = self.searchItems[category]
        ##         else:
        ##             items = [item for item in items if filter.lower() in item.lower()]
        ##     if items:
        ##         child = self.AppendItem(self.root, category, image=count)
        ##         self.SetItemFont(child, catFont)
        ##         self.SetItemData(child, count)
        ##         if not firstChild: firstChild = child
        ##         for childItem in items:
        ##             image = count
        ##             if DoesModifiedExist(childItem):
        ##                 image = len(_demoPngsList)
        ##             theDemo = self.AppendItem(child, childItem, image=image)
        ##             self.SetItemData(theDemo, count)
        ##             self.treeMap[childItem] = theDemo
        ##             if current and (childItem, category) == current:
        ##                 selectItem = theDemo


        self.Expand(self.root)
        if firstChild:
            self.Expand(firstChild)
        if filter:
            self.ExpandAll()
        elif expansionState:
            self.SetExpansionState(expansionState)
        if selectItem:
            self.skipLoad = True
            self.SelectItem(selectItem)
            self.skipLoad = False

        self.Thaw()
        self.searchItems = {}

    def GetItemFromLabel(self, tree, searchText, rootItem):
        item, cookie = tree.GetFirstChild(rootItem)

        while item.IsOk():
            text = tree.GetItemText(item)
            if text.lower() == searchText.lower():
                return item
            if tree.ItemHasChildren(item):
                match = self.GetItemFromLabel(tree, searchText, item)
                if match.IsOk():
                    return match
            item, cookie = tree.GetNextChild(rootItem, cookie)

        return wx.TreeItemId()

    def OnTreeItemExpanded(self, event):
        item = event.GetItem()
        wx.LogMessage("OnTreeItemExpanded: %s" % self.GetItemText(item))
        event.Skip()

    def OnTreeItemCollapsed(self, event):
        item = event.GetItem()
        wx.LogMessage("OnTreeItemCollapsed: %s" % self.GetItemText(item))
        event.Skip()

    def OnTreeLeftDown(self, event):
        # reset the overview text if the tree item is clicked on again
        pt = event.GetPosition()
        item, flags = self.HitTest(pt)
        if item == self.GetSelection():
            gMainWin.SetOverview(self.GetItemText(item) + " Overview", gMainWin.curOverview)
        event.Skip()

    def OnTreeSelChanged(self, event=None):
        self.item = self.GetFocusedItem()
        itemText = self.GetItemText(self.item)

        if self.item:
            print("OnTreeSelChanged: %s\n" % self.GetItemText(self.item))
            fileOrDirPath = self.GetItemData(self.item)
            # treeItemText = self.GetItemText(self.item)
            print('fileOrDirPath = %s' % fileOrDirPath)
            if not fileOrDirPath: # wxPython Overview/root
                pass
            elif os.path.isdir(fileOrDirPath):
                # Show the overview and code editor pages only.
                gMainWin.Load__demo__py(fileOrDirPath)
            else:
                if gMainWin.PyCompileFile(fileOrDirPath):
                    gMainWin.LoadDemo(fileOrDirPath)
                else:
                    gMainWin.LoadErrorPanel(fileOrDirPath)
        if event:
            event.Skip()

    #---------------------------------------------
    def zOnTreeSelChanged(self, event=None):
        if self.dying or not self.loaded or self.skipLoad:
            return

        self.StopDownload()

        ## item = event.GetItem()
        item = self.GetFocusedItem()
        itemText = self.GetItemText(item)
        self.LoadDemo(itemText)

        self.StartDownload()

    def SetTreeBackForeColors(self, backColor=wx.WHITE, foreColor=wx.BLACK):
        self.SetBackgroundColour(backColor)
        self.SetForegroundColour(foreColor)

    def OnTreeContextMenu(self, event):
        menu = wx.Menu()

        pt = event.GetPoint()
        treeItem, flags = self.HitTest(pt)
        if treeItem:
            gMainWin.log.WriteText("OnRightUp: %s\n"
                               % self.GetItemText(treeItem))
            self.SelectItem(treeItem)
            self.SetFocusedItem(treeItem)

        if self.ItemHasChildren(treeItem):
            if self.IsExpanded(treeItem):
                ID_COLLAPSEALLCHILDREN = wx.NewId()
                menu.Append(wx.MenuItem(menu, ID_COLLAPSEALLCHILDREN, _(u'Collapse All Children')))
                menu.Bind(wx.EVT_MENU, self.OnCollapseAllChildren, id=ID_COLLAPSEALLCHILDREN)

                ID_COLLAPSE = wx.NewId()
                menu.Append(wx.MenuItem(menu, ID_COLLAPSE, _(u'Collapse')))
                menu.Bind(wx.EVT_MENU, self.OnCollapse, id=ID_COLLAPSE)
            else:
                ID_EXPANDALLCHILDREN = wx.NewId()
                menu.Append(wx.MenuItem(menu, ID_EXPANDALLCHILDREN, _(u'Expand All Children')))
                menu.Bind(wx.EVT_MENU, self.OnExpandAllChildren, id=ID_EXPANDALLCHILDREN)

                ID_EXPAND = wx.NewId()
                menu.Append(wx.MenuItem(menu, ID_EXPAND, _(u'Expand')))
                menu.Bind(wx.EVT_MENU, self.OnExpand, id=ID_EXPAND)

            menu.AppendSeparator()

        ID_COLLAPSEALL = wx.NewId()
        menu.Append(wx.MenuItem(menu, ID_COLLAPSEALL, _(u'Collapse All')))

        ID_EXPANDALL = wx.NewId()
        menu.Append(wx.MenuItem(menu, ID_EXPANDALL, _(u'Expand All')))

        menu.Bind(wx.EVT_MENU, self.OnCollapseAll, id=ID_COLLAPSEALL)
        menu.Bind(wx.EVT_MENU, self.OnExpandAll, id=ID_EXPANDALL)

        menu.AppendSeparator()

        demoSubMenu = gMainWin.BuildDemoMenu()
        menu.AppendSubMenu(demoSubMenu, _(u'Demo'))

        self.PopupMenu(menu)

        menu.Destroy()

    def OnCollapseAll(self, event):
        self.CollapseAll()

    def OnExpandAll(self, event):
        focusedItem = self.GetFocusedItem()
        self.ExpandAll()
        self.EnsureVisible(focusedItem)

    def OnCollapseAllChildren(self, event):
        focusedItem = self.GetFocusedItem()
        self.CollapseAllChildren(focusedItem)
        self.EnsureVisible(focusedItem)

    def OnExpandAllChildren(self, event):
        focusedItem = self.GetFocusedItem()
        self.ExpandAllChildren(focusedItem)
        self.EnsureVisible(focusedItem)

    def OnCollapse(self, event):
        focusedItem = self.GetFocusedItem()
        self.Collapse(focusedItem)
        self.EnsureVisible(focusedItem)

    def OnExpand(self, event):
        focusedItem = self.GetFocusedItem()
        self.Expand(focusedItem)
        self.EnsureVisible(focusedItem)

    def AppendItem(self, parent, text, image=-1, wnd=None):
        if USE_CUSTOMTREECTRL:
            item = TreeBaseClass.AppendItem(self, parent, text, image=image, wnd=wnd)
        else:
            item = TreeBaseClass.AppendItem(self, parent, text, image=image)
        return item

    ## def BuildTreeImageList(self): # TODO: refactor
    ##     imgList = wx.ImageList(16, 16)
    ##     for png in _demoPngsList:
    ##         imgList.Add(images.catalog[png].GetBitmap())
    ##
    ##     # add the image for modified demos.
    ##     imgList.Add(images.catalog["custom"].GetBitmap())
    ##
    ##     self.AssignImageList(imgList)

    def GetItemIdentity(self, item):
        return self.GetItemData(item)


#------------------------------------------------------------------------------

class MyApp(wx.App, wx.lib.mixins.inspection.InspectionMixin):
    __doc__ = wx.App.__doc__
    def OnInit(self):

        global gApp
        gApp = self

        # Check runtime version
        if version.VERSION_STRING != wx.VERSION_STRING:
            wx.MessageBox(caption="Warning",
                          message="You're using version %s of wxPython, but this copy of the demo was written for version %s.\n"
                          "There may be some version incompatibilities..."
                          % (wx.VERSION_STRING, version.VERSION_STRING))

        self.InitInspection()  # for the InspectionMixin base class

        # Now that we've warned the user about possible problems,
        # lets import images
        import images as i
        global images
        images = i

        # For debugging
        #self.SetAssertMode(wx.APP_ASSERT_DIALOG|wx.APP_ASSERT_EXCEPTION)

        wx.SystemOptions.SetOption("mac.window-plain-transition", 1)
        self.SetAppName("wxPyDemo")

        # Create and show the splash screen.  It will then create and
        # show the main frame when it is time to do so.  Normally when
        # using a SplashScreen you would create it, show it and then
        # continue on with the application's initialization, finally
        # creating and showing the main application window(s).  In
        # this case we have nothing else to do so we'll delay showing
        # the main frame until later (see ShowMain above) so the users
        # can see the SplashScreen effect.
        splash = MySplashScreen()
        splash.Show()

        # Add all the MouseWheel functionality and tweaks to all app widgets
        # so that when using the mousewheel when hovered over a widget does
        # user friendly stuff,
        # like Ex: *SCROLL* the widget under the mouse pointer.
        # without losing or setting focus to it, which can be very annoying.
        self.enteredWindow = self
        self.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterWindow)
        self.Bind(wx.EVT_MOUSEWHEEL, self.OnMouseWheel)

        return True

    def OnEnterWindow(self, event):
        event.Skip()
        print('GetClassName = %s' % event.GetEventObject().GetClassName())
        self.enteredWindow = event.GetEventObject()

    def GetEnteredWindow(self):
        return self.enteredWindow

    def OnMouseWheel(self, event):
        evtObj = event.GetEventObject()
        wr = event.GetWheelRotation()

        print('GetEventObject = %s' % evtObj)
        print('GetEnteredWindow = %s' % self.GetEnteredWindow())
        print('GetWheelRotation = %s' % wr)
        print('wx.Window.FindFocus().GetClassName() = %s' % wx.Window.FindFocus().GetClassName())

        # Gittery/Ugly.
        #HACK# windowWithFocus = wx.Window.FindFocus()
        #HACK# windowWithFocusClassName = windowWithFocus.GetClassName()
        #HACK# if windowWithFocusClassName in ('wxHtmlWindow'): # reverse/nullify the action fix
        #HACK#     if wr > 0:
        #HACK#         windowWithFocus.ScrollLines(3)
        #HACK#     elif wr < 0:
        #HACK#         windowWithFocus.ScrollLines(-3)

        enteredWindow = self.GetEnteredWindow()
        className = enteredWindow.GetClassName()
        # if enteredWindow == evtObj:
            # print('Eat the MouseWheel Event')
            # event.Skip() # Else eat the event. We dont want two different ctrls doing something at the same time.
        if wr < 0:
            print('Down')
            if className in ('wxStyledTextCtrl'):
                xoffset = enteredWindow.GetXOffset()
                ms = wx.GetMouseState()
                ctrlDown = ms.ControlDown()
                shiftDown = ms.ShiftDown()
                altDown = ms.AltDown()
                #-- Shift + MouseWheel = Scroll Horizontally
                if shiftDown and not altDown and not ctrlDown:
                    enteredWindow.SetXOffset(xoffset + 30)
                    return

                #-- Ctrl + MouseWheel = Zoom
                # Duplicate Default stc ctrl zooming behavior to bypass
                # (MouseWheel not working after a undetermined amount of time)2.9BUG
                elif ctrlDown and not altDown and not shiftDown:
                   enteredWindow.SetZoom(enteredWindow.GetZoom() - 1)
                   return

                #-- MouseWheel = Scroll Vertically
                # Duplicate Default stc scrolling behavior to bypass
                # (MouseWheel not working after a undetermined amount of time)2.9BUG
                else:
                   enteredWindow.LineScroll(0, 3)
                   return

            elif className in ('wxNotebook'):
                enteredWindow.AdvanceSelection(False)
            elif className in ('wxTextCtrl', 'wxTreeCtrl', 'wxHtmlWindow', 'wxListCtrl', 'wxListView'):
                enteredWindow.ScrollLines(3)
                # enteredWindow.LineScroll(0, 3)
            elif className in ('wxCheckListBox', 'wxListBox', 'wxComboBox', 'wxChoice'):
                if enteredWindow.GetSelection() == wx.NOT_FOUND:
                    enteredWindow.Select(0)
                elif not enteredWindow.GetSelection() == enteredWindow.GetCount() - 1:
                    enteredWindow.Select(enteredWindow.GetSelection() + 1)
        elif wr > 0:
            print('Up')
            if className in ('wxStyledTextCtrl'):
                xoffset = enteredWindow.GetXOffset()
                ms = wx.GetMouseState()
                ctrlDown = ms.ControlDown()
                shiftDown = ms.ShiftDown()
                altDown = ms.AltDown()
                if shiftDown and wr > 0 and not altDown and not ctrlDown:
                    if not xoffset <= 0:
                        enteredWindow.SetXOffset(xoffset - 30)
                        return
                    else:
                        return

                #-- Ctrl + MouseWheel = Zoom
                # Duplicate Default stc ctrl zooming behavior to bypass
                # (MouseWheel not working after a undetermined amount of time)2.9BUG
                elif ctrlDown and not altDown and not shiftDown:
                   enteredWindow.SetZoom(enteredWindow.GetZoom() + 1)
                   return

                #-- MouseWheel = Scroll Vertically
                # Duplicate Default stc scrolling behavior to bypass
                # (MouseWheel not working after a undetermined amount of time)2.9BUG
                else:
                   enteredWindow.LineScroll(0, -3)
                   return

            elif className in ('wxNotebook'):
                enteredWindow.AdvanceSelection(True)
            elif className in ('wxTextCtrl', 'wxTreeCtrl', 'wxHtmlWindow', 'wxListCtrl', 'wxListView'):
                enteredWindow.ScrollLines(-3)
                # enteredWindow.LineScroll(0, -3)
            elif className in ('wxCheckListBox', 'wxListBox', 'wxComboBox', 'wxChoice'):
                if enteredWindow.GetSelection() == wx.NOT_FOUND:
                    enteredWindow.Select(0)
                elif enteredWindow.GetSelection(): # not 0
                    enteredWindow.Select(enteredWindow.GetSelection() - 1)

#------------------------------------------------------------------------------

def main():
    try:
        demoPath = os.path.dirname(__file__)
        os.chdir(demoPath)
    except Exception as exc:
        pass
    app = MyApp(False)
    app.MainLoop()

#------------------------------------------------------------------------------


mainOverview = """<html><body>
<h2>wxPython</h2>

<p> wxPython is a <b>GUI toolkit</b> for the Python programming
language.  It allows Python programmers to create programs with a
robust, highly functional graphical user interface, simply and easily.
It is implemented as a Python extension module (native code) that
wraps the popular wxWindows cross platform GUI library, which is
written in C++.

<p> Like Python and wxWindows, wxPython is <b>Open Source</b> which
means that it is free for anyone to use and the source code is
available for anyone to look at and modify.  Or anyone can contribute
fixes or enhancements to the project.

<p> wxPython is a <b>cross-platform</b> toolkit.  This means that the
same program will run on multiple platforms without modification.
Currently supported platforms are 32-bit Microsoft Windows, most Unix
or unix-like systems, and Macintosh OS X. Since the language is
Python, wxPython programs are <b>simple, easy</b> to write and easy to
understand.

<p> <b>This demo</b> is not only a collection of test cases for
wxPython, but is also designed to help you learn about and how to use
wxPython.  Each sample is listed in the tree control on the left.
When a sample is selected in the tree then a module is loaded and run
(usually in a tab of this notebook,) and the source code of the module
is loaded in another tab for you to browse and learn from.

"""


#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

if __name__ == '__main__':
    __name__ = 'Main'
    main()

#------------------------------------------------------------------------------
