#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 11/30/2003 - Jeff Grimmett (grimmtooth@softhome.net)
#
# o EVT_SPIN events (or something about them) freezes up the app.


#-Imports----------------------------------------------------------------------

#--wxPython Imports.
import wx


#- wxPython Demo --------------------------------------------------------------
__wxPyOnlineDocs__ = 'https://wxpython.org/Phoenix/docs/html/wx.SpinButton.html'
__wxPyDemoPanel__ = 'TestPanel'

overview = """<html><body>
<h2><center>SpinButton</center></h2>

A wx.SpinButton has two small up and down (or left and right) arrow buttons.
It is often used next to a text control for increment and decrementing a value.
Portable programs should try to use wx.SpinCtrl instead as wx.SpinButton is not
implemented for all platforms (Win32 and GTK only currently).

NB: the range supported by this control (and wx.SpinCtrl) depends on the platform
but is at least -0x8000 to 0x7fff. Under GTK and Win32 with sufficiently new version
of comctrl32.dll (at least 4.71 is required, 5.80 is recommended) the full 32 bit
range is supported.
</body></html>
"""


#----------------------------------------------------------------------

class TestPanel(wx.Panel):
    def __init__(self, parent, log):
        wx.Panel.__init__(self, parent, -1)
        self.log = log
        self.count = 0

        wx.StaticText(self, -1, "This example uses the wx.SpinButton control.", (45, 15))

        self.text = wx.TextCtrl(self, -1, "1", (30, 50), (60, -1))
        h = self.text.GetSize().height
        w = self.text.GetSize().width + self.text.GetPosition().x + 2

        self.spin = wx.SpinButton(self, -1,
                                  (w, 50),
                                  (h*2/3, h),
                                  wx.SP_VERTICAL)
        self.spin.SetRange(1, 100)
        self.spin.SetValue(1)

        self.Bind(wx.EVT_SPIN, self.OnSpin, self.spin)


    def OnSpin(self, event):
        self.text.SetValue(str(event.GetPosition()))


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
