#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-Imports----------------------------------------------------------------------

#--Python Imports.
import os.path

#--wxPython Imports.
import wx
import wx.lib.dialogs


#- wxPython Demo --------------------------------------------------------------
__wxPyOnlineDocs__ = 'http://wxpython.org/Phoenix/docs/html/lib.dialogs.ScrolledMessageDialog.html'
__wxPyDemoPanel__ = 'TestPanel'

overview = """\

<code><b>ScrolledMessageDialog</b>(parent, msg, caption, pos=wx.DefaultPosition, size=(500,300))</code>

This class represents a message dialog that uses a wxTextCtrl to display the
message. This allows more flexible information display without having to be
as much concerned with layout requirements. A text file can simply be used

This dialog offers no special attributes or methods beyond those supported
by wxDialog.

"""


class TestPanel(wx.Panel):
    def __init__(self, parent, log):
        self.log = log
        wx.Panel.__init__(self, parent, -1)

        b = wx.Button(self, -1, "Create and Show a ScrolledMessageDialog", (50, 50))
        self.Bind(wx.EVT_BUTTON, self.OnButton, b)


    def OnButton(self, event):

        if os.path.exists(os.path.splitext(wx.lib.dialogs.__file__)[0] + '.py'):
            fPath = os.path.splitext(wx.lib.dialogs.__file__)[0] + '.py'
            ## print(fPath)
            f = open(fPath, "r")
            msg = f.read()
            f.close()
        else:
            msg = "I'm a ScrolledMessageDialog.\n\n" * 10

        dlg = wx.lib.dialogs.ScrolledMessageDialog(self, msg, "ScrolledMessageDialog Demo")
        dlg.ShowModal()


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
