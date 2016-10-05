#!/usr/bin/env python

#-Imports---------------------------------------------------------------------

#--wxPython Imports.
import wx


if __name__ == '__main__':
    app = wx.App()
    frame = wx.Frame(None, wx.ID_ANY, "Minimal Menu Demo")

    def OnClose(event):
        frame.Close(True)

    menuBar = wx.MenuBar()
    menu = wx.Menu()
    menu.Append(wx.ID_EXIT, "&Exit\tCtrl+Q")
    menu.Bind(wx.EVT_MENU, OnClose)
    menuBar.Append(menu, "&File")
    frame.SetMenuBar(menuBar)

    frame.CreateStatusBar().SetStatusText('wxPython %s' % wx.version())
    frame.Show()
    app.MainLoop()
