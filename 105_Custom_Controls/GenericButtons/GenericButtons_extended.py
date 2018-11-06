#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-Imports----------------------------------------------------------------------

#--Python Imports.
import os
import sys

#--wxPython Imports.
import wx
import wx.lib.buttons  as  buttons

#--Local Imports.
## import images

#-Globals----------------------------------------------------------------------
try:
    gFileDir = os.path.dirname(os.path.abspath(__file__))
except Exception:
    gFileDir = os.path.dirname(os.path.abspath(sys.argv[0]))
gBmpDir = gFileDir + os.sep + 'bitmaps'

#- wxPython Demo --------------------------------------------------------------
__wxPyOnlineDocs__ = 'https://wxpython.org/Phoenix/docs/html/wx.lib.buttons.html'
__wxPyDemoPanel__ = 'TestPanel'

overview = buttons.__doc__


class TestPanel(wx.Panel):
    def __init__(self, parent, log):
        wx.Panel.__init__(self, parent, -1)
        self.log = log
        ##self.SetBackgroundColour("sky blue")

        sizer = wx.FlexGridSizer(cols=3, hgap=20, vgap=20)

        # A regular button, selected as the default button.
        b = wx.Button(self, -1, "A real button")
        b.SetDefault()
        self.Bind(wx.EVT_BUTTON, self.OnButton, b)
        sizer.Add(b)

        # Same thing, but NOT set as the default button.
        b = wx.Button(self, -1, "non-default")
        self.Bind(wx.EVT_BUTTON, self.OnButton, b)
        sizer.Add(b)
        sizer.Add((10, 10))

        # Plain old text button based off GenButton().
        b = buttons.GenButton(self, -1, 'Hello')
        self.Bind(wx.EVT_BUTTON, self.OnButton, b)
        sizer.Add(b)

        # Plain old text button, disabled.
        b = buttons.GenButton(self, -1, 'disabled')
        self.Bind(wx.EVT_BUTTON, self.OnButton, b)
        b.Enable(False)
        sizer.Add(b)

        # This time, we let the botton be as big as it can be.
        # Also, this one is fancier, with custom colors and bezel size.
        b = buttons.GenButton(self, -1, 'bigger')
        self.Bind(wx.EVT_BUTTON, self.OnBiggerButton, b)
        b.SetFont(wx.Font(20, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False))
        b.SetBezelWidth(5)
        b.SetMinSize(wx.DefaultSize)
        b.SetBackgroundColour("Navy")
        b.SetForegroundColour(wx.WHITE)
        b.SetToolTip("This is a BIG button...")
        # let the sizer set best size
        sizer.Add(b, flag=wx.ADJUST_MINSIZE)

        # An image button.
        ## bmp = images.Test2.GetBitmap()
        bmp = wx.Bitmap(gBmpDir + os.sep + "test2.bmp", wx.BITMAP_TYPE_BMP)
        b = buttons.GenBitmapButton(self, -1, bmp)
        self.Bind(wx.EVT_BUTTON, self.OnButton, b)
        sizer.Add(b)

        # An image button, disabled.
        ## bmp = images.Test2.GetBitmap()
        bmp = wx.Bitmap(gBmpDir + os.sep + "test2.bmp", wx.BITMAP_TYPE_BMP)
        b = buttons.GenBitmapButton(self, -1, bmp)
        self.Bind(wx.EVT_BUTTON, self.OnButton, b)
        sizer.Add(b)
        b.Enable(False)

        # An image button, using a mask to get rid of the
        # undesireable part of the image.
        b = buttons.GenBitmapButton(self, -1, None)
        self.Bind(wx.EVT_BUTTON, self.OnButton, b)
        ## bmp = images.Bulb1.GetBitmap()
        bmp = wx.Bitmap(gBmpDir + os.sep + "bulb1.bmp", wx.BITMAP_TYPE_BMP)
        mask = wx.Mask(bmp, wx.BLUE)
        bmp.SetMask(mask)
        b.SetBitmapLabel(bmp)
        #@ bmp = images.Bulb2.GetBitmap()
        bmp = wx.Bitmap(gBmpDir + os.sep + "bulb2.bmp", wx.BITMAP_TYPE_BMP)
        mask = wx.Mask(bmp, wx.BLUE)
        bmp.SetMask(mask)
        b.SetBitmapSelected(bmp)
        b.SetInitialSize()
        sizer.Add(b)

        # A toggle button.
        b = buttons.GenToggleButton(self, -1, "Toggle Button")
        self.Bind(wx.EVT_BUTTON, self.OnToggleButton, b)
        sizer.Add(b)

        # An image toggle button.
        b = buttons.GenBitmapToggleButton(self, -1, None)
        self.Bind(wx.EVT_BUTTON, self.OnToggleButton, b)
        ## bmp = images.Bulb1.GetBitmap()
        bmp = wx.Bitmap(gBmpDir + os.sep + "bulb1.bmp", wx.BITMAP_TYPE_BMP)
        mask = wx.Mask(bmp, wx.BLUE)
        bmp.SetMask(mask)
        b.SetBitmapLabel(bmp)
        ## bmp = images.Bulb2.GetBitmap()
        bmp = wx.Bitmap(gBmpDir + os.sep + "bulb2.bmp", wx.BITMAP_TYPE_BMP)
        mask = wx.Mask(bmp, wx.BLUE)
        bmp.SetMask(mask)
        b.SetBitmapSelected(bmp)
        b.SetToggle(True)
        b.SetInitialSize()
        sizer.Add(b)

        # A bitmap button with text.
        b = buttons.GenBitmapTextButton(self, -1, None, "Bitmapped Text", size=(200, 45))
        self.Bind(wx.EVT_BUTTON, self.OnButton, b)
        ## bmp = images.Bulb1.GetBitmap()
        bmp = wx.Bitmap(gBmpDir + os.sep + "bulb1.bmp", wx.BITMAP_TYPE_BMP)
        mask = wx.Mask(bmp, wx.BLUE)
        bmp.SetMask(mask)
        b.SetBitmapLabel(bmp)
        ## bmp = images.Bulb2.GetBitmap()
        bmp = wx.Bitmap(gBmpDir + os.sep + "bulb2.bmp", wx.BITMAP_TYPE_BMP)
        mask = wx.Mask(bmp, wx.BLUE)
        bmp.SetMask(mask)
        b.SetBitmapSelected(bmp)
        b.SetUseFocusIndicator(False)
        b.SetInitialSize()
        sizer.Add(b)

        # A flat text button.
        b = buttons.GenButton(self, -1, 'Flat buttons too!', style=wx.BORDER_NONE)
        self.Bind(wx.EVT_BUTTON, self.OnButton, b)
        sizer.Add(b, flag=wx.ALIGN_CENTER_VERTICAL)

        # A flat image button.
        ## bmp = images.Test2.GetBitmap()
        bmp = wx.Bitmap(gBmpDir + os.sep + "test2.bmp", wx.BITMAP_TYPE_BMP)
        bmp.SetMaskColour("blue")
        b = buttons.GenBitmapButton(self, -1, bmp, style=wx.BORDER_NONE)
        self.Bind(wx.EVT_BUTTON, self.OnButton, b)
        sizer.Add(b)
        ##b.SetBackgroundColour("sky blue")
        ##b.SetBackgroundColour("pink")

        vbox = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(vbox)

        b = buttons.ThemedGenButton(self, -1, 'Drawn with native renderer')
        self.Bind(wx.EVT_BUTTON, self.OnButton, b)
        vbox.Add(b, 0, wx.ALL, 5)

        b = buttons.ThemedGenToggleButton(self, -1, 'native renderered toggle')
        self.Bind(wx.EVT_BUTTON, self.OnButton, b)
        vbox.Add(b, 0, wx.ALL, 5)

        border = wx.BoxSizer(wx.VERTICAL)
        border.Add(sizer, 0, wx.ALL, 25)
        self.SetSizer(border)


    def OnButton(self, event):
        self.log.WriteText("Button Clicked: %d\n" % event.GetId())

    def OnBiggerButton(self, event):
        self.log.WriteText("Bigger Button Clicked: %d\n" % event.GetId())
        b = event.GetEventObject()
        txt = "big " + b.GetLabel()
        b.SetLabel(txt)
        self.GetSizer().Layout()

    def OnToggleButton(self, event):
        msg = (event.GetIsDown() and "on") or "off"
        self.log.WriteText("Button %d Toggled: %s\n" % (event.GetId(), msg))


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


