#!/usr/bin/env python

#-Imports---------------------------------------------------------------------

#--wxPython Imports.
import wx


if __name__ == '__main__':
    app = wx.App()
    frame = wx.Frame(None, wx.ID_ANY, "Minimal SearchCtrl Demo")

    search1 = wx.SearchCtrl(frame)

    search2 = wx.SearchCtrl(frame)
    search2.SetDescriptiveText("Set Descriptive Text")
    search2.ShowSearchButton(True)
    search2.ShowCancelButton(True)

    vbSizer = wx.BoxSizer(wx.VERTICAL)
    vbSizer.Add(search1, 0, wx.EXPAND | wx.ALL, 15)
    vbSizer.Add(search2, 0, wx.EXPAND | wx.ALL, 15)
    frame.SetSizer(vbSizer)

    frame.CreateStatusBar().SetStatusText('wxPython %s' % wx.version())
    frame.Show()
    app.MainLoop()
