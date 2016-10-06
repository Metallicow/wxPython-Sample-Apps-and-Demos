#!/usr/bin/env python

#-Imports----------------------------------------------------------------------

#--wxPython Imports.
import wx


if __name__ == '__main__':
    app = wx.App()
    frame = wx.Frame(None, wx.ID_ANY, "Minimal StaticBox Demo")

    statBox = wx.StaticBox(frame, -1, "This is a wx.StaticBox")
    statBoxSizer = wx.StaticBoxSizer(statBox, wx.VERTICAL)

    st = wx.StaticText(frame, -1,
            'Controls placed "inside" the StaticBox are really its siblings.')
    statBoxSizer.Add(st, 0, wx.TOP|wx.LEFT, 10)

    border = wx.BoxSizer()
    border.Add(statBoxSizer, 1, wx.EXPAND | wx.ALL, 25)
    frame.SetSizer(border)

    frame.CreateStatusBar().SetStatusText('wxPython %s' % wx.version())
    frame.Show()
    app.MainLoop()
