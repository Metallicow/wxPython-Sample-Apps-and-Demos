#!/usr/bin/env python

#----------------------------------------------------------------------------
# Name:         ImageBrowser.py
# Purpose:      Image Selection dialog for wxPython demo
#
# Author:       Lorne White (email: lorne.white@telusplanet.net)
#
# Version       0.5
# Date:         Feb 26, 2001
# Licence:      wxWindows license
#----------------------------------------------------------------------------

__wxPyDemoPanel__ = 'TestPanel'

import os

import wx
import wx.lib.imagebrowser as ib


#---------------------------------------------------------------------------

class TestPanel(wx.Panel):
    def __init__(self, parent, log):
        self.log = log
        wx.Panel.__init__(self, parent, -1)

        b = wx.Button(self, -1, "Create and Show an ImageDialog", (50,50))
        self.Bind(wx.EVT_BUTTON, self.OnButton, b)


    def OnButton(self, event):
        # get current working directory
        dir = os.getcwd()

        # set the initial directory for the demo bitmaps
        initial_dir = os.path.join(dir, 'bitmaps')

        # open the image browser dialog
        dlg = ib.ImageDialog(self, initial_dir)

        dlg.Centre()

        if dlg.ShowModal() == wx.ID_OK:
            # show the selected file
            self.log.WriteText("You Selected File: " + dlg.GetFile())
        else:
            self.log.WriteText("You pressed Cancel\n")

        dlg.Destroy()


#---------------------------------------------------------------------------


def runTest(frame, nb, log):
    win = TestPanel(nb, log)
    return win


#---------------------------------------------------------------------------


overview = """\
"""


#- __main__ Demo ---------------------------------------------------------------

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

        try:
            self.SetIcon(wx.IconFromLocation(wx.IconLocation(sys.executable)))
        except Exception as exc:
            raise exc

    def OnDestroy(self, event):
        self.Destroy()


class TestApp(wx.App):
    def OnInit(self):
        gMainWin = TestFrame(None)
        gMainWin.SetTitle('Extended Frame Demo')
        gMainWin.Show()

        return True

#---------------------------------------------------------------------------


if __name__ == '__main__':
    import sys
    print('Python %s.%s.%s %s' % sys.version_info[0:4])
    print('wxPython %s' % wx.version())
    gApp = TestApp(redirect=False,
            filename=None,
            useBestVisual=False,
            clearSigInt=True)

    gApp.MainLoop()
