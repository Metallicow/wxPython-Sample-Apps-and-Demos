#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-Imports----------------------------------------------------------------------

#--wxPython Imports.
import  wx


if __name__ == '__main__':
    app = wx.App()
    frame = wx.Frame(None, wx.ID_ANY, "Minimal SpinCtrl Demo")

    def OnSpin(event):
        spinctrl = event.GetEventObject()
        print('OnSpin: %d\n' % spinctrl.GetValue())

    def OnText(event):
        spinctrl = event.GetEventObject()
        print('OnText: %d\n' % spinctrl.GetValue())

    spinctrl = wx.SpinCtrl(frame, wx.ID_ANY, "", (30, 50))
    spinctrl.SetRange(1, 100)
    spinctrl.SetValue(5)

    spinctrl.Bind(wx.EVT_SPINCTRL, OnSpin)
    spinctrl.Bind(wx.EVT_TEXT, OnText)

    frame.CreateStatusBar().SetStatusText('wxPython %s' % wx.version())
    frame.Show()
    app.MainLoop()