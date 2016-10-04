#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-Imports----------------------------------------------------------------------

#--wxPython Imports.
import wx


#- wxPython Demo --------------------------------------------------------------

__wxPyOnlineDocs__ = 'http://wxpython.org/Phoenix/docs/html/CheckListBox.html'
__wxPyDemoPanel__ = 'TestPanel'

overview = """\
A checklistbox is like a Listbox, but allows items to be checked or unchecked rather
than relying on extended selection (e.g. shift-select) to select multiple items in
the list. 

This class is currently implemented under Windows and GTK. 

This demo shows the basic CheckListBox and how to use the SetString method to change
labels dynamically.
"""


class TestPanel(wx.Panel):
    def __init__(self, parent, log):
        wx.Panel.__init__(self, parent, -1)
        self.log = log

        sampleList = ['zero', 'one', 'two', 'three', 'four', 'five',
                      'six', 'seven', 'eight', 'nine', 'ten', 'eleven',
                      'twelve', 'thirteen', 'fourteen']

        wx.StaticText(self, -1, "This example uses the wxCheckListBox control.", (45, 15))

        lb = wx.CheckListBox(self, -1, (80, 50), wx.DefaultSize, sampleList)
        self.Bind(wx.EVT_LISTBOX, self.EvtListBox, lb)
        self.Bind(wx.EVT_CHECKLISTBOX, self.EvtCheckListBox, lb)
        lb.SetSelection(0)
        self.lb = lb

        lb.Bind(wx.EVT_RIGHT_DOWN, self.OnDoHitTest)
        
        pos = lb.GetPosition().x + lb.GetSize().width + 25
        btn = wx.Button(self, -1, "Test SetString", (pos, 50))
        self.Bind(wx.EVT_BUTTON, self.OnTestButton, btn)

    def EvtListBox(self, event):
        self.log.WriteText('EvtListBox: %s\n' % event.GetString())

    def EvtCheckListBox(self, event):
        index = event.GetSelection()
        label = self.lb.GetString(index)
        status = 'un'
        if self.lb.IsChecked(index):
            status = ''
        self.log.WriteText('Box %s is %schecked \n' % (label, status))
        self.lb.SetSelection(index)    # so that (un)checking also selects (moves the highlight)
        

    def OnTestButton(self, event):
        self.lb.SetString(4, "SetString")

    def OnDoHitTest(self, event):
        item = self.lb.HitTest(evt.GetPosition())
        self.log.write("HitTest: %d\n" % item)


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
