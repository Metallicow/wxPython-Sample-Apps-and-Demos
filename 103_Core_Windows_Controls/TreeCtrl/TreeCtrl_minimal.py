#!/usr/bin/env python

#-Imports---------------------------------------------------------------------

#--wxPython Imports.
import wx


if __name__ == '__main__':
    app = wx.App()
    frame = wx.Frame(None, -1, 'Minimal TreeCtrl Demo - wxPython %s' % wx.version())
    frame.treectrl = tree = wx.TreeCtrl(frame, -1)
    frame.treectrl.root = root = tree.AddRoot("The Root Item")
    for x in range(3):
        child = tree.AppendItem(root, "Item %d" % x)
        tree.SetItemData(child, None)

        for y in range(3):
            last = tree.AppendItem(child, "item %d-%s" % (x, chr(ord("a") + y)))
            tree.SetItemData(last, None)

            for z in range(3):
                item = tree.AppendItem(last, "item %d-%s-%d" % (x, chr(ord("a") + y), z))
                tree.SetItemData(item, None)
    tree.ExpandAll()
    tree.SelectItem(root)
    frame.Show()
    app.MainLoop()
