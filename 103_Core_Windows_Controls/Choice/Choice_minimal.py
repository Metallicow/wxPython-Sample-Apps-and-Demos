#!/usr/bin/env python

#-Imports---------------------------------------------------------------------

#--wxPython Imports.
import wx


if __name__ == '__main__':
    app = wx.App()
    frame = wx.Frame(None, -1, 'Minimal CheckListBox Demo')
    sampleList1 = ['zero', 'one', 'two', 'three', 'four', 'five', 'six',
                   'seven', 'eight', 'nine', 'ten']
    sampleList2 = ['Choice %d' % i for i in range(100)]
    c1 = wx.Choice(frame, -1, choices=sampleList1, pos=(20, 20))
    c1.Select(3)
    c2 = wx.Choice(frame, -1, choices=sampleList2, pos=(20, 60))
    c2.Select(0)
    frame.CreateStatusBar().SetStatusText('wxPython %s' % wx.version())
    frame.Show()
    app.MainLoop()
