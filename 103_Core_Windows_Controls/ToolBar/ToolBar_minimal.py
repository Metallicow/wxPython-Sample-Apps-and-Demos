#!/usr/bin/env python

#-Imports---------------------------------------------------------------------

#--wxPython Imports.
import wx


if __name__ == '__main__':
    app = wx.App()
    frame = wx.Frame(None, wx.ID_ANY, "Minimal ToolBar Demo")

    tb = frame.CreateToolBar()
    tb.AddTool(wx.ID_OPEN, "Open",
               wx.Bitmap('bitmaps/new_folder.png'),
               "Open Short Help", wx.ITEM_NORMAL)

    tb.AddTool(wx.ID_SAVE, "Save",
               wx.Bitmap('bitmaps/filesave.png'),
               "Save Short Help", wx.ITEM_NORMAL)
    tb.Realize()

    frame.CreateStatusBar().SetStatusText('wxPython %s' % wx.version())
    frame.Show()
    app.MainLoop()
