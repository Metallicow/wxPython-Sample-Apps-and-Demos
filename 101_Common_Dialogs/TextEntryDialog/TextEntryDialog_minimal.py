#!/usr/bin/env python

#-Imports---------------------------------------------------------------------

#--wxPython Imports.
import wx


if __name__ == '__main__':
    app = wx.App()

    dlg = wx.TextEntryDialog(None,
            'What is your favorite programming language?',
            'Eh??', 'Python')
    dlg.SetValue("Python is the best!")
    if dlg.ShowModal() == wx.ID_OK:
        print(dlg.GetValue())
    dlg.Destroy()

    app.MainLoop()
