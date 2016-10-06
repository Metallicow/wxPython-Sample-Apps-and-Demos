#!/usr/bin/env python

#-Imports---------------------------------------------------------------------

#--wxPython Imports.
import wx


if __name__ == '__main__':
    app = wx.App()
    frame = wx.Frame(None, wx.ID_ANY, "Minimal ToggleButton Demo")

    togBtn1 = wx.ToggleButton(frame, -1, 'ToggleButton 1', pos=(20, 20))
    togBtn2 = wx.ToggleButton(frame, -1, 'ToggleButton 2', pos=(20, 60))

    frame.CreateStatusBar().SetStatusText('wxPython %s' % wx.version())
    frame.Show()
    app.MainLoop()
