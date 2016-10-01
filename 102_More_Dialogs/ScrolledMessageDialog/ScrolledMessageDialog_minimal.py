#!/usr/bin/env python

#-Imports---------------------------------------------------------------------

#--wxPython Imports.
import wx
import wx.lib.dialogs


if __name__ == '__main__':
    app = wx.App()

    message = "I'm a ScrolledMessageDialog.\n\n" * 10
    dlg = wx.lib.dialogs.ScrolledMessageDialog(None,
            message, "Minimal ScrolledMessageDialog Demo")
    dlg.ShowModal()
    dlg.Destroy()

    app.MainLoop()
