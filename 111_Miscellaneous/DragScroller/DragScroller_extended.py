#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-Imports----------------------------------------------------------------------

#--wxPython Imports.
import wx
import wx.lib.dragscroller

#- wxPython Demo --------------------------------------------------------------
__wxPyOnlineDocs__ = 'https://wxpython.org/Phoenix/docs/html/wx.lib.colourdb.html'
__wxPyDemoPanel__ = 'TestWindow'

overview = """<html><body>
<h2<center>>DragScroller</center></h2>
<p>
A helper class that adds scrolling to a wx.ScrolledWindow in the direction
of the drag.
</body></html>
"""

def runTest(frame, nb, log):
    win = TestWindow(nb, log)
    return win


#------------------------------------------------------------------------------


class TestWindow(wx.ScrolledWindow):
    def __init__(self, parent, log, id=wx.ID_ANY):
        wx.ScrolledWindow.__init__(self, parent, id)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_RIGHT_DOWN, self.OnRightDown)
        self.Bind(wx.EVT_RIGHT_UP, self.OnRightUp)

        self.SetScrollbars(1, 1, 2000, 2000, 0, 0)

        self.scroller = wx.lib.dragscroller.DragScroller(self)

    def OnPaint(self, event):
        dc = wx.PaintDC(self)
        dc.Clear()
        self.PrepareDC(dc)

        st1 = 'Right click and drag in the direction you want to scroll.'
        st2 = 'The distance from the start of the drag determines the speed.'

        pen = wx.Pen(wx.BLACK, 5)
        dc.SetPen(pen)

        x, y = 0, 0
        for y in range(10):
            for x in range(10):
                dc.DrawCircle(x*400+20, y*400+20, 200)

        brush = wx.TRANSPARENT_BRUSH
        pen = wx.Pen(wx.BLACK, 1)
        dc.SetBrush(brush)
        dc.SetPen(pen)
        w1, h1, d1, e1 = sz = dc.GetFullTextExtent(st1)
        w2, h2, d2, e2 = sz = dc.GetFullTextExtent(st2)
        x1, y1, width1, height1 = 10, 10, max(w1, w2) + 20, h1 + h2 + 40
        # print('x, y = (%d, %d)' % (x, y))

        dc.DrawRectangle(0 + 10, 0 + 10, width1, height1)
        dc.DrawText(st1, 20, 20)
        dc.DrawText(st2, 20, 50)


    def OnRightDown(self, event):
        self.scroller.Start(event.GetPosition())

    def OnRightUp(self, event):
        self.scroller.Stop()


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

        panel = TestWindow(self, log)
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
