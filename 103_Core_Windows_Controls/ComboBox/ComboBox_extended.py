#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-Imports----------------------------------------------------------------------

#--wxPython Imports.
import wx


#- wxPython Demo --------------------------------------------------------------
__wxPyOnlineDocs__ = 'http://wxpython.org/Phoenix/docs/html/ComboBox.html'
__wxPyDemoPanel__ = 'TestPanel'

overview = """\
<html><body>
<center><h2>wx.ComboBox</h2></center>
<p>
A ComboBox is like a combination of an edit control and a listbox. It can be
displayed as static list with editable or read-only text field; or a drop-down
list with text field; or a drop-down list without a text field.
<p>
This example shows both a preset ComboBox and one that is dynamically created
(that is, it is initially empty but then we 'grow' it out of program-supplied
data). The former is common for read-only controls.
<p>
This example also shows the two form factors for the ComboBox. The first is more
common, and resembles a Choice control. The latter, although less common, shows
how all the values in the ComboBox can be visible, yet the functionality is the
same for both.
<p>
Finally, this demo shows how event handling can differ. The first ComboBox is set
up to handle EVT_TEXT_ENTER events, in which text is typed in and then ENTER is
hit by the user. This allows the user to enter a line of text which can then be
processed by the program. EVT_TEXT can also be processed, but in that case the
event is generated every time that the user hits a key in the ComboBox entry field.
</body></html>
"""


class TestPanel(wx.Panel):
    def OnSetFocus(self, event):
        # print("OnSetFocus")
        event.Skip()

    def OnKillFocus(self, event):
        # print("OnKillFocus")
        event.Skip()

    def __init__(self, parent, log):
        self.log = log
        wx.Panel.__init__(self, parent, -1)

        sampleList = ['zero', 'one', 'two', 'three', 'four', 'five',
                      #'this is a long item that needs a scrollbar...',
                      'six', 'seven', 'eight']

        wx.StaticText(self, -1, "This example uses the wx.ComboBox control.", (8, 10))
        wx.StaticText(self, -1, "Select one:", (15, 50), (75, 18))

        # This combobox is created with a preset list of values.
        cb = wx.ComboBox(self, 500, "default value", (90, 50),
                         (160, -1), sampleList,
                         wx.CB_DROPDOWN
                         #| wx.TE_PROCESS_ENTER
                         #| wx.CB_SORT
                         )

        self.Bind(wx.EVT_COMBOBOX, self.EvtComboBox, cb)
        self.Bind(wx.EVT_TEXT, self.EvtText, cb)
        self.Bind(wx.EVT_TEXT_ENTER, self.EvtTextEnter, cb)
        cb.Bind(wx.EVT_SET_FOCUS, self.OnSetFocus)
        cb.Bind(wx.EVT_KILL_FOCUS, self.OnKillFocus)

        # Once the combobox is set up, we can append some more data to it.
        cb.Append("foo", "This is some client data for this item")

        # This combobox is created with no values initially.
        cb = wx.ComboBox(
            self, 501, "default value", (90, 80), (160, -1), [], wx.CB_DROPDOWN)

        # Here we dynamically add our values to the second combobox.
        for item in sampleList:
            cb.Append(item, item.upper())

        self.Bind(wx.EVT_COMBOBOX, self.EvtComboBox, cb)

    # When the user selects something, we go here.
    def EvtComboBox(self, event):
        cb = event.GetEventObject()
        data = cb.GetClientData(event.GetSelection())
        self.log.WriteText('EvtComboBox: %s\nClientData: %s\n' % (event.GetString(), data))

        if event.GetString() == 'one':
            self.log.WriteText("You follow directions well!\n\n")

    # Capture events every time a user hits a key in the text entry field.
    def EvtText(self, event):
        self.log.WriteText('EvtText: %s\n' % event.GetString())
        event.Skip()

    # Capture events when the user types something into the control then
    # hits ENTER.
    def EvtTextEnter(self, event):
        self.log.WriteText('EvtTextEnter: %s' % event.GetString())
        event.Skip()


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
