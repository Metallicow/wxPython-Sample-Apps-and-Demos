#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-Imports----------------------------------------------------------------------

#--wxPython Imports.
import wx


#- wxPython Demo --------------------------------------------------------------
__wxPyOnlineDocs__ = 'https://wxpython.org/Phoenix/docs/html/wx.RadioBox.html'
__wxPyDemoPanel__ = 'TestPanel'

overview = """\
<html><body>
<center><h2>wx.RadioBox</h2></center>
<p>
A RadioBox is used to select one of a number of mutually exclusive
choices.  It is displayed as a vertical column or horizontal row of
labelled buttons, surrounded by a box that can optionally have a
label.
</body></html>
"""


class TestPanel(wx.Panel):
    def __init__(self, parent, log):
        self.log = log
        wx.Panel.__init__(self, parent, -1)
        #self.SetBackgroundColour(wx.BLUE)

        sampleList = ['zero', 'one', 'two', 'three', 'four', 'five',
                      'six', 'seven', 'eight']

        sizer = wx.BoxSizer(wx.VERTICAL)

        rb = wx.RadioBox(
                self, -1, "wx.RadioBox", wx.DefaultPosition, wx.DefaultSize,
                sampleList, 2, wx.RA_SPECIFY_COLS
                )

        self.Bind(wx.EVT_RADIOBOX, self.EvtRadioBox, rb)
        #rb.SetBackgroundColour(wx.BLUE)
        rb.SetToolTip(wx.ToolTip("This is a ToolTip!"))
        #rb.SetLabel("wx.RadioBox")

        sizer.Add(rb, 0, wx.ALL, 20)

        rb = wx.RadioBox(
                self, -1, "", wx.DefaultPosition, wx.DefaultSize,
                sampleList, 3, wx.RA_SPECIFY_COLS | wx.NO_BORDER
                )

        self.Bind(wx.EVT_RADIOBOX, self.EvtRadioBox, rb)
        rb.SetToolTip(wx.ToolTip("This box has no label"))

        sizer.Add(rb, 0, wx.LEFT|wx.RIGHT|wx.BOTTOM, 20)

        self.SetSizer(sizer)


    def EvtRadioBox(self, event):
        self.log.WriteText('EvtRadioBox: %d\n' % event.GetInt())


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
