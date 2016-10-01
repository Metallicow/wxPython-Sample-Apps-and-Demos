#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-Imports----------------------------------------------------------------------

#--Python Imports.
import random

#--wxPython Imports.
import wx


#-Globals----------------------------------------------------------------------
HEX = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
NUM = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def random_hex_color():
    random.shuffle(HEX) # Order is random now
    ## print(HEX)
    randomcolor = ''
    for item in range(0, 6):
        random.shuffle(HEX) # Twice for doubles and good luck :)
        ## print(HEX[item])
        randomcolor = randomcolor + '%s' % HEX[item]
    ## print(randomcolor)
    return '#%s' % randomcolor


class MyParentFrame(wx.MDIParentFrame):
    def __init__(self):
        wx.MDIParentFrame.__init__(self, None, -1, "MDI Parent", size=(600, 400))

        self.winCount = 0
        menu = wx.Menu()
        menu.Append(wx.ID_NEW, "&New Window\tCtrl+N")
        menu.AppendSeparator()
        menu.Append(wx.ID_EXIT, "E&xit")

        menubar = wx.MenuBar()
        menubar.Append(menu, "&File")
        self.SetMenuBar(menubar)

        self.CreateStatusBar()

        self.Bind(wx.EVT_MENU, self.OnNewWindow, id=wx.ID_NEW)
        self.Bind(wx.EVT_MENU, self.OnExit, id=wx.ID_EXIT)


    def OnExit(self, evt):
        self.Close(True)

    def OnNewWindow(self, evt):
        self.winCount = self.winCount + 1
        win = wx.MDIChildFrame(self, -1, "Child Window: %d" % self.winCount)
        canvas = wx.Panel(win)
        canvas.SetBackgroundColour(random_hex_color())
        win.Show(True)



#- __main__ -------------------------------------------------------------------


if __name__ == '__main__':
    class MyApp(wx.App):
        def OnInit(self):
            # wx.InitAllImageHandlers()
            frame = MyParentFrame()
            frame.Show(True)
            self.SetTopWindow(frame)
            return True

    app = MyApp(False)
    app.MainLoop()
