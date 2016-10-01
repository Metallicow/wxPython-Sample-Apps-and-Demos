#!/usr/bin/env python

#-Imports----------------------------------------------------------------------

#--wxPython Imports.
import wx


if __name__ == '__main__':
    app = wx.App()
    frame = wx.Frame(None, wx.ID_ANY, "Minimal Notebook Demo")

    colors = (
        '#F39D76', '#F5B57F', '#F9CD8A', '#FFF99D', '#C7E19D', '#A8D59D',
        '#88C99D', '#8CCCCA', '#8DCFF3', '#93A9D5', '#9595C5', '#9681B6',
        '#AF88B8', '#C78FB9', '#F59FBC', '#F49E9C')
    nb = wx.Notebook(frame, wx.ID_ANY, size=(21, 21), style=wx.BK_DEFAULT)
    for i in range(len(colors)):
        p = wx.Panel(nb, wx.ID_ANY)
        p.SetBackgroundColour(colors[i])
        nb.AddPage(p, 'Page %d' % i)

    frame.CreateStatusBar().SetStatusText('wxPython %s' % wx.version())
    frame.Show()
    app.MainLoop()
