#!/usr/bin/env python

#-Imports---------------------------------------------------------------------

#--wxPython Imports.
import wx


if __name__ == '__main__':
    app = wx.App()
    frame = wx.Frame(None, wx.ID_ANY, "Minimal Gauge Demo")

    gauge1 = wx.Gauge(frame, wx.ID_ANY, 100, pos=(20, 20), size=(250, 25))
    gauge1.SetValue(20)

    gauge2 = wx.Gauge(frame, wx.ID_ANY, 50, pos=(20, 60), size=(250, 25))
    gauge2.Pulse()

    frame.CreateStatusBar().SetStatusText('wxPython %s' % wx.version())
    frame.Show()
    app.MainLoop()
