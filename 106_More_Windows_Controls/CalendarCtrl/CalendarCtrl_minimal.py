#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-Imports---------------------------------------------------------------------

#--wxPython Imports.
import wx
import wx.adv


if __name__ == '__main__':
    app = wx.App()
    frame = wx.Frame(None, -1, 'Minimal CalendarCtrl Demo')
    cal = wx.adv.CalendarCtrl(frame, -1, wx.DateTime().Today(),
                              style=wx.adv.CAL_SEQUENTIAL_MONTH_SELECTION)
    frame.Show()
    app.MainLoop()
