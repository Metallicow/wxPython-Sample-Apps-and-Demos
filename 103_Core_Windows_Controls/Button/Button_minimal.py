#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-Imports.--------------------------------------------------------------------

#--wxPython Imports.
import wx

if __name__ == '__main__':
    def OnButton(event):
        print('Button clicked!')

    app = wx.App()
    frame = wx.Frame(None, -1, 'Minimal Button Demo')
    frame.button = wx.Button(frame, -1, 'I am a wx.Button')
    frame.button.Bind(wx.EVT_BUTTON, OnButton)
    frame.CreateStatusBar().SetStatusText('wxPython %s' % wx.version())
    frame.Show()
    app.MainLoop()
