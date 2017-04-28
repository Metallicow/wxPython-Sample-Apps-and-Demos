#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-Imports----------------------------------------------------------------------

#--Python Imports.
import os
import sys
import re
import keyword

#--wxPython Imports.
import wx
import wx.stc as stc

import images


#-Globals----------------------------------------------------------------------
# try:
    # gFileDir = os.path.dirname(os.path.abspath(__file__))
# except:
    # gFileDir = os.path.dirname(os.path.abspath(sys.argv[0]))

gFileDir = os.path.dirname(os.path.abspath(sys.argv[0])) # PyInstaller
gBmpDir = gFileDir + os.sep + 'bitmaps'

ID_HIGHLIGHTERSTYLE1 = 10001
ID_HIGHLIGHTERSTYLE2 = 10002
ID_HIGHLIGHTERSTYLE3 = 10003
ID_HIGHLIGHTERSTYLE4 = 10004
ID_HIGHLIGHTERSTYLE5 = 10005
ID_HIGHLIGHTERSTYLE6 = 10006
ID_HIGHLIGHTERSTYLE7 = 10007
ID_HIGHLIGHTERSTYLE8 = 10008
ID_HIGHLIGHTERSTYLE9 = 10009
ID_UNHIGHLIGHTERSTYLE1 = 10101
ID_UNHIGHLIGHTERSTYLE2 = 10102
ID_UNHIGHLIGHTERSTYLE3 = 10103
ID_UNHIGHLIGHTERSTYLE4 = 10104
ID_UNHIGHLIGHTERSTYLE5 = 10105
ID_UNHIGHLIGHTERSTYLE6 = 10106
ID_UNHIGHLIGHTERSTYLE7 = 10107
ID_UNHIGHLIGHTERSTYLE8 = 10108
ID_UNHIGHLIGHTERSTYLE9 = 10109
ID_UNHIGHLIGHTSELECTION = 10298
ID_UNHIGHLIGHTALL = 10299


if wx.Platform == '__WXMSW__':
    faces = { 'times': 'Times New Roman',
              'mono' : 'Courier New',
              'helv' : 'Arial',
              'other': 'Comic Sans MS',
              'size' : 10,
              'size2':  8,
             }
elif wx.Platform == '__WXMAC__':
    faces = { 'times': 'Times New Roman',
              'mono' : 'Monaco',
              'helv' : 'Arial',
              'other': 'Comic Sans MS',
              'size' : 12,
              'size2': 10,
             }
else:
    faces = { 'times': 'Times',
              'mono' : 'Courier',
              'helv' : 'Helvetica',
              'other': 'new century schoolbook',
              'size' : 12,
              'size2': 10,
             }


class PythonSTC(stc.StyledTextCtrl):
    def __init__(self, parent, id=wx.ID_ANY,
                 pos=wx.DefaultPosition, size=wx.DefaultSize,
                 style=0):
        stc.StyledTextCtrl.__init__(self, parent, id, pos, size, style)

        self.SetLexer(stc.STC_LEX_PYTHON)
        self.SetKeyWords(0, " ".join(keyword.kwlist))
        self.SetKeyWords(1, " ".join(['True', 'False', 'None']))

        # Enable folding
        self.SetProperty("fold", "1")

        # Highlight tab/space mixing (shouldn't be any)
        self.SetProperty("tab.timmy.whinge.level", "1")

        # Set left and right margins
        self.SetMargins(2, 2)

        # Global default styles for all languages
        self.StyleSetSpec(stc.STC_STYLE_DEFAULT,        'fore:#000000,back:#FFFFFF,face:%(mono)s,size:%(size)d' % faces)
        self.StyleClearAll()  # Reset all to be like the default

        # Global default styles for all languages
        # self.StyleSetSpec(stc.STC_STYLE_DEFAULT,     "face:%(mono)s,size:%(size)d" % faces)
        # self.StyleSetSpec(stc.STC_STYLE_LINENUMBER,  "back:#C0C0C0,face:%(mono)s,size:%(size2)d" % faces)
        # self.StyleSetSpec(stc.STC_STYLE_CONTROLCHAR, "face:%(other)s" % faces)
        # self.StyleSetSpec(stc.STC_STYLE_BRACELIGHT,  "fore:#FFFFFF,back:#0000FF,bold")
        # self.StyleSetSpec(stc.STC_STYLE_BRACEBAD,    "fore:#000000,back:#FF0000,bold")

        self.StyleSetSpec(stc.STC_STYLE_DEFAULT,        'fore:#000000,back:#FFFFFF,face:%(mono)s,size:%(size)d' % faces)
        self.StyleSetSpec(stc.STC_STYLE_LINENUMBER,     'fore:#000000,back:#99AA99,face:%(mono)s,size:%(size2)d' % faces)
        self.StyleSetSpec(stc.STC_STYLE_BRACELIGHT,     'fore:#FF0000,back:#0000FF,bold')
        self.StyleSetSpec(stc.STC_STYLE_BRACEBAD,       'fore:#000000,back:#FF0000,bold')
        self.StyleSetSpec(stc.STC_STYLE_CONTROLCHAR,    'fore:#000000,back:#FFFFFF,face:%(mono)s' % faces)
        self.StyleSetSpec(stc.STC_STYLE_INDENTGUIDE,    'fore:#33FF33,back:#FF0000')
        self.StyleSetSpec(stc.STC_STYLE_CALLTIP,        'fore:#000000,back:#FF0000,face:%(mono)s,size:%(size2)d' % faces)
        # self.StyleSetSpec(stc.STC_STYLE_LASTPREDEFINED, 'fore:#000000,back:#FF0000,face:%(mono)s,size:%(size2)d' % faces)
        # self.StyleSetSpec(stc.STC_STYLE_MAX,            'fore:#000000,back:#FF0000,face:%(mono)s,size:%(size2)d' % faces)

        self.DefaultPythonStyles()

        #Indicator/Smart Highlighter Stuff
        self.highlightTextDict = {}
        self._forHighlighterPerformance = (0, 0)

        self.HIGHLIGHTERSTYLE00 = 1 #On-The-Fly Highlighter
        self.HIGHLIGHTERSTYLE01 = 2
        self.HIGHLIGHTERSTYLE02 = 3
        self.HIGHLIGHTERSTYLE03 = 4
        self.HIGHLIGHTERSTYLE04 = 5
        self.HIGHLIGHTERSTYLE05 = 6
        self.HIGHLIGHTERSTYLE06 = 7
        self.HIGHLIGHTERSTYLE07 = 8
        self.HIGHLIGHTERSTYLE08 = 9
        self.HIGHLIGHTERSTYLE09 = 10

        wx.CallAfter(self.BindSTCEvents)


    def BindSTCEvents(self):
        self.Bind(stc.EVT_STC_UPDATEUI,           self.OnSTCUpdateUI)             # General GUI Updates
        self.Bind(stc.EVT_STC_MARGINCLICK,        self.OnSTCMarginClick)             # If you click a margin, this is an event.
        # self.Bind(stc.EVT_STC_ROMODIFYATTEMPT,    self.OnSTCReadOnlyModifyAttempt)   # Ring the Bell, Notify that the document is in Read-Only Mode
        # self.Bind(stc.EVT_STC_DWELLSTART,         self.OnSTCMouseDwellStart)
        # self.Bind(stc.EVT_STC_DWELLEND,           self.OnSTCMouseDwellEnd)
        # self.Bind(stc.EVT_STC_ZOOM,               self.OnSTCZoom)
        # self.Bind(stc.EVT_STC_HOTSPOT_DCLICK,     self.OnSTCHotSpotDClick)
        # self.Bind(stc.EVT_STC_AUTOCOMP_SELECTION, self.OnSTCAutoCompSelection)
        # self.Bind(stc.EVT_STC_CALLTIP_CLICK,      self.OnSTCCallTipClick)
        # self.Bind(stc.EVT_STC_MACRORECORD,        self.OnSTCMacroRecord)
        # self.Bind(stc.EVT_STC_CHARADDED,          self.OnSTCCharAdded) # Brace Completion
        self.Bind(stc.EVT_STC_DOUBLECLICK,        self.OnSTCDoubleClick)

        self.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
        self.Bind(wx.EVT_KEY_UP, self.OnKeyUp)
        self.Bind(wx.EVT_CONTEXT_MENU,  self.OnSTCContextMenu)

        self.Bind(wx.EVT_MOUSEWHEEL, self.OnMouseWheel)
        ## self.Bind(wx.EVT_MOUSE_AUX1_DCLICK, self.OnMouseAux1DClick)
        self.Bind(wx.EVT_MOUSE_AUX1_DOWN,   self.OnMouseAux1Down)
        ## self.Bind(wx.EVT_MOUSE_AUX1_UP,     self.OnMouseAux1Up)
        ## self.Bind(wx.EVT_MOUSE_AUX2_DCLICK, self.OnMouseAux2DClick)
        self.Bind(wx.EVT_MOUSE_AUX2_DOWN,   self.OnMouseAux2Down)
        ## self.Bind(wx.EVT_MOUSE_AUX2_UP,     self.OnMouseAux2Up)


    def ShowAutoCompleteBox(self, event=None):
        kw = keyword.kwlist[:]
        # kw.append("zzzzzz?2")

        kw = sorted(kw) # Python sorts are case sensitive
        self.AutoCompSetIgnoreCase(False)  # so this needs to match

        # Images are specified with a appended "?type"
        for i in range(len(kw)):
            if kw[i] in keyword.kwlist:
                kw[i] = kw[i] + "?1"

        self.AutoCompShow(0, " ".join(kw))

    def OnKeyDown(self, event):
        event.Skip()
        key = event.GetKeyCode()
        evtCtrlIsDown = event.ControlDown()
        evtAltIsDown = event.AltDown()
        evtShiftIsDown = event.ShiftDown()

        if key == wx.WXK_SPACE and evtCtrlIsDown \
                and not evtAltIsDown and not evtShiftIsDown:
            self.ShowAutoCompleteBox()



            # Tips
            # if event.ShiftDown():
                # self.CallTipSetBackground("yellow")
                # self.CallTipShow(pos, 'lots of of text: blah, blah, blah\n\n'
                                 # 'show some suff, maybe parameters..\n\n'
                                 # 'fubar(param1, param2)')



    def OnKeyUp(self, event):
        event.Skip()
        key = event.GetKeyCode()
        evtCtrlIsDown = event.ControlDown()
        evtAltIsDown = event.AltDown()
        evtShiftIsDown = event.ShiftDown()


    def DefaultPythonStyles(self):
        # Make the default Python styles ...
        # default
        self.StyleSetSpec(stc.STC_P_DEFAULT,        'fore:#000000,back:#FFFFFF,face:%(mono)s,size:%(size)d' % faces)
        # comments
        self.StyleSetSpec(stc.STC_P_COMMENTLINE,    'fore:#007F00,back:#EAFFE9,face:%(mono)s,size:%(size)d' % faces)
        # number
        self.StyleSetSpec(stc.STC_P_NUMBER,         'fore:#FF0000,back:#FFFFFF,size:%(size)d' % faces)
        # string
        self.StyleSetSpec(stc.STC_P_STRING,         'fore:#FF8000,back:#FFFFFF,face:%(mono)s,size:%(size)d' % faces)
        # single quoted string
        self.StyleSetSpec(stc.STC_P_CHARACTER,      'fore:#FF8000,back:#FFFFFF,face:%(mono)s,size:%(size)d' % faces)
        # keyword
        self.StyleSetSpec(stc.STC_P_WORD,           'fore:#FF0000,back:#FFFFFF,face:%(mono)s,size:%(size)d' % faces)
        # keyword2
        self.StyleSetSpec(stc.STC_P_WORD2,          'fore:#6000FF,back:#FFFFFF,face:%(mono)s,size:%(size)d' % faces)
        # triple quotes
        self.StyleSetSpec(stc.STC_P_TRIPLE,         'fore:#000000,back:#FFF7EE,size:%(size)d' % faces)
        # triple double quotes
        self.StyleSetSpec(stc.STC_P_TRIPLEDOUBLE,   'fore:#FF8000,back:#FFF7EE,size:%(size)d' % faces)
        # class name definition
        self.StyleSetSpec(stc.STC_P_CLASSNAME,      'fore:#0000FF,back:#FFFFFF,bold,underline,size:%(size)d' % faces)
        # function or method name definition
        self.StyleSetSpec(stc.STC_P_DEFNAME,        'fore:#007F7F,back:#FFFFFF,bold,size:%(size)d' % faces)
        # operators
        self.StyleSetSpec(stc.STC_P_OPERATOR,       'fore:#000000,back:#FFFFFF,bold,size:%(size)d' % faces)
        # identifiers
        self.StyleSetSpec(stc.STC_P_IDENTIFIER,     'fore:#000000,back:#FFFFFF,face:%(mono)s,size:%(size)d' % faces)
        # comment-blocks
        self.StyleSetSpec(stc.STC_P_COMMENTBLOCK,   'fore:#7F7F7F,back:#F8FFF8,size:%(size)d' % faces)
        # end of line where string is not closed
        self.StyleSetSpec(stc.STC_P_STRINGEOL,      'fore:#000000,back:#E0C0E0,face:%(mono)s,eol,size:%(size)d' % faces)

    def SetUpEditorFromConfig(self, stcConfig):
        global gStcConfig
        gStcConfig = stcConfig


        # # Set up the numbers in the margin for margin #1
        # self.SetMarginType(1, wx.stc.STC_MARGIN_NUMBER)
        # # Reasonable value for, say, 4-5 digits using a mono font (40 pix)
        # self.SetMarginWidth(1, 40)

        # Indentation and tab stuff
        self.SetIndent(gStcConfig.ReadInt('iIndentSize', 4))
        self.SetIndentationGuides(gStcConfig.ReadInt('bShowIndentationGuides', 1))
        self.SetBackSpaceUnIndents(gStcConfig.ReadInt('bBackSpaceUnIndents', 0))
        self.SetTabIndents(gStcConfig.ReadInt('bTabIndents', 1))
        self.SetTabWidth(gStcConfig.ReadInt('iTabWidth', 4))
        self.SetUseTabs(gStcConfig.ReadInt('bUseTabs', 0))

        # White space
        self.SetViewWhiteSpace(gStcConfig.ReadInt('bViewWhiteSpace', 1))

        self.UsePopUp(False) #Setup own custom context menu

        self.SetScrollWidthTracking(True) #Sets whether the maximum width line displayed is used to set scroll width.

        self.SetMultipleSelection(gStcConfig.ReadInt('bMultipleSelection', 1))
        self.SetAdditionalCaretForeground(gStcConfig.Read('sAdditionalCaretForeground', '#0000FF'))
        self.SetAdditionalCaretsBlink(gStcConfig.ReadInt('bAdditionalCaretsBlink', 1))
        self.SetAdditionalCaretsVisible(gStcConfig.ReadInt('bAdditionalCaretsVisible', 1))
        self.SetAdditionalSelAlpha(gStcConfig.ReadInt('iAdditionalSelAlpha', 256))
        # self.SetAdditionalSelBackground('#880000')      #Set the background colour of additional selections.
        # self.SetAdditionalSelForeground('#004400')      #Set the foreground colour of additional selections.
        self.SetAdditionalSelectionTyping(gStcConfig.ReadInt('bAdditionalSelectionTyping', 1))

        self.SetVirtualSpaceOptions(gStcConfig.ReadInt('iVirtualSpaceOptions', 1)) #Allow Rect/Selection in virtual space

        self.SetMultiPaste(stc.STC_MULTIPASTE_EACH)

        # EOL: Since we are loading/saving ourselves, and the
        # strings will always have \n's in them, set the STC to
        # edit them that way.
        self.SetEOLMode(gStcConfig.ReadInt('iEOLMode', 2))
        self.SetViewEOL(gStcConfig.ReadInt('bViewEOL', 0))

        # Right-edge mode indicator
        self.SetEdgeMode(gStcConfig.ReadInt('iLongLineEdgeMode', 1))
        self.SetEdgeColumn(gStcConfig.ReadInt('iLongLineEdge', 80))

        # Setup a margin to hold bookmarks
        self.SetMarginType(1, stc.STC_MARGIN_SYMBOL)
        self.SetMarginSensitive(1, True)
        if gStcConfig.ReadInt('bShowBookmarkMargin', 1):
            self.SetMarginWidth(1, 16)
        else:
            self.SetMarginWidth(1, 0)

        # Define the bookmark images
        self.MarkerDefineBitmap(0, images.WXPdemo.GetBitmap())

        # Setup a margin to hold line numbers
        self.SetMarginType(2, stc.STC_MARGIN_NUMBER)
        if gStcConfig.ReadInt('bShowLineNumbersMargin', 1):
            self.SetMarginWidth(2, 40) #5 digits using a small mono font (40 pixels). Good up to 9999
        else:
            self.SetMarginWidth(2, 0)

        # Setup a margin to hold fold markers
        self.SetMarginType(3, stc.STC_MARGIN_SYMBOL)
        self.SetMarginMask(3, stc.STC_MASK_FOLDERS)
        self.SetMarginSensitive(3, True)
        self.SetMarginWidth(3, 16)

        # Setup a margin to hold text
        #TODO stc.STC_MARGIN_BACK, stc.STC_MARGIN_FORE, stc.STC_MARGIN_TEXT, stc.STC_MARGIN_RTEXT
        self.SetMarginType(4, stc.STC_MARGIN_TEXT)
        self.SetMarginSensitive(4, True)
        self.SetMarginWidth(4, 16)

        # and now set up the fold markers
        self.MarkerDefine(stc.STC_MARKNUM_FOLDEREND,     stc.STC_MARK_BOXPLUSCONNECTED,  "white", "black")
        self.MarkerDefine(stc.STC_MARKNUM_FOLDEROPENMID, stc.STC_MARK_BOXMINUSCONNECTED, "white", "black")
        self.MarkerDefine(stc.STC_MARKNUM_FOLDERMIDTAIL, stc.STC_MARK_TCORNER,  "white", "black")
        self.MarkerDefine(stc.STC_MARKNUM_FOLDERTAIL,    stc.STC_MARK_LCORNER,  "white", "black")
        self.MarkerDefine(stc.STC_MARKNUM_FOLDERSUB,     stc.STC_MARK_VLINE,    "white", "black")
        self.MarkerDefine(stc.STC_MARKNUM_FOLDER,        stc.STC_MARK_BOXPLUS,  "white", "black")
        self.MarkerDefine(stc.STC_MARKNUM_FOLDEROPEN,    stc.STC_MARK_BOXMINUS, "white", "black")

        # Caret color
        self.SetCaretForeground(gStcConfig.Read('sCaretForegroundColor', '#0000FF'))
        self.SetCaretPeriod(gStcConfig.ReadInt('iCaretSpeed', 400))
        self.SetCaretLineVisible(gStcConfig.ReadInt('bCaretLineVisible', 1))
        self.SetCaretLineBackground(gStcConfig.Read('sCaretLineBackground', '#D7DEEB'))
        if gStcConfig.ReadInt('bUseCaretLineBackgroundAlpha', 0):
            self.SetCaretLineBackAlpha(gStcConfig.ReadInt('iCaretLineBackgroundAlpha', 100))
        self.SetCaretWidth(gStcConfig.ReadInt('iCaretPixelWidth', 2))
        self.SetCaretStyle(gStcConfig.ReadInt('iCaretStyle', 1))

        # Selection background
        # self.SetSelBackground(1, '#66CCFF')

        # self.SetSelBackground(True, wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))
        # self.SetSelForeground(True, wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))

        #Indicator/Smart Highlighter Stuff
        self.IndicatorSetStyle(self.HIGHLIGHTERSTYLE00, stc.STC_INDIC_ROUNDBOX)
        self.IndicatorSetForeground(self.HIGHLIGHTERSTYLE00, wx.GREEN)
        self.IndicatorSetStyle(self.HIGHLIGHTERSTYLE01, stc.STC_INDIC_ROUNDBOX)
        self.IndicatorSetForeground(self.HIGHLIGHTERSTYLE01, wx.BLUE)
        self.IndicatorSetStyle(self.HIGHLIGHTERSTYLE02, stc.STC_INDIC_ROUNDBOX)
        self.IndicatorSetForeground(self.HIGHLIGHTERSTYLE02, wx.RED)
        self.IndicatorSetStyle(self.HIGHLIGHTERSTYLE03, stc.STC_INDIC_ROUNDBOX)
        self.IndicatorSetForeground(self.HIGHLIGHTERSTYLE03, wx.CYAN)
        self.IndicatorSetStyle(self.HIGHLIGHTERSTYLE04, stc.STC_INDIC_ROUNDBOX)
        self.IndicatorSetForeground(self.HIGHLIGHTERSTYLE04, wx.YELLOW)
        self.IndicatorSetStyle(self.HIGHLIGHTERSTYLE05, stc.STC_INDIC_ROUNDBOX)
        self.IndicatorSetForeground(self.HIGHLIGHTERSTYLE05, wx.LIGHT_GREY)
        self.IndicatorSetStyle(self.HIGHLIGHTERSTYLE06, stc.STC_INDIC_ROUNDBOX)
        self.IndicatorSetForeground(self.HIGHLIGHTERSTYLE06, wx.BLACK)
        self.IndicatorSetStyle(self.HIGHLIGHTERSTYLE07, stc.STC_INDIC_ROUNDBOX)
        self.IndicatorSetForeground(self.HIGHLIGHTERSTYLE07, '#FF8000')#Orange
        self.IndicatorSetStyle(self.HIGHLIGHTERSTYLE08, stc.STC_INDIC_ROUNDBOX)
        self.IndicatorSetForeground(self.HIGHLIGHTERSTYLE08, '#FF00FF')#Purple
        self.IndicatorSetStyle(self.HIGHLIGHTERSTYLE09, stc.STC_INDIC_ROUNDBOX)
        self.IndicatorSetForeground(self.HIGHLIGHTERSTYLE09, '#FF69B4')#Pink

        #Show how to set the alpha fill colour of the given indicator.
        # Note: Hmmm For whatever odd reason, 64 seems to be the magic number on MSW XP to darken the color...
        # 0 seems to work for off and other numbers don't seem to work at all...
        self.IndicatorSetAlpha(self.HIGHLIGHTERSTYLE00, 64)#Set the alpha fill colour of the given indicator.
        self.IndicatorSetAlpha(self.HIGHLIGHTERSTYLE09, 64)

        self.SetIndicatorCurrent(self.HIGHLIGHTERSTYLE00)

        # register some images for use in the AutoComplete box.
        # self.RGBAImageSetWidth(32)
        # self.RGBAImageSetHeight(16)
        # self.RegisterRGBAImage(1, wx.Bitmap(gBmpDir + os.sep + 'pykey3216.png', wx.BITMAP_TYPE_PNG))
        self.RegisterImage(1, wx.Bitmap(gBmpDir + os.sep + 'pykey3216.png', wx.BITMAP_TYPE_PNG))


    def OnMouseWheel(self, event):
        """
        wx.EVT_MOUSEWHEEL
        Allow Shift + MouseWheel Horizontal Scrolling
        """

        if hasattr(wx.GetApp(), 'enteredWindow'): # wxPythonDemo Main.py
            wx.GetApp().OnMouseWheel(event)
            return

        xoffset = self.GetXOffset()
        wr = event.GetWheelRotation()

        ms = wx.GetMouseState()
        ctrlDown = ms.ControlDown()
        shiftDown = ms.ShiftDown()
        altDown = ms.AltDown()

        if xoffset < 0:#Dont scroll back past zero position
            self.SetXOffset(0)
            self.Refresh()
            return

        ###-- Alt + MouseWheel = Hyper Scrolling Vertically
        ###Imitate hyperscrolling functionality with a clickwheel only style mouse
        ##if altDown and wr < 0 and not shiftDown and not ctrlDown:
        ##    while wx.GetKeyState(wx.WXK_ALT):
        ##        wx.MilliSleep(1)
        ##        self.LineScroll(0, 1)
        ##    if sys.platform.startswith('win'):
        ##        wx.CallAfter(self.PressKeyAlt)
        ##    return
        ##elif altDown and wr > 0 and not shiftDown and not ctrlDown:
        ##    while wx.GetKeyState(wx.WXK_ALT):
        ##        wx.MilliSleep(1)
        ##        self.LineScroll(0, -1)
        ##    if sys.platform.startswith('win'):
        ##        wx.CallAfter(self.PressKeyAlt)
        ##    return

        #-- Shift + MouseWheel = Scroll Horizontally
        if shiftDown and wr < 0 and not altDown and not ctrlDown:
            self.SetXOffset(xoffset + 30)
            return
        elif shiftDown and wr > 0 and not altDown and not ctrlDown:
            if not xoffset <= 0:
                self.SetXOffset(xoffset - 30)
                return
            else:
                return

        ###-- Ctrl + MouseWheel = Zoom
        ### Duplicate Default stc ctrl zooming behavior to bypass
        ### (MouseWheel not working after a undetermined amount of time)BUG
        ##if ctrlDown and wr < 0 and not altDown and not shiftDown:
        ##    self.SetZoom(self.GetZoom() - 1)
        ##    return
        ##elif ctrlDown and wr > 0 and not altDown and not shiftDown:
        ##    self.SetZoom(self.GetZoom() + 1)
        ##    return
        ##
        ###-- MouseWheel = Scroll Vertically
        ### Duplicate Default stc scrolling behavior to bypass
        ### (MouseWheel not working after a undetermined amount of time)BUG
        ##elif wr < 0:
        ##    self.LineScroll(0, 3)
        ##    return
        ##elif wr > 0:
        ##    self.LineScroll(0, -3)
        ##    return
        event.Skip()

    def OnMouseAux1Down(self, event):
        gMainWin.nb.AdvanceSelection(False)
        print('OnMouseAux1Down')
    def OnMouseAux1Up(self, event):
        print('OnMouseAux1Up')
    def OnMouseAux2Down(self, event):
        gMainWin.nb.AdvanceSelection(True)
        print('OnMouseAux2Down')
    def OnMouseAux2Up(self, event):
        print('OnMouseAux2Up')
    def OnMouseAux1DClick(self, event):
        print('OnMouseAux1DClick')
    def OnMouseAux2DClick(self, event):
        print('OnMouseAux2DClick')

    def OnSTCUpdateUI(self, event=None):
        event.Skip()
        if not (self.GetSelectionStart(), self.GetSelectionEnd()) == self._forHighlighterPerformance:
            #Smart Highlighter
            self.HighlightSelectionOnTheFly()

        self.OnUpdateStatusBarInfos()

    def OnSTCDoubleClick(self, event):
        self.HighlightSelectionOnTheFly()

    def OnHighlightText(self, event):
        """
        Check event id to determine what highlighter style to use,
        then permanently highlight text.
        """
        evtId = event.GetId()
        # print('evtId', evtId)
        strId = str(evtId)
        if   strId.endswith('01'): highlighterStyle=self.HIGHLIGHTERSTYLE01
        elif strId.endswith('02'): highlighterStyle=self.HIGHLIGHTERSTYLE02
        elif strId.endswith('03'): highlighterStyle=self.HIGHLIGHTERSTYLE03
        elif strId.endswith('04'): highlighterStyle=self.HIGHLIGHTERSTYLE04
        elif strId.endswith('05'): highlighterStyle=self.HIGHLIGHTERSTYLE05
        elif strId.endswith('06'): highlighterStyle=self.HIGHLIGHTERSTYLE06
        elif strId.endswith('07'): highlighterStyle=self.HIGHLIGHTERSTYLE07
        elif strId.endswith('08'): highlighterStyle=self.HIGHLIGHTERSTYLE08
        elif strId.endswith('09'): highlighterStyle=self.HIGHLIGHTERSTYLE09
        self.HighlightTextPermanently(highlighterStyle=highlighterStyle)

    def OnUnhighlightStyle(self, event):
        evtId = event.GetId()
        print('evtId', evtId)
        strId = str(evtId)
        if   strId.endswith('01'): highlighterStyle=self.HIGHLIGHTERSTYLE01
        elif strId.endswith('02'): highlighterStyle=self.HIGHLIGHTERSTYLE02
        elif strId.endswith('03'): highlighterStyle=self.HIGHLIGHTERSTYLE03
        elif strId.endswith('04'): highlighterStyle=self.HIGHLIGHTERSTYLE04
        elif strId.endswith('05'): highlighterStyle=self.HIGHLIGHTERSTYLE05
        elif strId.endswith('06'): highlighterStyle=self.HIGHLIGHTERSTYLE06
        elif strId.endswith('07'): highlighterStyle=self.HIGHLIGHTERSTYLE07
        elif strId.endswith('08'): highlighterStyle=self.HIGHLIGHTERSTYLE08
        elif strId.endswith('09'): highlighterStyle=self.HIGHLIGHTERSTYLE09
        self.SetIndicatorCurrent(highlighterStyle)
        self.IndicatorClearRange(0, self.GetLength())
        self.SetIndicatorCurrent(self.HIGHLIGHTERSTYLE00)#Set back to On-The-Fly Highlighter after done.
        delthese = []
        for text, style in list(self.highlightTextDict.items()):
            if style == highlighterStyle:
                delthese.append(text)
        for text in delthese:
            del self.highlightTextDict[text]
        self.OnSelectNone(self)
        self.HighlightTextPermanently(highlighterStyle=highlighterStyle)

    def OnUnhighlightText(self, event):
        self.UnhighlightText()

    def OnUnhighlightAll(self, event):
        """
        Unhighlight all styles... The permanently highlighted stuff.
        """
        for style in range(self.HIGHLIGHTERSTYLE01, self.HIGHLIGHTERSTYLE09 + 1):
            self.SetIndicatorCurrent(style)
            self.IndicatorClearRange(0, self.GetLength())
        self.SetIndicatorCurrent(self.HIGHLIGHTERSTYLE00)#Set back to On-The-Fly Highlighter after done.
        self.highlightTextDict = {}

    def HighlightSelectionOnTheFly(self, text=None):
        """
        Highlight Current Selection Matchs On-The-Fly.

        timeit test Py2.7.5 x1000
        stc.STC_FIND_REGEXP Method
        FindText: [11.085237626693713, 11.154881154332408, 11.089765059677294]
        re Method
        Regex: [7.711642673014154, 7.711089617365346, 7.718059265515734]
        """
        #Indicator style should be default On-The-Fly Highlighter at this point,
        #so no need to SetIndicatorCurrent.

        self.IndicatorClearRange(0, self.GetLength())
        text = text or self.GetSelectedText()
        charList = [' ','.','!','?', ',',':',';','"',"'",
                    '(',')','[',']','<','>','{','}','|',
                    '\\','/','*','&','@','#','+','$',
                    '%','^','`','~','=','+']
        for item in charList:
            if item in text:
                return
        if not text or '\n' in text:
            return
        if text in self.highlightTextDict:
            return
        selstart = self.GetSelectionStart()
        selend = self.GetSelectionEnd()

        length = len(text)
        count = 0

        # flags = 0 #Do case-sensitive matches
        flags = re.IGNORECASE #Do case-insensitive matches
        for match in re.finditer(r'\b%s\b'%text, self.GetText(), flags):# \b matches word boundary
            self.IndicatorFillRange(position=match.start(), fillLength=length)
            count += 1
        if count == 1:#Unhighlight current caret selection if only 1 found
            if selstart > selend:
                selstart, selend = selend, selstart
            self.IndicatorClearRange(position=selstart, clearLength=length)

        self._forHighlighterPerformance = (selstart, selend)

    def HighlightSelectionsWithPermantentMarker(self):
        """
        timeit.repeat Test Py2.7.5
        stc.STC_FIND_REGEXP method
        FindText: [1.7875809046949023, 1.7837719813146862, 1.7834051116761778]
        re method
        Regex: [1.4007414816111066, 1.4018309157660909, 1.3992097969329222]
        """
        for style in range(self.HIGHLIGHTERSTYLE01, self.HIGHLIGHTERSTYLE09 + 1):
            self.SetIndicatorCurrent(style)
            self.IndicatorClearRange(0, self.GetLength())
        for text, highlighterStyle in list(self.highlightTextDict.items()):
            if not text:
                return
            self.SetIndicatorCurrent(highlighterStyle)
            length = len(text)

            flags = 0 #Do case-sensitive matches
            # flags = re.IGNORECASE #Do case-insensitive matches
            for match in re.finditer(text, self.GetText(), flags):
                self.IndicatorFillRange(position=match.start(), fillLength=length)

        self.SetIndicatorCurrent(self.HIGHLIGHTERSTYLE00)#Set back to On-The-Fly Highlighter after done.

    def HighlightTextPermanently(self, text=None, highlighterStyle=None, flags=None):
        text = text or self.GetSelectedText()
        if text:
            #Add the text to the dictionary for permanent highlighting.
            self.highlightTextDict[text] = highlighterStyle
            self.HighlightSelectionsWithPermantentMarker()

    def UnhighlightText(self, text=None):
        text = text or self.GetSelectedText()
        if text in self.highlightTextDict:
            del self.highlightTextDict[text]
            self.HighlightSelectionsWithPermantentMarker()

    def OnSTCContextMenu(self, event):
        menu = wx.Menu()
        mi = wx.MenuItem(menu, wx.ID_UNDO, '&Undo', ' Undo last action')
        menu.Append(mi)
        if not self.CanUndo(): mi.Enable(False)

        mi = wx.MenuItem(menu, wx.ID_REDO, 'Redo', ' Redo last modifications')
        menu.Append(mi)
        if not self.CanRedo(): mi.Enable(False)

        menu.AppendSeparator()

        sel = self.GetSelection()

        mi = wx.MenuItem(menu, wx.ID_CUT, 'Cut', ' Cut selected text')
        menu.Append(mi)
        if sel[0] == sel[1]: mi.Enable(False)

        mi = wx.MenuItem(menu, wx.ID_COPY, 'Copy', ' Copy selected text')
        menu.Append(mi)
        if sel[0] == sel[1]: mi.Enable(False)

        mi = wx.MenuItem(menu, wx.ID_PASTE, 'Paste', ' Paste from clipboard')
        menu.Append(mi)
        if not self.CanPaste(): mi.Enable(False)

        mi = wx.MenuItem(menu, wx.ID_DELETE, 'Delete', ' Delete selected text')
        menu.Append(mi)
        if sel[0] == sel[1]: mi.Enable(False)

        menu.Append(wx.MenuItem(menu, wx.ID_SELECTALL, 'Select All', ' Select All Text in Document'))

        menu.AppendSeparator()

        submenu = wx.Menu()
        t1 = 'Highlight Selection Using Style '
        t2 = 'Unhighlight Style '
        t3 = 'Unhighlight Selection'
        t4 = 'Unhighlight All'
        submenu.Append(wx.MenuItem(menu, ID_HIGHLIGHTERSTYLE1, '%s1'%t1, '%s1'%t1))
        submenu.Append(wx.MenuItem(menu, ID_HIGHLIGHTERSTYLE2, '%s2'%t1, '%s2'%t1))
        submenu.Append(wx.MenuItem(menu, ID_HIGHLIGHTERSTYLE3, '%s3'%t1, '%s3'%t1))
        submenu.Append(wx.MenuItem(menu, ID_HIGHLIGHTERSTYLE4, '%s4'%t1, '%s4'%t1))
        submenu.Append(wx.MenuItem(menu, ID_HIGHLIGHTERSTYLE5, '%s5'%t1, '%s5'%t1))
        submenu.Append(wx.MenuItem(menu, ID_HIGHLIGHTERSTYLE6, '%s6'%t1, '%s6'%t1))
        submenu.Append(wx.MenuItem(menu, ID_HIGHLIGHTERSTYLE7, '%s7'%t1, '%s7'%t1))
        submenu.Append(wx.MenuItem(menu, ID_HIGHLIGHTERSTYLE8, '%s8'%t1, '%s8'%t1))
        submenu.Append(wx.MenuItem(menu, ID_HIGHLIGHTERSTYLE9, '%s9'%t1, '%s9'%t1))
        menu.AppendSubMenu(submenu, 'Highlight')

        submenu = wx.Menu()
        submenu.Append(wx.MenuItem(menu, ID_UNHIGHLIGHTSELECTION, t3, t3))
        submenu.AppendSeparator()
        submenu.Append(wx.MenuItem(menu, ID_UNHIGHLIGHTERSTYLE1, '%s1'%t2, '%s1'%t2))
        submenu.Append(wx.MenuItem(menu, ID_UNHIGHLIGHTERSTYLE2, '%s2'%t2, '%s2'%t2))
        submenu.Append(wx.MenuItem(menu, ID_UNHIGHLIGHTERSTYLE3, '%s3'%t2, '%s3'%t2))
        submenu.Append(wx.MenuItem(menu, ID_UNHIGHLIGHTERSTYLE4, '%s4'%t2, '%s4'%t2))
        submenu.Append(wx.MenuItem(menu, ID_UNHIGHLIGHTERSTYLE5, '%s5'%t2, '%s5'%t2))
        submenu.Append(wx.MenuItem(menu, ID_UNHIGHLIGHTERSTYLE6, '%s6'%t2, '%s6'%t2))
        submenu.Append(wx.MenuItem(menu, ID_UNHIGHLIGHTERSTYLE7, '%s7'%t2, '%s7'%t2))
        submenu.Append(wx.MenuItem(menu, ID_UNHIGHLIGHTERSTYLE8, '%s8'%t2, '%s8'%t2))
        submenu.Append(wx.MenuItem(menu, ID_UNHIGHLIGHTERSTYLE9, '%s9'%t2, '%s9'%t2))
        submenu.AppendSeparator()
        submenu.Append(wx.MenuItem(menu, ID_UNHIGHLIGHTALL, t4, t4))
        menu.AppendSubMenu(submenu, 'Unhighlight')

        b1 = self.OnHighlightText
        b2 = self.OnUnhighlightStyle
        menu.Bind(wx.EVT_MENU, b1, id=ID_HIGHLIGHTERSTYLE1)
        menu.Bind(wx.EVT_MENU, b1, id=ID_HIGHLIGHTERSTYLE2)
        menu.Bind(wx.EVT_MENU, b1, id=ID_HIGHLIGHTERSTYLE3)
        menu.Bind(wx.EVT_MENU, b1, id=ID_HIGHLIGHTERSTYLE4)
        menu.Bind(wx.EVT_MENU, b1, id=ID_HIGHLIGHTERSTYLE5)
        menu.Bind(wx.EVT_MENU, b1, id=ID_HIGHLIGHTERSTYLE6)
        menu.Bind(wx.EVT_MENU, b1, id=ID_HIGHLIGHTERSTYLE7)
        menu.Bind(wx.EVT_MENU, b1, id=ID_HIGHLIGHTERSTYLE8)
        menu.Bind(wx.EVT_MENU, b1, id=ID_HIGHLIGHTERSTYLE9)
        menu.Bind(wx.EVT_MENU, b2, id=ID_UNHIGHLIGHTERSTYLE1)
        menu.Bind(wx.EVT_MENU, b2, id=ID_UNHIGHLIGHTERSTYLE2)
        menu.Bind(wx.EVT_MENU, b2, id=ID_UNHIGHLIGHTERSTYLE3)
        menu.Bind(wx.EVT_MENU, b2, id=ID_UNHIGHLIGHTERSTYLE4)
        menu.Bind(wx.EVT_MENU, b2, id=ID_UNHIGHLIGHTERSTYLE5)
        menu.Bind(wx.EVT_MENU, b2, id=ID_UNHIGHLIGHTERSTYLE6)
        menu.Bind(wx.EVT_MENU, b2, id=ID_UNHIGHLIGHTERSTYLE7)
        menu.Bind(wx.EVT_MENU, b2, id=ID_UNHIGHLIGHTERSTYLE8)
        menu.Bind(wx.EVT_MENU, b2, id=ID_UNHIGHLIGHTERSTYLE9)
        menu.Bind(wx.EVT_MENU, self.OnUnhighlightText, id=ID_UNHIGHLIGHTSELECTION)
        menu.Bind(wx.EVT_MENU, self.OnUnhighlightAll, id=ID_UNHIGHLIGHTALL)

        # These seems to be linux specific. Need to rebind basic context funcs here so they work.
        menu.Bind(wx.EVT_MENU, self.OnUndo, id=wx.ID_UNDO)
        menu.Bind(wx.EVT_MENU, self.OnRedo, id=wx.ID_REDO)
        menu.Bind(wx.EVT_MENU, self.OnCut, id=wx.ID_CUT)
        menu.Bind(wx.EVT_MENU, self.OnCopy, id=wx.ID_COPY)
        menu.Bind(wx.EVT_MENU, self.OnPaste, id=wx.ID_PASTE)
        menu.Bind(wx.EVT_MENU, self.OnDeleteBack, id=wx.ID_DELETE)
        menu.Bind(wx.EVT_MENU, self.OnSelectAll, id=wx.ID_SELECTALL)

        self.PopupMenu(menu)
        menu.Destroy()

    def OnUndo(self, event): self.Undo()
    def OnRedo(self, event): self.Redo()
    def OnCut(self, event): self.Cut()
    def OnCopy(self, event): self.Copy()
    def OnPaste(self, event): self.Paste()
    def OnSelectAll(self, event): self.SelectAll()
    def OnDeleteBack(self, event): self.DeleteBack()
    def OnSelectNone(self, event):
        """Select nothing in the document. (DeSelect)"""
        # self.SelectNone()#Deselects selected text in the control. Doesn't retain position
        self.SetEmptySelection(self.GetCurrentPos())

    def OnUpdateStatusBarInfos(self):
        self.parent.editorStatusBar.Clear()
        position = self.GetCurrentPos()
        getcharatpos = self.GetCharAt(position)
        column = self.GetColumn(position)
        selstart = self.GetSelectionStart()
        selend = self.GetSelectionEnd()
        multsel = self.GetMultipleSelection()
        if self.GetMultipleSelection() and self.GetSelections() > 1:
            self.parent.editorStatusBar.WriteText(' Length %s   Lines %s   Ln %s   Col %s   Pos %s   Sel %s   Char %s %s   Zoom %s' %(self.GetLength(), self.GetLineCount(), self.GetCurrentLine()+1, self.GetColumn(position), position, u'N/A', getcharatpos, chr(getcharatpos), self.GetZoom()))
        else:
            selstart = self.GetSelectionStart()
            selend = self.GetSelectionEnd()
            if self.LineFromPosition(selstart) == self.LineFromPosition(selend):
                numSelectedLines = 0
            elif selstart < selend:
                numSelectedLines = self.LineFromPosition(selend) - self.LineFromPosition(selstart) + 1
            elif selstart > selend:
                numSelectedLines = self.LineFromPosition(selstart) - self.LineFromPosition(selend) + 1
            self.parent.editorStatusBar.WriteText(' Length %s   Lines %s   Ln %s   Col %s   Pos %s   Sel %s | %s   Char %s %s   Zoom %s' %(self.GetLength(), self.GetLineCount(), self.GetCurrentLine()+1, self.GetColumn(position), position, (selend-selstart), numSelectedLines , getcharatpos, chr(getcharatpos), self.GetZoom()))
        return

    def OnSTCMarginClick(self, event):
        # Fold and unfold as needed
        if event.GetMargin() == 3:
            if event.GetShift() and event.GetControl():
                self.OnFoldAll()
            else:
                lineClicked = self.LineFromPosition(event.GetPosition())
                if self.GetFoldLevel(lineClicked) &\
                        stc.STC_FOLDLEVELHEADERFLAG:
                    if event.GetShift():
                        self.SetFoldExpanded(lineClicked, True)
                        self.OnExpand(lineClicked, True, True, 1)
                    elif event.GetControl():
                        if self.GetFoldExpanded(lineClicked):
                            self.SetFoldExpanded(lineClicked, False)
                            self.OnExpand(lineClicked, False, True, 0)
                        else:
                            self.SetFoldExpanded(lineClicked, True)
                            self.OnExpand(lineClicked, True, True, 100)
                    else:
                        self.ToggleFold(lineClicked)

    def OnFoldAll(self):
        """Folding folds, marker - to +"""
        lineCount = self.GetLineCount()
        expanding = True
        # Find out if folding or unfolding
        for lineNum in range(lineCount):
            if self.GetFoldLevel(lineNum) &\
                    stc.STC_FOLDLEVELHEADERFLAG:
                expanding = not self.GetFoldExpanded(lineNum)
                break
        lineNum = 0
        while lineNum < lineCount:
            level = self.GetFoldLevel(lineNum)
            if level & stc.STC_FOLDLEVELHEADERFLAG and \
               (level & stc.STC_FOLDLEVELNUMBERMASK) ==\
                    stc.STC_FOLDLEVELBASE:
                if expanding:
                    self.SetFoldExpanded(lineNum, True)
                    lineNum = self.OnExpand(lineNum, True)
                    lineNum = lineNum - 1
                else:
                    lastChild = self.GetLastChild(lineNum, -1)
                    self.SetFoldExpanded(lineNum, False)
                    if lastChild > lineNum:
                        self.HideLines(lineNum+1, lastChild)
            lineNum = lineNum + 1

    def OnExpand(self, line, doexpand, force=False, visLevels=0, level=-1):
        """Expanding folds, marker + to -"""
        lastChild = self.GetLastChild(line, level)
        line = line + 1
        while line <= lastChild:
            if force:
                if visLevels > 0:
                    self.ShowLines(line, line)
                else:
                    self.HideLines(line, line)
            else:
                if doexpand:
                    self.ShowLines(line, line)
            if level == -1:
                level = self.GetFoldLevel(line)
            if level & stc.STC_FOLDLEVELHEADERFLAG:
                if force:
                    if visLevels > 1:
                        self.SetFoldExpanded(line, True)
                    else:
                        self.SetFoldExpanded(line, False)
                    line = self.OnExpand(line, doexpand, force, visLevels-1)
                else:
                    if doexpand and self.GetFoldExpanded(line):
                        line = self.OnExpand(line, True, force, visLevels-1)
                    else:
                        line = self.OnExpand(line, False, force, visLevels-1)
            else:
                line = line + 1
        return line

    def RegisterModifiedEvent(self, eventHandler):
        self.Bind(wx.stc.EVT_STC_CHANGE, eventHandler)


