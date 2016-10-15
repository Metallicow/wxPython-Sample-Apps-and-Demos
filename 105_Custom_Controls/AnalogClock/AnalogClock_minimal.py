#!/usr/bin/env python

#-Imports---------------------------------------------------------------------

#--wxPython Imports.
import wx
import wx.lib.analogclock as ac

if __name__ == '__main__':
    app = wx.App()
    frame = wx.Frame(None, -1, 'Minimal AnalogClock Demo')
    clock = ac.AnalogClock(frame, size=(200, 200))
    frame.CreateStatusBar().SetStatusText('wxPython %s' % wx.version())
    frame.Show()
    app.MainLoop()
