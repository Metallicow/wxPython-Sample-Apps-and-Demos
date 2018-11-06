#!/usr/bin/env python

#-Imports---------------------------------------------------------------------

#--wxPython Imports.
import wx


if __name__ == '__main__':
    app = wx.App()
    frame = wx.Frame(None, wx.ID_ANY, "Minimal RadioBox Demo")

    sampleList = ["True", "False", "None"]
    rb = wx.RadioBox(frame, wx.ID_ANY, "wx.RadioBox", choices=sampleList,
                     majorDimension=3, style=wx.RA_SPECIFY_COLS | wx.NO_BORDER)

    frame.CreateStatusBar().SetStatusText('wxPython %s' % wx.version())
    frame.Show()
    app.MainLoop()
