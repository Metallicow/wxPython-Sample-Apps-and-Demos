#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This is a sample app based on wx.lib.colourdb I originally whipped up to help
out another user on the wxPython mailing list.
https://groups.google.com/d/topic/wxpython-users/CmSAzlVK8DY/discussion

- Metallicow

License: Free
"""

#-Imports---------------------------------------------------------------------

#--wxPython Imports.
import wx
import wx.lib.colourdb


#- wxPython Demo -------------------------------------------------------------
__wxPyOnlineDocs__ = 'http://wxpython.org/Phoenix/docs/html/wx.lib.colourdb.html'
__wxPyDemoPanel__ = 'TestPanel'

overview = """<html><body>
<h2><center>ColourDB</center></h2>

<p>wxWindows maintains a database of standard RGB colours for a predefined
set of named colours (such as "BLACK'', "LIGHT GREY''). The application
may add to this set if desired by using Append. There is only one instance
of this class: <b>TheColourDatabase</b>.

<p>The <code>colourdb</code> library is a lightweight API that pre-defines
a multitude of colors for you to use 'out of the box', and this demo serves
to show you these colors (it also serves as a handy reference).

<p>A secondary benefit of this demo is the use of the <b>ScrolledWindow</b> class
and the use of various *DC() classes, including background tiling and the use of
font data to generate a "building block" type of construct for repetitive use.

<p>
<B><font size=+2>Important note</font></b>

<p>
With implementation of V2.5 and later, it is required to have a wx.App already
initialized before <b><code>wx.updateColourDB()</code></b> can be called.
Trying to do otherwise will cause an exception to be raised.
</body></html>
"""


def runTest(frame, nb, log):
    win = TestPanel(nb, log)
    return win


class TestPanel(wx.Panel):
    def __init__(self, parent, log):
        self.log = log
        wx.Panel.__init__(self, parent, -1)

        btn = wx.Button(self, -1, "Show ColourDBSelector App", (50, 50))
        btn.Bind(wx.EVT_BUTTON, self.OnButton)

    def OnButton(self, event):
        frame = ColourDBSelectorFrame(None)
        frame.SetTitle('ColourDBSelector App')
        frame.Show()


#- Rippable Code -------------------------------------------------------------


class ColourDBSelectorPanel(wx.Panel):
    def __init__(self, parent, id=wx.ID_ANY,
                 pos=wx.DefaultPosition, size=wx.DefaultSize,
                 style=wx.BORDER_SIMPLE, name='panel'):
        wx.Panel.__init__(self, parent, id, pos, size, style, name)
        self.SetBackgroundColour(wx.WHITE)

        hwSizer = wx.WrapSizer(wx.HORIZONTAL)

        colorList = wx.lib.colourdb.getColourInfoList()
        # For each COLOR NAME that has a space in it, the next one is a duplicate
        # without a space.
        # Lets remove the duplicates ones with spaces so they are consistant
        # with standard UPPERCASE globals.
        self.colorList = [color for color in colorList if not ' ' in color[0]]
        print('len(self.colorList) = %s' % len(self.colorList))

        self.colorMenu = self.MakeContextMenu()
        self.Bind(wx.EVT_RIGHT_UP, self.OnRightUp)

        for color in self.colorList:
            win = wx.Window(self, -1, size=(12, 12), style=wx.BORDER_SIMPLE)
            win.SetBackgroundColour(wx.Colour(color[1], color[2], color[3]))
            ttStr = '%s' % (color[0] + '\n' + '(%s, %s, %s)' % (color[1], color[2], color[3]))
            win.SetToolTip(wx.ToolTip(ttStr))
            win.Bind(wx.EVT_LEFT_UP, self.OnLeftUp)
            hwSizer.Add(win, 0, wx.ALL, 2)

        self.SetSizer(hwSizer)

    def MakeContextMenu(self):
        m = wx.Menu()
        for color in self.colorList:
            m.Append(-1, '%s' % (color[0] + ' ' + '(%s, %s, %s)' % (color[1], color[2], color[3])))
        return m

    def OnRightUp(self, event):
        self.PopupMenu(self.colorMenu)

    def OnLeftUp(self, event):
        evtObj = event.GetEventObject()
        print(evtObj.GetBackgroundColour())
        # Do other code here...
        # Example: copy colour str to clipboard,
        # send colour somewhere to do something with,
        # etc...
        self.SetBackgroundColour(evtObj.GetBackgroundColour())
        self.Refresh()


#- __main__ Demo -------------------------------------------------------------


class printLog:
    def __init__(self):
        pass

    def write(self, txt):
        print('%s' % txt)

    def WriteText(self, txt):
        print('%s' % txt)


class ColourDBSelectorFrame(wx.Frame):
    def __init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString,
                 pos=wx.DefaultPosition, size=wx.DefaultSize,
                 style=wx.DEFAULT_FRAME_STYLE, name='frame'):
        wx.Frame.__init__(self, parent, id, title, pos, size, style, name)

        panel = ColourDBSelectorPanel(self)

        self.Bind(wx.EVT_CLOSE, self.OnDestroy)

    def OnDestroy(self, event):
        self.Destroy()


class ColourDBSelectorApp(wx.App):
    def OnInit(self):
        gMainWin = ColourDBSelectorFrame(None)
        gMainWin.SetTitle('ColourDBSelector App')
        gMainWin.Show()
        return True


#- __main__ ------------------------------------------------------------------



if __name__ == '__main__':
    import sys
    print('Python %s.%s.%s %s' % sys.version_info[0:4])
    print('wxPython %s' % wx.version())
    gApp = ColourDBSelectorApp(redirect=False,
                               filename=None,
                               useBestVisual=False,
                               clearSigInt=True)
    gApp.MainLoop()
