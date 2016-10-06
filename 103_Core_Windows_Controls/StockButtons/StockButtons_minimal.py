#!/usr/bin/env python

#-Imports---------------------------------------------------------------------

#--wxPython Imports.
import wx


if __name__ == '__main__':
    app = wx.App()
    frame = wx.Frame(None, wx.ID_ANY, "Minimal StockButtons Demo")

    gSizer = wx.GridSizer(cols=5, hgap=4, vgap=4)
    for i in dir(wx):
        if 'ID_' in i:
            print(i)
            try:
                execStr = "stockBtn = wx.Button(frame, wx.%s)" % i
                exec(execStr)
                if not stockBtn.GetLabel(): # Not a supported Stock ID.
                    stockBtn.Destroy()
                    continue
                stockBtn.SetToolTip(wx.ToolTip('wx.%s' % i))
                gSizer.Add(stockBtn)
            except Exception:
                pass
    frame.SetSizerAndFit(gSizer)

    frame.CreateStatusBar().SetStatusText('wxPython %s' % wx.version())
    frame.Show()
    app.MainLoop()
