#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-Imports----------------------------------------------------------------------

#--wxPython Imports.
import wx


#- wxPython Demo --------------------------------------------------------------
__wxPyOnlineDocs__ = 'https://wxpython.org/Phoenix/docs/html/wx.RadioButton.html'
__wxPyDemoPanel__ = 'TestPanel'

overview = """\
<html><body>
<P>
This demo shows how individual radio buttons can be used to build
more complicated selection mechanisms...
<P>
It uses 2 groups of wx.RadioButtons, where the groups are defined by
instantiation.  When a wx.RadioButton is created with the <I>wx.RB_GROUP</I>
style, all subsequent wx.RadioButtons created without it are implicitly
added to that group by the framework.
</body></html>
"""


class TestPanel(wx.Panel):
    def __init__(self, parent, log):

        wx.Panel.__init__(self, parent, -1)
        self.log = log
        panel = wx.Panel(self, -1)

        # Layout controls on panel:
        vbSizer = wx.BoxSizer(wx.VERTICAL)

        box1_title = wx.StaticBox(panel, -1, "Group 1")
        box1 = wx.StaticBoxSizer(box1_title, wx.VERTICAL)
        grid1 = wx.FlexGridSizer(cols=2)

        # 1st group of controls:
        self.group1_ctrls = []
        radio1 = wx.RadioButton(panel, -1, " Radio1 ", style=wx.RB_GROUP)
        radio2 = wx.RadioButton(panel, -1, " Radio2 ")
        radio3 = wx.RadioButton(panel, -1, " Radio3 ")
        text1 = wx.TextCtrl(panel, -1, "")
        text2 = wx.TextCtrl(panel, -1, "")
        text3 = wx.TextCtrl(panel, -1, "")
        self.group1_ctrls.append((radio1, text1))
        self.group1_ctrls.append((radio2, text2))
        self.group1_ctrls.append((radio3, text3))

        grpFlgs = wx.ALIGN_CENTRE | wx.LEFT | wx.RIGHT | wx.TOP
        for radio, text in self.group1_ctrls:
            grid1.Add(radio, 0, grpFlgs, 5)
            grid1.Add(text, 0, grpFlgs, 5)

        box1.Add( grid1, 0, wx.ALIGN_CENTRE | wx.ALL, 5)
        vbSizer.Add( box1, 0, wx.ALIGN_CENTRE | wx.ALL, 5)

        box2_title = wx.StaticBox(panel, -1, "Group 2")
        box2 = wx.StaticBoxSizer(box2_title, wx.VERTICAL)
        grid2 = wx.FlexGridSizer(cols=2)

        # 2nd group of controls:
        self.group2_ctrls = []
        radio4 = wx.RadioButton(panel, -1, " Radio1 ", style=wx.RB_GROUP)
        radio5 = wx.RadioButton(panel, -1, " Radio2 ")
        radio6 = wx.RadioButton(panel, -1, " Radio3 ")
        text4 = wx.TextCtrl(panel, -1, "")
        text5 = wx.TextCtrl(panel, -1, "")
        text6 = wx.TextCtrl(panel, -1, "")
        self.group2_ctrls.append((radio4, text4))
        self.group2_ctrls.append((radio5, text5))
        self.group2_ctrls.append((radio6, text6))

        for radio, text in self.group2_ctrls:
            grid2.Add(radio, 0, grpFlgs, 5)
            grid2.Add(text, 0, grpFlgs, 5)

        box2.Add(grid2, 0, wx.ALIGN_CENTRE | wx.ALL, 5)
        vbSizer.Add(box2, 0, wx.ALIGN_CENTRE | wx.ALL, 5)

        panel.SetSizer(vbSizer)
        vbSizer.Fit(panel)
        panel.Move((50,50))
        self.panel = panel

        # Setup event handling and initial state for controls:
        for radio, text in self.group1_ctrls:
            self.Bind(wx.EVT_RADIOBUTTON, self.OnGroup1Select, radio)

        for radio, text in self.group2_ctrls:
            self.Bind(wx.EVT_RADIOBUTTON, self.OnGroup2Select, radio)

        for radio, text in self.group1_ctrls + self.group2_ctrls:
            radio.SetValue(0)
            text.Enable(False)

    def OnGroup1Select(self, event):
        radio_selected = event.GetEventObject()
        self.log.WriteText('Group1 %s selected\n' % radio_selected.GetLabel())

        for radio, text in self.group1_ctrls:
            if radio is radio_selected:
                text.Enable(True)
            else:
                text.Enable(False)

    def OnGroup2Select(self, event):
        radio_selected = event.GetEventObject()
        self.log.WriteText('Group2 %s selected\n' % radio_selected.GetLabel())

        for radio, text in self.group2_ctrls:
            if radio is radio_selected:
                text.Enable(True)
            else:
                text.Enable(False)


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
