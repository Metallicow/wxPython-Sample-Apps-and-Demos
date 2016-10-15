#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-Imports----------------------------------------------------------------------

#--wxPython Imports.
import wx

#- wxPython Demo --------------------------------------------------------------
__wxPyOnlineDocs__ = 'http://wxpython.org/Phoenix/docs/html/wx.GenericDirCtrl.html'
__wxPyDemoPanel__ = 'TestPanel'

overview = """\
This control can be used to place a directory listing (with optional files)
on an arbitrary window. The control contains a TreeCtrl window representing
the directory hierarchy, and optionally, a Choice window containing a list
of filters.

The filters work in the same manner as in FileDialog.

"""


class TestPanel(wx.Panel):
    def __init__(self, parent, log):
        wx.Panel.__init__(self, parent, -1)

        self.log = log

        txt1 = wx.StaticText(self, -1, "style=0")
        dir1 = wx.GenericDirCtrl(self, -1, size=(200, 225), style=0)

        txt2 = wx.StaticText(self, -1, "wx.DIRCTRL_DIR_ONLY")
        dir2 = wx.GenericDirCtrl(self, -1, size=(200, 225), style=wx.DIRCTRL_DIR_ONLY)

        txt3 = wx.StaticText(self, -1, "wx.DIRCTRL_SHOW_FILTERS\nwx.DIRCTRL_3D_INTERNAL\nwx.DIRCTRL_MULTIPLE")
        dir3 = wx.GenericDirCtrl(self, -1, size=(200, 225),
                                 style=wx.DIRCTRL_SHOW_FILTERS |
                                       wx.DIRCTRL_3D_INTERNAL |
                                       wx.DIRCTRL_MULTIPLE,
                                 filter="All files (*.*)|*.*|Python files (*.py)|*.py")

        sz = wx.FlexGridSizer(cols=3, hgap=5, vgap=5)
        sz.Add((35, 35))  # some space above
        sz.Add((35, 35))
        sz.Add((35, 35))

        sz.Add(txt1)
        sz.Add(txt2)
        sz.Add(txt3)

        sz.Add(dir1, 0, wx.EXPAND)
        sz.Add(dir2, 0, wx.EXPAND)
        sz.Add(dir3, 0, wx.EXPAND)

        sz.Add((35,35))  # some space below

        sz.AddGrowableRow(2)
        sz.AddGrowableCol(0)
        sz.AddGrowableCol(1)
        sz.AddGrowableCol(2)

        self.SetSizer(sz)
        self.SetAutoLayout(True)


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