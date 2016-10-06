#!/usr/bin/env python

#-Imports---------------------------------------------------------------------

#--wxPython Imports.
import wx


if __name__ == '__main__':
    app = wx.App()
    frame = wx.Frame(None, wx.ID_ANY, "Minimal TextCtrl Demo")

    tc = wx.TextCtrl(frame, wx.ID_ANY, "I'm a wx.TextCtrl",
                     style=wx.TE_MULTILINE | wx.TE_RICH)

    frame.CreateStatusBar().SetStatusText('wxPython %s' % wx.version())
    frame.Show()
    app.MainLoop()
