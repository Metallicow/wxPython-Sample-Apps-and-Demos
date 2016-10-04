#!/usr/bin/env python

#-Imports.--------------------------------------------------------------------

#--wxPython Imports.
import wx


if __name__ == '__main__':
    app = wx.App()
    frame = wx.Frame(None, wx.ID_ANY, 'Minimal CheckBox Demo')
    panel = wx.Panel(frame, wx.ID_ANY)
    cb = wx.CheckBox(panel, wx.ID_ANY, 'wx.CheckBox', pos=(20, 20))
    frame.CreateStatusBar().SetStatusText('wxPython %s' % wx.version())
    frame.Show()
    app.MainLoop()
