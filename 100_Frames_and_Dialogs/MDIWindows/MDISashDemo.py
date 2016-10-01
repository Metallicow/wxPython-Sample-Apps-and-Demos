#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-Imports----------------------------------------------------------------------

#--Python Imports.
import random

#--wxPython Imports.
import wx
if not 'phoenix' in wx.version():  # Classic
    wx.adv = wx
else:
    import wx.adv

#-Globals----------------------------------------------------------------------

# There are better ways to do IDs, but this demo requires that the window
# IDs be in a specific range. There are better ways to do that, too, but
# this will do for purposes of this demo.

ID_WINDOW_TOP       = 5000
ID_WINDOW_LEFT1     = 5001
ID_WINDOW_LEFT2     = 5002
ID_WINDOW_BOTTOM    = 5003


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
        wx.MDIParentFrame.__init__(
            self, None, -1, "MDI Parent", size=(600,400),
            style = wx.DEFAULT_FRAME_STYLE | wx.HSCROLL | wx.VSCROLL
            )

        self.winCount = 0
        menu = wx.Menu()
        menu.Append(wx.ID_NEW, "&New Window\tCtrl+N")
        menu.AppendSeparator()
        menu.Append(wx.ID_EXIT, "E&xit")

        menubar = wx.MenuBar()
        menubar.Append(menu, "&File")
        self.SetMenuBar(menubar)

        #self.CreateStatusBar()

        self.Bind(wx.EVT_MENU, self.OnNewWindow, id=wx.ID_NEW)
        self.Bind(wx.EVT_MENU, self.OnExit, id=wx.ID_EXIT)

        self.Bind(
            wx.adv.EVT_SASH_DRAGGED_RANGE, self.OnSashDrag, id=ID_WINDOW_TOP,
            id2=ID_WINDOW_BOTTOM
            )

        self.Bind(wx.EVT_SIZE, self.OnSize)

        # Create some layout windows
        # A window like a toolbar
        win = wx.adv.SashLayoutWindow(self, ID_WINDOW_TOP, style=wx.NO_BORDER|wx.adv.SW_3D)
        win.SetDefaultSize((1000, 30))
        win.SetOrientation(wx.adv.LAYOUT_HORIZONTAL)
        win.SetAlignment(wx.adv.LAYOUT_TOP)
        win.SetBackgroundColour(wx.Colour(255, 0, 0))
        win.SetSashVisible(wx.adv.SASH_BOTTOM, True)

        self.topWindow = win

        # A window like a statusbar
        win = wx.adv.SashLayoutWindow(self, ID_WINDOW_BOTTOM, style=wx.NO_BORDER|wx.adv.SW_3D)
        win.SetDefaultSize((1000, 30))
        win.SetOrientation(wx.adv.LAYOUT_HORIZONTAL)
        win.SetAlignment(wx.adv.LAYOUT_BOTTOM)
        win.SetBackgroundColour(wx.Colour(0, 0, 255))
        win.SetSashVisible(wx.adv.SASH_TOP, True)

        self.bottomWindow = win

        # A window to the left of the client window
        win =  wx.adv.SashLayoutWindow(self, ID_WINDOW_LEFT1, style=wx.NO_BORDER|wx.adv.SW_3D)
        win.SetDefaultSize((120, 1000))
        win.SetOrientation(wx.adv.LAYOUT_VERTICAL)
        win.SetAlignment(wx.adv.LAYOUT_LEFT)
        win.SetBackgroundColour(wx.Colour(0, 255, 0))
        win.SetSashVisible(wx.adv.SASH_RIGHT, True)
        win.SetExtraBorderSize(10)
        textWindow = wx.TextCtrl(win, -1, "", style=wx.TE_MULTILINE|wx.SUNKEN_BORDER)
        textWindow.SetValue("A sub window")

        self.leftWindow1 = win

        # Another window to the left of the client window
        win = wx.adv.SashLayoutWindow(self, ID_WINDOW_LEFT2, style=wx.NO_BORDER|wx.adv.SW_3D)
        win.SetDefaultSize((120, 1000))
        win.SetOrientation(wx.adv.LAYOUT_VERTICAL)
        win.SetAlignment(wx.adv.LAYOUT_LEFT)
        win.SetBackgroundColour(wx.Colour(0, 255, 255))
        win.SetSashVisible(wx.adv.SASH_RIGHT, True)

        self.leftWindow2 = win


    def OnSashDrag(self, event):
        if event.GetDragStatus() == wx.adv.SASH_STATUS_OUT_OF_RANGE:
            return

        eID = event.GetId()

        if eID == ID_WINDOW_TOP:
            self.topWindow.SetDefaultSize((1000, event.GetDragRect().height))
        elif eID == ID_WINDOW_LEFT1:
            self.leftWindow1.SetDefaultSize((event.GetDragRect().width, 1000))
        elif eID == ID_WINDOW_LEFT2:
            self.leftWindow2.SetDefaultSize((event.GetDragRect().width, 1000))
        elif eID == ID_WINDOW_BOTTOM:
            self.bottomWindow.SetDefaultSize((1000, event.GetDragRect().height))

        wx.adv.LayoutAlgorithm().LayoutMDIFrame(self)
        self.GetClientWindow().Refresh()

    def OnSize(self, event):
        wx.adv.LayoutAlgorithm().LayoutMDIFrame(self)

    def OnExit(self, event):
        self.Close(True)

    def OnNewWindow(self, event):
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
