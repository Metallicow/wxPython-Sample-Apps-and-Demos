#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-Imports----------------------------------------------------------------------

#--wxPython Imports.
import wx


#- wxPython Demo --------------------------------------------------------------
__wxPyOnlineDocs__ = 'http://wxpython.org/Phoenix/docs/html/StockButtons.html'
__wxPyDemoPanel__ = 'TestPanel'

overview = """<html><body>
<h2><center>Stock Buttons</center></h2>

It is now possible to create \"stock\" buttons.  Basically this means
that you only have to provide one of the stock IDs (and an empty
label) when creating the button and wxWidgets will choose the stock
label to go with it automatically.  Additionally on the platforms that
have a native concept of a stock button (currently only GTK2) then the
native stock button will be used.

<p>This sample shows buttons for all of the currently available stock
IDs.  Notice that when the button is created that no label is given,
and compare that with the button that is created.

</body></html>
"""


class TestPanel(wx.ScrolledWindow):
    def __init__(self, parent, log):
        self.log = log
        wx.ScrolledWindow.__init__(self, parent, -1)

        fgSizer = wx.FlexGridSizer(cols=5, hgap=4, vgap=4)

        for i in dir(wx):
            if 'ID_' in i:
                print(i)
                try:
                    stockBtn = wx.Button(self, eval('wx.%s' % i))
                    if not stockBtn.GetLabel(): # Not a supported Stock ID.
                        stockBtn.Destroy()
                        continue
                    stockBtn.SetToolTip(wx.ToolTip('wx.%s' % i))
                    fgSizer.Add(stockBtn)
                except Exception:
                    pass

        self.SetSizer(fgSizer)

        self.SetScrollRate(20, 20)


#- wxPy Demo -----------------------------------------------------------------


def runTest(frame, nb, log):
    win = TestPanel(nb, log)
    return win


#- __main__ Demo --------------------------------------------------------------


class printLog:
    def __init__(self):
        pass

    def write(self, txt):
        print('%s' % txt)

    def WriteText(self, txt):
        print('%s' % txt)


class TestFrame(wx.Frame):
    def __init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString,
                 pos=wx.DefaultPosition, size=wx.DefaultSize,
                 style=wx.DEFAULT_FRAME_STYLE, name='frame'):
        wx.Frame.__init__(self, parent, id, title, pos, size, style, name)

        log = printLog()

        panel = TestPanel(self, log)
        self.Bind(wx.EVT_CLOSE, self.OnDestroy)


    def OnDestroy(self, event):
        self.Destroy()


class TestApp(wx.App):
    def OnInit(self):
        gMainWin = TestFrame(None)
        gMainWin.SetTitle('Test Demo')
        gMainWin.Show()

        return True


#- __main__ -------------------------------------------------------------------


if __name__ == '__main__':
    import sys
    print('Python %s.%s.%s %s' % sys.version_info[0:4])
    print('wxPython %s' % wx.version())
    gApp = TestApp(redirect=False,
                   filename=None,
                   useBestVisual=False,
                   clearSigInt=True)
    gApp.MainLoop()
