#!/usr/bin/env python

#-Imports---------------------------------------------------------------------

#--wxPython Imports.
import wx


if __name__ == '__main__':
    app = wx.App()

    frame = wx.Frame(None, wx.ID_ANY, 'Minimal FontEnumerator Demo',
                     size=(400, 550))

    fontEnum = wx.FontEnumerator()
    fontEnum.EnumerateFacenames()
    list = sorted(fontEnum.GetFacenames())

    tc = wx.TextCtrl(frame, wx.ID_ANY, '', style=wx.TE_MULTILINE | wx.TE_RICH)
    l = 0
    nc = wx.NullColour
    for facename in list:
        lenFace = len(facename)
        tc.AppendText(u'%s\n' % facename)
        f = wx.Font(14,
                    wx.FONTFAMILY_DEFAULT,
                    wx.FONTSTYLE_NORMAL,
                    wx.FONTWEIGHT_NORMAL,
                    False, facename)
        tc.SetStyle(l, l + lenFace + 1, wx.TextAttr(nc, nc, f))
        l = l + lenFace + 1
    tc.SetInsertionPoint(0)
    tc.SetForegroundColour(wx.BLACK)

    frame.CreateStatusBar().SetStatusText('wxPython %s' % wx.version())
    frame.Show()
    app.MainLoop()
