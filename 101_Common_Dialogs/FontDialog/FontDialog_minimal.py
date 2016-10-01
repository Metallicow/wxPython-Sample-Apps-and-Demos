#!/usr/bin/env python

#-Imports---------------------------------------------------------------------

#--wxPython Imports.
import wx


if __name__ == '__main__':
    app = wx.App()

    dlg = wx.FontDialog(None, wx.FontData())

    if dlg.ShowModal() == wx.ID_OK:
        data = dlg.GetFontData()
        font = data.GetChosenFont()
        colour = data.GetColour()
        print('%s' % font.GetFaceName())
        print('%s' % font.GetPointSize())
        print('%s' % colour.Get())
    dlg.Destroy()

    app.MainLoop()
