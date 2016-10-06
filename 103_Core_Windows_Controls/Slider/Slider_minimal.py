#!/usr/bin/env python

#-Imports---------------------------------------------------------------------

#--wxPython Imports.
import wx


if __name__ == '__main__':
    app = wx.App()
    frame = wx.Frame(None, wx.ID_ANY, "Minimal Slider Demo")

    slider = wx.Slider(frame, wx.ID_ANY,
        value=25, minValue=0, maxValue=100,
        style=wx.SL_HORIZONTAL | wx.SL_AUTOTICKS | wx.SL_LABELS)
    slider.SetTickFreq(5)

    frame.CreateStatusBar().SetStatusText('wxPython %s' % wx.version())
    frame.Show()
    app.MainLoop()
