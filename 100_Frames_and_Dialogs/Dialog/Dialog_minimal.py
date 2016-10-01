#!/usr/bin/env python

#-Imports---------------------------------------------------------------------

#--wxPython Imports.
import wx

if __name__ == '__main__':
    gApp = wx.App(False)
    dlg = wx.Dialog(None, wx.ID_ANY, "Minimal Dialog Demo")
    dlg.ShowModal()
    dlg.Destroy()
    gApp.MainLoop()
