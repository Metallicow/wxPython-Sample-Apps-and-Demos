#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-Imports----------------------------------------------------------------------

#--Python Imports.
import  time

#--wxPython Imports.
import wx


#- wxPython Demo --------------------------------------------------------------
__wxPyOnlineDocs__ = 'http://wxpython.org/Phoenix/docs/html/StatusBar.html'
__wxPyDemoPanel__ = 'TestPanel'

overview = """\
A status bar is a narrow window that can be placed along the bottom of
a frame to give small amounts of status information. It can contain
one or more fields, one or more of which can be variable length
according to the size of the window.

This example demonstrates how to create a custom status bar with actual
gadgets embedded in it. In this case, the first field is just plain text,
The second one has a checkbox that enables the timer, and the third
field has a clock that shows the current time when it is enabled.

"""

RELATIVEWIDTHS = False


class CustomStatusBar(wx.StatusBar):
    def __init__(self, parent, log):
        wx.StatusBar.__init__(self, parent, -1)

        # This status bar has three fields.
        self.SetFieldsCount(3)
        if RELATIVEWIDTHS:
            # Sets the three fields to be relative widths to each other.
            self.SetStatusWidths([-2, -1, -2])
        else:
            self.SetStatusWidths([-2, 90, 140])
        self.log = log
        self.sizeChanged = False
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.Bind(wx.EVT_IDLE, self.OnIdle)

        # Field 0 ... just text.
        self.SetStatusText("A Custom StatusBar...", 0)

        # This will fall into field 1 (the second field).
        self.cb = wx.CheckBox(self, 1001, "toggle clock")
        self.Bind(wx.EVT_CHECKBOX, self.OnToggleClock, self.cb)
        self.cb.SetValue(True)

        # Set the initial position of the checkbox.
        self.Reposition()

        # We're going to use a timer to drive a 'clock' in the last field.
        self.timer = wx.PyTimer(self.Notify)
        self.timer.Start(1000)
        self.Notify()


    def Notify(self):
        # Handles events from the timer we started in __init__().
        # We're using it to drive a 'clock' in field 2 (the third field).
        t = time.localtime(time.time())
        st = time.strftime("%d-%b-%Y   %I:%M:%S", t)
        self.SetStatusText(st, 2)
        self.log.WriteText("tick...\n")

    def OnToggleClock(self, event):
        # The checkbox was clicked.
        if self.cb.GetValue():
            self.timer.Start(1000)
            self.Notify()
        else:
            self.timer.Stop()

    def OnSize(self, event):
        event.Skip()
        self.Reposition()  # For normal size events.

        # Set a flag so the idle time handler will also do the repositioning.
        # It is done this way to get around a buglet where GetFieldRect is not
        # accurate during the EVT_SIZE resulting from a frame maximize.
        self.sizeChanged = True

    def OnIdle(self, event):
        if self.sizeChanged:
            self.Reposition()

    def Reposition(self):
        # Reposition the checkbox.
        rect = self.GetFieldRect(1)
        rect.x += 1
        rect.y += 1
        self.cb.SetRect(rect)
        self.sizeChanged = False


class TestCustomStatusBar(wx.Frame):
    def __init__(self, parent, log):
        wx.Frame.__init__(self, parent, -1, 'Test Custom StatusBar')

        self.sb = CustomStatusBar(self, log)
        self.SetStatusBar(self.sb)
        tc = wx.TextCtrl(self, -1, "", style=wx.TE_READONLY|wx.TE_MULTILINE)

        self.SetSize((640, 480))
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)

    def OnCloseWindow(self, event):
        self.sb.timer.Stop()
        del self.sb.timer
        self.Destroy()

#---------------------------------------------------------------------------

class TestPanel(wx.Panel):
    def __init__(self, parent, log):
        self.log = log
        wx.Panel.__init__(self, parent, -1)

        b = wx.Button(self, -1, "Show the StatusBar sample", (50, 50))
        self.Bind(wx.EVT_BUTTON, self.OnButton, b)


    def OnButton(self, event):
        win = TestCustomStatusBar(self, self.log)
        win.Show(True)


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
