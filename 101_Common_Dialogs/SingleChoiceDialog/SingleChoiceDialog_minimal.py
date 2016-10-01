#!/usr/bin/env python

#-Imports---------------------------------------------------------------------

#--wxPython Imports.
import wx


if __name__ == '__main__':
    app = wx.App()

    dlg = wx.SingleChoiceDialog(None,
            'Minimal SingleChoiceDialog Demo', 'The Caption',
            ['zero', 'one', 'two', 'three', 'four', 'five',
             'six', 'seven', 'eight', 'nine', 'ten'],
            wx.CHOICEDLG_STYLE
            )
    if dlg.ShowModal() == wx.ID_OK:
        print(dlg.GetStringSelection())
    dlg.Destroy()

    app.MainLoop()
