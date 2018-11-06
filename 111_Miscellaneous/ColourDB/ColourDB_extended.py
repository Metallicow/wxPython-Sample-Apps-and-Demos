#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-Imports---------------------------------------------------------------------

#--wxPython Imports.
import wx
import wx.lib.colourdb

#--Local Imports.
try:
    import images  # PyEmbeddedImage
except ImportError:
    images = None  # Load bitmap from local directory

#- wxPython Demo -------------------------------------------------------------
__wxPyOnlineDocs__ = 'https://wxpython.org/Phoenix/docs/html/wx.lib.colourdb.html'
__wxPyDemoPanel__ = 'TestPanel'

overview = """<html><body>
<h2><center>ColourDB</center></h2>

<p>wxWindows maintains a database of standard RGB colours for a predefined
set of named colours (such as "BLACK'', "LIGHT GREY''). The application
may add to this set if desired by using Append. There is only one instance
of this class: <b>TheColourDatabase</b>.

<p>The <code>colourdb</code> library is a lightweight API that pre-defines
a multitude of colors for you to use 'out of the box', and this demo serves
to show you these colors (it also serves as a handy reference).

<p>A secondary benefit of this demo is the use of the <b>ScrolledWindow</b> class
and the use of various *DC() classes, including background tiling and the use of
font data to generate a "building block" type of construct for repetitive use.

<p>
<B><font size=+2>Important note</font></b>

<p>
With implementation of V2.5 and later, it is required to have a wx.App already
initialized before <b><code>wx.updateColourDB()</code></b> can be called.
Trying to do otherwise will cause an exception to be raised.
</body></html>
"""

#----------------------------------------------------------------------

class TestWindow(wx.ScrolledWindow):
    def __init__(self, parent, log):
        wx.ScrolledWindow.__init__(self, parent, -1)

        wx.lib.colourdb.updateColourDB()

        # Populate our color list
        self.clrList = wx.lib.colourdb.getColourInfoList()

        # Just for style points, we'll use this as a background image.
        if images is not None:
            self.bg_bmp = images.GridBG.GetBitmap()
        else:
            self.bg_bmp = wx.Bitmap("bitmaps/GridBG.png")

        # This could also be done by getting the window's default font;
        # either way, we need to have a font loaded for later on.
        #self.SetBackgroundColour("WHITE")
        self.font = wx.Font(10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)

        # Create drawing area and set its font
        dc = wx.ClientDC(self)
        dc.SetFont(self.font)

        # Using GetFullTextExtent(), we calculate a basic 'building block'
        # that will be used to draw a depiction of the color list. We're
        # using 'Wy' as the model becuase 'W' is a wide character and 'y'
        # has a descender. This constitutes a 'worst case' scenario, which means
        # that no matter what we draw later, text-wise, we'll have room for it
        w,h,d,e = dc.GetFullTextExtent("Wy")

        # Height plus descender
        self.textHeight = h + d

        # Pad a little bit
        self.lineHeight = self.textHeight + 5

        # ... and this is the basic width.
        self.cellWidth = w

        # jmg 11/8/03: why 24?
        numCells = 24

        # 'prep' our scroll bars.
        self.SetScrollbars(
            self.cellWidth, self.lineHeight, numCells, len(self.clrList) + 2
            )

        # Bind event handlers
        self.SetBackgroundStyle(wx.BG_STYLE_ERASE)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)


    # tile the background bitmap loaded in __init__()
    def TileBackground(self, dc):
        sz = self.GetClientSize()
        w = self.bg_bmp.GetWidth()
        h = self.bg_bmp.GetHeight()

        # adjust for scrolled position
        spx, spy = self.GetScrollPixelsPerUnit()
        vsx, vsy = self.GetViewStart()
        dx,  dy  = (spx * vsx) % w, (spy * vsy) % h

        x = -dx

        while x < sz.width:
            y = -dy
            while y < sz.height:
                dc.DrawBitmap(self.bg_bmp, x, y)
                y = y + h

            x = x + w

    # Redraw the background over a 'damaged' area.
    def OnEraseBackground(self, event):
        dc = event.GetDC()

        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRegion(rect)

        self.TileBackground(dc)

    def OnPaint(self, event):
        dc = wx.PaintDC(self)
        self.PrepareDC(dc)
        self.Draw(dc, self.GetUpdateRegion(), self.GetViewStart())

    def Draw(self, dc, rgn=None, vs=None):
        dc.SetTextForeground("BLACK")
        dc.SetPen(wx.Pen("BLACK", 1, wx.PENSTYLE_SOLID))
        dc.SetFont(self.font)
        colours = self.clrList
        numColours = len(colours)

        if rgn:
            # determine the subset of the color list that has been exposed
            # and needs drawn. This is based on all the precalculation we
            # did in __init__()
            rect = rgn.GetBox()
            pixStart = vs[1]*self.lineHeight + rect.y
            pixStop  = pixStart + rect.height
            start = pixStart / self.lineHeight - 1
            stop = pixStop / self.lineHeight
        else:
            start = 0
            stop = numColours

        for line in range(int(max(0,start)), int(min(stop,numColours))):
            clr = colours[line][0]
            y = (line+1) * self.lineHeight + 2

            dc.DrawText(clr, self.cellWidth, y)

            brush = wx.Brush(clr, wx.BRUSHSTYLE_SOLID)
            dc.SetBrush(brush)
            dc.DrawRectangle(10 * self.cellWidth, y,
                             6 * self.cellWidth, self.textHeight)

            dc.DrawText(str(tuple(colours[line][1:])),
                        18 * self.cellWidth, y)

            hexstr = "#%02X%02X%02X" % tuple(colours[line][1:])
            dc.DrawText(hexstr, 25 * self.cellWidth, y)


# On wxGTK there needs to be a panel under wx.ScrolledWindows if they are
# going to be in a wxNotebook. And, in this demo, we are.
class TestPanel(wx.Panel):
    def __init__(self, parent, log):
        wx.Panel.__init__(self, parent, -1)
        self.win = TestWindow(self, log)
        self.Bind(wx.EVT_SIZE, self.OnSize)


    def OnSize(self, event):
        self.win.SetSize(event.GetSize())


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
        gMainWin = TestFrame(None)
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
