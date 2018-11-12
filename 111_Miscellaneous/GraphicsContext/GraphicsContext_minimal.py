#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-Imports.--------------------------------------------------------------------

#--wxPython Imports.
import wx

if __name__ == '__main__':
    def OnPaint(event):
        evtObj = event.GetEventObject()
        dc = wx.PaintDC(evtObj)
        gc = wx.GraphicsContext.Create(dc)
        gc.SetBrush(wx.Brush((0, 0, 0, 128), wx.BRUSHSTYLE_SOLID))
        gc.SetPen(wx.Pen((255, 0, 0, 128), 3, wx.PENSTYLE_SOLID))
        gc.DrawRectangle(10, 10, 100, 100)

    app = wx.App()
    frame = wx.Frame(None, -1, 'Minimal GraphicsContext Demo')
    panel = wx.Panel(frame, wx.ID_ANY)
    panel.Bind(wx.EVT_PAINT, OnPaint)
    frame.CreateStatusBar().SetStatusText('wxPython %s' % wx.version())
    frame.Show()
    app.MainLoop()
