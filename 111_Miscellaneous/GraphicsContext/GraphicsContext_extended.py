#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-Imports---------------------------------------------------------------------

#--Python Imports.
import os
import sys
import colorsys
from math import cos, sin, radians

#--wxPython Imports.
import wx


#-Globals----------------------------------------------------------------------
try:
    gFileDir = os.path.dirname(os.path.abspath(__file__))
except:
    gFileDir = os.path.dirname(os.path.abspath(sys.argv[0]))
gBmpDir = gFileDir + os.sep + 'bitmaps'


#- wxPython Demo -------------------------------------------------------------
__wxPyOnlineDocs__ = 'https://wxpython.org/Phoenix/docs/html/wx.GraphicsContext.html'
__wxPyDemoPanel__ = 'TestPanel'


overview = """<html><body>
<h2><center>wx.GraphicsContext and wx.GraphicsPath</center></h2>

The new advanced 2D drawing API is implemented via the
wx.GraphicsContext and wx.GraphicsPath classes.  They wrap GDI+ on
Windows, Cairo on wxGTK and CoreGraphics on OS X.  They allow
path-based drawing with alpha-blending and anti-aliasing, and use a
floating point cooridnate system.

<p>When viewing this sample pay attention to how the rounded edges are
smoothed with anti-aliased drawing, and how the shapes on the lower
half of the window are partially transparent, allowing you to see what
was drawn before.

</body></html>
"""

#----------------------------------------------------------------------

BASE  = 80.0    # sizes used in shapes drawn below
BASE2 = BASE/2
BASE4 = BASE/4

USE_BUFFER = ('wxMSW' in wx.PlatformInfo) # use buffered drawing on Windows


class TestPanel(wx.Panel):
    def __init__(self, parent, log):
        self.log = log
        wx.Panel.__init__(self, parent, -1)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        if USE_BUFFER:
            self.Bind(wx.EVT_SIZE, self.OnSize)


    def OnSize(self, event):
        # When there is a size event then recreate the buffer to match
        # the new size of the window.
        self.InitBuffer()
        event.Skip()

    def OnPaint(self, event):
        if USE_BUFFER:
            # The buffer already contains our drawing, so no need to
            # do anything else but create the buffered DC.  When this
            # method exits and dc is collected then the buffer will be
            # blitted to the paint DC automagically
            dc = wx.BufferedPaintDC(self, self._buffer)
        else:
            # Otherwise we need to draw our content to the paint DC at
            # this time.
            dc = wx.PaintDC(self)
            gc = self.MakeGC(dc)
            self.Draw(gc)

    def InitBuffer(self):
        sz = self.GetClientSize()
        sz.width = max(1, sz.width)
        sz.height = max(1, sz.height)
        self._buffer = wx.Bitmap(sz.width, sz.height, 32)

        dc = wx.MemoryDC(self._buffer)
        dc.SetBackground(wx.Brush(self.GetBackgroundColour()))
        dc.Clear()
        gc = self.MakeGC(dc)
        self.Draw(gc)

    def MakeGC(self, dc):
        try:
            if False:
                # If you want to force the use of Cairo instead of the
                # native GraphicsContext backend then create the
                # context like this.  It works on Windows so far, (on
                # wxGTK the Cairo context is already being used as the
                # native default.)
                gcr = wx.GraphicsRenderer.GetCairoRenderer
                gc = gcr() and gcr().CreateContext(dc)
                if gc is None:
                    wx.MessageBox("Unable to create Cairo Context.", "Oops")
                    gc = wx.GraphicsContext.Create(dc)
            else:
                # Otherwise, creating it this way will use the native
                # backend, (GDI+ on Windows, CoreGraphics on Mac, or
                # Cairo on GTK).
                gc = wx.GraphicsContext.Create(dc)

        except NotImplementedError:
            dc.DrawText("This build of wxPython does not support the wx.GraphicsContext "
                        "family of classes.",
                        25, 25)
            return None
        return gc

    def Draw(self, gc):
        font = wx.SystemSettings.GetFont(wx.SYS_DEFAULT_GUI_FONT)
        font.SetWeight(wx.FONTWEIGHT_BOLD)
        gc.SetFont(font, wx.BLACK)

        # make a path that contains a circle and some lines, centered at 0,0
        path = gc.CreatePath()
        path.AddCircle(0, 0, BASE2)
        path.MoveToPoint(0, -BASE2)
        path.AddLineToPoint(0, BASE2)
        path.MoveToPoint(-BASE2, 0)
        path.AddLineToPoint(BASE2, 0)
        path.CloseSubpath()
        path.AddRectangle(-BASE4, -BASE4/2, BASE2, BASE4)

        # Now use that path to demonstrate various capbilites of the grpahics context
        gc.PushState()             # save current translation/scale/other state
        gc.Translate(60, 75)       # reposition the context origin

        gc.SetPen(wx.Pen("navy", 1))
        gc.SetBrush(wx.Brush("pink"))

        # show the difference between stroking, filling and drawing
        for label, PathFunc in [("StrokePath", gc.StrokePath),
                                ("FillPath",   gc.FillPath),
                                ("DrawPath",   gc.DrawPath)]:
            w, h = gc.GetTextExtent(label)

            gc.DrawText(label, -w/2, -BASE2-h-4)
            PathFunc(path)
            gc.Translate(2*BASE, 0)

        gc.PopState()          # restore saved state
        gc.PushState()         # save it again
        gc.Translate(60, 200)  # offset to the lower part of the window

        gc.DrawText("Scale", 0, -BASE2)
        gc.Translate(0, 20)

        # for testing clipping
        ## gc.Clip(0, 0, 100, 100)
        ## rgn = wx.RegionFromPoints([ (0,0), (75,0), (75,25,), (100, 25),
        ##                             (100,100), (0,100), (0,0)  ])
        ## gc.ClipRegion(rgn)
        ## gc.ResetClip()

        gc.SetBrush(wx.Brush(wx.Colour(178,  34,  34, 128)))  # 128 == half transparent
        for cnt in range(8):
            gc.Scale(1.08, 1.08)  # increase scale by 8%
            gc.Translate(5,5)
            gc.DrawPath(path)

        gc.PopState()           # restore saved state
        gc.PushState()          # save it again
        gc.Translate(335, 200)
        gc.DrawText("Rotate", 0, -BASE2)

        # Move the origin over to the next location
        gc.Translate(30, 75)

        # draw our path again, rotating it about the central point,
        # and changing colors as we go
        for angle in range(0, 360, 30):
            gc.PushState()         # save this new current state so we can
                                   # pop back to it at the end of the loop
            r, g, b = [int(c * 255) for c in colorsys.hsv_to_rgb(float(angle)/360, 1, 1)]
            gc.SetBrush(wx.Brush(wx.Colour(r, g, b, 64)))
            gc.SetPen(wx.Pen(wx.Colour(r, g, b, 128)))

            # use translate to artfully reposition each drawn path
            gc.Translate(1.5 * BASE2 * cos(radians(angle)),
                         1.5 * BASE2 * sin(radians(angle)))

            # use Rotate to rotate the path
            gc.Rotate(radians(angle))

            # now draw it
            gc.DrawPath(path)
            gc.PopState()

        # Draw a bitmap with an alpha channel on top of the last group
        bmp = wx.Bitmap(gBmpDir + os.sep + 'toucan.png')
        bsz = bmp.GetSize()
        gc.DrawBitmap(bmp,
                      #-bsz.width,
                      #-bsz.height/2,

                      -bsz.width/2.5,
                      -bsz.height/2.5,

                      bsz.width, bsz.height)

        gc.PopState()


#- wxPy demo -----------------------------------------------------------------


def runTest(frame, nb, log):
    win = TestPanel(nb, log)
    return win


#- __main__ Demo -------------------------------------------------------------


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
        gMainWin = TestFrame(None, size=(550, 450))
        gMainWin.SetTitle('Test Demo')
        gMainWin.Show()

        return True


#- __main__ ------------------------------------------------------------------


if __name__ == '__main__':
    import sys
    print('Python %s.%s.%s %s' % sys.version_info[0:4])
    print('wxPython %s' % wx.version())
    gApp = TestApp(redirect=False,
                   filename=None,
                   useBestVisual=False,
                   clearSigInt=True)
    gApp.MainLoop()
