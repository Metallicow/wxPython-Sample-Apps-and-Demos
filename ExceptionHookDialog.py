#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-Imports-----------------------------------------------------------------------

#--Python Imports.
import os
import sys
import time
import traceback
import re

#--wxPython Imports.
import wx
if 'phoenix' in wx.version():
    PHOENIX = True
else:
    PHOENIX = False

import wx.lib.sized_controls as SC
import wx.stc as stc
from wx.lib.embeddedimage import PyEmbeddedImage

#--Microsoft Windows Only Imports.
## import winsound

_ = wx.GetTranslation

gExcDialogParent = None
gExcPanelParent = None

xception48 = PyEmbeddedImage(
    "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")

if wx.Platform == '__WXMSW__':
    # For Microsoft Windows OS
    faces = {
            'times': 'Times New Roman',
            'mono' : 'Courier New',
            'helv' : 'Arial',
            'other': 'Comic Sans MS',
            'size' : 10,
            'size2': 8,
            }
elif wx.Platform == '__WXMAC__':
    # For Macintosh Apple OS
    faces = {
            'times': 'Times New Roman',
            'mono' : 'Monaco',
            'helv' : 'Arial',
            'other': 'Comic Sans MS',
            'size' : 10,
            'size2': 8,
            }
else:
    # For Whatever else OS
    faces = {
            'times': 'Times',
            'mono' : 'Courier',
            'helv' : 'Helvetica',
            'other': 'new century schoolbook',
            'size' : 10,
            'size2': 8,
             }

stcStyles = {
    # default style
    stc.STC_STYLE_DEFAULT :
    'fore:#000000,back:#FFFFFF,face:%(mono)s,size:%(size)d' %faces,
    # default python style
    stc.STC_P_DEFAULT :
    'fore:#000000,back:#FFFFFF,face:%(mono)s,size:%(size)d' %faces,
    # comments
    stc.STC_P_COMMENTLINE :
    'fore:#007F00,back:#EAFFE9,face:%(mono)s,size:%(size)d' %faces,
    # number
    stc.STC_P_NUMBER :
    'fore:#FF0000,back:#FFFFFF,size:%(size)d' %faces,
    # string
    stc.STC_P_STRING :
    'fore:#FF8000,back:#FFFFFF,face:%(mono)s,size:%(size)d' %faces,
    # single quoted string
    stc.STC_P_CHARACTER :
    'fore:#FF8000,back:#FFFFFF,face:%(mono)s,size:%(size)d' %faces,
    # keyword
    stc.STC_P_WORD :
    'fore:#FF0000,back:#FFFFFF,face:%(mono)s,size:%(size)d' %faces,
    # keyword2
    stc.STC_P_WORD2 :
    'fore:#6000FF,back:#FFFFFF,face:%(mono)s,size:%(size)d' %faces,
    # triple quotes
    stc.STC_P_TRIPLE :
    'fore:#000000,back:#FFF7EE,size:%(size)d' %faces,
    # triple double quotes
    stc.STC_P_TRIPLEDOUBLE :
    'fore:#FF8000,back:#FFF7EE,size:%(size)d' %faces,
    # class name definition
    stc.STC_P_CLASSNAME :
    'fore:#0000FF,back:#FFFFFF,bold,underline,size:%(size)d' %faces,
    # function or method name definition
    stc.STC_P_DEFNAME :
    'fore:#007F7F,back:#FFFFFF,bold,size:%(size)d' %faces,
    # operators
    stc.STC_P_OPERATOR :
    'fore:#000000,back:#FFFFFF,bold,size:%(size)d' %faces,
    # identifiers
    stc.STC_P_IDENTIFIER :
    'fore:#000000,back:#FFFFFF,face:%(mono)s,size:%(size)d' %faces,
    # comment-blocks
    stc.STC_P_COMMENTBLOCK :
    'fore:#7F7F7F,back:#F8FFF8,size:%(size)d' %faces,
    # end of line where string is not closed
    stc.STC_P_STRINGEOL :
    'fore:#000000,back:#FFFFFF,face:%(mono)s,size:%(size)d' %faces,
    }

class ExceptionSTC(stc.StyledTextCtrl):
    def __init__(self, parent, id=wx.ID_ANY):
        stc.StyledTextCtrl.__init__(self, parent, id, style=wx.BORDER_STATIC)
        self.SetMarginWidth(1, 0)# This makes it look like just a simple textctrl.

        self.SetLexer(stc.STC_LEX_PYTHON)

        kwdList1 = [u'Traceback']
        kwdListPython = [
            # KeywordList formated as Python's built-in Exception heirarchy
            u'BaseException',
                u'SystemExit',
                u'KeyboardInterrupt',
                u'GeneratorExit',
                u'Exception',
                    u'StopIteration',
                    u'ArithmeticError',
                        u'FloatingPointError',
                        u'OverflowError',
                        u'ZeroDivisionError',
                    u'AssertionError',
                    u'AttributeError',
                    u'BufferError',
                    u'EOFError',
                    u'ImportError',
                    u'LookupError',
                        u'IndexError',
                        u'KeyError',
                    u'MemoryError',
                    u'NameError',
                        u'UnboundLocalError',
                    u'OSError',
                        u'BlockingIOError',
                        u'ChildProcessError',
                        u'ConnectionError',
                            u'BrokenPipeError',
                            u'ConnectionAbortedError',
                            u'ConnectionRefusedError',
                            u'ConnectionResetError',
                        u'FileExistsError',
                        u'FileNotFoundError',
                        u'InterruptedError',
                        u'IsADirectoryError',
                        u'NotADirectoryError',
                        u'PermissionError',
                        u'ProcessLookupError',
                        u'TimeoutError',
                    u'ReferenceError',
                    u'RuntimeError',
                        u'NotImplementedError',
                    u'SyntaxError',
                        u'IndentationError',
                            u'TabError',
                    u'SystemError',
                    u'TypeError',
                    u'ValueError',
                        u'UnicodeError',
                            u'UnicodeDecodeError',
                            u'UnicodeEncodeError',
                            u'UnicodeTranslateError',
                    u'Warning',
                        u'DeprecationWarning',
                        u'PendingDeprecationWarning',
                        u'RuntimeWarning',
                        u'SyntaxWarning',
                        u'UserWarning',
                        u'FutureWarning',
                        u'ImportWarning',
                        u'UnicodeWarning',
                        u'BytesWarning',
                        u'ResourceWarning',
                    ]
        kwdListwxPython = [u'DragError',
                           u'LOG_Error',
                           u'LOG_FatalError',
                           u'LogError',
                           u'LogFatalError',
                           u'LogSysError',
                           u'PyAssertionError',
                           u'PyDeadObjectError',
                           u'PyNoAppError',
                           u'PyUnbornObjectError',
                           ]
        kwdList2 = []
        for keywordList in [kwdListPython, kwdListwxPython]:
            for keyword in keywordList:
                kwdList2.append(keyword)

        self.SetKeyWords(0, ' '.join(kwdList1))
        self.SetKeyWords(1, ' '.join(kwdList2))

        self.SetWrapMode(stc.STC_WRAP_WORD)

        self.StyleClearAll() # Reset all to be like the default.

        if sys.version_info[0] == 2:
            for style, styleString in stcStyles.iteritems():
                self.StyleSetSpec(style, styleString)
        elif sys.version_info[0] == 3:
            for style, styleString in list(stcStyles.items()):
                self.StyleSetSpec(style, styleString)

        # Other Styling Stuff
        self.StyleSetBold(stc.STC_P_WORD, True)
        self.StyleSetHotSpot(stc.STC_P_WORD, True)
        self.StyleSetBold(stc.STC_P_STRING, True)
        self.StyleSetHotSpot(stc.STC_P_STRING, True)

        self.StyleSetBold(stc.STC_P_WORD2, True)
        self.StyleSetHotSpot(stc.STC_P_WORD2, True)

        self.UsePopUp(False)
        self.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
        self.Bind(wx.EVT_RIGHT_UP, self.OnContextMenu)
        self.Bind(wx.EVT_CONTEXT_MENU, self.OnContextMenu)
        self.Bind(stc.EVT_STC_ROMODIFYATTEMPT, self.OnSTCReadOnlyModifyAttempt)
        self.Bind(stc.EVT_STC_HOTSPOT_DCLICK, self.OnSTCHotSpotDClick)

        self.CmdKeyAssign(ord('C'), stc.STC_SCMOD_CTRL,  stc.STC_CMD_COPY)
        self.CmdKeyAssign(ord('A'), stc.STC_SCMOD_CTRL,  stc.STC_CMD_SELECTALL)

    def OnSTCHotSpotDClick(self, event):
        curLine = self.GetCurrentLine()
        lineText = self.GetLine(curLine)
        findFilepath = re.match(pattern=r'  File "(.+)", line ([0-9]+)',
                                string=lineText,
                                flags=0)
        if findFilepath:
            ## print('group = ', findFilepath.group())
            ## print('group(1) = ', findFilepath.group(1))
            ## print('group(2) = ', findFilepath.group(2))
            ## print('start = ', findFilepath.start())
            ## print('end = ', findFilepath.end())
            ## print('span = ', findFilepath.span())

            filePath = u'%s' %findFilepath.group(1)
            goToLine = int(findFilepath.group(2)) - 1

            # Open file and goto line.
            if os.path.exists(filePath):
                ## print(gExcDialogParent)
                ## print(gExcPanelParent)
                try:
                    if gExcDialogParent:
                        gExcDialogParent.OnActuallyOpenTheFile(filepath=filePath, gotoline=goToLine) # You may need to modify this source code to direct the filepath/etc to your local stc open function.
                    elif gExcPanelParent:
                        gExcPanelParent.OnActuallyOpenTheFile(filepath=filePath, gotoline=goToLine) # You may need to modify this source code to direct the filepath/etc to your local stc open function.
                except AttributeError:
                    font = wx.Font(faces['size'],
                                   wx.FONTFAMILY_DEFAULT,
                                   wx.FONTSTYLE_NORMAL,
                                   wx.FONTWEIGHT_NORMAL,
                                   False,
                                   faces['mono'])
                    ExceptionHookDialog(parent=None,
                                        excInfo=sys.exc_info(),
                                        title=_(u'ERROR'),
                                        message=_(u'class ExceptionSTC(stc.StyledTextCtrl):\n'
                                        u'    def OnSTCHotSpotDClick(self, event):\n'
                                        u'You may need to modify this source code to direct\n'
                                        u'the filepath/etc to your local stc open function.'),
                                        messageFont=font
                                        ).ShowModal()
                except Exception as exc:
                    ExceptionHookDialog().ShowModal()

    def OnSTCReadOnlyModifyAttempt(self, event):
        """
        Ring the bell to notify the user that the
        document is in Read-Only Mode
        """
        wx.Bell()

    def OnKeyDown(self, event):
        event.Skip()
        key = event.GetKeyCode()
        print(key)
        if key == ord('A') and event.ControlDown():
            self.OnSelectAll()
        elif key == ord('C') and event.ControlDown():
            self.OnCopy()

    def OnContextMenu(self, event):
        menu = wx.Menu()

        ## menu.Append(wx.ID_UNDO, 'Undo\tCtrl+Z')
        ## menu.Append(wx.ID_REDO, 'Redo\tCtrl+Y')
        ## menu.AppendSeparator()
        ## menu.Append(wx.ID_CUT, 'Cut\tCtrl+X')
        menu.Append(wx.ID_COPY, 'Copy\tCtrl+C')
        ## menu.Append(wx.ID_PASTE, 'Paste\tCtrl+V')
        menu.Append(wx.ID_SELECTALL, 'Select All\tCtrl+A')
        menu.AppendSeparator()
        ## menu.Append(wx.ID_DELETE, 'Delete\tDel')
        ## menu.AppendSeparator()

        ID_COPYMESSAGETOCLIPBOARD = wx.NewId()
        copymessageinfo = wx.MenuItem(menu, ID_COPYMESSAGETOCLIPBOARD, u'&%s' %(_(u'Copy Message Info to Clipboard')))
        if PHOENIX:
            menu.Append(copymessageinfo)
        else:
            menu.AppendItem(copymessageinfo)

        ## menu.Bind(wx.EVT_MENU, self.OnUndo, id=wx.ID_UNDO)
        ## menu.Bind(wx.EVT_MENU, self.OnRedo, id=wx.ID_REDO)
        ## menu.Bind(wx.EVT_MENU, self.OnCut, id=wx.ID_CUT)
        menu.Bind(wx.EVT_MENU, self.OnCopy, id=wx.ID_COPY)
        ## menu.Bind(wx.EVT_MENU, self.OnPaste, id=wx.ID_PASTE)
        menu.Bind(wx.EVT_MENU, self.OnSelectAll, id=wx.ID_SELECTALL)
        ## menu.Bind(wx.EVT_MENU, self.OnDeleteBack, id=wx.ID_DELETE)
        menu.Bind(wx.EVT_MENU, self.OnCopyMessageToClipboard, id=ID_COPYMESSAGETOCLIPBOARD)

        self.PopupMenu(menu)
        menu.Destroy()

    def OnUndo(self, event=None): self.Undo()
    def OnRedo(self, event=None): self.Redo()
    def OnCut(self, event=None): self.Cut()
    def OnCopy(self, event=None): self.Copy()
    def OnPaste(self, event=None): self.Paste()
    def OnSelectAll(self, event=None): self.SelectAll()
    def OnDeleteBack(self, event=None): self.DeleteBack()

    def OnCopyMessageToClipboard(self, event):
        ## if wx.TheClipboard.Open():
        ##     wx.TheClipboard.SetData(wx.TextDataObject(u'%s' %self.message))
        ##     wx.TheClipboard.Close()

        self.SelectAll()
        self.Copy()
        curSel = self.GetCurrentPos()
        self.SetSelection(curSel, curSel)#DeSelect

        
class ExceptionPanel(wx.Panel):
    def __init__(self, parent, excInfo=None, message=None, bmp=None,
                 messageFont=None):
        wx.Panel.__init__(self, parent)

        global gExcPanelParent
        gExcPanelParent = parent

        if excInfo:
            excType, excValue, excTrace = excInfo[0], excInfo[1], excInfo[2]
        else:
            excType, excValue, excTrace = sys.exc_info()

        if not bmp:
            # Use a custom bitmap/icon.
            ## sBitmap = wx.ArtProvider.GetBitmap(wx.ART_ERROR, wx.ART_MESSAGE_BOX)
            sBitmap = xception48.GetBitmap()
        else:
            sBitmap = bmp

        vbSizer = wx.BoxSizer(wx.VERTICAL)
        # Create the top row, containing the error icon and text message.
        hbSizer = wx.BoxSizer(wx.HORIZONTAL)

        if message:
            message_text = message
        else:
            message_text = (_(u"I'm afraid there has been an unhandled error.") +
                            '\n' +
                            _(u"Please send the contents of the text control below to the application's developer."))
        message_label = wx.StaticText(self, wx.ID_ANY, message_text)
        message_label.SetToolTip(wx.ToolTip(message_text))
        if messageFont:
            message_label.SetFont(messageFont)
        hbSizer.Add(wx.StaticBitmap(self, wx.ID_ANY, sBitmap),
                          flag=wx.ALL, border=10)
        hbSizer.Add(message_label, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT, 10)

        # Create the text control with the error information.
        text_ctrl = ExceptionSTC(self)

        formatException = traceback.format_exception(excType, excValue, excTrace)

        t = time.localtime(time.time())
        st = time.strftime(u'%b-%d-%Y %I:%M %p', t)
        text_ctrl.AppendText(u"%s '%s'\n\n"%(_(u'TimeOfTraceback:'), st))
        for value in formatException:
            text_ctrl.AppendText(u'%s'%value)
        text_ctrl.EmptyUndoBuffer()
        text_ctrl.SetReadOnly(True)
        text_ctrl.SetUseVerticalScrollBar(True)

        vbSizer.Add(hbSizer, 0, wx.EXPAND)
        vbSizer.Add(text_ctrl, proportion=1, flag=wx.EXPAND | wx.TOP, border=5)
        self.SetSizer(vbSizer)


# We'll use a SizedDialog instead of Dialog so there is
# a gripper on the frame and a sizer border around the contents
## class ExceptionHookDialog(wx.Dialog):
class ExceptionHookDialog(SC.SizedDialog):
    """
    This class displays an wxPython Exception error dialog with
    detailed information about the input exception, including a traceback.

    Usage:
    import sys
    import wx
    import traceback
    import ExceptionHookDialog as ExceptionHookDialog
    try:
        yourCodeHere...
    except Exception as exc:
        ExceptionHookDialog().ShowModal()
    """
    def __init__(self, parent=None, excInfo=None, title=_(u'Unhandled Error!'),
                 message=None, messageFont=None, id=wx.ID_ANY,
                 pos=wx.DefaultPosition, size=wx.DefaultSize,
                 style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER |
                       wx.MAXIMIZE_BOX | wx.STAY_ON_TOP | wx.CLIP_CHILDREN,
                 name='dialog'):
        SC.SizedDialog.__init__(self, parent, id, title, pos, size, style, name)
        ## wx.Dialog.__init__(self, parent, id, title, pos, size, style, name)

        global gExcDialogParent
        gExcDialogParent = parent

        if excInfo:
            excType, excValue, excTrace = excInfo[0], excInfo[1], excInfo[2]
        else:
            excType, excValue, excTrace = sys.exc_info()

        # Use a custom bitmap/icon.
        ## errorBmp = wx.ArtProvider.GetBitmap(wx.ART_ERROR, wx.ART_MESSAGE_BOX)
        errorBmp = xception48.GetBitmap()

        ## panel = wx.Panel(self, wx.ID_ANY)
        panel = self.GetContentsPane()
        panel.SetWindowStyle(wx.SUNKEN_BORDER)
        # panel.SetWindowStyle(wx.BORDER_STATIC)
        # panel.SetWindowStyle(wx.BORDER_THEME)
        # panel.SetWindowStyle(wx.BORDER_SIMPLE)


        # Create the Close button in the bottom row.
        close_button = wx.Button(panel, label=_(u'Close'))
        close_button.Bind(wx.EVT_BUTTON, self.OnClose)
        close_button.SetFocus()
        close_button.SetDefault()

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(ExceptionPanel(panel, excInfo=(excType, excValue, excTrace),
                                 message=message, bmp=errorBmp, messageFont=messageFont),
                                 1, wx.EXPAND | wx.ALL, 0)
        sizer.Add(close_button, flag=wx.ALIGN_CENTER | wx.ALL, border=10)

        panel.SetSizer(sizer)

        self.Bind(wx.EVT_CLOSE, self.OnClose)

        self.SetMinSize((525, 350))
        if PHOENIX:
            self.SetIcon(wx.Icon(errorBmp))
        else: # Classic
            self.SetIcon(wx.IconFromBitmap(errorBmp))
        self.Centre()
        wx.Bell()
        ## winsound.MessageBeep(winsound.MB_ICONHAND)

    def OnClose(self, event):
        ## print('OnClose')
        self.Destroy()


class ExceptionStrDialog(SC.SizedDialog):
    """
    This class displays an wxPython Exception error dialog with
    detailed information about the input exception, including a traceback.

    Usage:
    import sys
    import wx
    import traceback
    import ExceptionHookDialog as ExceptionHookDialog
    try:
        yourCodeHere...
    except Exception as exc:
        ExceptionHookDialog().ShowModal()
    """
    def __init__(self, parent=None, excStr=None, title=_(u'Unhandled Error!'),
                 message=None, messageFont=None, id=wx.ID_ANY,
                 pos=wx.DefaultPosition, size=wx.DefaultSize,
                 style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER |
                       wx.MAXIMIZE_BOX | wx.STAY_ON_TOP | wx.CLIP_CHILDREN,
                 name='dialog'):
        SC.SizedDialog.__init__(self, parent, id, title, pos, size, style, name)
        ## wx.Dialog.__init__(self, parent, id, title, pos, size, style, name)

        global gExcDialogParent
        gExcDialogParent = parent

        # Use a custom bitmap/icon.
        ## errorBmp = wx.ArtProvider.GetBitmap(wx.ART_ERROR, wx.ART_MESSAGE_BOX)
        errorBmp = xception48.GetBitmap()

        ## panel = wx.Panel(self, wx.ID_ANY)
        panel = self.GetContentsPane()
        panel.SetWindowStyle(wx.SUNKEN_BORDER)
        # panel.SetWindowStyle(wx.BORDER_STATIC)
        # panel.SetWindowStyle(wx.BORDER_THEME)
        # panel.SetWindowStyle(wx.BORDER_SIMPLE)


        if not excStr:
            raise Exception('Need a string for the ExceptionStrDialog')

        else:
            excStrSTC = ExceptionSTC(panel, wx.ID_ANY)
            excStrSTC.SetText('%s' % excStr)
        
        # Create the Close button in the bottom row.
        close_button = wx.Button(panel, label=_(u'Close'))
        close_button.Bind(wx.EVT_BUTTON, self.OnClose)
        close_button.SetFocus()
        close_button.SetDefault()

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(excStrSTC,
                                 1, wx.EXPAND | wx.ALL, 0)
        sizer.Add(close_button, flag=wx.ALIGN_CENTER | wx.ALL, border=10)

        panel.SetSizer(sizer)

        self.Bind(wx.EVT_CLOSE, self.OnClose)

        self.SetMinSize((525, 350))
        if PHOENIX:
            self.SetIcon(wx.Icon(errorBmp))
        else: # Classic
            self.SetIcon(wx.IconFromBitmap(errorBmp))
        self.Centre()
        wx.Bell()
        ## winsound.MessageBeep(winsound.MB_ICONHAND)

    def OnClose(self, event):
        ## print('OnClose')
        self.Destroy()
        
if __name__ == '__main__':

    #- Override sys.excepthook ----------------------------
    # Place this bit of code in your app if you want to
    # overide sys.excepthook.
    # Otherwise sys.excepthook defaults to sys.stderr
    def custom_excepthook(excType, excValue, excTrace):
        excInfo=(excType, excValue, excTrace)
        ExceptionHookDialog(excInfo=excInfo).ShowModal()

    # Our ExceptionHookDialog will be called every time there is an error.
    sys.excepthook = custom_excepthook
    #------------------------------------------------------

    app = wx.App(0)

    list = []
    dict = {}
    tuple = ()

    # causeAnUnhandledError

    ## ExceptionStrDialog(excStr='Traceback: testing\n\nHmm what went wrong...?').ShowModal()
    
    # Intentionally cause some handled errors for testing.
    # Uncomment out the code to test each ErrorType.
    try:
        ## import causeImportError
        ## causeNameError
        ## causeZeroDivisionError = 100/0
        ## causeOverflowError = range(0, int('9999999999999'*9999999999999))
        ## causeMemoryError = int('99999999'*99999999)
        ## causeTypeError = 'str' + int(5)
        ## causeIndexError = list[0]
        ## causeKeyError = dict['MissingKey']
        ## causeAttributeError = tuple.x
        ## causeSyntaxError = \
        ## causeIOError = open('missingFile.txt').read()
        ## causeAssertionError = None
        ## assert callable(causeAssertionError)
        ## raise Exception('Hmm. What went wrong...?')
        ## causeLookupError = u''.decode('causeLookupError')
        ## causeValueError = list.remove('causeValueError')
        ## causeUnicodeEncodeError = u'\u0411'.encode("iso-8859-15")
        causeUnicodeDecodeError = '\x81'.decode("utf-8")
    except Exception as exc:
        major, minor, micro, release = sys.version_info[0:-1]
        pythonVersion = u'%d.%d.%d-%s'%(major, minor, micro, release)
        ExceptionHookDialog(parent=None,
                            excInfo=sys.exc_info(),
                            title=_(u'Handled ErrorType Testing'),
                            message=_(u'I intentionally caused this error.\n'
                                      u'Python %s'%(pythonVersion))).ShowModal()


    app.MainLoop()

