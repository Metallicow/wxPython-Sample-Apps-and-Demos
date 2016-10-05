#!/usr/bin/env python

#-Imports---------------------------------------------------------------------

#--wxPython Imports.
import wx


if __name__ == '__main__':
    app = wx.App()
    frame = wx.Frame(None, wx.ID_ANY, "Minimal RadioButton Demo")

    radio1 = wx.RadioButton(frame, -1, " Radio1 ", pos=(20, 20), style=wx.RB_GROUP)
    radio2 = wx.RadioButton(frame, -1, " Radio2 ", pos=(20, 40))
    radio3 = wx.RadioButton(frame, -1, " Radio3 ", pos=(20, 60))

    frame.CreateStatusBar().SetStatusText('wxPython %s' % wx.version())
    frame.Show()
    app.MainLoop()
