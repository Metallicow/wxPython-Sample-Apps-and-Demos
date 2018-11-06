#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-Imports----------------------------------------------------------------------

#--python Imports.
import os
import sys

#--wxPython Imports.
import wx

#- wxPython Demo --------------------------------------------------------------
__wxPyOnlineDocs__ = 'https://wxpython.org/Phoenix/docs/html/wx.Treebook.html'
__wxPyDemoPanel__ = 'TestTreebook'

overview = """\
<html><body>
<h2>wx.Treebook</h2>
<p>
This class is a control similar to a notebook control, but with a
wx.TreeCtrl instead of a set of tabs.
</p>
</body></html>
"""

try:
    gFileDir = os.path.dirname(os.path.abspath(__file__))
except:
    gFileDir = os.path.dirname(os.path.abspath(sys.argv[0]))
gBmpDir = gFileDir + os.sep + 'bitmaps'
## import images

colourList = ["Aquamarine", "Grey", "Blue", "Blue Violet", "Brown", "Cadet Blue",
              "Coral", "Wheat", "Cyan", "Dark Grey", "Dark Green",
              "Steel Blue",
              ]

class ColoredPanel(wx.Window):
    def __init__(self, parent, color):
        wx.Window.__init__(self, parent, wx.ID_ANY, style=wx.SIMPLE_BORDER)
        self.SetBackgroundColour(color)
        if wx.Platform == '__WXGTK__':
            self.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)

#----------------------------------------------------------------------------

def getNextImageID(count):
    imID = 0
    while True:
        yield imID
        imID += 1
        if imID == count:
            imID = 0


class TestTreebook(wx.Treebook):
    def __init__(self, parent, log, id=wx.ID_ANY):
        wx.Treebook.__init__(self, parent, id, style=
                             wx.BK_DEFAULT
                             #wx.BK_TOP
                             #wx.BK_BOTTOM
                             #wx.BK_LEFT
                             #wx.BK_RIGHT
                            )
        self.log = log

        # make an image list using the LBXX images
        il = wx.ImageList(32, 32)
        for x in range(12):
            ## obj = getattr(images, 'LB%02d' % (x+1))
            ## bmp = obj.GetBitmap()
            bmp = wx.Bitmap(gBmpDir + os.sep + 'LB%02d.png' % (x+1), wx.BITMAP_TYPE_PNG)
            il.Add(bmp)
        self.AssignImageList(il)
        imageIdGenerator = getNextImageID(il.GetImageCount())

        # Now make a bunch of panels for the tree book.
        first = True
        for colour in colourList:
            win = self.makeColorPanel(colour)
            if sys.version_info[0] == 3:
                self.AddPage(win, colour, imageId=next(imageIdGenerator))
            else:
                self.AddPage(win, colour, imageId=imageIdGenerator.next())
            if first:
                st = wx.StaticText(win.win, -1,
                          "You can put nearly any type of window here,\n"
                          "and the wx.TreeCtrl can be on either side of the\n"
                          "Treebook",
                          wx.Point(10, 10))
                first = False

            win = self.makeColorPanel(colour)
            st = wx.StaticText(win.win, -1, "this is a sub-page", (10,10))
            if sys.version_info[0] == 3:
                self.AddSubPage(win, 'a sub-page', imageId=next(imageIdGenerator))
            else:
                self.AddSubPage(win, 'a sub-page', imageId=imageIdGenerator.next())

        self.Bind(wx.EVT_TREEBOOK_PAGE_CHANGED, self.OnPageChanged)
        self.Bind(wx.EVT_TREEBOOK_PAGE_CHANGING, self.OnPageChanging)

        # This is a workaround for a sizing bug on Mac...
        wx.CallLater(100, self.AdjustSize)

    def AdjustSize(self):
        self.PostSizeEvent()

    def makeColorPanel(self, color):
        p = wx.Panel(self, -1)
        win = ColoredPanel(p, color)
        p.win = win
        def OnCPSize(evt, win=win):
            win.SetPosition((0,0))
            win.SetSize(evt.GetSize())
        p.Bind(wx.EVT_SIZE, OnCPSize)
        return p

    def OnPageChanged(self, event):
        old = event.GetOldSelection()
        new = event.GetSelection()
        sel = self.GetSelection()
        self.log.WriteText('OnPageChanged,  old:%d, new:%d, sel:%d\n' % (old, new, sel))
        event.Skip()

    def OnPageChanging(self, event):
        old = event.GetOldSelection()
        new = event.GetSelection()
        sel = self.GetSelection()
        self.log.WriteText('OnPageChanging, old:%d, new:%d, sel:%d\n' % (old, new, sel))
        event.Skip()


#- wxPy Demo -----------------------------------------------------------------


def runTest(frame, nb, log):
    win = TestTreebook(nb, log)
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

        panel = TestTreebook(self, log)
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
