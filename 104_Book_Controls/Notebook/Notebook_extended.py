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
__wxPyOnlineDocs__ = 'https://wxpython.org/Phoenix/docs/html/wx.Notebook.html'
__wxPyDemoPanel__ = 'TestNB'

overview = """\
<html><body>
  <h2>wx.Notebook</h2>
  <p>
  This class represents a notebook control, which manages multiple
  windows with associated tabs.
  <p>
  To use the class, create a wx.Notebook object and call Notebook.AddPage or
  Notebook.InsertPage, passing a window to be used as the page. Do not
  explicitly delete the window for a page that is currently managed
  by wx.Notebook.
  <p>
  <b>NotebookPage</b> is a typedef for wx.Window.
  <h5>Window Styles</h5>
  <ul>
    <li>wx.NB_TOP: Place tabs on the top side.
    <li>wx.NB_LEFT: Place tabs on the left side.
    <li>wx.NB_RIGHT: Place tabs on the right side.
    <li>wx.NB_BOTTOM: Place tabs under instead of above the notebook pages.
    <li>wx.NB_FIXEDWIDTH: (Windows only) All tabs will have same width.
    <li>wx.NB_MULTILINE: (Windows only) There can be several rows of tabs.
    <li>wx.NB_NOPAGETHEME: (Windows only) Display a solid colour on notebook
          pages, and not a gradient, which can reduce performance.
    <li>wx.NB_FLAT: (Windows CE only) Show tabs in a flat style.
  </ul>
  <h5>Events Emitted by this Class</h5>
  <ul>
    <li>wx.EVT_NOTEBOOK_PAGE_CHANGED: The page selection was changed.
          Processes a wxEVT_NOTEBOOK_PAGE_CHANGED event.
    <li>wx.EVT_NOTEBOOK_PAGE_CHANGING: The page selection is about to be
          changed. Processes a wxEVT_NOTEBOOK_PAGE_CHANGING event.
          This event can be vetoed.
  </ul>
</body></html>
"""


class TestNB(wx.Notebook):
    def __init__(self, parent, log):
        wx.Notebook.__init__(self, parent, id=wx.ID_ANY, size=(21, 21), style=
                             wx.BK_DEFAULT
                             #wx.BK_TOP
                             #wx.BK_BOTTOM
                             #wx.BK_LEFT
                             #wx.BK_RIGHT
                             # | wx.NB_MULTILINE
                             )
        self.log = log

        # Add a Colored Panel Page with a small description.
        win = wx.Panel(self, wx.ID_ANY)
        win.SetBackgroundColour(wx.BLUE)
        self.AddPage(win, "Panel")
        st = wx.StaticText(win, -1,
                           "You can put nearly any type of window here,\n"
                           "and if the platform supports it then the\n"
                           "tabs can be on any side of the notebook.",
                           (10, 10))
        st.SetForegroundColour(wx.WHITE)
        st.SetBackgroundColour(wx.BLUE)

        # Show how to put an image on one of the notebook tabs,
        # first make the image list:
        il = wx.ImageList(16, 16)
        idx1 = il.Add(wx.Bitmap(gBmpDir + os.sep + 'book16.png', wx.BITMAP_TYPE_PNG))
        self.AssignImageList(il)

        # ...now put an image on the first notebook tab we just created.
        self.SetPageImage(0, idx1)

        # Add a TextCtrl Page.
        win = wx.TextCtrl(self, wx.ID_ANY,
                    ("%s\n\n" % wx.TextCtrl.__doc__) * 100,
                    style=wx.TE_MULTILINE)
        self.AddPage(win, "TextCtrl")

        # Add a Notebook Page.
        colors = (
            '#F39D76', '#F5B57F', '#F9CD8A', '#FFF99D', '#C7E19D', '#A8D59D',
            '#88C99D', '#8CCCCA', '#8DCFF3', '#93A9D5', '#9595C5', '#9681B6',
            '#AF88B8', '#C78FB9', '#F59FBC', '#F49E9C')
        win = wx.Notebook(self, wx.ID_ANY, size=(21, 21), style=wx.BK_LEFT)
        for i in range(len(colors)):
            p = wx.Panel(win, wx.ID_ANY)
            p.SetBackgroundColour(colors[i])
            win.AddPage(p, 'Page %d' % i)
        self.AddPage(win, "Notebook")

        # Add a TreeCtrl Page.
        win = wx.TreeCtrl(self, -1)
        root = win.AddRoot("The Root Item")
        for x in range(3):
            child = win.AppendItem(root, "Item %d" % x)
            win.SetItemData(child, None)

            for y in range(3):
                last = win.AppendItem(child, "item %d-%s" % (x, chr(ord("a") + y)))
                win.SetItemData(last, None)

                for z in range(3):
                    item = win.AppendItem(last, "item %d-%s-%d" % (x, chr(ord("a") + y), z))
                    win.SetItemData(item, None)
        win.ExpandAll()
        win.SelectItem(root)
        self.AddPage(win, "TreeCtrl")

        # Bind Notebook Event Handlers.
        self.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.OnPageChanged)
        self.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGING, self.OnPageChanging)


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
    testWin = TestNB(nb, log)
    return testWin


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

        panel = TestNB(self, log)
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
