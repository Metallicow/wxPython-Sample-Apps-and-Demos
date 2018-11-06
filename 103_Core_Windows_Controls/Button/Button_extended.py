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
except:
    gFileDir = os.path.dirname(os.path.abspath(sys.argv[0]))
gBmpDir = gFileDir + os.sep + 'bitmaps'


#- wxPython Demo --------------------------------------------------------------

__wxPyOnlineDocs__ = 'https://wxpython.org/Phoenix/docs/html/wx.Button.html'
__wxPyDemoPanel__ = 'TestPanel'

overview = """<html><body>
<h2><center>Button</center></h2>

Button Demo that shows all the methods of the wx.Button class.

</body></html>
"""


class TestPanel(wx.Panel):
    def __init__(self, parent, log):
        self.log = log
        wx.Panel.__init__(self, parent, -1)

        bmp = wx.Bitmap(gBmpDir + os.sep + 'snakey16.png', wx.BITMAP_TYPE_PNG)
        b1 = wx.Button(self, -1, "Button")
        b1.SetToolTip(wx.ToolTip(wx.Button.SetDefault.__doc__))
        b1.SetDefault()

        b2 = wx.Button(self, -1, "wx.BU_ALIGN_MASK", style=wx.BU_ALIGN_MASK)
        b2.SetBitmap(bmp)

        b3 = wx.Button(self, -1, "wx.BU_AUTODRAW", style=wx.BU_AUTODRAW)
        b3.SetBitmap(bmp)

        b4 = wx.Button(self, -1, "wx.BU_BOTTOM", style=wx.BU_BOTTOM)
        b4.SetBitmap(bmp)

        b5 = wx.Button(self, -1, "wx.BU_EXACTFIT", style=wx.BU_EXACTFIT)
        b5.SetBitmap(bmp)

        b6 = wx.Button(self, -1, "wx.BU_LEFT", style=wx.BU_LEFT)
        b6.SetBitmap(bmp)

        b7 = wx.Button(self, -1, "wx.BU_NOTEXT", style=wx.BU_NOTEXT)
        b7.SetBitmap(bmp)

        b8 = wx.Button(self, -1, "wx.BU_RIGHT", style=wx.BU_RIGHT)
        b8.SetBitmap(bmp)

        b9 = wx.Button(self, -1, "wx.BU_TOP", style=wx.BU_TOP)
        b9.SetBitmap(bmp)

        b10 = wx.Button(self, -1, "wx.BORDER_NONE", style=wx.BORDER_NONE)
        b10.SetBitmap(bmp)

        b11 = wx.Button(self, -1, "wx.BORDER_SIMPLE", style=wx.BORDER_SIMPLE)
        b11.SetBitmap(bmp)

        b12 = wx.Button(self, -1, "Multiline\nText")
        b12.SetBitmap(bmp)

        b13 = wx.Button(self, -1, "SetBitmapPosition\nwx.NORTH")
        b13.SetToolTip(wx.ToolTip(wx.Button.SetBitmapPosition.__doc__))
        b13.SetBitmap(bmp)
        b13.SetBitmapPosition(wx.NORTH)

        b14 = wx.Button(self, -1, "SetBitmapPosition\nwx.SOUTH")
        b14.SetToolTip(wx.ToolTip(wx.Button.SetBitmapPosition.__doc__))
        b14.SetBitmap(bmp)
        b14.SetBitmapPosition(wx.SOUTH)

        b15 = wx.Button(self, -1, "SetBitmapPosition\nwx.EAST")
        b15.SetToolTip(wx.ToolTip(wx.Button.SetBitmapPosition.__doc__))
        b15.SetBitmap(bmp)
        b15.SetBitmapPosition(wx.EAST)

        b16 = wx.Button(self, -1, "SetBitmapMargins\n(w, h)")
        b16.SetToolTip(wx.ToolTip(wx.Button.SetBitmapMargins.__doc__))
        b16.SetBitmap(bmp)
        w, h = 30, 10
        b16.SetBitmapMargins((w, h))

        b17 = wx.Button(self, -1, "SetBitmap")
        b17.SetToolTip(wx.ToolTip(wx.Button.SetBitmap.__doc__))
        b17.SetBitmap(bmp)

        b18 = wx.Button(self, -1, "SetBitmapLabel")
        b18.SetToolTip(wx.ToolTip(wx.Button.SetBitmapLabel.__doc__))
        b18.SetBitmapLabel(bmp)

        b19 = wx.Button(self, -1, "SetBitmapCurrent")
        b19.SetToolTip(wx.ToolTip(wx.Button.SetBitmapCurrent.__doc__))
        b19.SetBitmap(bmp)
        b19.SetBitmapCurrent(wx.Bitmap(gBmpDir + os.sep + 'snakey12_16.png', wx.BITMAP_TYPE_PNG))

        b20 = wx.Button(self, -1, "SetBitmapDisabled")
        b20.SetToolTip(wx.ToolTip(wx.Button.SetBitmapDisabled.__doc__))
        b20.SetBitmap(bmp)
        b20.SetBitmapDisabled(wx.Bitmap(gBmpDir + os.sep + 'pencil16.png', wx.BITMAP_TYPE_PNG))
        b20.Enable(False)

        b21 = wx.Button(self, -1, "SetBitmapFocus")
        b21.SetToolTip(wx.ToolTip(wx.Button.SetBitmapFocus.__doc__))
        b21.SetBitmap(bmp)
        b21.SetBitmapFocus(wx.Bitmap(gBmpDir + os.sep + 'undo16.png', wx.BITMAP_TYPE_PNG))

        b22 = wx.Button(self, -1, "SetBitmapPressed")
        b22.SetToolTip(wx.ToolTip(wx.Button.SetBitmapPressed.__doc__))
        b22.SetBitmap(bmp)
        b22.SetBitmapPressed(wx.Bitmap(gBmpDir + os.sep + 'phoenix16.png', wx.BITMAP_TYPE_PNG))

        b23 = wx.Button(self, -1, "SetAuthNeeded")
        b23.SetToolTip(wx.ToolTip(wx.Button.SetAuthNeeded.__doc__ + "\n\n" +
                       "Note: This method doesn't do anything if the platform is not Windows Vista or newer."))
        b23.SetAuthNeeded(True)

        b24 = wx.Button(self, -1, "")
        b24.SetToolTip(wx.ToolTip(wx.Button.SetLabel.__doc__))
        b24.SetLabel('SetLabel')


        gSizer = wx.FlexGridSizer(rows=6, cols=4, hgap=4, vgap=4)

        for btn in self.GetChildren():
            gSizer.Add(btn, 1, wx.ALL)
            btn.Bind(wx.EVT_BUTTON, self.OnButton)

        self.SetSizer(gSizer)

    def OnButton(self, event):
        self.log.WriteText('Clicked Button\n')


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
