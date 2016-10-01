#!/usr/bin/env python

#-Imports.---------------------------------------------------------------------

#--wxPython Imports.
import wx

if __name__ == '__main__':
    app = wx.App()
    miniframe = wx.MiniFrame(None, -1, 'Minimal MiniFrame Demo',
                             style=wx.DEFAULT_FRAME_STYLE)
    miniframe.Show()
    app.MainLoop()
