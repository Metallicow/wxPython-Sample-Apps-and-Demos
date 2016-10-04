#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-Imports----------------------------------------------------------------------

#--wxPython Imports.
import wx

#- wxPython Demo --------------------------------------------------------------

overview = """
A checkbox is a labelled box which is either on (checkmark is visible) or off
(no checkmark).

"""

__wxPyOnlineDocs__ = 'http://wxpython.org/Phoenix/docs/html/CheckBox.html'
__wxPyDemoPanel__ = 'TestPanel'


class TestPanel(wx.Panel):
    def __init__(self, parent, log):
        self.log = log
        wx.Panel.__init__(self, parent, -1)

        st = wx.StaticText(self, -1, 
                "This example demonstrates the wx.CheckBox control.")

        cb1 = wx.CheckBox(self, -1, "Apples")
        cb2 = wx.CheckBox(self, -1, "Oranges")
        cb2.SetValue(True)
        cb3 = wx.CheckBox(self, -1, "Pears")

        cb4 = wx.CheckBox(self, -1, "3-state checkbox",
                          style=wx.CHK_3STATE|wx.CHK_ALLOW_3RD_STATE_FOR_USER)
        cb5 = wx.CheckBox(self, -1, "Align Right", style=wx.ALIGN_RIGHT)

        for cb in self.GetChildren():
            cb.Bind(wx.EVT_CHECKBOX, self.OnCheckBox)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.AddMany([cb1,
                       cb2,
                       cb3,
                       (20, 20),
                       cb4,
                       (20, 20),
                       cb5
                       ])

        border = wx.BoxSizer(wx.VERTICAL)
        border.Add(st, 0, wx.ALL, 15)
        border.Add(sizer, 0, wx.LEFT, 50)
        self.SetSizer(border)


    def OnCheckBox(self, event):
        evtObj = event.GetEventObject()
        self.log.WriteText('OnCheckBox: %s = %d\n' % (
            evtObj.GetLabel(), event.IsChecked()))
        cb = event.GetEventObject()
        if cb.Is3State():
            self.log.WriteText("\t3StateValue: %s\n" % cb.Get3StateValue())


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
    import os
    import sys
    print('Python %s.%s.%s %s' % sys.version_info[0:4])
    print('wxPython %s' % wx.version())
    gApp = TestApp(redirect=False,
                   filename=None,
                   useBestVisual=False,
                   clearSigInt=True)
    gApp.MainLoop()
