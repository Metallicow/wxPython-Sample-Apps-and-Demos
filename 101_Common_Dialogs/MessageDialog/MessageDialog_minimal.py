#!/usr/bin/env python

#-Imports----------------------------------------------------------------------

#--wxPython Imports.
import wx
import wx.lib.dialogs


if __name__ == '__main__':
    app = wx.App()

    msg = "I'm a MessageDialog   \n\n" * 5
    cap = "MessageDialog Caption"
    sty = wx.ICON_INFORMATION
    dlg = wx.MessageDialog(None, message=msg, caption=cap, style=sty)
    dlg.ShowModal()
    dlg.Destroy()

    app.MainLoop()
