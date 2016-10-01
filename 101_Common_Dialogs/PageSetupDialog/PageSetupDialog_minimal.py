#!/usr/bin/env python

#-Imports---------------------------------------------------------------------

#--wxPython Imports.
import wx


if __name__ == '__main__':
    app = wx.App()

    data = wx.PageSetupDialogData()
    data.SetMarginTopLeft((15, 15))
    data.SetMarginBottomRight((15, 15))
    ## data.SetDefaultMinMargins(True)
    data.SetPaperId(wx.PAPER_LETTER)

    dlg = wx.PageSetupDialog(None, data)

    if dlg.ShowModal() == wx.ID_OK:
        data = dlg.GetPageSetupData()
        tl = data.GetMarginTopLeft()
        br = data.GetMarginBottomRight()
        print('Margins are: %s %s\n' % (str(tl), str(br)))

    dlg.Destroy()

    app.MainLoop()
