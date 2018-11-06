#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-Imports----------------------------------------------------------------------

#--wxPython Imports.
import  wx

#- wxPython Demo --------------------------------------------------------------
__wxPyOnlineDocs__ = 'https://wxpython.org/Phoenix/docs/html/wx.SpinCtrl.html'
__wxPyDemoPanel__ = 'TestPanel'

overview = """\
wx.SpinCtrl combines wx.TextCtrl and wx.SpinButton in one control.

Portable programs should try to use this control as wx.SpinButton is not
implemented for all platforms (Win32 and GTK only currently).

NB: the range supported by this control depends on the platform
but is at least -0x8000 to 0x7fff. Under GTK and Win32 with sufficiently new version
of comctrl32.dll (at least 4.71 is required, 5.80 is recommended) the full 32 bit
range is supported.


"""

#----------------------------------------------------------------------

class TestPanel(wx.Panel):
    def __init__(self, parent, log):
        wx.Panel.__init__(self, parent, -1)
        self.log = log

        wx.StaticText(self, -1, "This example uses the wx.SpinCtrl control.", (45, 15))
        sc = wx.SpinCtrl(self, -1, "", (30, 50))
        sc.SetRange(1, 100)
        sc.SetValue(5)
        self.sc = sc

        self.Bind(wx.EVT_SPINCTRL, self.OnSpin, sc)
        self.Bind(wx.EVT_TEXT, self.OnText, sc)


    def OnSpin(self, evt):
        self.log.WriteText('OnSpin: %d\n' % self.sc.GetValue())

    def OnText(self, evt):
        self.log.WriteText('OnText: %d\n' % self.sc.GetValue())


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

