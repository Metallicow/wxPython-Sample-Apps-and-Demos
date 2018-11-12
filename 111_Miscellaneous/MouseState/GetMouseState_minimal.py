#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-Imports.--------------------------------------------------------------------

#--wxPython Imports.
import wx

if __name__ == '__main__':
    def OnMouseEvents(event):
        evtObj = event.GetEventObject()
        ms = wx.GetMouseState()
        print(ms.GetX(), ms.GetY())
        print('LeftIsDown = %s' % ms.LeftIsDown())
        print('MiddleIsDown = %s' % ms.MiddleIsDown())
        print('RightIsDown = %s' % ms.RightIsDown())
        ## print('AltDown = %s' % ms.AltDown())
        ## print('ControlDown = %s' % ms.ControlDown())
        ## print('ShiftDown = %s' % ms.ShiftDown())
        ## print('MetaDown = %s' % ms.MetaDown())
        print('')

    app = wx.App()
    frame = wx.Frame(None, -1, 'Minimal GraphicsContext Demo')
    panel = wx.Panel(frame, wx.ID_ANY)
    panel.Bind(wx.EVT_MOUSE_EVENTS, OnMouseEvents)
    frame.CreateStatusBar().SetStatusText('wxPython %s' % wx.version())
    frame.Show()
    app.MainLoop()
