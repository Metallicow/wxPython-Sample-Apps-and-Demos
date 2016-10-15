#!/usr/bin/env python

#-Imports---------------------------------------------------------------------

#--wxPython Imports.
import wx
import wx.lib.colourselect as csel

if __name__ == '__main__':
    app = wx.App()
    frame = wx.Frame(None, -1, 'Minimal ColourSelect Demo')
    coloursel1 = csel.ColourSelect(frame, -1, colour=wx.RED, pos=(50, 50))
    coloursel2 = csel.ColourSelect(frame, -1, label='ColourSelect', colour=wx.BLUE, pos=(100, 100))
    frame.CreateStatusBar().SetStatusText('wxPython %s' % wx.version())
    frame.Show()
    app.MainLoop()
