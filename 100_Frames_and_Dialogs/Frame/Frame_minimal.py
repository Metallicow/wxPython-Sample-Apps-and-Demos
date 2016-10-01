#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-Imports.--------------------------------------------------------------------

#--wxPython Imports.
import wx

if __name__ == '__main__':
    app = wx.App()
    frame = wx.Frame(None, -1, 'Minimal Frame Demo')
    frame.Show()
    app.MainLoop()
