#!/usr/bin/env python
# -*- coding: utf-8 -*-

#--Python Imports.
import os
import sys

#--wxPython Imports.
import wx

#--Local Imports.
## import images

#-Globals----------------------------------------------------------------------
try:
    gFileDir = os.path.dirname(os.path.abspath(__file__))
except Exception:
    gFileDir = os.path.dirname(os.path.abspath(sys.argv[0]))
gBmpDir = gFileDir + os.sep + 'bitmaps'


#- wxPython Demo --------------------------------------------------------------
__wxPyOnlineDocs__ = 'http://wxpython.org/Phoenix/docs/html/ListCtrl.html'
__wxPyDemoPanel__ = 'TestPanel'

overview = """\
This example demonstrates the ListCtrl's Virtual List features. A Virtual list
can contain any number of cells, but data is not loaded into the control itself.
It is loaded on demand via virtual methods <code>OnGetItemText(), OnGetItemImage()</code>,
and <code>OnGetItemAttr()</code>. This greatly reduces the amount of memory required
without limiting what can be done with the list control itself.
"""



class TestVirtualListCtrl(wx.ListCtrl):
    def __init__(self, parent, log):
        wx.ListCtrl.__init__(
            self, parent, -1,
            style=wx.LC_REPORT|wx.LC_VIRTUAL|wx.LC_HRULES|wx.LC_VRULES
            )

        self.log = log

        self.il = wx.ImageList(16, 16)
        ## self.idx1 = self.il.Add(images.Smiles.GetBitmap())
        self.idx1 = self.il.Add(wx.Bitmap(gBmpDir + os.sep + 'smiles.bmp', wx.BITMAP_TYPE_BMP))
        empty = self.makeBlank()
        self.idx2 = self.il.Add(empty)
        self.SetImageList(self.il, wx.IMAGE_LIST_SMALL)

        self.InsertColumn(0, "First")
        self.InsertColumn(1, "Second")
        self.InsertColumn(2, "Third")
        self.SetColumnWidth(0, 175)
        self.SetColumnWidth(1, 175)
        self.SetColumnWidth(2, 175)

        self.SetItemCount(1000000)

        self.attr1 = wx.ListItemAttr()
        self.attr1.SetBackgroundColour("yellow")

        self.attr2 = wx.ListItemAttr()
        self.attr2.SetBackgroundColour("light blue")

        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnItemSelected)
        self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnItemActivated)
        self.Bind(wx.EVT_LIST_ITEM_DESELECTED, self.OnItemDeselected)


    def makeBlank(self):
        empty = wx.Bitmap(16, 16, 32)
        dc = wx.MemoryDC(empty)
        dc.SetBackground(wx.Brush((0, 0, 0, 0)))
        dc.Clear()
        del dc
        empty.SetMaskColour((0, 0, 0))
        return empty

    def OnItemSelected(self, event):
        self.currentItem = event.Index
        self.log.WriteText('OnItemSelected: "%s", "%s", "%s", "%s"\n' %
                           (self.currentItem,
                            self.GetItemText(self.currentItem),
                            self.getColumnText(self.currentItem, 1),
                            self.getColumnText(self.currentItem, 2)))

    def OnItemActivated(self, event):
        self.currentItem = event.Index
        self.log.WriteText("OnItemActivated: %s\nTopItem: %s\n" %
                           (self.GetItemText(self.currentItem), self.GetTopItem()))

    def getColumnText(self, index, col):
        item = self.GetItem(index, col)
        return item.GetText()

    def OnItemDeselected(self, evt):
        self.log.WriteText("OnItemDeselected: %s" % evt.Index)

    #-----------------------------------------------------------------
    # These methods are callbacks for implementing the "virtualness"
    # of the list...  Normally you would determine the text,
    # attributes and/or image based on values from some external data
    # source, but for this demo we'll just calculate them
    def OnGetItemText(self, item, col):
        return "Item %d, column %d" % (item, col)

    def OnGetItemImage(self, item):
        if item % 3 == 0:
            return self.idx1
        else:
            return self.idx2

    def OnGetItemAttr(self, item):
        if item % 3 == 1:
            return self.attr1
        elif item % 3 == 2:
            return self.attr2
        else:
            return None


class TestPanel(wx.Panel):
    def __init__(self, parent, log):
        wx.Panel.__init__(self, parent, -1, style=wx.WANTS_CHARS)

        self.log = log
        sizer = wx.BoxSizer(wx.VERTICAL)

        if wx.Platform == "__WXMAC__" and \
               hasattr(wx.GetApp().GetTopWindow(), "LoadDemo"):
            self.useNative = wx.CheckBox(self, -1, "Use native listctrl")
            self.useNative.SetValue(
                not wx.SystemOptions.GetOptionInt("mac.listctrl.always_use_generic") )
            self.Bind(wx.EVT_CHECKBOX, self.OnUseNative, self.useNative)
            sizer.Add(self.useNative, 0, wx.ALL | wx.ALIGN_RIGHT, 4)

        self.list = TestVirtualListCtrl(self, self.log)
        sizer.Add(self.list, 1, wx.EXPAND)

        self.SetSizer(sizer)
        self.SetAutoLayout(True)

    def OnUseNative(self, event):
        wx.SystemOptions.SetOptionInt("mac.listctrl.always_use_generic", not event.IsChecked())
        wx.GetApp().GetTopWindow().LoadDemo("ListCtrl_virtual")


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
