#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-Imports----------------------------------------------------------------------

#--Python Imports.
import os
import sys

#--wxPython Imports.
import wx

USE_GENERIC = 0

if USE_GENERIC:
    from wx.lib.stattext import GenStaticText as StaticText
    from wx.lib.statbmp  import GenStaticBitmap as StaticBitmap
else:
    StaticText = wx.StaticText
    StaticBitmap = wx.StaticBitmap

#--Local Imports.
## import images

#-Globals----------------------------------------------------------------------
try:
    gFileDir = os.path.dirname(os.path.abspath(__file__))
except Exception:
    gFileDir = os.path.dirname(os.path.abspath(sys.argv[0]))
gBmpDir = gFileDir + os.sep + 'bitmaps'

#- wxPython Demo --------------------------------------------------------------
__wxPyOnlineDocs__ = 'http://wxpython.org/Phoenix/docs/html/StaticBitmap.html'
__wxPyDemoPanel__ = 'TestPanel'

overview = """\
A StaticBitmap control displays a bitmap.

A bitmap can be derived from most image formats using the wx.Image class.

"""


class TestPanel(wx.Panel):
    def __init__(self, parent, log):
        wx.Panel.__init__(self, parent, -1)
        self.log = log
        ##self.SetBackgroundColour("sky blue")

        StaticText(self, -1, "This is a wx.StaticBitmap.", (45, 15))

        ## bmp = images.Test2.GetBitmap()
        bmp = wx.Bitmap(gBmpDir + os.sep + 'test2.bmp', wx.BITMAP_TYPE_BMP)
        mask = wx.Mask(bmp, wx.BLUE)
        bmp.SetMask(mask)
        StaticBitmap(self, -1, bmp, (80, 50), (bmp.GetWidth(), bmp.GetHeight()))

        ## bmp = images.Robin.GetBitmap()
        bmp = wx.Bitmap(gBmpDir + os.sep + 'robin.jpg', wx.BITMAP_TYPE_JPEG)
        StaticBitmap(self, -1, bmp, (80, 150))

        StaticText(self, -1, "Hey, if Ousterhout can do it, so can I.", (200, 175))


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
