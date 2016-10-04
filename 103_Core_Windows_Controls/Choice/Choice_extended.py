#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-Imports----------------------------------------------------------------------

#--wxPython Imports.
import wx


#- wxPython Demo --------------------------------------------------------------

__wxPyOnlineDocs__ = 'http://wxpython.org/Phoenix/docs/html/Choice.html'
__wxPyDemoPanel__ = 'TestPanel'

overview = """
A Choice control is used to select one of a list of strings. Unlike a listbox,
only the current selection is visible until the user pulls down the menu of
choices.

This demo illustrates how to set up the Choice control and how to extract the
selected choice once it is selected.

Note that the syntax of the constructor is different than the C++ implementation.
The number of choices and the choice array are consilidated into one python
<code>list</code>.
"""


class TestPanel(wx.Panel):
    def __init__(self, parent, log):
        self.log = log
        wx.Panel.__init__(self, parent, -1)

        sampleList = ['zero', 'one', 'two', 'three', 'four', 'five',
                      'six', 'seven', 'eight']

        wx.StaticText(self, -1, "This example uses the wxChoice control.", (15, 10))
        wx.StaticText(self, -1, "Select one:", (15, 50), (75, -1))
        self.ch = wx.Choice(self, -1, (100, 50), choices=sampleList)
        self.Bind(wx.EVT_CHOICE, self.EvtChoice, self.ch)


    def EvtChoice(self, event):
        self.log.WriteText('EvtChoice: %s\n' % event.GetString())
        self.ch.Append("A new item")

        if event.GetString() == 'one':
            self.log.WriteText('Well done!\n')


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
