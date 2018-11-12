#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-Imports----------------------------------------------------------------------

#--Python Imports.
import os
import sys
from math import pi as M_PI  # used by many snippets

#--wxPython Imports.
import wx

try:
    import wx.lib.wxcairo
    import cairo
    haveCairo = True
except ImportError:
    haveCairo = False

import wx.stc as stc

#--Local Imports.
from snippets import snip_list, snippet_normalize

#-Globals----------------------------------------------------------------------
try:
    gFileDir = os.path.dirname(os.path.abspath(__file__))
except Exception:
    gFileDir = os.path.dirname(os.path.abspath(sys.argv[0]))
gSnipDir = gFileDir + os.sep + 'snippets'

#- wxPython Demo --------------------------------------------------------------
__wxPyOnlineDocs__ = 'https://wxpython.org/Phoenix/docs/html/wx.lib.wxcairo.html'
__wxPyDemoPanel__ = 'TestPanel'

if haveCairo:
    extra = "\n<h3>wx.lib.wxcairo</h3>\n%s" % (
        wx.lib.wxcairo.__doc__.replace('\n\n', '\n<p>'))
else:
    extra = '\n<p>See the docstring in the wx.lib.wxcairo module for details about installing dependencies.'

overview = """<html><body>
<h2><center>Cairo Integration</center></h2>

The wx.lib.wxcairo module provides a bit of glue that will allow you to
use the Pycairo package drawing directly on wx.DC's.

<p> This sample draws the standard 'snippet' examples that come with
the Pycairo pacakge, and a few others.  The C version of the samples
can be seen at http://cairographics.org/samples/

<p> In most snippets you'll see a call to a snippet_normalize()
function.  This is part of the demo and not part of Cairo.  It is
simply scaling the context such that the range of 0.0 to 1.0 is the
min(width, height) of the window in pixels.  In other words, it allows
the rendering code to use a range or 0.0 to 1.0 and it will always fit
in the drawing area.  (Try resizing the demo and reselecting a snippet
to see this.)

<pre>
def snippet_normalize(ctx, width, height):
    size = min(width, height)
    ctx.scale(size, size)
    ctx.set_line_width(0.04)
</pre>

%s
</body></html>
""" % extra

#----------------------------------------------------------------------

# TODO:  Add the ability for the user to edit and render their own snippet

class DisplayPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, style=wx.BORDER_SIMPLE)
        if not self.IsDoubleBuffered():
            self.SetDoubleBuffered(True)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.curr_snippet = ''


    def OnPaint(self, evt):
        dc = wx.PaintDC(self)

        if self.curr_snippet:
            width, height = self.GetClientSize()
            cr = wx.lib.wxcairo.ContextFromDC(dc)
            exec(self.curr_snippet, globals(), locals())

    def SetSnippet(self, text):
        self.curr_snippet = text
        self.Refresh()


class TestPanel(wx.Panel):
    def __init__(self, parent, log):
        self.log = log
        wx.Panel.__init__(self, parent, wx.ID_ANY)

        self.lb = wx.ListBox(self, choices=snip_list)
        self.lb.SetSelection(0)
        self.canvas = DisplayPanel(self)
        self.editor = stc.StyledTextCtrl(self, style=wx.BORDER_SIMPLE)
        self.editor.SetEditable(False)

        self.text = ''

        self.lb.Bind(wx.EVT_LISTBOX, self.OnListBoxSelect)
        self.Bind(wx.EVT_SIZE, self.OnSize)

        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(self.lb, 0, wx.EXPAND)
        sizer.Add((15,1))
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(self.canvas, 1, wx.EXPAND)
        vbox.Add((1, 15))
        vbox.Add(self.editor, 1, wx.EXPAND)
        sizer.Add(vbox, 1, wx.EXPAND)
        border = wx.BoxSizer()
        border.Add(sizer, 1, wx.EXPAND|wx.ALL, 30)
        self.SetSizer(border)

        wx.CallAfter(self.OnLoadSnippet)


    def OnLoadSnippet(self, index=0):
        snippet_file = gSnipDir + os.sep + '%s.py' % self.lb.GetString(self.lb.GetSelection())
        self.text = file(snippet_file).read()
        self.canvas.SetSnippet(self.text)
        self.editor.SetEditable(True)
        self.editor.SetValue(self.text)
        self.editor.SetEditable(False)

    def OnListBoxSelect(self, event):
        snippet_file = gSnipDir + os.sep + '%s.py' % event.GetString()
        self.text = file(snippet_file).read()
        self.canvas.SetSnippet(self.text)
        self.editor.SetEditable(True)
        self.editor.SetValue(self.text)
        self.editor.SetEditable(False)

    def OnSize(self, event):
        event.Skip()
        self.canvas.SetSnippet(self.text)
        self.editor.SetEditable(True)
        self.editor.SetValue(self.text)
        self.editor.SetEditable(False)


#- wxPy Demo -----------------------------------------------------------------


if not haveCairo:
    from wx.lib.msgpanel import MessagePanel
    def runTest(frame, nb, log):
        win = MessagePanel(nb, 'This demo requires the Pycairo package,\n'
                           'or there is some other unmet dependency.',
                           'Sorry', wx.ICON_WARNING)
        return win
else:
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
