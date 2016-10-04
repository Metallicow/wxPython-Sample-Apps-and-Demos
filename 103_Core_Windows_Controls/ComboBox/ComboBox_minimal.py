#!/usr/bin/env python

#-Imports---------------------------------------------------------------------

#--wxPython Imports.
import wx


if __name__ == '__main__':
    app = wx.App()
    frame = wx.Frame(None, wx.ID_ANY, "Minimal ComboBox Demo")

    def OnComboBox(event):
        print(event.GetString())

    sampleList = ["Default value", "one", "two", "three", "42", "wxPython",
                  "wx.CB_DROPDOWN", "wx.CB_SORT", "wx.EVT_COMBOBOX",
                  "__init__.py", "@User"]
    cb1 = wx.ComboBox(frame, wx.ID_ANY, "Default value",
                      pos=(20, 20), choices=sampleList,
                      style=wx.CB_DROPDOWN)

    cb2 = wx.ComboBox(frame, wx.ID_ANY, "wx.CB_SORT",
                      pos=(20, 50), choices=sampleList,
                      style=wx.CB_DROPDOWN | wx.CB_SORT)
    cb2.Bind(wx.EVT_COMBOBOX, OnComboBox)

    frame.CreateStatusBar().SetStatusText('wxPython %s' % wx.version())
    frame.Show()
    app.MainLoop()
