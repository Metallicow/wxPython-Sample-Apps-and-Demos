#!/usr/bin/env python

#-Imports---------------------------------------------------------------------

#--wxPython Imports.
import wx


if __name__ == '__main__':
    app = wx.App()

    dlg = wx.ColourDialog(None)
    if dlg.ShowModal() == wx.ID_OK:
        print('%s' % str(dlg.GetColourData().GetColour().Get()))
    dlg.Destroy()

    app.MainLoop()
