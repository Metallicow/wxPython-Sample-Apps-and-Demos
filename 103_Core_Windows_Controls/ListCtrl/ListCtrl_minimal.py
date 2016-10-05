#!/usr/bin/env python

#-Imports---------------------------------------------------------------------

#--wxPython Imports.
import wx


if __name__ == '__main__':
    app = wx.App()
    frame = wx.Frame(None, wx.ID_ANY, "Minimal ListCtrl Demo")

    wxPyVer = wx.version()
    lc = wx.ListCtrl(frame, -1, style=wx.LC_REPORT)
    lc.InsertColumn(0, "ListCtrl")
    lc.InsertColumn(1, "style")
    lc.InsertColumn(2, "wx.version()")
    for i in range(100):
        lc.InsertItem(i, 'InsertItem %d' % i)
        lc.SetItem(i, 1, 'wx.LC_REPORT')
        lc.SetItem(i, 2, 'wxPython ' + wxPyVer)
    lc.SetColumnWidth(0, 100)
    lc.SetColumnWidth(1, 125)
    lc.SetColumnWidth(2, wx.LIST_AUTOSIZE)

    frame.CreateStatusBar().SetStatusText('wxPython %s' % wxPyVer)
    frame.Show()
    app.MainLoop()
