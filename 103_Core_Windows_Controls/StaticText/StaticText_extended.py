#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-Imports----------------------------------------------------------------------

#--wxPython Imports.
import wx

USE_GENERIC = 0

if USE_GENERIC:
    from wx.lib.stattext import GenStaticText as StaticText
else:
    StaticText = wx.StaticText


#- wxPython Demo --------------------------------------------------------------
__wxPyOnlineDocs__ = 'http://wxpython.org/Phoenix/docs/html/StaticText.html'
__wxPyDemoPanel__ = 'TestPanel'

overview = """<html><body>
<h2><center>wx.StaticText</center></h2>

A StaticText control displays one or more lines of read-only text.

</body></html>
"""


class TestPanel(wx.Panel):
    def __init__(self, parent, log):
        wx.Panel.__init__(self, parent, -1)
        self.log = log
        ##self.SetBackgroundColour("sky blue")

        StaticText(self, -1, "This is an example of static text", (20, 10))
        StaticText(self, -1, "using the wx.StaticText Control.", (20, 30))

        StaticText(
            self, -1, "align left(default)", pos=(20, 70), size=(120, -1)
            ).SetBackgroundColour('Yellow')

        StaticText(
            self, -1, "align center", pos=(160, 70), size=(120, -1),
            style=wx.ALIGN_CENTER).SetBackgroundColour('#FF8000')

        StaticText(
            self, -1, "align right", pos=(300, 70), size=(120, -1),
            style=wx.ALIGN_RIGHT).SetBackgroundColour(wx.RED)

        str = "This is a different font."
        text = StaticText(self, -1, str, pos=(20, 120))
        font = wx.Font(18,
                       wx.FONTFAMILY_SWISS,
                       wx.FONTSTYLE_NORMAL,
                       wx.FONTWEIGHT_NORMAL)
        text.SetFont(font)

        StaticText(self, -1,
                   ("Multi-line wx.StaticText" "\n"
                    "line 2" "\n"
                    "line 3" "\n"
                    "\n"
                    "after empty line"),
                   (20,170))
        StaticText(self, -1,
                   ("Align right multi-line" "\n"
                    "line 2" "\n"
                    "line 3" "\n"
                    "\n"
                    "after empty line"),
                   (220,170), style=wx.ALIGN_RIGHT)


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
