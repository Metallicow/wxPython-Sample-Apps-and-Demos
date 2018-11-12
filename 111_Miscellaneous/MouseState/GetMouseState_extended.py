#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-Imports----------------------------------------------------------------------

#--wxPython Imports.
import wx


#- wxPython Demo --------------------------------------------------------------

__wxPyOnlineDocs__ = 'https://wxpython.org/Phoenix/docs/html/wx.MouseState.html'
__wxPyDemoPanel__ = 'TestPanel'

overview = """<html><body>
<h2><center>wx.GetMouseState</center></h2>

The mouse and modifier state can be polled with the wx.GetMouseState
function.  It returns an instance of a wx.MouseState object that
contains the current position of the mouse pointer in screen
coordinates, as well as boolean values indicating the up/down status
of the mouse buttons and the modifier keys.

</body></html>
"""


class StaticText(wx.StaticText):
    """
    A StaticText that only updates the label if it has changed, to
    help reduce potential flicker since these controls would be
    updated very frequently otherwise.
    """
    def SetLabel(self, label):
        if label != self.GetLabel():
            wx.StaticText.SetLabel(self, label)


class TestPanel(wx.Panel):
    def __init__(self, parent, log):
        self.log = log
        wx.Panel.__init__(self, parent, -1)

        sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(sizer)
        sizer.Add((25, 25))
        sizer.Add(wx.StaticText(
                      self, -1,
                      "Mouse and modifier state can be polled with wx.GetMouseState"),
                  0, wx.CENTER|wx.ALL, 10)
        sizer.Add(wx.StaticLine(self), 0, wx.EXPAND | wx.TOP, 10)

        row = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(row, 0, wx.CENTER)

        fgs = wx.FlexGridSizer(cols=2, hgap=5, vgap=10)
        row.Add(fgs, 0, wx.ALL, 30)

        lbl = StaticText(self, -1, "X pos:")
        self.x = StaticText(self, -1, "00000")
        fgs.Add(lbl)
        fgs.Add(self.x)

        lbl = StaticText(self, -1, "Y pos:")
        self.y = StaticText(self, -1, "00000")
        fgs.Add(lbl)
        fgs.Add(self.y)

        lbl = StaticText(self, -1, "Left down:")
        self.lft = StaticText(self, -1, "False")
        fgs.Add(lbl)
        fgs.Add(self.lft)

        lbl = StaticText(self, -1, "Middle down:")
        self.mid = StaticText(self, -1, "False")
        fgs.Add(lbl)
        fgs.Add(self.mid)

        lbl = StaticText(self, -1, "Right down:")
        self.rgt = StaticText(self, -1, "False")
        fgs.Add(lbl)
        fgs.Add(self.rgt)

        lbl = StaticText(self, -1, "AUX1 down:")
        self.aux1 = StaticText(self, -1, "False")
        fgs.Add(lbl)
        fgs.Add(self.aux1)

        lbl = StaticText(self, -1, "AUX2 down:")
        self.aux2 = StaticText(self, -1, "False")
        fgs.Add(lbl)
        fgs.Add(self.aux2)

        fgs = wx.FlexGridSizer(cols=2, hgap=5, vgap=10)
        row.Add(fgs, 0, wx.ALL, 30)

        lbl = StaticText(self, -1, "Control down:")
        self.ctrl = StaticText(self, -1, "False")
        fgs.Add(lbl)
        fgs.Add(self.ctrl)

        lbl = StaticText(self, -1, "Shift down:")
        self.shft = StaticText(self, -1, "False")
        fgs.Add(lbl)
        fgs.Add(self.shft)

        lbl = StaticText(self, -1, "Alt down:")
        self.alt = StaticText(self, -1, "False")
        fgs.Add(lbl)
        fgs.Add(self.alt)

        lbl = StaticText(self, -1, "Meta down:")
        self.meta = StaticText(self, -1, "False")
        fgs.Add(lbl)
        fgs.Add(self.meta)

        lbl = StaticText(self, -1, "Cmd down:")
        self.cmd = StaticText(self, -1, "False")
        fgs.Add(lbl)
        fgs.Add(self.cmd)

        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.OnTimer, self.timer)
        self.timer.Start(100)


    def OnTimer(self, evt):
        ms = wx.GetMouseState()
        self.x.SetLabel(str(ms.x))
        self.y.SetLabel(str(ms.y))

        self.lft.SetLabel(str(ms.leftIsDown))
        self.mid.SetLabel(str(ms.middleIsDown))
        self.rgt.SetLabel(str(ms.rightIsDown))
        self.aux1.SetLabel(str(ms.aux1IsDown))
        self.aux2.SetLabel(str(ms.aux2IsDown))

        self.ctrl.SetLabel(str(ms.controlDown))
        self.shft.SetLabel(str(ms.shiftDown))
        self.alt.SetLabel(str(ms.altDown))
        self.meta.SetLabel(str(ms.metaDown))
        self.cmd.SetLabel(str(ms.cmdDown))

    def ShutdownDemo(self):
        self.timer.Stop()
        del self.timer


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
        gMainWin = TestFrame(None, size=(450, 350))
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
