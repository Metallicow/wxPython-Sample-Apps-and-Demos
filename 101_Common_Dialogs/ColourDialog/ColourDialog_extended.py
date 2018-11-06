#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-Imports---------------------------------------------------------------------

#--wxPython Imports.
import wx


#- wxPython Demo -------------------------------------------------------------

__wxPyOnlineDocs__ = 'https://wxpython.org/Phoenix/docs/html/wx.ColourDialog.html'
__wxPyDemoPanel__ = 'TestPanel'

overview = """\
This class represents the colour chooser dialog.

Use of this dialog is a multi-stage process.

The actual information about how to display the dialog and the colors in the
dialog's 'registers' are contained in a wx.ColourData instance that is created by
the dialog at init time. Before displaying the dialog, you may alter these settings
to suit your needs. In the example, we set the dialog up to show the extended colour
data selection pane. Otherwise, only the more compact and less extensive colour
dialog is shown.  You may also preset the colour as well as other items.

If the user selects something and selects OK, then the wx.ColourData instance contains
the colour data that the user selected. Before destroying the dialog, retrieve the data.
<b>Do not try to retain the wx.ColourData instance.</b> It will probably not be valid
after the dialog is destroyed.

Along with he wx.ColourDialog documentation, see also the wx.ColourData documentation
for details.
"""


class TestPanel(wx.Panel):
    def __init__(self, parent, log):
        self.log = log
        wx.Panel.__init__(self, parent, -1)

        if not hasattr(self, "colourData"):
            # For saving the last picked color locally in between ColourDialog uses.
            self.colourData = wx.ColourData()
            self.colourData.SetColour(self.GetBackgroundColour())

        b = wx.Button(self, -1, "Create and Show a ColourDialog", (50,50))
        self.Bind(wx.EVT_BUTTON, self.OnButton, b)


    def OnButton(self, evt):
        dlg = wx.ColourDialog(self, self.colourData)

        # Ensure the full colour dialog is displayed,
        # not the abbreviated version.
        dlg.GetColourData().SetChooseFull(True)

        if dlg.ShowModal() == wx.ID_OK:

            # If the user selected OK, then the dialog's wx.ColourData will
            # contain valid information. Fetch the data ...
            data = dlg.GetColourData()

            # ... then do something with it. The actual colour data will be
            # returned as a three-tuple (r, g, b) in this particular case.
            color = data.GetColour().Get()
            self.log.WriteText('You selected: %s\n' % str(color))
            self.colourData.SetColour(color)
            self.SetBackgroundColour(color)
            self.Refresh()

        # Once the dialog is destroyed, Mr. wx.ColourData is no longer your
        # friend. Don't use it again!
        dlg.Destroy()


#- wxPy Demo -----------------------------------------------------------------


def runTest(frame, nb, log):
    win = TestPanel(nb, log)
    return win


#- __main__ Demo -------------------------------------------------------------


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


#- __main__ ------------------------------------------------------------------


if __name__ == '__main__':
    import sys
    print('Python %s.%s.%s %s' % sys.version_info[0:4])
    print('wxPython %s' % wx.version())
    gApp = TestApp(redirect=False,
            filename=None,
            useBestVisual=False,
            clearSigInt=True)

    gApp.MainLoop()
