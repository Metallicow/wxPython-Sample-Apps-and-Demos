#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-Imports----------------------------------------------------------------------

#--wxPython Imports.
import wx


#- wxPython Demo --------------------------------------------------------------

__wxPyOnlineDocs__ = 'https://wxpython.org/Phoenix/docs/html/wx.FontEnumerator.html'
__wxPyDemoPanel__ = 'TestPanel'

overview = """<html><body>
wxFontEnumerator enumerates either all available fonts on the system or only
the ones with given attributes - either only fixed-width (suited for use in
programs such as terminal emulators and the like) or the fonts available in
the given encoding.
</body></html>
"""


class TestPanel(wx.Panel):
    def __init__(self, parent, log):
        wx.Panel.__init__(self, parent, -1)

        fontEnum = wx.FontEnumerator()
        fontEnum.EnumerateFacenames()
        list = fontEnum.GetFacenames()

        list = sorted(list)

        s1 = wx.StaticText(self, -1, "Face names:")

        self.lb1 = wx.ListBox(self, -1, wx.DefaultPosition, (200, 250),
                             list, wx.LB_SINGLE)

        self.Bind(wx.EVT_LISTBOX, self.OnSelect, id=self.lb1.GetId())

        self.txt = wx.StaticText(self, -1, "Sample text...", (285, 50))

        row = wx.BoxSizer(wx.HORIZONTAL)
        row.Add(s1, 0, wx.ALL, 5)
        row.Add(self.lb1, 0, wx.ALL, 5)
        row.Add(self.txt, 0, wx.ALL|wx.ADJUST_MINSIZE, 5)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(row, 0, wx.ALL, 30)
        self.SetSizer(sizer)
        self.Layout()

        self.lb1.SetSelection(0)
        self.OnSelect(None)
        wx.CallLater(300, self.SetTextSize)


    def SetTextSize(self):
        self.txt.SetSize(self.txt.GetBestSize())

    def OnSelect(self, event):
        face = self.lb1.GetStringSelection()
        font = wx.Font(28,
                       wx.FONTFAMILY_DEFAULT,
                       wx.FONTSTYLE_NORMAL,
                       wx.FONTWEIGHT_NORMAL,
                       False, face)
        self.txt.SetLabel(face)
        self.txt.SetFont(font)
        if wx.Platform == "__WXMAC__":
            self.Refresh()

##         st = font.GetNativeFontInfo().ToString()
##         ni2 = wx.NativeFontInfo()
##         ni2.FromString(st)
##         font2 = wx.FontFromNativeInfo(ni2)


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
