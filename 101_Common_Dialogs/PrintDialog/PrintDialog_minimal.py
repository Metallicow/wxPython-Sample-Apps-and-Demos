#!/usr/bin/env python

#-Imports---------------------------------------------------------------------

#--wxPython Imports.
import wx


if __name__ == '__main__':
    app = wx.App()

    data = wx.PrintDialogData()

    data.EnableSelection(True)
    data.EnablePrintToFile(True)
    data.EnablePageNumbers(True)
    data.SetMinPage(1)
    data.SetMaxPage(5)
    ## data.SetAllPages(True)

    dlg = wx.PrintDialog(None, data)

    if dlg.ShowModal() == wx.ID_OK:
        data = dlg.GetPrintDialogData()
        print('GetAllPages: %d\n' % data.GetAllPages())

    dlg.Destroy()

    app.MainLoop()
