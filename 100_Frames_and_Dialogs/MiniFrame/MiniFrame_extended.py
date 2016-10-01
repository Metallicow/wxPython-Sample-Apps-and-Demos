#!/usr/bin/env python
# -*- coding: utf-8 -*-

__doc__ = """\
A MiniFrame is a Frame with a small title bar. It is suitable for floating
toolbars that must not take up too much screen area. In other respects, it's the
same as a wx.Frame.
"""

__wxPyOnlineDocs__ = 'http://wxpython.org/Phoenix/docs/html/MiniFrame.html'
__wxPyDemoPanel__ = 'TestPanel'

#-Imports-----------------------------------------------------------------------

#--Python Imports.
import os
import sys

#--wxPython Imports.
import wx


#-Globals-----------------------------------------------------------------------
try:
    gFileDir = os.path.dirname(os.path.abspath(__file__))
except:
    gFileDir = os.path.dirname(os.path.abspath(sys.argv[0]))
gBmpDir = gFileDir + os.sep + 'bitmaps'


class MyMiniFrame(wx.MiniFrame):
    def __init__(self, parent, id, title, pos=wx.DefaultPosition,
                 size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE,
                 name='frame'):

        wx.MiniFrame.__init__(self, parent, id, title, pos, size, style, name)
        panel = wx.Panel(self, -1)

        button = wx.Button(panel, 1003, "Close Me")
        button.SetPosition((15, 15))

        button2 = wx.Button(panel, -1, "ToggleWindowStyle(wx.STAY_ON_TOP)")
        button2.SetPosition((30, 50))

        self.Bind(wx.EVT_BUTTON, self.OnCloseMe, button)
        self.Bind(wx.EVT_BUTTON, self.OnToggleWindowStyle, button2)
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)

        
    def OnToggleWindowStyle(self, event):
        self.ToggleWindowStyle(wx.STAY_ON_TOP)

    def OnCloseMe(self, event):
        self.Close(True)

    def OnCloseWindow(self, event):
        self.Destroy()

#---------------------------------------------------------------------------

class TestPanel(wx.Panel):
    def __init__(self, parent, log):
        self.log = log
        wx.Panel.__init__(self, parent, -1)

        b1 = wx.Button(self, -1, "Create and Show a MiniFrame", (50, 50))
        self.Bind(wx.EVT_BUTTON, self.OnButton1, b1)

        b2 = wx.Button(self, -1, "Create and Show a MiniFrame With Effect", (50, 100))
        self.Bind(wx.EVT_BUTTON, self.OnButton2, b2)

        self.list = wx.ListBox(self, choices=['wx.SHOW_EFFECT_NONE',
                                              'wx.SHOW_EFFECT_ROLL_TO_LEFT',
                                              'wx.SHOW_EFFECT_ROLL_TO_RIGHT',
                                              'wx.SHOW_EFFECT_ROLL_TO_TOP',
                                              'wx.SHOW_EFFECT_ROLL_TO_BOTTOM',
                                              'wx.SHOW_EFFECT_SLIDE_TO_LEFT',
                                              'wx.SHOW_EFFECT_SLIDE_TO_RIGHT',
                                              'wx.SHOW_EFFECT_SLIDE_TO_TOP',
                                              'wx.SHOW_EFFECT_SLIDE_TO_BOTTOM',
                                              'wx.SHOW_EFFECT_BLEND',
                                              'wx.SHOW_EFFECT_EXPAND'
                                              # 'wx.SHOW_EFFECT_MAX'
                                              ],
                               pos=(50, 155), size=(220, 160),
                               style=wx.LB_SINGLE)
        self.list.Select(0)

        tt = "Timeout in milliseconds\n0 is system default"
        self.spin = wx.SpinCtrl(self, -1, tt,
                                pos=(50, 130), style=wx.ALIGN_LEFT)
        self.spin.SetToolTip(wx.ToolTip(tt))
        self.spin.SetRange(0, 5000)
        self.spin.SetValue(0)

    def OnButton1(self, evt):
        win = MyMiniFrame(self, -1, "This is a wx.MiniFrame", size=(350, 200),
                      style=wx.DEFAULT_FRAME_STYLE)
        win.Centre()
        win.Show(True)

    def OnButton2(self, evt):
        win = MyMiniFrame(self, -1, "This is a wx.MiniFrame", size=(350, 200),
                      style=wx.DEFAULT_FRAME_STYLE)
        win.Centre()
        win.ShowWithEffect(effect=eval(self.list.GetString(self.list.GetSelection())),
                           timeout=self.spin.GetValue())


#- __main__ Demo ---------------------------------------------------------------

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

        try:
            self.SetIcon(wx.IconFromLocation(wx.IconLocation(sys.executable)))
        except Exception as exc:
            raise exc

    def OnDestroy(self, event):
        self.Destroy()


class TestApp(wx.App):
    def OnInit(self):
        gMainWin = TestFrame(None)
        gMainWin.SetTitle('Extended Frame Demo')
        gMainWin.Show()

        return True

#---------------------------------------------------------------------------


if __name__ == '__main__':
    import sys
    print('Python %s.%s.%s %s' % sys.version_info[0:4])
    print('wxPython %s' % wx.version())
    gApp = TestApp(redirect=False,
            filename=None,
            useBestVisual=False,
            clearSigInt=True)

    gApp.MainLoop()
