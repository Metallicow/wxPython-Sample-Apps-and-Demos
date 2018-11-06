#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-Imports----------------------------------------------------------------------

#--wxPython Imports.
import wx
import wx.adv

#- wxPython Demo --------------------------------------------------------------

__wxPyOnlineDocs__ = 'https://wxpython.org/Phoenix/docs/html/wx.adv.DatePickerCtrl.html'
__wxPyDemoPanel__ = 'TestPanel'

overview = """<html><body>
<h2><center>wx.adv.DatePickerCtrl</center></h2>

This control allows the user to select a date. Unlike
wx.calendar.CalendarCtrl, which is a relatively big control,
wx.adv.DatePickerCtrl is implemented as a small window showing the
currently selected date. The control can be edited using the keyboard,
and can also display a popup window for more user-friendly date
selection, depending on the styles used and the platform.

</body></html>
"""

#----------------------------------------------------------------------

class TestPanel(wx.Panel):
    def __init__(self, parent, log):
        self.log = log
        wx.Panel.__init__(self, parent, -1)

        sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(sizer)

        dpc = wx.adv.DatePickerCtrl(self, size=(120,-1),
                                style = wx.adv.DP_DROPDOWN
                                      | wx.adv.DP_SHOWCENTURY
                                      | wx.adv.DP_ALLOWNONE )
        self.Bind(wx.adv.EVT_DATE_CHANGED, self.OnDateChanged, dpc)
        sizer.Add(dpc, 0, wx.ALL, 50)

        # In some cases the widget used above will be a native date
        # picker, so show the generic one too.
        # dpc = wx.adv.DatePickerCtrlGeneric(self, size=(120,-1),
                                       # style = wx.TAB_TRAVERSAL
                                       # | wx.adv.DP_DROPDOWN
                                       # | wx.adv.DP_SHOWCENTURY
                                       # | wx.adv.DP_ALLOWNONE )
        # self.Bind(wx.adv.EVT_DATE_CHANGED, self.OnDateChanged, dpc)
        # sizer.Add(dpc, 0, wx.LEFT, 50)


    def OnDateChanged(self, evt):
        self.log.write("OnDateChanged: %s\n" % evt.GetDate())


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
