#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-Imports----------------------------------------------------------------------

#--Python Imports.
import os

#--wxPython Imports.
import wx

#- wxPython Demo --------------------------------------------------------------
__wxPyOnlineDocs__ = 'http://wxpython.org/Phoenix/docs/html/FileHistory.html'
__wxPyDemoPanel__ = 'TestPanel'

overview = """<html><body>
<h3>FileHistory</h3>

wxFileHistory encapsulates functionality to record the last few files
visited, and to allow the user to quickly load these files using the
list appended to a menu, such as the File menu.

<p>Note that this inclusion is not automatic; as illustrated in this example,
you must add files (and remove them) as deemed necessary within the framework
of your program.

<p>Note also the additional cleanup required for this class, namely trapping the
enclosing window's Destroy event and deleting the file history control and its
associated menu.
</body></html>
"""


def runTest(frame, nb, log):
    win = TestPanel(nb, log)
    return win


#----------------------------------------------------------------------

text = """\
Right-click on the panel above the line to get a menu.  This menu will
be managed by a FileHistory object and so the files you select will
automatically be added to the end of the menu and will be selectable
the next time the menu is viewed.  The filename selected, either via the
Open menu item, or from the history, will be displayed in the log
window below.
"""

#----------------------------------------------------------------------

class TestPanel(wx.Panel):
    def __init__(self, parent, log):
        self.log = log
        wx.Panel.__init__(self, parent, -1)
        box = wx.BoxSizer(wx.VERTICAL)

        # Make and layout the controls
        fs = self.GetFont().GetPointSize()
        bf = wx.Font(fs+4, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        nf = wx.Font(fs+2, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)

        t = wx.StaticText(self, wx.ID_ANY, "FileHistory")
        t.SetFont(bf)
        box.Add(t, 0, wx.CENTER|wx.ALL, 5)

        box.Add(wx.StaticLine(self, -1), 0, wx.EXPAND)
        box.Add((10,20))

        t = wx.StaticText(self, -1, text)
        t.SetFont(nf)
        box.Add(t, 0, wx.CENTER | wx.ALL, 5)

        self.SetSizer(box)
        self.SetAutoLayout(True)

        # Make a menu
        self.menu = m = wx.Menu()

        # Little know wx Fact #42: there are a number of pre-set IDs
        # in the wx package, to be used for common controls such as those
        # illustrated below. Neat, huh?
        m.Append(wx.ID_NEW,     "&New")
        m.Append(wx.ID_OPEN,    "&Open...")
        m.Append(wx.ID_CLOSE,   "&Close")
        m.Append(wx.ID_SAVE,    "&Save")
        m.Append(wx.ID_SAVEAS,  "Save &as...")
        m.Enable(wx.ID_NEW, False)
        m.Enable(wx.ID_CLOSE, False)
        m.Enable(wx.ID_SAVE, False)
        m.Enable(wx.ID_SAVEAS, False)

        # and a file history
        self.filehistory = wx.FileHistory()
        self.filehistory.UseMenu(self.menu)

        # and finally the event handler bindings
        self.Bind(wx.EVT_RIGHT_UP, self.OnRightClick)

        self.Bind(wx.EVT_MENU, self.OnFileOpenDialog, id=wx.ID_OPEN)

        self.Bind(
            wx.EVT_MENU_RANGE, self.OnFileHistory, id=wx.ID_FILE1, id2=wx.ID_FILE9
            )

        self.Bind(wx.EVT_WINDOW_DESTROY, self.Cleanup)


    def Cleanup(self, *args):
        # A little extra cleanup is required for the FileHistory control
        del self.filehistory
        self.menu.Destroy()

    def OnRightClick(self, evt):
        self.PopupMenu(self.menu)

    def OnFileOpenDialog(self, evt):
        dlg = wx.FileDialog(self,
                           defaultDir = os.getcwd(),
                           wildcard = "All Files|*",
                           style = wx.FD_OPEN | wx.FD_CHANGE_DIR)

        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            self.log.write("You selected %s\n" % path)

            # add it to the history
            self.filehistory.AddFileToHistory(path)

        dlg.Destroy()

    def OnFileHistory(self, evt):
        # get the file based on the menu ID
        fileNum = evt.GetId() - wx.ID_FILE1
        path = self.filehistory.GetHistoryFile(fileNum)
        self.log.write("You selected %s\n" % path)

        # add it back to the history so it will be moved up the list
        self.filehistory.AddFileToHistory(path)


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
