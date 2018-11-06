#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-Imports----------------------------------------------------------------------

#--wxPython Imports.
import wx


#- wxPython Demo --------------------------------------------------------------
__wxPyOnlineDocs__ = 'https://wxpython.org/Phoenix/docs/html/wx.Gauge.html'
__wxPyDemoPanel__ = 'TestPanel'

overview = """\
A Gauge is a horizontal or vertical bar which shows a quantity in a graphical
fashion. It is often used to indicate progress through lengthy tasks, such as
file copying or data analysis.

When the Gauge is initialized, it's "complete" value is usually set; at any rate,
before using the Gauge, the maximum value of the control must be set. As the task
progresses, the Gauge is updated by the program via the <code>SetValue</code> method.

This control is for use within a GUI; there is a seperate ProgressDialog class
to present the same sort of control as a dialog to the user.
"""


class TestPanel(wx.Panel):
    def __init__(self, parent, log):
        wx.Panel.__init__(self, parent, -1)
        self.log = log
        self.count = 0

        wx.StaticText(self, -1, "This example shows the wx.Gauge control.", (45, 15))

        self.g1 = wx.Gauge(self, -1, 50, (110, 50), (250, 25))
        self.g2 = wx.Gauge(self, -1, 75, (110, 95), (250, 25))
        self.g3 = wx.Gauge(self, -1, 100, (110, 135), (25, 100), wx.GA_VERTICAL)
        # self.g3.SetBezelFace(12)
        # self.g3.SetShadowWidth(8)

        self.Bind(wx.EVT_TIMER, self.TimerHandler)
        self.timer = wx.Timer(self)
        self.timer.Start(100)

    def __del__(self):
        self.timer.Stop()

    def TimerHandler(self, event):
        self.count = self.count + 1

        if self.count >= 50:
            self.count = 0

        self.g1.SetValue(self.count)
        self.g2.Pulse()
        self.g3.Pulse()


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
