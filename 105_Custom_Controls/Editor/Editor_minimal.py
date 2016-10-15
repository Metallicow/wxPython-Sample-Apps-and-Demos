#!/usr/bin/env python

#-Imports---------------------------------------------------------------------

#--wxPython Imports.
import wx
import wx.lib.editor as editor

if __name__ == '__main__':
    app = wx.App()
    frame = wx.Frame(None, -1, 'Minimal Editor Demo')
    ed = editor.Editor(frame, wx.ID_ANY)
    ed.SetText(['Hello world!'])
    frame.CreateStatusBar().SetStatusText('wxPython %s' % wx.version())
    frame.Show()
    app.MainLoop()
