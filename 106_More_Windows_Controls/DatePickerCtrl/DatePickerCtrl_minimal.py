#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-Imports----------------------------------------------------------------------

#--wxPython Imports.
import wx
import wx.adv


if __name__ == '__main__':
    app = wx.App()
    frame = wx.Frame(None, -1, 'Minimal DatePickerCtrl Demo')
    panel = wx.Panel(frame)
    dpc = wx.adv.DatePickerCtrl(panel, size=(120, -1), pos=(10, 10),
                            style = wx.adv.DP_DROPDOWN
                                  | wx.adv.DP_SHOWCENTURY
                                  | wx.adv.DP_ALLOWNONE )
    frame.CreateStatusBar().SetStatusText('wxPython %s' % wx.version())
    frame.Show()
    app.MainLoop()
