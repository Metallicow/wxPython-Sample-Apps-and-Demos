#!/usr/bin/env python
# -*- coding: utf-8 -*-

#--wxPython Imports.
import wx
import wx.lib.multisash as sash
import wx.stc as stc

#- wxPython Demo --------------------------------------------------------------
__wxPyOnlineDocs__ = 'http://wxpython.org/Phoenix/docs/html/lib.multisash.html'
__wxPyDemoPanel__ = 'TestWindow'

overview = """<html><body>
<h2><center>MultiSash</center></h2>

MultiSash allows the user to split a window any number of times
either horizontally or vertically, and to close the split off windows
when desired.

</body></html>
"""

#---------------------------------------------------------------------------

sampleText="""\
You can drag the little tab on the vertical sash left to create another view,
or you can drag the tab on the horizontal sash to the top to create another
horizontal view.

The red blocks on the sashes will destroy the view (bottom,left) this block
belongs to.

A yellow rectangle also highlights the current selected view.

By calling GetSaveData on the multiSash control the control will return its
contents and the positions of each sash as a dictionary.
Calling SetSaveData with such a dictionary will restore the control to the
state it was in when it was saved.

If the class, that is used as a view, has GetSaveData/SetSaveData implemented,
these will also be called to save/restore their state. Any object can be
returned by GetSaveData, as it is just another object in the dictionary.
"""


class TestWindow(stc.StyledTextCtrl):

    # shared document reference
    doc = None

    def __init__(self, parent, log=None):
        stc.StyledTextCtrl.__init__(self, parent, -1, style=wx.NO_BORDER)
        self.log = log

        self.SetMarginWidth(1,0)

        if wx.Platform == '__WXMSW__':
            fSize = 10
        else:
            fSize = 12

        self.StyleSetFont(
            stc.STC_STYLE_DEFAULT,
            wx.Font(fSize, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
            )

        if self.doc:
            self.SetDocPointer(self.doc)
        else:
            self.SetText(sampleText)
            TestWindow.doc = self.GetDocPointer()


    def ShutDownDemo(self):
        # Reset doc reference in case this demo is run again
        TestWindow.doc = None


#- wxPy Demo -----------------------------------------------------------------


def runTest(frame, nb, log):
    multi = sash.MultiSash(nb, -1, pos=(0,0), size=(640, 480))

    # Use this method to set the default class that will be created when
    # a new sash is created. The class's constructor needs 1 parameter
    # which is the parent of the window
    multi.SetDefaultChildClass(TestWindow)

    return multi


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

        multi = sash.MultiSash(self, -1, pos=(0,0), size=(640, 480))

        # Use this method to set the default class that will be created when
        # a new sash is created. The class's constructor needs 1 parameter
        # which is the parent of the window
        multi.SetDefaultChildClass(TestWindow)
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
