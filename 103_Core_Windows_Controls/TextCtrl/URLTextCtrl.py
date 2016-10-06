#!/usr/bin/env python
# -*- coding: utf-8 -*-


#-Imports.---------------------------------------------------------------------

#--Python Imports.
import webbrowser

#--wxPython Imports.
import wx

urls = """
http://www.python.org/

http://wxpython.org/

http://micropython.org/

http://www.scintilla.org/

"""

class MyTextCtrl(wx.TextCtrl):
    def __init__(self, parent, id=wx.ID_ANY, value=wx.EmptyString,
                 pos=wx.DefaultPosition, size=wx.DefaultSize,
                 style=wx.TE_MULTILINE | wx.TE_AUTO_URL,
                 val=wx.DefaultValidator, name='textCtrl'):
        """Default class constructor."""
        wx.TextCtrl.__init__(self, parent, id, value, pos, size, style, val, name)

        self.SetValue(urls)
        self.BindEvents()


    def BindEvents(self):
        self.Bind(wx.EVT_TEXT_URL, self.OnTextURL)

    def OnTextURL(self, event):
        ## print('OnTextURL')
        if event.MouseEvent.LeftUp():
            ## print('OnTextURL LeftUp %s' % url)
            url = self.GetRange(event.GetURLStart(), event.GetURLEnd())
            webbrowser.open_new_tab(url)
        event.Skip()


class MyTestFrame(wx.Frame):
    def __init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString,
                 pos=wx.DefaultPosition, size=wx.DefaultSize,
                 style=wx.DEFAULT_FRAME_STYLE, name='frame'):
        wx.Frame.__init__(self, parent, id, title, pos, size, style, name)

        urlTextCtrl = MyTextCtrl(self)

        self.Bind(wx.EVT_CLOSE, self.OnDestroy)

    def OnDestroy(self, event):
        self.Destroy()


class TextURLApp(wx.App):
    def OnInit(self):
        gMainWin = MyTestFrame(None)
        gMainWin.SetTitle('Text URL Demo')
        self.SetTopWindow(gMainWin)
        gMainWin.Show()
        return True


if __name__ == '__main__':
    gApp = TextURLApp(redirect=False,
                      filename=None,
                      useBestVisual=False,
                      clearSigInt=True)
    gApp.MainLoop()
