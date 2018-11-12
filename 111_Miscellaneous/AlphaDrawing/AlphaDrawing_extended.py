#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-Imports---------------------------------------------------------------------

#--wxPython Imports.
import wx

#- wxPython Demo -------------------------------------------------------------
__wxPyOnlineDocs__ = 'https://wxpython.org/Phoenix/docs/html/wx.GCDC.html'
__wxPyDemoPanel__ = 'TestPanel'

overview = """<html><body>
<h2><center>Alpha Drawing</center></h2>

The wx.GCDC class is a class that implemented the wx.DC API using the
new wx.GraphicsContext class, and so it supports anti-aliased drawing
using pens and brushes, that can optionally also be drawn using an
alpha transparency.  (On the Mac all the DC classes are using this new
implementation.)  This is accomplished by enabling the wx.Colour class
to have a fourth component for the alpha value, where 0 is fully
transparent, and 255 is fully opaque.

</body></html>
"""


class TestPanel(wx.Panel):
    def __init__(self, parent, log):
        self.log = log
        wx.Panel.__init__(self, parent, -1)
        self.Bind(wx.EVT_PAINT, self.OnPaint)

        txt = """\
If this build of wxPython includes the new wx.GCDC class (which
provides the wx.DC API on top of the new wx.GraphicsContext class)
then these squares should be transparent.
"""
        wx.StaticText(self, -1, txt, (20, 20))


    def OnPaint(self, evt):
        pdc = wx.PaintDC(self)
        try:
            dc = wx.GCDC(pdc)
        except:
            dc = pdc
        rect = wx.Rect(0,0, 100, 100)
        for RGB, pos in [((178,  34,  34), ( 50,  90)),
                         (( 35, 142,  35), (110, 150)),
                         ((  0,   0, 139), (170,  90))
                         ]:
            r, g, b = RGB
            penclr   = wx.Colour(r, g, b, wx.ALPHA_OPAQUE)
            brushclr = wx.Colour(r, g, b, 128)   # half transparent
            dc.SetPen(wx.Pen(penclr))
            dc.SetBrush(wx.Brush(brushclr))
            rect.SetPosition(pos)
            dc.DrawRoundedRectangle(rect, 8)

        # some additional testing stuff
        #dc.SetPen(wx.Pen(wx.Colour(0,0,255, 196)))
        #dc.SetBrush(wx.Brush(wx.Colour(0,0,255, 64)))
        #dc.DrawCircle(50, 275, 25)
        #dc.DrawEllipse(100, 275, 75, 50)


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
        gMainWin = TestFrame(None, size=(450, 350))
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
