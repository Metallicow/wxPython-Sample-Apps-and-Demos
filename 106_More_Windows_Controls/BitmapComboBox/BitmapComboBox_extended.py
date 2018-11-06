#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-Imports----------------------------------------------------------------------

#--Python Imports.
import os
import sys

#--wxPython Imports.
import wx
import wx.adv

#-Globals----------------------------------------------------------------------
try:
    gFileDir = os.path.dirname(os.path.abspath(__file__))
except Exception:
    gFileDir = os.path.dirname(os.path.abspath(sys.argv[0]))
gBmpDir = gFileDir + os.sep + 'bitmaps'

#- wxPython Demo --------------------------------------------------------------

__wxPyOnlineDocs__ = 'https://wxpython.org/Phoenix/docs/html/wx.adv.BitmapComboBox.html'
__wxPyDemoPanel__ = 'TestPanel'

overview = """<html><body>
<h2><center>wx.combo.BitmapComboBox</center></h2>

A combobox that displays a bitmap in front of the list items. It
currently only allows using bitmaps of one size, and resizes itself so
that a bitmap can be shown next to the text field.

</body></html>
"""

class TestPanel(wx.Panel):
    def __init__(self, parent, log):
        self.log = log
        wx.Panel.__init__(self, parent, -1)

        bcb1 = wx.adv.BitmapComboBox(self, pos=(25, 25), size=(200, -1))
        bcb2 = wx.adv.BitmapComboBox(self, pos=(250, 25), size=(200, -1))

        for bcb in [bcb1, bcb2]:
            for x in range(12):
                name = 'LB%02d.png' % (x+1)
                img = wx.Image(gBmpDir + os.sep + name)
                img.Rescale(20, 20)
                bmp = img.ConvertToBitmap()
                bcb.Append('%s' % name, bmp, name)
            self.Bind(wx.EVT_COMBOBOX, self.OnCombo, bcb)


    def OnCombo(self, event):
        bcb = event.GetEventObject()
        idx = event.GetInt()
        st = bcb.GetString(idx)
        cd = bcb.GetClientData(idx)
        self.log.WriteText("EVT_COMBOBOX: Id %d, string '%s', clientData '%s'" % (idx, st, cd))


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
