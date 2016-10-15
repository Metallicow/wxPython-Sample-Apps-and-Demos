#!/usr/bin/env python
# -*- coding: utf-8 -*-

#--wxPython Imports.
import wx
from wx.lib.combotreebox import ComboTreeBox

#- wxPython Demo --------------------------------------------------------------
__wxPyOnlineDocs__ = 'http://wxpython.org/Phoenix/docs/html/wx.lib.combotreebox.html'
__wxPyDemoPanel__ = 'TestComboTreeBox'

overview = wx.lib.combotreebox.__doc__



class TestComboTreeBox(wx.Panel):
    def __init__(self, parent, log):
        super(TestComboTreeBox, self).__init__(parent)
        self.log = log
        panelSizer = wx.FlexGridSizer(cols=2)
        panelSizer.AddGrowableCol(1)
        for style, labelText in [(0, 'Default style:'),
                                 (wx.CB_READONLY, 'Read-only style:')]:
            label = wx.StaticText(self, label=labelText)
            panelSizer.Add(label, flag=wx.ALL|wx.ALIGN_CENTER_VERTICAL,
                           border=5)
            comboBox = self._createComboTreeBox(style)
            panelSizer.Add(comboBox, flag=wx.EXPAND|wx.ALL, border=5)
        self.SetSizerAndFit(panelSizer)

    def _createComboTreeBox(self, style):
        comboBox = ComboTreeBox(self, style=style)
        self._bindEventHandlers(comboBox)
        for i in range(5):
            child = comboBox.Append('Item %d'%i)
            for j in range(5):
                grandChild = comboBox.Append('Item %d.%d'%(i,j), child)
                for k in range(5):
                    comboBox.Append('Item %d.%d.%d'%(i,j, k), grandChild)
        return comboBox

    def _bindEventHandlers(self, comboBox):
        for eventType, handler in [(wx.EVT_COMBOBOX, self.OnItemSelected),
                                   (wx.EVT_TEXT, self.OnItemEntered)]:
            comboBox.Bind(eventType, handler)

    def OnItemSelected(self, event):
        self.log.WriteText('You selected: %s\n'%event.GetString())
        event.Skip()

    def OnItemEntered(self, event):
        self.log.WriteText('You entered: %s\n'%event.GetString())
        event.Skip()


#- wxPy Demo -----------------------------------------------------------------


def runTest(frame, nb, log):
    win = TestComboTreeBox(nb, log)
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

        panel = TestComboTreeBox(self, log)
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


