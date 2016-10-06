#!/usr/bin/env python

#-Imports----------------------------------------------------------------------

#--wxPython Imports.
import wx


if __name__ == '__main__':
    app = wx.App()
    frame = wx.Frame(None, wx.ID_ANY, "Minimal StaticBimap Demo")

    bmp = wx.Bitmap('bitmaps/robin.jpg')
    statBmp = wx.StaticBitmap(frame, -1, bmp)

    frame.CreateStatusBar().SetStatusText('wxPython %s' % wx.version())
    frame.Show()
    app.MainLoop()
