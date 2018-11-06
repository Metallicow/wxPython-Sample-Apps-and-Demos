#!/usr/bin/env python

#-Imports---------------------------------------------------------------------

#--wxPython Imports.
import wx


if __name__ == '__main__':
    app = wx.App()

    lst = ['apple', 'pear', 'banana', 'coconut', 'orange', 'grape', 'peach',
           'pineapple', 'blueberry', 'raspberry', 'blackberry', 'strawberry',
           'apricot', 'mango', 'gooseberry']
    dlg = wx.MultiChoiceDialog(None,
                               "Pick some fruit from this list...",
                               "wx.MultiChoiceDialog", sorted(lst))
    if dlg.ShowModal() == wx.ID_OK:
        print(dlg.GetSelections())
    dlg.Destroy()

    app.MainLoop()
