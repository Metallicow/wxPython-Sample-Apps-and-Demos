#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-Imports----------------------------------------------------------------------

#--wxPython Imports.
import wx
import wx.lib.scrolledpanel as scrolled


#- wxPython Demo --------------------------------------------------------------
__wxPyOnlineDocs__ = 'http://wxpython.org/Phoenix/docs/html/MessageDialog.html'
__wxPyDemoPanel__ = 'TestPanel'

overview = """\
<html>
<body>
<h2>wx.MessageDialog</h2>

<p>
This class represents a dialog that shows a single or multi-line message, with
 a choice of OK, Yes, No, Cancel and Help buttons. Additionally, various style
 flags can determine whether an icon is displayed, and, if so, what kind.
 The return value of ShowModal indicates which button was pressed.
</p>

<h4>Window Styles</h4>
<p>
This class supports the following styles:
</p>
<p>
<b>OK</b>: Puts an Ok button in the message box. May be combined with CANCEL.
</p>
<p>
<b>CANCEL</b>: Puts a Cancel button in the message box.
 Must be combined with either OK or YES_NO.
</p>
<p>
<b>YES_NO</b>: Puts Yes and No buttons in the message box. It is recommended to
 always use CANCEL with this style as otherwise the message box won't have a
 close button under wxMSW and the user will be forced to answer it.
</p>
<p>
<b>HELP</b>: Puts a Help button to the message box. This button can have
 special appearance or be specially positioned if its label is not changed from
 the default one. Notice that using this button is not supported when showing a
 message box from non-main thread in OSX/Cocoa and it is not supported in
 OSX/Carbon at all.
</p>
<p>
<b>NO_DEFAULT</b>: Makes the "No" button default, can only be used with YES_NO.
</p>
<p>
<b>CANCEL_DEFAULT</b>: Makes the "Cancel" button default, can only be used
 with CANCEL
</p>
<p>
<b>YES_DEFAULT</b>: Makes the "Yes" button default, this is the default
 behaviour and this flag exists solely for symmetry with NO_DEFAULT .
</p>
<p>
<b>OK_DEFAULT</b>: Makes the "OK" button default, this is the default behaviour
 and this flag exists solely for symmetry with CANCEL_DEFAULT .
</p>
<p>
<b>ICON_NONE</b>: Displays no icon in the dialog if possible (an icon might
 still be displayed if the current platform mandates its use). This style may
 be used to prevent the dialog from using the default icon based on YES_NO
 presence as explained in ICON_QUESTION and ICON_INFORMATION documentation
 below.
</p>
<p>
<b>ICON_EXCLAMATION</b>: Displays an exclamation, or warning,
 icon in the dialog.
</p>
<p>
<b>ICON_ERROR</b>: Displays an error icon in the dialog.
</p>
<p>
<b>ICON_HAND</b>: Displays an error symbol, this is a MSW-inspired synonym for
 ICON_ERROR .
</p>
<p>
<b>ICON_QUESTION</b>: Displays a question mark symbol. This icon is
 automatically used with YES_NO so it's usually unnecessary to specify it
 explicitly. This style is not supported for message dialogs under wxMSW when
 a task dialog is used to implement them (i.e. when running under Windows Vista
 or later) because Microsoft guidelines indicate that no icon should be used
 for routine confirmations. If it is specified, no icon will be displayed.
</p>
<p>
<b>ICON_INFORMATION</b>: Displays an information symbol. This icon is used by
 default if YES_NO is not given so it is usually unnecessary to specify it
 explicitly.
</p>
<p>
<b>ICON_AUTH_NEEDED</b>: Displays an authentication needed symbol. This style
 is only supported for message dialogs under wxMSW when a task dialog is used
 to implement them (i.e. when running under Windows Vista or later). In other
 cases the default icon selection logic will be used. Note this can be combined
 with other styles to provide a fallback. For instance, using ICON_AUTH_NEEDED
 | ICON_QUESTION will show a shield symbol on Windows Vista or above and a
 question symbol on other platforms.
</p>
<p>
<b>STAY_ON_TOP</b>: Makes the message box stay on top of all other windows and
 not only just its parent (currently implemented only under MSW and GTK).
</p>
<p>
<b>CENTRE</b>: Centre the message box on its parent or on the screen if parent
 is not specified. Setting this style under MSW makes no differences as the
 dialog is always centered on the parent.
</p>

</body>
</html>
"""


class TestPanel(scrolled.ScrolledPanel):
    def __init__(self, parent, log):
        self.log = log
        scrolled.ScrolledPanel.__init__(self, parent, wx.ID_ANY)

        vbSizer = wx.BoxSizer(wx.VERTICAL)
        hbSizer0 = wx.BoxSizer(wx.HORIZONTAL)
        hbSizer1 = wx.BoxSizer(wx.HORIZONTAL)
        hbSizer2 = wx.BoxSizer(wx.HORIZONTAL)

        showMsgDlgButton = wx.Button(self, wx.ID_ANY,
                                     "Create and Show a MessageDialog")
        showMsgDlgButton.Bind(wx.EVT_BUTTON, self.OnShowMessageDialog)
        hbSizer2.Add(showMsgDlgButton, 0, wx.ALIGN_CENTER | wx.ALL, 10)


        generateCodeButton = wx.Button(self, wx.ID_ANY,
                                       "Generate Code Snippet")
        generateCodeButton.Bind(wx.EVT_BUTTON, self.OnGenerateCodeSnippet)
        hbSizer2.Add(generateCodeButton, 0, wx.ALIGN_CENTER | wx.ALL, 10)
        vbSizer.Add(hbSizer2, 0, wx.ALIGN_CENTER | wx.ALL, 1)

        self.caption = wx.TextCtrl(self, wx.ID_ANY, "A Message Box",
                                   style=wx.TE_NOHIDESEL)
        self.caption.SetToolTip(wx.ToolTip("Set the caption."))
        vbSizer.Add(self.caption, 0, wx.EXPAND | wx.ALL, 5)

        self.message = wx.TextCtrl(self, wx.ID_ANY,
                                   "Hello from Python and wxPython!",
                                   size=(-1, 60),
                                   style=wx.TE_MULTILINE | wx.TE_NOHIDESEL)
        self.message.SetToolTip(wx.ToolTip("Set the message."))
        vbSizer.Add(self.message, 0, wx.EXPAND | wx.ALL, 5)

        self.extended = wx.CheckBox(self, -1, "Add extended message")
        self.extended.Bind(wx.EVT_CHECKBOX, self.OnCheckBox)
        vbSizer.Add(self.extended, 0, wx.ALL, 5)

        self.extendedMsg = wx.TextCtrl(self, wx.ID_ANY, "Extended Message",
                                   size=(-1, 60),
                                   style=wx.TE_MULTILINE | wx.TE_NOHIDESEL)
        self.extendedMsg.SetToolTip(wx.ToolTip("Set the extended message."))
        self.extendedMsg.Enable(False)
        vbSizer.Add(self.extendedMsg, 0, wx.EXPAND | wx.ALL, 5)

        self.okBtnLabel = wx.TextCtrl(self, wx.ID_ANY, "OK",
                                      style=wx.TE_NOHIDESEL)
        self.okBtnLabel.SetToolTip(wx.ToolTip("Set the wx.OK button's label."))
        self.yesBtnLabel = wx.TextCtrl(self, wx.ID_ANY, "Yes",
                                       style=wx.TE_NOHIDESEL)
        self.yesBtnLabel.SetToolTip(wx.ToolTip("Set the wx.YES button's label."))
        self.noBtnLabel = wx.TextCtrl(self, wx.ID_ANY, "No",
                                       style=wx.TE_NOHIDESEL)
        self.noBtnLabel.SetToolTip(wx.ToolTip("Set the wx.NO button's label."))
        self.cancelBtnLabel = wx.TextCtrl(self, wx.ID_ANY, "Cancel",
                                          style=wx.TE_NOHIDESEL)
        self.cancelBtnLabel.SetToolTip(wx.ToolTip("Set the wx.CANCEL button's label."))
        self.helpBtnLabel = wx.TextCtrl(self, wx.ID_ANY, "Help",
                                        style=wx.TE_NOHIDESEL)
        self.helpBtnLabel.SetToolTip(wx.ToolTip("Set the wx.HELP button's label."))
        hbSizer0.Add(self.okBtnLabel, 1, wx.ALL, 2)
        hbSizer0.Add(self.yesBtnLabel, 1, wx.ALL, 2)
        hbSizer0.Add(self.noBtnLabel, 1, wx.ALL, 2)
        hbSizer0.Add(self.cancelBtnLabel, 1, wx.ALL, 2)
        hbSizer0.Add(self.helpBtnLabel, 1, wx.ALL, 2)
        vbSizer.Add(hbSizer0, 0, wx.EXPAND | wx.ALL, 5)

        self.statBox = wx.StaticBox(self, wx.ID_ANY, "Buttons Styles")
        self.ok = wx.CheckBox(self.statBox, -1, "wx.OK")
        self.ok.SetValue(True)
        self.ok.Bind(wx.EVT_CHECKBOX, self.OnCheckBox)
        self.yes_no = wx.CheckBox(self.statBox, -1, "wx.YES_NO")
        self.yes_no.Bind(wx.EVT_CHECKBOX, self.OnCheckBox)
        self.cancel = wx.CheckBox(self.statBox, -1, "wx.CANCEL")
        self.cancel.Bind(wx.EVT_CHECKBOX, self.OnCheckBox)
        self.yes = wx.CheckBox(self.statBox, -1, "wx.YES")
        self.yes.Bind(wx.EVT_CHECKBOX, self.OnCheckBox)
        self.no = wx.CheckBox(self.statBox, -1, "wx.NO")
        self.no.Bind(wx.EVT_CHECKBOX, self.OnCheckBox)
        self.ok_default = wx.CheckBox(self.statBox, -1, "wx.OK_DEFAULT")
        self.ok_default.Bind(wx.EVT_CHECKBOX, self.OnCheckBox)
        self.yes_default = wx.CheckBox(self.statBox, -1, "wx.YES_DEFAULT")
        self.yes_default.Bind(wx.EVT_CHECKBOX, self.OnCheckBox)
        self.no_default = wx.CheckBox(self.statBox, -1, "wx.NO_DEFAULT")
        self.no_default.Bind(wx.EVT_CHECKBOX, self.OnCheckBox)
        self.cancel_default = wx.CheckBox(self.statBox, -1, "wx.CANCEL_DEFAULT")
        self.cancel_default.Bind(wx.EVT_CHECKBOX, self.OnCheckBox)
        self.help = wx.CheckBox(self.statBox, -1, "wx.HELP")
        self.help.Bind(wx.EVT_CHECKBOX, self.OnCheckBox)
        self.stay_on_top = wx.CheckBox(self.statBox, -1, "wx.STAY_ON_TOP")
        self.stay_on_top.Bind(wx.EVT_CHECKBOX, self.OnCheckBox)
        self.centre = wx.CheckBox(self.statBox, -1, "wx.CENTRE")
        self.centre.Bind(wx.EVT_CHECKBOX, self.OnCheckBox)

        self.dialogIconStyles = wx.RadioBox(self, wx.ID_ANY, "Dialog Styles",
                                            choices=["wx.ICON_INFORMATION",
                                                     "wx.ICON_QUESTION",
                                                     "wx.ICON_EXCLAMATION",
                                                     "wx.ICON_WARNING",
                                                     "wx.ICON_ERROR",
                                                     "wx.ICON_STOP",
                                                     "wx.ICON_HAND",
                                                     "wx.ICON_AUTH_NEEDED",
                                                     "wx.ICON_ASTERISK",
                                                     "wx.ICON_MASK",
                                                     "wx.ICON_NONE"],
                                            majorDimension=2,
                                            style=wx.RA_SPECIFY_COLS)

        vsbSizer = wx.StaticBoxSizer(self.statBox, wx.VERTICAL)
        vsbSizer.Add(self.ok, 0, wx.ALL, 2)
        vsbSizer.Add(self.yes_no, 0, wx.ALL, 2)
        vsbSizer.Add(self.cancel, 0, wx.ALL, 2)
        vsbSizer.Add(self.yes, 0, wx.ALL, 2)
        vsbSizer.Add(self.no, 0, wx.ALL, 2)
        vsbSizer.Add(self.ok_default, 0, wx.ALL, 2)
        vsbSizer.Add(self.yes_default, 0, wx.ALL, 2)
        vsbSizer.Add(self.no_default, 0, wx.ALL, 2)
        vsbSizer.Add(self.cancel_default, 0, wx.ALL, 2)
        vsbSizer.Add(self.help, 0, wx.ALL, 2)
        vsbSizer.Add(self.stay_on_top, 0, wx.ALL, 2)
        vsbSizer.Add(self.centre, 0, wx.ALL, 2)

        hbSizer1.Add(vsbSizer, 0, wx.ALL, 5)
        hbSizer1.Add(self.dialogIconStyles, 0, wx.ALL, 5)

        vbSizer.Add(hbSizer1, 0)

        self.SetSizer(vbSizer)

        self.SetupScrolling()


    def OnCheckBox(self, event):
        obj = event.GetEventObject()

        widgets = [self.yes_no,
                   self.yes, self.no,
                   self.yes_default, self.no_default]

        if obj == self.ok:
            if self.ok.IsChecked():
                for checks in widgets:
                    checks.SetValue(0)
            else:
                self.ok_default.SetValue(0)
        elif obj == self.yes_no:
            if self.yes_no.IsChecked():
                self.yes.SetValue(0)
                self.no.SetValue(0)
                self.ok.SetValue(0)
                self.ok_default.SetValue(0)
            else:
                self.yes_default.SetValue(0)
                self.no_default.SetValue(0)
        elif obj == self.yes:
            if self.yes.IsChecked():
                if not self.no.GetValue():
                    self.no.SetValue(1)
                self.yes_no.SetValue(0)
                self.ok.SetValue(0)
                self.ok_default.SetValue(0)
            else:
                self.no.SetValue(0)
                self.ok.SetValue(0)
                self.ok_default.SetValue(0)
                self.yes_default.SetValue(0)
                self.no_default.SetValue(0)
        elif obj == self.no:
            if self.no.IsChecked():
                if not self.yes.GetValue():
                    self.yes.SetValue(1)
                self.yes_no.SetValue(0)
                self.ok.SetValue(0)
                self.ok_default.SetValue(0)
            else:
                self.yes.SetValue(0)
                self.ok.SetValue(0)
                self.ok_default.SetValue(0)
                self.yes_default.SetValue(0)
                self.no_default.SetValue(0)
        elif obj == self.ok_default:
            if self.ok_default.IsChecked():
                if not self.ok.IsChecked():
                    self.ok.SetValue(1)
                self.yes.SetValue(0)
                self.no.SetValue(0)
                self.yes_no.SetValue(0)
            self.yes_default.SetValue(0)
            self.no_default.SetValue(0)
            self.cancel_default.SetValue(0)
        elif obj == self.yes_default:
            if self.yes_default.IsChecked():
                if not self.yes.IsChecked():
                    self.yes.SetValue(1)
                    self.no.SetValue(1)
                if self.yes_no.IsChecked():
                    self.yes.SetValue(0)
                    self.no.SetValue(0)
                elif self.no.IsChecked():
                    self.yes_no.SetValue(0)
                self.ok.SetValue(0)
            self.ok_default.SetValue(0)
            self.no_default.SetValue(0)
            self.cancel_default.SetValue(0)
        elif obj == self.no_default:
            if self.no_default.IsChecked():
                if not self.no.IsChecked():
                    self.yes.SetValue(1)
                    self.no.SetValue(1)
                if self.yes_no.IsChecked():
                    self.yes.SetValue(0)
                    self.no.SetValue(0)
                elif self.no.IsChecked():
                    self.yes_no.SetValue(0)
                self.ok.SetValue(0)
            self.ok_default.SetValue(0)
            self.yes_default.SetValue(0)
            self.cancel_default.SetValue(0)
        elif obj == self.cancel_default:
            if self.cancel_default.IsChecked():
                if not self.cancel.IsChecked():
                    self.cancel.SetValue(1)
            self.ok_default.SetValue(0)
            self.yes_default.SetValue(0)
            self.no_default.SetValue(0)
        elif obj == self.extended:
            if self.extended.IsChecked():
                self.extendedMsg.Enable(True)
            else:
                self.extendedMsg.Enable(False)

    def GetBtnStyle(self):
        btnStyle = 0
        for child in self.statBox.GetChildren():
            if isinstance(child, wx.CheckBox):
                if child.GetValue():
                    btnStyle |= eval(child.GetLabel())

        btnStyle |= eval(self.dialogIconStyles.GetString(
                         self.dialogIconStyles.GetSelection()))

        return btnStyle

    def OnShowMessageDialog(self, event):
        btnStyle = self.GetBtnStyle()
        dlg = wx.MessageDialog(self, self.message.GetValue(),
                               self.caption.GetValue(),
                               style=btnStyle
                               )
        if self.ok.IsChecked() or self.cancel.IsChecked():
            dlg.SetOKCancelLabels(ok=self.okBtnLabel.GetValue(),
                                  cancel=self.cancelBtnLabel.GetValue())
        elif self.yes.IsChecked() and self.no.IsChecked() \
            or self.yes_no.IsChecked() \
            or self.cancel.IsChecked():
            dlg.SetYesNoCancelLabels(yes=self.yesBtnLabel.GetValue(),
                                     no=self.noBtnLabel.GetValue(),
                                     cancel=self.cancelBtnLabel.GetValue())
        if self.help.IsChecked():
            dlg.SetHelpLabel(help=self.helpBtnLabel.GetValue())

        if self.extended.IsChecked():
            dlg.SetExtendedMessage(self.extendedMsg.GetValue())
        dlg.ShowModal()
        dlg.Destroy()

    def GetStyleString(self):
        styleStr = ""
        one = 0
        for cb in [self.ok, self.yes_no, self.yes, self.no, self.cancel,
                   self.ok_default, self.yes_default,
                   self.no_default, self.cancel_default,
                   self.help, self.stay_on_top, self.centre]:
            if cb.IsChecked():
                if one:
                    styleStr += "|" + cb.GetLabel()
                else:
                    styleStr += cb.GetLabel()
                one = 1
        sel = self.dialogIconStyles.GetSelection()
        styleStr += "|" + self.dialogIconStyles.GetString(sel)
        return styleStr

    def OnGenerateCodeSnippet(self, event):
        msg = self.message.GetValue()
        cap = self.caption.GetValue()
        sty = self.GetStyleString()
        generateCodeTemplate = '''\
def OnShowMessageDialog(self, event=None):
    msg = "{msg}"
    cap = "{cap}"
    sty = {sty}
    dlg = wx.MessageDialog(self, message=msg,
                           caption=cap,
                           style=sty
                           )
    dlg.ShowModal()
    dlg.Destroy()'''.format(msg=msg,
                            cap=cap,
                            sty=sty)

        frame = wx.MiniFrame(self, title="Generated Code Snippet",
                             style=wx.DEFAULT_FRAME_STYLE)
        frame.text = wx.TextCtrl(frame, -1, generateCodeTemplate,
                                 style=wx.TE_MULTILINE | wx.TE_NOHIDESEL)
        frame.Show()

        ### Python2/3
        ##import wx.libsix as six
        ##six.exec_(compile(generateCodeTemplate + "\nOnShowMessageDialog(self)",
        ##            "",
        ##            "exec"))


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
