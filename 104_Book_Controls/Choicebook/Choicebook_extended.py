#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-Imports----------------------------------------------------------------------

#--wxPython Imports.
import  wx

#- wxPython Demo --------------------------------------------------------------
__wxPyOnlineDocs__ = 'https://wxpython.org/Phoenix/docs/html/wx.Choicebook.html'
__wxPyDemoPanel__ = 'TestChoicebook'

overview = """<html><body>
<h2>wx.Choicebook</h2>
<p>

This class is a control similar to a notebook control, but uses a
wx.Choice to manage the selection of the pages.
</body></html>
"""

pageTexts = ["Yet",
             "Another",
             "Way",
             "To",
             "Select",
             "Pages"
             ]
          

class TestChoicebook(wx.Choicebook):
    def __init__(self, parent, log, id=wx.ID_ANY):
        wx.Choicebook.__init__(self, parent, id)
        self.log = log

        # Now make a bunch of panels for the choice book
        count = 1
        for txt in pageTexts:
            win = wx.Panel(self)
            if count == 1:
                st = wx.StaticText(win, wx.ID_ANY,
                          "wx.Choicebook is yet another way to switch between 'page' windows",
                          (10, 10))
            else:
                st = wx.StaticText(win, wx.ID_ANY, "Page: %d" % count, (10,10))
            count += 1
            
            self.AddPage(win, txt)

        self.Bind(wx.EVT_CHOICEBOOK_PAGE_CHANGED, self.OnPageChanged)
        self.Bind(wx.EVT_CHOICEBOOK_PAGE_CHANGING, self.OnPageChanging)


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

#----------------------------------------------------------------------------

def runTest(frame, nb, log):
    win = TestChoicebook(nb, log)
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

        panel = TestChoicebook(self, log)
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
