#!/usr/bin/env python

#-Imports---------------------------------------------------------------------

#--wxPython Imports.
import wx


if __name__ == '__main__':
    app = wx.App()
    frame = wx.Frame(None, -1, 'Minimal BitmapButton Demo - wxPython %s' % wx.version())
    bmp = wx.Bitmap('bitmaps/phoenix32.png', wx.BITMAP_TYPE_PNG)
    bmpBtn1 = wx.BitmapButton(frame, -1, bmp, pos=(32, 32))
    bmpBtn2 = wx.BitmapButton(frame, -1, bmp, pos=(128, 32))
    frame.Show()
    app.MainLoop()
