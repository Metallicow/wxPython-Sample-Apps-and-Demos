#!/usr/bin/env python

#-Imports---------------------------------------------------------------------

#--wxPython Imports.
import wx


if __name__ == '__main__':
    app = wx.App()
    frame = wx.Frame(None, -1, 'Minimal CheckListBox Demo')
    sampleList = ['zero', 'one', 'two', 'three', 'four', 'five', 'six',
                  'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
                  'thirteen', 'fourteen']
    clb = wx.CheckListBox(frame, -1, choices=sampleList)
    frame.CreateStatusBar().SetStatusText('wxPython %s' % wx.version())
    frame.Show()
    app.MainLoop()
