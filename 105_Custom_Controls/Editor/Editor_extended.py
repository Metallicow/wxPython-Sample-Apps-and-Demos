#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-Imports----------------------------------------------------------------------

#--wxPython Imports.
import wx
import wx.lib.editor as editor

#- wxPython Demo --------------------------------------------------------------
__wxPyOnlineDocs__ = 'http://wxpython.org/Phoenix/docs/html/wx.lib.editor.html'
__wxPyDemoPanel__ = 'TestPanel'

overview = """
The Editor class implements a simple text editor using wxPython.  You
can create a custom editor by subclassing Editor.  Even though much of
the editor is implemented in Python, it runs surprisingly smoothly on
normal hardware with small files.

How to use it
-------------
The demo code (demo/Editor.py) shows how to use Editor as a simple text
box. Use the SetText() and GetText() methods to set or get text from
the component; these both use a list of strings.

The samples/FrogEdit directory has an example of a simple text editor
application that uses the Editor component.

Subclassing
-----------
To add or change functionality, you can subclass this
component. One example of this might be to change the key
Alt key commands. In that case you would (for example) override the
SetAltFuncs() method.

"""


class TestPanel(wx.Panel):
    def __init__(self, parent, log):
        self.log = log
        wx.Panel.__init__(self, parent, -1)
        ed = TestEditor(self, log)
        box = wx.BoxSizer(wx.VERTICAL)
        box.Add(ed, 1, wx.ALL | wx.GROW, 1)
        self.SetSizer(box)
        self.SetAutoLayout(True)
    
    
class TestEditor(editor.Editor):
    def __init__(self, parent, log, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.SUNKEN_BORDER):
        editor.Editor.__init__(self, parent, id, pos, size, style)

        self.SetText(["",
                      "This is a simple text editor, the class name is",
                      "Editor.  Type a few lines and try it out.",
                      "",
                      "It uses Windows-style key commands that can be overridden by subclassing.",
                      "Mouse select works. Here are the key commands:",
                      "",
                      "Cursor movement:     Arrow keys or mouse",
                      "Beginning of line:   Home",
                      "End of line:         End",
                      "Beginning of buffer: Control-Home",
                      "End of the buffer:   Control-End",
                      "Select text:         Hold down Shift while moving the cursor",
                      "Copy:                Control-Insert, Control-C",
                      "Cut:                 Shift-Delete,   Control-X",
                      "Paste:               Shift-Insert,   Control-V",
                      ""])
                
                
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
        gMainWin.SetTitle('Test Editor Demo')
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
