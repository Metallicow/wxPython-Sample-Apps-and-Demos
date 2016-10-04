#!/usr/bin/env python

#-Imports---------------------------------------------------------------------

#--wxPython Imports.
import wx
import wx.adv

if __name__ == '__main__':
    app = wx.App()
    frame = wx.Frame(None, -1, 'Minimal CommandLinkButton Demo')

    cmd = wx.adv.CommandLinkButton(frame, -1, "wx.CommandLinkButton",
                 """\
This type of button includes both a main label and a 'note' that is meant to
contain a description of what the button does or what it is used for.  On
Windows 7 it is a new native widget type, on the other platforms it is
implemented generically.""", pos=(25,25))

    frame.CreateStatusBar().SetStatusText('wxPython %s' % wx.version())
    frame.Show()
    app.MainLoop()
