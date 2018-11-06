#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 11/17/2003 - Jeff Grimmett (grimmtooth@softhome.net)
#
# o Updated for wx namespace
#
# 11/28/2003 - Jeff Grimmett (grimmtooth@softhome.net)
#
# o Changed the event binding slightly.

#-Imports----------------------------------------------------------------------

#--wxPython Imports.
import wx


#- wxPython Demo --------------------------------------------------------------

__wxPyOnlineDocs__ = 'https://wxpython.org/Phoenix/docs/html/wx.FindReplaceDialog.html'
__wxPyDemoPanel__ = 'TestPanel'

overview = """\
FindReplaceDialog is a standard modeless dialog which is used to allow the user
to search for some text (and possibly replace it with something else). The actual
searching is supposed to be done in the owner window which is the parent of this
dialog. Note that it means that unlike for the other standard dialogs this one
<u>must have a parent window</u>. Also note that there is no way to use this
dialog in a modal way; <b>it is always, by design and implementation, modeless</b>.

FileReplaceDialog requires the use of <b>FindReplaceData</b>. This holds the
data for the dialog. It is used to initialize the dialog with the default values
and will keep the last values from the dialog when it is closed. It is also
updated each time a FindDialogEvent is generated so instead of using the
FindDialogEvent methods you can also directly query this object. <b>Care must be
taken not to use this object after the dialog is destroyed.</b> The data within
will be invalid after the parent dialog is destroyed.
"""


class TestPanel(wx.Panel):
    def __init__(self, parent, log):
        wx.Panel.__init__(self, parent, -1)
        self.log = log
        self.findData = wx.FindReplaceData()

        self.fbtn = wx.Button(self, -1, "Show Find Dialog", (25, 50))
        self.Bind(wx.EVT_BUTTON, self.OnShowFind, self.fbtn)

        self.frbtn = wx.Button(self, -1, "Show Find && Replace Dialog", (25, 90))
        self.Bind(wx.EVT_BUTTON, self.OnShowFindReplace, self.frbtn)

    def BindFindEvents(self, win):
        win.Bind(wx.EVT_FIND, self.OnFind)
        win.Bind(wx.EVT_FIND_NEXT, self.OnFind)
        win.Bind(wx.EVT_FIND_REPLACE, self.OnFind)
        win.Bind(wx.EVT_FIND_REPLACE_ALL, self.OnFind)
        win.Bind(wx.EVT_FIND_CLOSE, self.OnFindClose)

    def EnableButtons(self):
        self.fbtn.Enable()
        self.frbtn.Enable()

    def DisableButtons(self):
        self.fbtn.Disable()
        self.frbtn.Disable()

    def OnShowFind(self, evt):
        self.DisableButtons()
        dlg = wx.FindReplaceDialog(self, self.findData, "Find")
        self.BindFindEvents(dlg)
        dlg.Show(True)


    def OnShowFindReplace(self, evt):
        self.DisableButtons()
        dlg = wx.FindReplaceDialog(self, self.findData, "Find & Replace", wx.FR_REPLACEDIALOG)
        self.BindFindEvents(dlg)
        dlg.Show(True)


    def OnFind(self, evt):
        #print(repr(evt.GetFindString()), repr(self.findData.GetFindString()))
        map = {
            wx.wxEVT_COMMAND_FIND : "FIND",
            wx.wxEVT_COMMAND_FIND_NEXT : "FIND_NEXT",
            wx.wxEVT_COMMAND_FIND_REPLACE : "REPLACE",
            wx.wxEVT_COMMAND_FIND_REPLACE_ALL : "REPLACE_ALL",
            }

        et = evt.GetEventType()

        if et in map:
            evtType = map[et]
        else:
            evtType = "**Unknown Event Type**"

        if et in [wx.wxEVT_COMMAND_FIND_REPLACE, wx.wxEVT_COMMAND_FIND_REPLACE_ALL]:
            replaceTxt = "Replace text: %s" % evt.GetReplaceString()
        else:
            replaceTxt = ""

        self.log.WriteText("%s -- Find text: %s   Replace text: %s  Flags: %d  \n" %
                (evtType, evt.GetFindString(), replaceTxt, evt.GetFlags()))


    def OnFindClose(self, evt):
        self.log.WriteText("FindReplaceDialog closing...\n")
        evt.GetDialog().Destroy()
        self.EnableButtons()


#- wxPy Demo -----------------------------------------------------------------


def runTest(frame, nb, log):
    win = TestPanel(nb, log)
    return win


#- __main__ Demo --------------------------------------------------------------


class printLog:
    def __init__(self):
        pass

    def write(self, txt):
        print('%s' % txt)

    def WriteText(self, txt):
        print('%s' % txt)


class TestFrame(wx.Frame):
    def __init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString,
                 pos=wx.DefaultPosition, size=wx.DefaultSize,
                 style=wx.DEFAULT_FRAME_STYLE, name='frame'):
        wx.Frame.__init__(self, parent, id, title, pos, size, style, name)

        log = printLog()

        panel = TestPanel(self, log)
        self.Bind(wx.EVT_CLOSE, self.OnDestroy)


    def OnDestroy(self, event):
        self.Destroy()


class TestApp(wx.App):
    def OnInit(self):
        gMainWin = TestFrame(None)
        gMainWin.SetTitle('Test Demo')
        gMainWin.Show()

        return True


#- __main__ -------------------------------------------------------------------


if __name__ == '__main__':
    import sys
    print('Python %s.%s.%s %s' % sys.version_info[0:4])
    print('wxPython %s' % wx.version())
    gApp = TestApp(redirect=False,
            filename=None,
            useBestVisual=False,
            clearSigInt=True)

    gApp.MainLoop()
