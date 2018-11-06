#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-Imports----------------------------------------------------------------------

#--Python Imports.
import os
import sys

#--wxPython Imports.
import wx

#-Globals----------------------------------------------------------------------
try:
    gFileDir = os.path.dirname(os.path.abspath(__file__))
except Exception:
    gFileDir = os.path.dirname(os.path.abspath(sys.argv[0]))
gBmpDir = gFileDir + os.sep + 'bitmaps'

#- wxPython Demo --------------------------------------------------------------
__wxPyOnlineDocs__ = 'https://wxpython.org/Phoenix/docs/html/wx.ToggleButton.html'
__wxPyDemoPanel__ = 'TestPanel'

overview = """\
wx.ToggleButton is a button that stays pressed when clicked by the user.
In other words, it is similar to wxCheckBox in functionality but looks like a
wxButton.
"""


class TestPanel(wx.Panel):
    def __init__(self, parent, log):
        wx.Panel.__init__(self, parent, -1)
        self.log = log
        panel = wx.Panel(self, -1)
        buttons = wx.BoxSizer(wx.HORIZONTAL)

        for word in "These are toggle buttons".split():
            b = wx.ToggleButton(panel, -1, word)
            self.Bind(wx.EVT_TOGGLEBUTTON, self.OnToggle, b)
            buttons.Add(b, flag=wx.ALL, border=5)

        panel.SetAutoLayout(True)
        panel.SetSizer(buttons)
        buttons.Fit(panel)
        panel.Move((50,50))

        b = wx.ToggleButton(self, -1, "can have bitmaps too", pos=(50,125))
        b.SetBitmap(wx.Bitmap(gBmpDir + os.sep + 'mondrian.ico', wx.BITMAP_TYPE_ICO))
        b.SetInitialSize() # adjust default size for the bitmap
        self.Bind(wx.EVT_TOGGLEBUTTON, self.OnToggle, b)

    def OnToggle(self, event):
        self.log.WriteText("Button %d toggled\n" % event.GetId())


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
