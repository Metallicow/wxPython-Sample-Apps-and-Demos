#!/usr/bin/env python

#-Imports---------------------------------------------------------------------

#--wxPython Imports.
import wx


if __name__ == '__main__':
    app = wx.App()

    dlg = wx.DirDialog(None, "Choose a directory:")
    if dlg.ShowModal() == wx.ID_OK:
        print('%s' % dlg.GetPath())
    dlg.Destroy()

    app.MainLoop()
