#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-Imports----------------------------------------------------------------------

#--wxPython Imports.
import  wx

#- wxPython Demo --------------------------------------------------------------
__wxPyOnlineDocs__ = 'http://wxpython.org/Phoenix/docs/html/SplitterWindow.html'
__wxPyDemoPanel__ = 'TestPanel'

overview = """\
This class manages up to two subwindows. The current view can be split
into two programmatically (perhaps from a menu command), and unsplit
either programmatically or via the wx.SplitterWindow user interface.
"""

#---------------------------------------------------------------------------

class MySplitter(wx.SplitterWindow):
    def __init__(self, parent, ID, log):
        wx.SplitterWindow.__init__(self, parent, ID,
                                   style=wx.SP_LIVE_UPDATE
                                   )
        self.log = log

        self.Bind(wx.EVT_SPLITTER_SASH_POS_CHANGED, self.OnSashChanged)
        self.Bind(wx.EVT_SPLITTER_SASH_POS_CHANGING, self.OnSashChanging)

    def OnSashChanged(self, event):
        self.log.WriteText("sash changed to %s\n" % str(event.GetSashPosition()))

    def OnSashChanging(self, event):
        self.log.WriteText("sash changing to %s\n" % str(event.GetSashPosition()))
        # uncomment this to not allow the change
        #event.SetSashPosition(-1)


class TestPanel(wx.Panel):
    def __init__(self, parent, log):
        self.log = log
        wx.Panel.__init__(self, parent)

        splitter = MySplitter(self, -1, log)

        #sty = wx.BORDER_NONE
        #sty = wx.BORDER_SIMPLE
        sty = wx.BORDER_SUNKEN

        p1 = wx.Window(splitter, style=sty)
        p1.SetBackgroundColour("pink")
        wx.StaticText(p1, -1, "Panel One", (5,5))

        p2 = wx.Window(splitter, style=sty)
        p2.SetBackgroundColour("sky blue")
        wx.StaticText(p2, -1, "Panel Two", (5,5))

        splitter.SetMinimumPaneSize(20)
        splitter.SplitVertically(p1, p2, -100)

        szr = wx.BoxSizer()
        szr.Add(splitter, 1, wx.EXPAND)
        self.SetSizer(szr)


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

