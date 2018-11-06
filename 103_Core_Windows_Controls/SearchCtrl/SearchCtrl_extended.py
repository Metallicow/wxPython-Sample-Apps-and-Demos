#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-Imports----------------------------------------------------------------------

#--wxPython Imports.
import  wx

#- wxPython Demo --------------------------------------------------------------
__wxPyOnlineDocs__ = 'https://wxpython.org/Phoenix/docs/html/wx.SearchCtrl.html'
__wxPyDemoPanel__ = 'TestPanel'

overview = """<html><body>
<h2><center>wx.SearchCtrl</center></h2>

A search control is a composite control with a 
search button, a text control, and a cancel button.
</body></html>
"""

#----------------------------------------------------------------------

class TestPanel(wx.Panel):
    def __init__(self, parent, log):
        self.log = log
        wx.Panel.__init__(self, parent)

        # Create controls.
        sb = wx.StaticBox(self, -1, "Options")
        searchBtnOpt = wx.CheckBox(self, -1, "Search button")
        searchBtnOpt.SetValue(True)
        cancelBtnOpt = wx.CheckBox(self, -1, "Cancel button")
        menuBtnOpt   = wx.CheckBox(self, -1, "Search menu")

        self.search = wx.SearchCtrl(self, size=(200,-1), style=wx.TE_PROCESS_ENTER)
        self.search.SetDescriptiveText("Set Descriptive Text")

        # Setup the layout.
        box = wx.StaticBoxSizer(sb, wx.VERTICAL)
        box.Add(searchBtnOpt, 0, wx.ALL, 5)
        box.Add(cancelBtnOpt, 0, wx.ALL, 5)
        box.Add(menuBtnOpt,   0, wx.ALL, 5)

        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(box, 0, wx.ALL, 15)
        sizer.Add((15,15))
        sizer.Add(self.search, 0, wx.ALL, 15)

##         self.tc = wx.TextCtrl(self)  # just for testing that heights match...
##         sizer.Add(self.tc, 0, wx.TOP, 15)

        self.SetSizer(sizer)

        # Set event bindings.
        self.Bind(wx.EVT_CHECKBOX, self.OnToggleSearchButton, searchBtnOpt)
        self.Bind(wx.EVT_CHECKBOX, self.OnToggleCancelButton, cancelBtnOpt)
        self.Bind(wx.EVT_CHECKBOX, self.OnToggleSearchMenu, menuBtnOpt)

        self.Bind(wx.EVT_SEARCHCTRL_SEARCH_BTN, self.OnSearch, self.search)
        self.Bind(wx.EVT_SEARCHCTRL_CANCEL_BTN, self.OnCancel, self.search)
        self.Bind(wx.EVT_TEXT_ENTER, self.OnDoSearch, self.search)
        ##self.Bind(wx.EVT_TEXT, self.OnDoSearch, self.search)


    def OnToggleSearchButton(self, event):
        self.search.ShowSearchButton(event.GetInt())

    def OnToggleCancelButton(self, event):
        self.search.ShowCancelButton(event.GetInt())

    def OnToggleSearchMenu(self, event):
        if event.GetInt():
            menu = self.MakeMenu()
            self.search.SetMenu(menu)
        else:
            self.search.SetMenu(None)

    def OnSearch(self, event):
        self.log.WriteText("OnSearch")

    def OnCancel(self, event):
        self.log.WriteText("OnCancel")

    def OnDoSearch(self, event):
        self.log.WriteText("OnDoSearch: " + self.search.GetValue())

    def MakeMenu(self):
        menu = wx.Menu()
        item = menu.Append(-1, "Recent Searches")
        item.Enable(False)
        for txt in ["You can maintain",
                    "a list of old",
                    "search strings here",
                    "and bind EVT_MENU to",
                    "catch their selections"]:
            menu.Append(-1, txt)
        return menu


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

