#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-Imports---------------------------------------------------------------------

#--wxPython Imports.
import wx


class TestPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, wx.ID_ANY)

        cp = wx.CollapsiblePane(self, label='wx.CollapsiblePane',
                                style=wx.CP_DEFAULT_STYLE | wx.CP_NO_TLW_RESIZE)
        tc  = wx.TextCtrl(cp.GetPane(), wx.ID_ANY, "testing text")

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(cp, 0, wx.ALL | wx.EXPAND, 25)
        self.SetSizer(sizer)


if __name__ == '__main__':
    import sys
    print('Python %s.%s.%s %s' % sys.version_info[0:4])
    print('wxPython %s' % wx.version())
    app = wx.App()
    frame = wx.Frame(None, -1, 'wx.CollapsiblePane Demo')
    pnl = TestPanel(frame)
    frame.Show()
    app.MainLoop()
