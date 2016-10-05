#!/usr/bin/env python

#-Imports---------------------------------------------------------------------

#--wxPython Imports.
import wx


if __name__ == '__main__':
    app = wx.App()
    frame = wx.Frame(None, wx.ID_ANY, "Minimal PopupMenu Demo")
    panel = wx.Panel(frame, wx.ID_ANY)

    def OnContextMenu(event):
        # Make a menu.
        menu = wx.Menu()
        # Show how to add the items to the menu.
        myID1 = 101
        myID2 = 102
        item1 = wx.MenuItem(menu, myID1, "One")
        item2 = wx.MenuItem(menu, myID2, "Two")
        if 'phoenix' in wx.version():
            menu.Append(item1)
            menu.Append(item2)
        else:  # Classic
            menu.AppendItem(item1)
            menu.AppendItem(item2)
        menu.Bind(wx.EVT_MENU, OnPopupOne, id=myID1)
        menu.Bind(wx.EVT_MENU, OnPopupTwo, id=myID2)
        # Popup the menu.  If an item is selected then its handler
        # will be called before PopupMenu returns.
        evtObj = event.GetEventObject()
        evtObj.PopupMenu(menu)
        menu.Destroy()

    def OnPopupOne(event):
        print("Popup one")

    def OnPopupTwo(event):
        print("Popup two")

    panel.Bind(wx.EVT_CONTEXT_MENU, OnContextMenu)

    frame.CreateStatusBar().SetStatusText('wxPython %s' % wx.version())
    frame.Show()
    app.MainLoop()
