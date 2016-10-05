#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-Imports----------------------------------------------------------------------

#--Python Imports.
import os
import sys
import time

#--wxPython Imports.
import wx

#-Globals----------------------------------------------------------------------
try:
    gFileDir = os.path.dirname(os.path.abspath(__file__))
except:
    gFileDir = os.path.dirname(os.path.abspath(sys.argv[0]))
gBmpDir = gFileDir + os.sep + 'bitmaps'

#- wxPython Demo --------------------------------------------------------------
__wxPyOnlineDocs__ = 'http://wxpython.org/Phoenix/docs/html/Menu.html'
__wxPyDemoPanel__ = 'TestPanel'

overview = """\
<html><body>
 <center><h2>wx.Menu</h2></center>
 <p>
 A demo of using wx.MenuBar and wx.Menu in various ways.
 <p>
 A menu is a popup (or pull down) list of items, one of which may be selected
 before the menu goes away (clicking elsewhere dismisses the menu).
 Menus may be used to construct either menu bars or popup menus.
 <p>
 A menu item has an integer ID associated with it which can be used to identify
 the selection, or to change the menu item in some way. A menu item with a
 special identifier -1 is a separator item and doesn't have an associated
 command but just makes a separator line appear in the menu.
 <p>
 Menu items may be either normal items, check items or radio items.
 Normal items don't have any special properties while the check items have a
 boolean flag associated to them and they show a checkmark in the menu when
 the flag is set. wxWindows automatically toggles the flag value when the item
 is clicked and its value may be retrieved using either IsChecked method of
 wx.Menu or wx.MenuBar itself or by using wxEvent.IsChecked when you get the
 menu notification for the item in question.
 <p>
 The radio items are similar to the check items except that all the other items
 in the same radio group are unchecked when a radio item is checked. The radio
 group is formed by a contiguous range of radio items, i.e. it starts at the
 first item of this kind and ends with the first item of a different kind
 (or the end of the menu). Notice that because the radio groups are defined in
 terms of the item positions inserting or removing the items in the menu
 containing the radio items risks to not work correctly. Finally note that
 the radio items are only supported under Windows and GTK+ currently.
</body></html>
"""


class MyFrame(wx.Frame):

    def __init__(self, parent, id, log):
        wx.Frame.__init__(self, parent, id, 'Playing with menus', size=(500, 250))
        self.log = log
        self.CenterOnScreen()

        self.CreateStatusBar()
        self.SetStatusText("This is the statusbar")

        tc = wx.TextCtrl(self, -1, (
            "A bunch of bogus menus have been created for this frame. "
            "You can play around with them to see how they behave and then "
            "check the source for this sample to see how to implement them."
            ), style=wx.TE_READONLY | wx.TE_MULTILINE)

        # Prepare the menu bar
        menuBar = wx.MenuBar()

        # 1st menu from left
        menu1 = wx.Menu()
        menu1.Append(101, "&Mercury", "This the text in the Statusbar")
        menu1.Append(102, "&Venus", "")
        menu1.Append(103, "&Earth", "You may select Earth too")
        menu1.AppendSeparator()
        menu1.Append(104, "&Close", "Close this frame")
        # Add menu to the menu bar
        menuBar.Append(menu1, "&Planets")

        # 2nd menu from left
        menu2 = wx.Menu()
        menu2.Append(201, "Hydrogen")
        menu2.Append(202, "Helium")
        # a submenu in the 2nd menu
        submenu = wx.Menu()
        submenu.Append(2031,"Lanthanium")
        submenu.Append(2032,"Cerium")
        submenu.Append(2033,"Praseodymium")
        menu2.Append(203, "Lanthanides", submenu)
        # Append 2nd menu
        menuBar.Append(menu2, "&Elements")

        menu3 = wx.Menu()
        # Radio items
        menu3.Append(301, "IDLE", "a Python shell using tcl/tk as GUI", wx.ITEM_RADIO)
        menu3.Append(302, "PyCrust", "a Python shell using wxPython as GUI", wx.ITEM_RADIO)
        menu3.Append(303, "psi", "a simple Python shell using wxPython as GUI", wx.ITEM_RADIO)
        menu3.AppendSeparator()
        menu3.Append(304, "project1", "", wx.ITEM_NORMAL)
        menu3.Append(305, "project2", "", wx.ITEM_NORMAL)
        menuBar.Append(menu3, "&Shells")

        menu4 = wx.Menu()
        # Check menu items
        menu4.Append(401, "letters", "abcde...", wx.ITEM_CHECK)
        menu4.Append(402, "digits", "123...", wx.ITEM_CHECK)
        menu4.Append(403, "letters and digits", "abcd... + 123...", wx.ITEM_CHECK)
        menuBar.Append(menu4, "Chec&k")

        menu5 = wx.Menu()
        # Show how to put an icon in the menu item
        item = wx.MenuItem(menu5, 500, "&Smile!\tCtrl+S", "This one has an icon")
        bmp = wx.Bitmap(gBmpDir + os.sep + 'smiley16.png', wx.BITMAP_TYPE_PNG)
        item.SetBitmap(bmp)
        menu5.Append(item)

        menuitemwithbmp = wx.MenuItem(menu5, wx.ID_ANY, "Submenu with Bitmap")
        # Show how to change the background colour of the menu item
        menuitemwithbmp.SetBackgroundColour(wx.YELLOW)
        # Show how to change the menu item's text colour
        menuitemwithbmp.SetTextColour(wx.BLUE)
        # Show how to change the menu item's font
        fnt = wx.Font(10,
                      wx.FONTFAMILY_DEFAULT,
                      wx.FONTSTYLE_NORMAL,
                      wx.FONTWEIGHT_BOLD,
                      False, '')
        menuitemwithbmp.SetFont(fnt)
        submenu = wx.Menu(style=wx.MENU_TEAROFF)
        submenu.Append(wx.MenuItem(menu5, wx.ID_ANY, "Woot!"))
        bmp = wx.Bitmap(gBmpDir + os.sep + 'book16.png', wx.BITMAP_TYPE_PNG)
        menuitemwithbmp.SetBitmap(bmp)
        menuitemwithbmp.SetSubMenu(submenu)
        menu5.Append(menuitemwithbmp)

        # Shortcuts
        menu5.Append(501, "Interesting thing\tCtrl+A", "Note the shortcut!")
        menu5.AppendSeparator()
        menu5.Append(502, "Hello\tShift+H")
        menu5.AppendSeparator()
        menu5.Append(503, "remove the submenu")
        menu6 = wx.Menu()
        menu6.Append(601, "Submenu Item")
        menu5.Append(504, "submenu", menu6)
        menu5.Append(505, "remove this menu")
        menu5.Append(506, "this is updated")
        menu5.Append(507, "insert after this...")
        menu5.Append(508, "...and before this")
        menuBar.Append(menu5, "&Fun")

        self.stockIDsMenu = self.CreateStockIDMenu()
        menuBar.Append(self.stockIDsMenu, "&StockIDs")

        self.SetMenuBar(menuBar)

        # Menu events
        self.Bind(wx.EVT_MENU_HIGHLIGHT_ALL, self.OnMenuHighlight)

        self.Bind(wx.EVT_MENU, self.Menu101, id=101)
        self.Bind(wx.EVT_MENU, self.Menu102, id=102)
        self.Bind(wx.EVT_MENU, self.Menu103, id=103)
        self.Bind(wx.EVT_MENU, self.CloseWindow, id=104)

        self.Bind(wx.EVT_MENU, self.Menu201, id=201)
        self.Bind(wx.EVT_MENU, self.Menu202, id=202)
        self.Bind(wx.EVT_MENU, self.Menu2031, id=2031)
        self.Bind(wx.EVT_MENU, self.Menu2032, id=2032)
        self.Bind(wx.EVT_MENU, self.Menu2033, id=2033)

        self.Bind(wx.EVT_MENU, self.Menu301To303, id=301)
        self.Bind(wx.EVT_MENU, self.Menu301To303, id=302)
        self.Bind(wx.EVT_MENU, self.Menu301To303, id=303)
        self.Bind(wx.EVT_MENU, self.Menu304, id=304)
        self.Bind(wx.EVT_MENU, self.Menu305, id=305)

        # Range of menu items.
        self.Bind(wx.EVT_MENU_RANGE, self.Menu401To403, id=401, id2=403)

        self.Bind(wx.EVT_MENU, self.Menu500, id=500)
        self.Bind(wx.EVT_MENU, self.Menu501, id=501)
        self.Bind(wx.EVT_MENU, self.Menu502, id=502)
        self.Bind(wx.EVT_MENU, self.TestRemove, id=503)
        self.Bind(wx.EVT_MENU, self.TestRemove2, id=505)
        self.Bind(wx.EVT_MENU, self.TestInsert, id=507)
        self.Bind(wx.EVT_MENU, self.TestInsert, id=508)

        wx.GetApp().Bind(wx.EVT_UPDATE_UI, self.TestUpdateUI, id=506)

    # Methods
        wx.CallAfter(self.RemoveEmptyStockMenuItems)


    def RemoveEmptyStockMenuItems(self):
        menuItemsList = self.stockIDsMenu.GetMenuItems()
        for menuItem in menuItemsList:
            if not self.stockIDsMenu.GetLabelText(menuItem.GetId()):
                self.stockIDsMenu.RemoveItem(menuItem.GetId())
        # Add the Seperator back in
        self.stockIDsMenu.Insert(0, wx.ID_ANY, 'wx.StockID MenuItems')
        self.stockIDsMenu.Insert(1, wx.ID_SEPARATOR)

    def CreateStockIDMenu(self):
        m = wx.Menu()
        for i in dir(wx):
            if i.startswith('ID_'):
                try:
                    mi = m.Append(eval('wx.%s' % i))
                except Exception as exc:
                    pass
        return m

    def OnMenuHighlight(self, event):
        # Show how to get menu item info from this event handler.
        id = event.GetMenuId()
        item = self.GetMenuBar().FindItemById(id)
        if item:
            text = item.GetText()
            help = item.GetHelp()
            ## print(text, item)
        # ...but in this case just call Skip so the default is done.
        event.Skip()

    def Menu101(self, event):
        self.log.WriteText('Welcome to Mercury\n')

    def Menu102(self, event):
        self.log.WriteText('Welcome to Venus\n')

    def Menu103(self, event):
        self.log.WriteText('Welcome to the Earth\n')

    def CloseWindow(self, event):
        self.Close()

    def Menu201(self, event):
        self.log.WriteText('Chemical element number 1\n')

    def Menu202(self, event):
        self.log.WriteText('Chemical element number 2\n')

    def Menu2031(self, event):
        self.log.WriteText('Element number 57\n')

    def Menu2032(self, event):
        self.log.WriteText('Element number 58\n')

    def Menu2033(self, event):
        self.log.WriteText('Element number 59\n')

    def Menu301To303(self, event):
        id = event.GetId()
        self.log.WriteText('Event id: %d\n' % id)

    def Menu304(self, event):
        self.log.WriteText('Not yet available\n')

    def Menu305(self, event):
        self.log.WriteText('Still vapour\n')

    def Menu401To403(self, event):
        self.log.WriteText('From a EVT_MENU_RANGE event\n')

    def Menu500(self, event):
        self.log.WriteText('Have a happy day!\n')

    def Menu501(self, event):
        self.log.WriteText('Look in the code how the shortcut has been realized\n')

    def Menu502(self, event):
        self.log.WriteText('Hello from Jean-Michel\n')

    def TestRemove(self, event):
        mb = self.GetMenuBar()
        submenuItem = mb.FindItemById(601)

        if not submenuItem:
            return

        submenu = submenuItem.GetMenu()
        menu = submenu.GetParent()

        # This works
        #menu.Remove(504)

        # this also works
        menu.RemoveItem(mb.FindItemById(504))

        # This doesn't work, as expected since submenuItem is not on menu
        #menu.RemoveItem(submenuItem)

    def TestRemove2(self, event):
        mb = self.GetMenuBar()
        mb.Remove(4)

    def TestUpdateUI(self, event):
        text = time.ctime()
        event.SetText(text)

    def TestInsert(self, event):
        theID = 508
        # get the menu
        mb = self.GetMenuBar()
        menuItem = mb.FindItemById(theID)
        menu = menuItem.GetMenu()

        # figure out the position to insert at
        pos = 0

        for i in menu.GetMenuItems():
            if i.GetId() == theID:
                break

            pos += 1

        # now insert the new item
        ID = wx.NewId()
        item = wx.MenuItem(menu, ID, "NewItem " + str(ID))
        menu.InsertItem(pos, item)


class TestPanel(wx.Panel):
    def __init__(self, parent, log):
        self.log = log
        wx.Panel.__init__(self, parent, -1)

        b = wx.Button(self, -1, "Show the Menu sample", (50,50))
        self.Bind(wx.EVT_BUTTON, self.OnButton, b)


    def OnButton(self, event):
        win = MyFrame(self, -1, self.log)
        win.Show(True)


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
