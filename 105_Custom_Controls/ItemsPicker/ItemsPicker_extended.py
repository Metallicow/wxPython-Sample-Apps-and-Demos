#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-Imports----------------------------------------------------------------------
#--Python Imports.
import os
import sys

#--wxPython Imports.
import wx
from wx.lib.itemspicker import (ItemsPicker,
                                EVT_IP_SELECTION_CHANGED,
                                IP_SORT_CHOICES, IP_SORT_SELECTED,
                                IP_REMOVE_FROM_CHOICES)

#-Globals----------------------------------------------------------------------
try:
    gFileDir = os.path.dirname(os.path.abspath(__file__))
except Exception:
    gFileDir = os.path.dirname(os.path.abspath(sys.argv[0]))
gBmpDir = gFileDir + os.sep + 'bitmaps'

#- wxPython Demo --------------------------------------------------------------
__wxPyOnlineDocs__ = 'http://wxpython.org/Phoenix/docs/html/lib.itemspicker.html'
__wxPyDemoPanel__ = 'TestPanel'

overview = """<html><body>
<h2><center>ItemsPicker</center></h2>

ItemsPicker is a widget that allows the user to choose a set of picked
items out of a given list

</body></html>
"""

#----------------------------------------------------------------------

class TestPanel(wx.Panel):
    def __init__(self, parent, log):
        self.log = log
        wx.Panel.__init__(self, parent, -1)
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        box = wx.StaticBox(self, -1, "ItemPicker styles")
        boxSizer = wx.StaticBoxSizer(box, wx.VERTICAL)
        self.sortChoices = wx.CheckBox(self, -1, 'IP_SORT_CHOICES')
        boxSizer.Add(self.sortChoices)
        self.sortSelected = wx.CheckBox(self, -1, 'IP_SORT_SELECTED')
        boxSizer.Add(self.sortSelected)
        self.removeFromChoices = wx.CheckBox(self, -1, 'IP_REMOVE_FROM_CHOICES')
        boxSizer.Add(self.removeFromChoices)
        sizer.Add(boxSizer, 0, wx.ALL, 10)
        b = wx.Button(self, -1, "Go")
        b.Bind(wx.EVT_BUTTON, self.Go)
        sizer.Add(b, 0, wx.ALL, 10)
        self.SetSizer(sizer)

    def Go(self, event):
        style = 0
        if self.sortChoices.GetValue():
            style |= IP_SORT_CHOICES
        if self.sortSelected.GetValue():
            style |= IP_SORT_SELECTED
        if self.removeFromChoices.GetValue():
            style |= IP_REMOVE_FROM_CHOICES
        d = ItemsPickerDialog(self, style, self.log)
        d.ShowModal()


class ItemsPickerDialog(wx.Dialog):
    def __init__(self, parent, style, log):
        wx.Dialog.__init__(self, parent, title='Pick some items...',
                           style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER)
        self.log = log
        sizer = wx.BoxSizer(wx.VERTICAL)
        b = wx.Button(self, -1, "Add Item")
        b.Bind(wx.EVT_BUTTON, self.OnAdd)
        sizer.Add(b, 0, wx.ALL, 5)
        self.ip = ItemsPicker(self, -1, choices=['ThisIsItem3', 'ThisIsItem6',
                                                 'ThisIsItem2', 'ThisIsItem5',
                                                 'ThisIsItem1', 'ThisIsItem4'],
                              label='Stuff:', selectedLabel='Selected stuff:',
                              ipStyle=style)
        self.ip.Bind(EVT_IP_SELECTION_CHANGED, self.OnSelectionChange)
        self.ip._source.SetMinSize((-1, 150))
        bmp2 = wx.Bitmap(gBmpDir + os.sep + "bp_btn2.png", wx.BITMAP_TYPE_PNG)
        self.ip.bAdd.SetBitmap(bmp2, dir=wx.RIGHT)
        self.ip.bAdd.SetLabel('Add')
        bmp1 = wx.Bitmap(gBmpDir + os.sep + "bp_btn1.png", wx.BITMAP_TYPE_PNG)
        self.ip.bRemove.SetBitmap(bmp1, dir=wx.LEFT)
        self.ip.bRemove.SetLabel('Remove')
        sizer.Add(self.ip, 1, wx.EXPAND | wx.ALL, 10)
        self.SetSizer(sizer)
        self.itemCount = 3
        self.Fit()
        self.SetMinSize(self.GetSize())

    def OnAdd(self, event):
        items = self.ip.GetItems()
        self.itemCount += 1
        newItem = "item%d" % self.itemCount
        self.ip.SetItems(items + [newItem])

    def OnSelectionChange(self, event):
        self.log.WriteText("EVT_IP_SELECTION_CHANGED %s\n" % \
                           ",".join(event.GetItems()))


#- wxPy Demo -----------------------------------------------------------------


def runTest(frame, nb, log):
    testWin = TestPanel(nb, log)
    return testWin


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
