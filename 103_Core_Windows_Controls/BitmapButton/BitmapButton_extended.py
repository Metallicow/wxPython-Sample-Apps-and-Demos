#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-Imports----------------------------------------------------------------------

#--Python Imports.
import os
import sys

#--wxPython Imports.
import wx

#--Local Imports.
## import images

#import wx.lib.buttons
#wx.BitmapButton = wx.lib.buttons.GenBitmapButton

#-Globals----------------------------------------------------------------------
try:
    gFileDir = os.path.dirname(os.path.abspath(__file__))
except Exception:
    gFileDir = os.path.dirname(os.path.abspath(sys.argv[0]))
gBmpDir = gFileDir + os.sep + 'bitmaps'


#- wxPython Demo --------------------------------------------------------------

__wxPyOnlineDocs__ = 'https://wxpython.org/Phoenix/docs/html/wx.BitmapButton.html'
__wxPyDemoPanel__ = 'TestPanel'

overview = """<html><body>
<h2>BitmapButton</h2>

<p>A BitmapButton control displays a bitmap. It can have a separate bitmap for each button state: normal, selected, disabled.</p>

<p>The bitmaps to be displayed should have a small number of colours, such as 16,
to avoid palette problems.</p>

<p>A bitmap can be derived from most image formats using the wx.Image class.</p>

</body></html>
"""


class TestPanel(wx.Panel):
    def __init__(self, parent, log):
        wx.Panel.__init__(self, parent, -1, style=wx.NO_FULL_REPAINT_ON_RESIZE)
        self.log = log

        if 0:  # a test case for catching wx.PyAssertionError

            #wx.GetApp().SetAssertMode(wx.PYAPP_ASSERT_SUPPRESS)
            #wx.GetApp().SetAssertMode(wx.PYAPP_ASSERT_EXCEPTION)
            #wx.GetApp().SetAssertMode(wx.PYAPP_ASSERT_DIALOG)
            #wx.GetApp().SetAssertMode(wx.PYAPP_ASSERT_EXCEPTION | wx.PYAPP_ASSERT_DIALOG)

            try:
                bmp = wx.Bitmap("nosuchfile.bmp", wx.BITMAP_TYPE_BMP)
                mask = wx.Mask(bmp, wx.BLUE)
            except wx.PyAssertionError:
                self.log.WriteText("Caught wx.PyAssertionError!  I will fix the problem.\n")
                ## bmp = images.Test2.GetBitmap()
                bmp = wx.Bitmap(gBmpDir + os.sep + "Test2.bmp", wx.BITMAP_TYPE_BMP)
                mask = wx.MaskColour(bmp, wx.BLUE)
        else:
            ## bmp = images.Test2.GetBitmap()
            bmp = wx.Bitmap(gBmpDir + os.sep + "Test2.bmp", wx.BITMAP_TYPE_BMP)
            mask = wx.Mask(bmp, wx.BLUE)

        bmp.SetMask(mask)
        b = wx.BitmapButton(self, -1, bmp, (20, 20),
                       (bmp.GetWidth()+10, bmp.GetHeight()+10))
        b.SetToolTip(wx.ToolTip("This is a bitmap button."))
        self.Bind(wx.EVT_BUTTON, self.OnClick, b)

        b = wx.BitmapButton(self, -1, bmp, (20, 120),
                            style = wx.NO_BORDER)

        # hide a little surprise in the button...
        ## img = images.Robin.GetImage()
        img = wx.Image(gBmpDir + os.sep + "Robin.jpg", wx.BITMAP_TYPE_JPEG)
        # we need to make it be the same size as the primary image, so
        # grab a subsection of this new image
        cropped = img.GetSubImage((20, 20, bmp.GetWidth(), bmp.GetHeight()))
        b.SetBitmapPressed(cropped.ConvertToBitmap())

        b.SetToolTip(wx.ToolTip("This is a bitmap button with \nwx.NO_BORDER style."))
        self.Bind(wx.EVT_BUTTON, self.OnClick, b)


    def OnClick(self, event):
        self.log.WriteText("Click! (%d)\n" % event.GetId())


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
