#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-Imports----------------------------------------------------------------------

#--wxPython Imports.
import wx

#- wxPython Demo --------------------------------------------------------------

__wxPyOnlineDocs__ = 'https://wxpython.org/Phoenix/docs/html/wx.InfoBar.html'
__wxPyDemoPanel__ = 'TestPanel'

overview = """<html><body>
<h2><center>wx.InfoBar</center></h2>

An info bar is a transient window shown at top or bottom of its parent
window to display non-critical information to the user.

<p>This class provides another way to show messages to the user,
intermediate between message boxes and status bar messages. The
message boxes are modal and thus interrupt the users work flow and
should be used sparingly for this reason. However status bar messages
are often too easy not to notice at all. An info bar provides a way to
present the messages which has a much higher chance to be noticed by
the user but without being annoying.

<p>Info bar may show an icon (on the left), text message and, optionally,
buttons allowing the user to react to the information presented. It
always has a close button at the right allowing the user to dismiss it
so it isn't necessary to provide a button just to close it.

</body></html>
"""

#----------------------------------------------------------------------

flags = [ (wx.ICON_NONE,        "ICON_NONE"),
          (wx.ICON_INFORMATION, "ICON_INFORMATION"),
          (wx.ICON_QUESTION,    "ICON_QUESTION"),
          (wx.ICON_WARNING,     "ICON_WARNING"),
          (wx.ICON_ERROR,       "ICON_ERROR")
          ]


class TestPanel(wx.Panel):
    def __init__(self, parent, log):
        self.log = log
        wx.Panel.__init__(self, parent, -1)

        # Create the InfoBar.  It starts out in a hidden state so it
        # won't be visible until we need it.
        self.info = wx.InfoBar(self)
        panel = wx.Panel(self)

        self.message = wx.TextCtrl(panel, -1, "Hello World", size=(250,-1))
        self.flags = wx.Choice(panel, choices=[f[1] for f in flags])
        self.flags.SetSelection(1) # wx.ICON_INFORMATION is the default

        smBtn = wx.Button(panel, -1, "Show Message")
        dmBtn = wx.Button(panel, -1, "Dismiss")
        addBtn = wx.Button(panel, -1, "Add Button")

        self.addBtnCount = 0  # Lets keep track of the buttons added.

        fgs = wx.FlexGridSizer(cols=3, vgap=10, hgap=10)
        fgs.Add(wx.StaticText(panel, -1, "Message:"), 0,
                wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT)
        fgs.Add(self.message)
        fgs.Add(self.flags)
        fgs.AddSpacer(5)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(smBtn, 0, wx.RIGHT, 5)
        hbox.Add(dmBtn)
        fgs.Add(hbox)
        fgs.AddSpacer(5)
        fgs.AddSpacer(5)
        fgs.Add(addBtn)

        panel.Sizer = wx.BoxSizer(wx.VERTICAL)
        text = """\
An info bar is a transient window shown at top or bottom of its parent window
to display non-critical information to the user."""
        panel.Sizer.Add(wx.StaticText(panel, -1, text), 0, wx.TOP|wx.LEFT, 25)
        panel.Sizer.Add(fgs, 1, wx.EXPAND|wx.ALL, 25)

        self.Sizer = wx.BoxSizer(wx.VERTICAL)
        self.Sizer.Add(self.info, 0, wx.EXPAND)
        self.Sizer.Add(panel, 1, wx.EXPAND)

        self.Bind(wx.EVT_BUTTON, self.OnShowMessage, smBtn)
        self.Bind(wx.EVT_BUTTON, self.OnDismiss, dmBtn)
        self.Bind(wx.EVT_BUTTON, self.OnAddButton, addBtn)


    def OnShowMessage(self, event):
        msg = self.message.GetValue()
        flag = flags[self.flags.GetSelection()][0]
        self.info.ShowMessage(msg, flag)

    def OnDismiss(self, event):
        self.info.Dismiss()

    def OnAddButton(self, event):
        self.addBtnCount += 1
        btnId = wx.NewId()
        self.info.AddButton(btnId, "new button%s" % self.addBtnCount)
        self.info.Bind(wx.EVT_BUTTON, self.OnButtonClicked, id=btnId)

    def OnButtonClicked(self, event):
        evtObj = event.GetEventObject()
        wx.MessageBox("%s clicked" % evtObj.GetLabel())
        # Calling event.Skip() will allow the default handler to run
        # which will dismiss the info bar.  If you don't want it to be
        # dismissed for a particular button then then don't call
        # Skip().
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
