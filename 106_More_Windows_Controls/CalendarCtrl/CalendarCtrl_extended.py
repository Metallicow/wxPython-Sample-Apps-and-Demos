#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-Imports----------------------------------------------------------------------

#--wxPython Imports.
import wx
import wx.adv
from wx.adv import CalendarCtrl

#- wxPython Demo --------------------------------------------------------------

__wxPyOnlineDocs__ = 'https://wxpython.org/Phoenix/docs/html/wx.adv.CalendarCtrl.html'
__wxPyDemoPanel__ = 'TestPanel'

overview = """\
<html><body>
<h2>CalendarCtrl</h2>

Yet <i>another</i> calendar control.  This one is a wrapper around the C++
version described in the docs.  This one will probably be a bit more efficient
than the one in wxPython.lib.calendar, but I like a few things about it better,
so I think both will stay in wxPython.
"""

#----------------------------------------------------------------------

description = """\
This sample shows the wx.calendar.CalendarCtrl in a variety of styles
and modes.  If this platform supports a native calendar widget then
that is what is shown to the left.  However it may not support all of
the features and attributes of the older wx calendar, so we now have
the ability to explicitly use the generic widget via the
GenericCalendarCtrl class, and that is what is used for the two
calendars below.
""".replace('\n', ' ')


class TestPanel(wx.Panel):
    def __init__(self, parent, log):
        wx.Panel.__init__(self, parent, wx.ID_ANY)
        self.log = log

        native = self.cal = CalendarCtrl(self, -1, wx.DateTime().Today(),
                                    style=wx.adv.CAL_SEQUENTIAL_MONTH_SELECTION)

        txt = wx.StaticText(self, -1, description)
        txt.Wrap(300)

        # cal = self.cal = GenericCalendarCtrl(self, -1, wx.DateTime().Today(),
                             # style = wx.adv.CAL_SHOW_HOLIDAYS
                             # | wx.adv.CAL_SUNDAY_FIRST
                             # | wx.adv.CAL_SEQUENTIAL_MONTH_SELECTION
                             # )

        # cal2 = wxcal.GenericCalendarCtrl(self, -1, wx.DateTime().Today())

        # Track a few holidays
        self.holidays = [(1,1), (10,31), (12,25) ]    # (these don't move around)
        self.OnChangeMonth()

        # bind some event handlers to each calendar
        for c in [native]:#, cal, cal2
            c.Bind(wx.adv.EVT_CALENDAR,                 self.OnCalSelected)
            ## c.Bind(wx.adv.EVT_CALENDAR_MONTH,           self.OnChangeMonth)
            c.Bind(wx.adv.EVT_CALENDAR_SEL_CHANGED,     self.OnCalSelChanged)
            c.Bind(wx.adv.EVT_CALENDAR_WEEKDAY_CLICKED, self.OnCalWeekdayClicked)

        # create some sizers for layout
        fgs = wx.FlexGridSizer(cols=2, hgap=50, vgap=50)
        fgs.Add(native)
        fgs.Add(txt)
        # fgs.Add(cal)
        # fgs.Add(cal2)
        box = wx.BoxSizer()
        box.Add(fgs, 1, wx.EXPAND|wx.ALL, 25)
        self.SetSizer(box)


    def OnCalSelected(self, event):
        self.log.write('OnCalSelected: %s\n' % event.GetDate())

    def OnCalWeekdayClicked(self, event):
        self.log.write('OnCalWeekdayClicked: %s\n' % event.GetWeekDay())

    def OnCalSelChanged(self, event):
        cal = event.GetEventObject()
        self.log.write("OnCalSelChanged:\n\t%s: %s\n\t%s: %s" %
                       ("EventObject", cal.__class__,
                        "Date       ", cal.GetDate(),
                        ))

    def OnChangeMonth(self, event=None):
        if event is None:
            cal = self.cal
        else:
            cal = event.GetEventObject()
        self.log.write('OnChangeMonth: %s\n' % cal.GetDate())
        cur_month = cal.GetDate().GetMonth() + 1   # convert wxDateTime 0-11 => 1-12
        for month, day in self.holidays:
            if month == cur_month:
                cal.SetHoliday(day)

        # August 14th is a special day, mark it with a blue square...
        if cur_month == 8:
            attr = wxcal.CalendarDateAttr(border=wx.adv.CAL_BORDER_SQUARE,
                                          colBorder="blue")
            cal.SetAttr(14, attr)
        else:
            cal.ResetAttr(14)


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
