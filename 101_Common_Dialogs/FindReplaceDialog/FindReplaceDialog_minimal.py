#!/usr/bin/env python

#-Imports---------------------------------------------------------------------

#--wxPython Imports.
import wx


if __name__ == '__main__':
    app = wx.App()

    frame = wx.Frame(None, wx.ID_ANY, 'Minimal FindReplaceDialog Demo')
    dlg = wx.FindReplaceDialog(frame, wx.FindReplaceData(),
                               "Find & Replace", wx.FR_REPLACEDIALOG)
    dlg.Show(True)
    def OnClose(event):
        frame.Close(True)
    dlg.Bind(wx.EVT_FIND_CLOSE, OnClose)

    app.MainLoop()
