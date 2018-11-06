#!/usr/bin/env python

#-Imports---------------------------------------------------------------------

#--wxPython Imports.
import wx
import wx.adv

if __name__ == '__main__':
    app = wx.App()
    frame = wx.Frame(None, -1, 'Minimal BitmapComboBox Demo')
    panel = wx.Panel(frame)
    bcb = wx.adv.BitmapComboBox(panel, pos=(10, 10), size=(200, -1))

    for name in dir(wx):
        if name.startswith('ART_'):
            id = eval('wx.%s' % name)
            bmp = wx.ArtProvider.GetBitmap(id, wx.ART_OTHER, (16, 16))
            bcb.Append('wx.%s' % name, bmp, name)

    frame.CreateStatusBar().SetStatusText('wxPython %s' % wx.version())
    frame.Show()
    app.MainLoop()
