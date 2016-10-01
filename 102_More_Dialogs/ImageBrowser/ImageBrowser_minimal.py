#!/usr/bin/env python

#-Imports.--------------------------------------------------------------------

#--wxPython Imports.
import wx
import wx.lib.imagebrowser as IB


if __name__ == '__main__':
    app = wx.App(False)

    dlg = IB.ImageDialog(None)
    dlg.Centre()
    if dlg.ShowModal() == wx.ID_OK:
        print("You Selected File: " + dlg.GetFile())
    else:
        print("You pressed Cancel")
    dlg.Destroy()

    app.MainLoop()
