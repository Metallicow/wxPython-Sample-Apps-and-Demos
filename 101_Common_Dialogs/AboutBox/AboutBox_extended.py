#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-Imports----------------------------------------------------------------------

#--wxPython Imports.
import wx
if not 'phoenix' in wx.version():  # Classic
    wx.adv = wx
else:
    import wx.adv

from wx.lib.wordwrap import wordwrap


#- wxPython Demo --------------------------------------------------------------

__wxPyOnlineDocs__ = 'http://wxpython.org/Phoenix/docs/html/adv.AboutDialogInfo.html'
__wxPyDemoPanel__ = 'TestPanel'

overview = """<html><body>
<h2><center>wx.AboutBox</center></h2>

This function shows the native standard about dialog containing the
information specified in info. If the current platform has a native
about dialog which is capable of showing all the fields in info, the
native dialog is used, otherwise the function falls back to the
generic wxWidgets version of the dialog.

</body></html>
"""


class TestPanel(wx.Panel):
    def __init__(self, parent, log):
        self.log = log
        wx.Panel.__init__(self, parent, -1)

        b = wx.Button(self, -1, "Show a wx.AboutBox", (50, 50))
        self.Bind(wx.EVT_BUTTON, self.OnButton, b)


    def OnButton(self, event):
        # First we create and fill the info object.
        info = wx.adv.AboutDialogInfo()
        info.Name = "Hello World"
        info.Version = "1.2.3"
        info.Copyright = "(C) 2006 Programmers and Coders Everywhere"
        info.Description = wordwrap(
            "A \"hello world\" program is a software program that prints out "
            "\"Hello world!\" on a display device. It is used in many introductory "
            "tutorials for teaching a programming language."

            "\n\nSuch a program is typically one of the simplest programs possible "
            "in a computer language. A \"hello world\" program can be a useful "
            "sanity test to make sure that a language's compiler, development "
            "environment, and run-time environment are correctly installed.",
            350, wx.ClientDC(self))
        info.WebSite = ("http://en.wikipedia.org/wiki/Hello_world", "Hello World home page")
        info.Developers = ("Joe Programmer",
                           "Jane Coder",
                           "Vippy the Mascot")

        licenseText = "blah " * 250 + "\n\n" + "yadda " * 100
        info.License = wordwrap(licenseText, 500, wx.ClientDC(self))

        # Then we call wx.AboutBox giving it that info object
        wx.adv.AboutBox(info)


#- run.py ---------------------------------------------------------------------


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
