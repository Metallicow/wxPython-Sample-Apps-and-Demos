#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-Imports----------------------------------------------------------------------

#--wxPython Imports.
import wx


#- wxPython Demo --------------------------------------------------------------
__wxPyOnlineDocs__ = 'http://wxpython.org/Phoenix/docs/html/SingleChoiceDialog.html'
__wxPyDemoPanel__ = 'TestPanel'

overview = """\
This class represents a dialog that shows a list of strings, and allows the user
to select one. Double-clicking on a list item is equivalent to single-clicking
and then pressing OK.

As with all dialogs, be sure to retrieve the information you need BEFORE you
destroy the dialog.
"""

class TestPanel(wx.Panel):
    def __init__(self, parent, log):
        self.log = log
        wx.Panel.__init__(self, parent, -1)

        b = wx.Button(self, -1, "Create and Show a SingleChoiceDialog", (50,50))
        self.Bind(wx.EVT_BUTTON, self.OnButton, b)


    def OnButton(self, evt):
        dlg = wx.SingleChoiceDialog(
                self, 'Test Single Choice', 'The Caption',
                ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight'],
                wx.CHOICEDLG_STYLE
                )

        if dlg.ShowModal() == wx.ID_OK:
            self.log.WriteText('You selected: %s\n' % dlg.GetStringSelection())

        dlg.Destroy()


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
