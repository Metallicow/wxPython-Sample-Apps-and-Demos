#!/usr/bin/env python

###############################################################################
# Name: PlateButtonDemo.py                                                    #
# Purpose: PlateButton Test and Demo File                                     #
# Author: Cody Precord <cprecord@editra.org>                                  #
# Copyright: (c) 2007 Cody Precord <staff@editra.org>                         #
# Licence: wxWindows Licence                                                  #
###############################################################################

#-----------------------------------------------------------------------------#
#--Python Imports.
import os

#--wxPython Imports.
import webbrowser
import wx
import wx.lib.scrolledpanel as scrolled
try:
    import wx.lib.platebtn as platebtn
except ImportError:
    import platebtn

#- wxPython Demo --------------------------------------------------------------
__wxPyOnlineDocs__ = 'https://wxpython.org/Phoenix/docs/html/wx.lib.platebtn.html'
__wxPyDemoPanel__ = 'TestPanel'

#-----------------------------------------------------------------------------#

class TestPanel(scrolled.ScrolledPanel):
    def __init__(self, parent, log):
        self.log = log
        scrolled.ScrolledPanel.__init__(self, parent, size=(400, 400))

        # Layout
        self.__DoLayout()
        self.SetupScrolling()

        # Event Handlers
        self.Bind(wx.EVT_BUTTON, self.OnButton)
        self.Bind(wx.EVT_TOGGLEBUTTON, self.OnToggleButton)
        self.Bind(wx.EVT_MENU, self.OnMenu)

    def __DoLayout(self):
        """Layout the panel"""
        # Make three different panels of buttons with different backgrounds
        # to test transparency and appearance of buttons under different use
        # cases
        p1 = wx.Panel(self)
        p2 = GradientPanel(self)
        p3 = wx.Panel(self)
        p3.SetBackgroundColour(wx.BLUE)

        self.__LayoutPanel(p1, "Default Background:")
        self.__LayoutPanel(p2, "Gradient Background:", exstyle=True)
        self.__LayoutPanel(p3, "Solid Background:")

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.AddMany([(p1, 0, wx.EXPAND), (p2, 0, wx.EXPAND),
                       (p3, 0, wx.EXPAND)])
        hsizer = wx.BoxSizer(wx.HORIZONTAL)
        hsizer.Add(sizer, 1, wx.EXPAND)
        self.SetSizer(hsizer)
        self.SetAutoLayout(True)

    def __LayoutPanel(self, panel, label, exstyle=False):
        """Puts a set of controls in the panel
        @param panel: panel to layout
        @param label: panels title
        @param exstyle: Set the PB_STYLE_NOBG or not

        """
        # Bitmaps (32x32) and (16x16)
        devil = Devil.GetBitmap() # 32x32
        monkey = Monkey.GetBitmap() # 32x32
        address = Address.GetBitmap() # 16x16
        folder = Home.GetBitmap()
        bookmark = Book.GetBitmap() # 16x16

        vsizer = wx.BoxSizer(wx.VERTICAL)
        hsizer1 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer1.Add((15, 15))
        hsizer2 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer2.Add((15, 15))
        hsizer3 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer3.Add((15, 15))
        hsizer4 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer4.Add((15, 15))

        # Button Styles
        default = platebtn.PB_STYLE_DEFAULT
        square  = platebtn.PB_STYLE_SQUARE
        sqgrad  = platebtn.PB_STYLE_SQUARE | platebtn.PB_STYLE_GRADIENT
        gradient = platebtn.PB_STYLE_GRADIENT
        droparrow = platebtn.PB_STYLE_DROPARROW
        toggle = default | platebtn.PB_STYLE_TOGGLE

        # Create a number of different PlateButtons
        # Each button is created in the below loop by using the data set in this
        # lists tuple
        #        (bmp,   label,                Style,   Variant, Menu, Color, Enable)
        btype = [(None,  "Normal PlateButton", default, None,    None, None,  True),
                 (devil, "Normal w/Bitmap",    default, None,    None, None,  True),
                 (devil, "Disabled",           default, None,    None, None,  False),
                 (None,  "Normal w/Menu",      default, None,    True, None,  True),
                 (folder, "Home Folder",       default, None,    True, None,  True),
                 # Row 2
                 (None,  "Square PlateButton", square,  None,    None, None,  True),
                 (address, "Square/Bitmap",     square,  None,    None, None,  True),
                 (monkey, "Square/Gradient",   sqgrad,  None,    None, None,   True),
                 (address, "Square/Small",       square,  wx.WINDOW_VARIANT_SMALL, True, None, True),
                 (address, "Small Bitmap",      default, wx.WINDOW_VARIANT_SMALL, None, wx.Colour(33, 33, 33), True),
                 # Row 3
                 (devil, "Custom Color",       default, None,    None, wx.RED, True),
                 (monkey, "Gradient Highlight", gradient, None,  None, None,   True),
                 (monkey, "Custom Gradient",   gradient, None,   None, wx.Colour(245, 55, 245), True),
                 (None,  "Drop Arrow",                  droparrow, None,    None, None,   True),
                 (devil,  "",                  default, None,    None, None,   True),
                 (bookmark,  "",               default, None,    True, None,   True),
                 (monkey,  "",                 square,  None,    None, None,   True),
                 # Row 4
                 (None,  "Toggle PlateButton", toggle, None,    None, None,  True),
                 (devil, "Toggle w/Bitmap",    toggle, None,    None, None,  True),
                 (None,  "Toggle w/Menu",      toggle, None,    True, None,  True),
                 ]

        # Make and layout three rows of buttons in the panel
        for btn in btype:
            if exstyle:
                # With this style flag set the button can appear transparent on
                # on top of a background that is not solid in color, such as the
                # gradient panel in this demo.
                #
                # Note: This flag only has affect on wxMSW and should only be
                #       set when the background is not a solid color. On wxMac
                #       it is a no-op as this type of transparency is achieved
                #       without any help needed. On wxGtk it doesn't hurt to
                #       set but also unfortunatly doesn't help at all.
                bstyle = btn[2] | platebtn.PB_STYLE_NOBG
            else:
                bstyle = btn[2]

            if btype.index(btn) < 5:
                tsizer = hsizer1
            elif btype.index(btn) < 10:
                tsizer = hsizer2
            elif btype.index(btn) < 17:
                tsizer = hsizer3
            else:
                tsizer = hsizer4

            tbtn = platebtn.PlateButton(panel, wx.ID_ANY, btn[1], btn[0], style=bstyle)

            # Set a custom window size variant?
            if btn[3] is not None:
                tbtn.SetWindowVariant(btn[3])

            # Make a menu for the button?
            if btn[4] is not None:
                menu = wx.Menu()
                if btn[0] is not None and btn[0] == folder:
                    for fname in os.listdir(wx.GetHomeDir()):
                        if not fname.startswith('.'):
                            menu.Append(wx.NewId(), fname)
                elif btn[0] is not None and btn[0] == bookmark:
                    for url in ['http://wxpython.org', 'http://slashdot.org',
                                'http://editra.org', 'http://xkcd.com']:
                        menu.Append(wx.NewId(), url, "Open %s in your browser" % url)
                else:
                    menu.Append(wx.NewId(), "Menu Item 1")
                    menu.Append(wx.NewId(), "Menu Item 2")
                    menu.Append(wx.NewId(), "Menu Item 3")
                tbtn.SetMenu(menu)

            # Set a custom colour?
            if btn[5] is not None:
                tbtn.SetPressColor(btn[5])

            if btn[2] == droparrow:

                tbtn.Bind(platebtn.EVT_PLATEBTN_DROPARROW_PRESSED, self.OnDropArrowPressed)

            # Enable/Disable button state
            tbtn.Enable(btn[6])

            tsizer.AddMany([(tbtn, 0, wx.ALIGN_CENTER), ((10, 10))])

        txt_sz = wx.BoxSizer(wx.HORIZONTAL)
        txt_sz.AddMany([((5, 5)), (wx.StaticText(panel, label=label), 0, wx.ALIGN_LEFT)])
        vsizer.AddMany([((10, 10)),
                        (txt_sz, 0, wx.ALIGN_LEFT),
                        ((10, 10)), (hsizer1, 0, wx.EXPAND), ((10, 10)),
                        (hsizer2, 0, wx.EXPAND), ((10, 10)),
                        (hsizer3, 0, wx.EXPAND), ((10, 10)),
                        (hsizer4, 0, wx.EXPAND), ((10, 10))])
        panel.SetSizer(vsizer)

    def OnDropArrowPressed(self, evt):
        self.log.WriteText("DROPARROW PRESSED\n")

    def OnButton(self, evt):
        self.log.WriteText("BUTTON CLICKED: Id: %d, Label: %s\n" % \
                       (evt.GetId(), evt.GetEventObject().LabelText))

    def OnToggleButton(self, evt):
        self.log.WriteText("TOGGLE BUTTON CLICKED: Id: %d, Label: %s, Pressed: %s\n" % \
                       (evt.GetId(), evt.GetEventObject().LabelText,
                        evt.GetEventObject().IsPressed()))

    def OnChildFocus(self, evt):
        """Override ScrolledPanel.OnChildFocus to prevent erratic
        scrolling on wxMac.

        """
        if wx.Platform != '__WXMAC__':
            evt.Skip()

        child = evt.GetWindow()
        self.ScrollChildIntoView(child)

    def OnMenu(self, evt):
        """Events from button menus"""
        self.log.WriteText("MENU SELECTED: %d\n" % evt.GetId())
        e_obj = evt.GetEventObject()
        mitem = e_obj.FindItemById(evt.GetId())
        if mitem != wx.NOT_FOUND:
            label = mitem.GetItemLabel()
            if label.startswith('http://'):
                webbrowser.open(label, True)

#-----------------------------------------------------------------------------#

class GradientPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.Bind(wx.EVT_PAINT, self.OnPaint)

    def OnPaint(self, evt):
        dc = wx.PaintDC(self)
        gc = wx.GraphicsContext.Create(dc)
        col1 = wx.SystemSettings.GetColour(wx.SYS_COLOUR_3DSHADOW)
        col2 = platebtn.AdjustColour(col1, -90)
        col1 = platebtn.AdjustColour(col1, 90)
        rect = self.GetClientRect()
        grad = gc.CreateLinearGradientBrush(0, 1, 0, rect.height - 1, col2, col1)

        pen_col = tuple([min(190, x) for x in platebtn.AdjustColour(col1, -60)])
        gc.SetPen(gc.CreatePen(wx.Pen(pen_col, 1)))
        gc.SetBrush(grad)
        gc.DrawRectangle(0, 1, rect.width - 0.5, rect.height - 0.5)

        evt.Skip()
#----------------------------------------------------------------------

def runTest(frame, nb, log):
    win = TestPanel(nb, log)
    return win

class TestLog:
    def __init__(self):
        pass

    def write(self, msg):
        print(msg)

    def WriteText(self, txt):
        print('%s' % txt)

#----------------------------------------------------------------------

overview = platebtn.__doc__

#----------------------------------------------------------------------
# Icon Data
# All icons from the Tango Icon Set
from wx.lib.embeddedimage import PyEmbeddedImage

#----------------------------------------------------------------------
Address = PyEmbeddedImage(
    "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAACQklEQVR4AZWTg5IkWRSGc403"
    "6afZ0HrsCYzNtm2UlSy1Cm3btm27/7l1S2OciC99voOIZIBrP8XIojKz9SGIlUXhRqgM/z/T"
    "4r9nus8RxHgjPCsmva3hAQ42jDjYacD0pAZlLfUwlPRAX9IHtqyfwnmQ2zqRoAjHSjeD44U/"
    "HjExOdHYWVbi5HgTJyeHONxtRntXNlRcMdgoC6RAHkKYBIW8HGnWNkhVg1RAkqmECUlPwJZL"
    "cLhIJNvY2yhAU6MMpigDcrTVSDO3IoutAxdhQo6migqy9IF+wfmXaoyO5REJi/UFDsuzySjW"
    "qyBXlpOqZRCDBQghIpWw0VYq0IjP/QLXUjpG59A70obKOo6c62AKY5FuaoYQKkGuKAcfbiSd"
    "tNBxXIKbIfchtwTg3qvf3YK+qXW0Ds1DsLegeXCefuhNkKmrwJP2ZaR9Lsr8cUH/9AYV8I52"
    "IliEFGNFtq4GuqRCkmSBPi6PdpNtqKWC6yGvPyXooAJBanAtjc6dZmml2/dABbcvh2ItIADN"
    "DOMZYZqMQFovax6nAr5iANn6GrCkEymQozv4vIDsoGtsGW3Dy6jrm0d55zRsjeOwNbmx+4GD"
    "8IGgqX8Or2JFBMcLCIzjyTWHZ5EsnkdzCEogzxMlhBAC4wScv5N+8uTfxzSZ8BcVKMUqFBQU"
    "wmazfRKHwwGzs8H3PzCeoIIEpR0VFVUYGRn5gNHRUR/5juqPCoIIiEk3nbDGEpgLKiFaSt1Y"
    "3UgeOFMxWKHw1CvwxvdeybfgTX4DJPzQUpOr/msAAAAASUVORK5CYII=")

#----------------------------------------------------------------------
Book = PyEmbeddedImage(
    "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAACEUlEQVR4AWKAATOP8kIzj4p/"
    "Zm5lf2HYxK3iDwibelY+3T8/nuPny0D9Py+CU3+/8A/4/8JX/P//eiZAZeTAW2kQheE4+082"
    "XCtY27Zte4Pats25tW3bDaqw7v1U6905k6TmJM+Hk3mfMxBhT0/PaCMjIzx4+AhcgqSCZggK"
    "xVvUfn6/h9bK99D6QzEiF6Gnw7AIAze3CgGFaWRmZorJZj6ZeGcRLTDzy8KBc/9QWeyOGTUU"
    "szMaZmenMKKUYrrv1t9FgujoaOw6/gnfrBmuf/UUfLPRYc/JL8hOc8aEHIiZyX4uGYHUw7jg"
    "zvtFAsYYth96hQ8mgbjwxhYXOR9NgrDj8Gs4ONigvSUIk3IkZrQ4NJV/wWTv1QPLBDuOfsAX"
    "i3Bc/eSCKx9dxPdOXotkDPqhfij6FsyOV8DX8yfQdXjLIoFOx5d76id+OsTj9q8Ajj//jsNe"
    "XrOzs0dZWRlkSRJnYGxsCMouE9Ah/nZKwr1/oYI/zsnYf/YvGNNBr9dDlmXQoMwyQXx8/Jzg"
    "i208PlnHzQkSEmPWFcxd4y/HJHrPyUiQnZ0NSZLWFhQUFMwFbzwzx51XlnP/oaGhKC8vX1tQ"
    "UVEhJrv5JWFoaEh09AlJE7Xa2looikKsLujo6EBxcbE4bYI6EqWlpejq6hJhVVVXFVBXgg6L"
    "us/tmTMXXkOw8bFM4OLikkyFzeDq6hpJ2f/HZaPgVfF+0AAAAABJRU5ErkJggg==")

#----------------------------------------------------------------------
Devil = PyEmbeddedImage(
    "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"
    "BL4FTwDA2aVGrF4AAAAASUVORK5CYII=")

#----------------------------------------------------------------------
Home = PyEmbeddedImage(
    "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")

#----------------------------------------------------------------------
Monkey = PyEmbeddedImage(
    "iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAHv0lEQVR42u2VA5AkzRaFv8ys"
    "7q6u1mjHWhu/tdIzFs+2bdu2bdvWb2ttDrc17UK+7oyZmI15Oz8CzyfixE31PSfv7ari//hX"
    "Q6xdFudeYJkg2BYW/sMDLfp8XzYBKBVkpdAnalp9XyN/Auy+5wYWxbgHWBUKBZ+IO7HzVy7s"
    "sRYNdIebk3Gi0SgA5VKJTL7A/uOna7fvP+UWy6VbXFc+D7j9bg1sXBLlbvC8sG2/936XrbKX"
    "zOuWpbGjlDKncEtZtFsGwAo7WE4Kp6UXp22QPYdOBL+86vaKV6u9EvgEzA6xaZkNs+PVTamm"
    "1z/mQVfE3DPHyBy/A4IaSoCcpAA0EGgMsSK0DKxBJDr5xs/+WswXS28H3s0skMwC31crbct6"
    "9aPvf2ls7OANHD1xhJEgyTCtpK05lHTYGFASyvXxuJrDKd3KkJvg0JEDZI/dweMefEUsrOSr"
    "G7lmr8DsLdj9kA0rlkbcLGMTedat3crSZatQVpjh4VP88Y+/QmePIwCa+tm8+UF0dfXg+R57"
    "997J3/70KzrbWii4IX5+1f49wLJZK1DVTiKQfCEQlAItqkjx53g01NPb2U46n2Pbgx/BiiVL"
    "oTCCd+Ywc+yAR2x7BAWrjYk6H7H9kfU1H3fsAOROsGLhArbveAyj4+MM9vfjhEVPI2cjt9Go"
    "azU0AcTmFQ7AlZ1JecGSLsvOljT7R/xgXk+bXNDpEA6F2fGQHbi5YdAeOghAa2QoQkkmqboe"
    "zapC4BYBCUIgpCTUPMDPfvUT3EqV3SfSHB3JBvPaLJmKwsFRrzKcD24C1or1i5wHdDbzreW9"
    "dmr/qOCipYNcv+s4iwY7sHWOSy5ey6KeOfjlLAQBWvugjQmECgOg/RqAEUfIelCoeCuHhjNc"
    "e81fKPhR7jw8wsaLlnLz7oP0NwXsPV3K1bcfIyM2r1ndF0odSSte+5SHsPOKZQzUHWkaOhon"
    "GiGoTKDdCloHnM5U+dIfjjA0AcIK1xlhqABf+tMxTud8hLTMucZvHMchCAIAFve2snPdSt7w"
    "3MdzMm/R0GxoS9/Ti91AsGxeH8mwQPsu7W2tFIplhBRUqi6oEDIcR0biPPNjf+PN37ieZ3zk"
    "z8hIokEzfvPXr+OZH/2LOWMYcqj5IJViolShvbWZoFYmasHqpQvxAkFDWwIiCDSWAO3VkGGH"
    "RXP7GM3XCNtxhkZHsWKtyEgMGY7Ve5kDMNEYsBMcHZ5ayxujjXNWop1TQ6eJROs50iUWDvSh"
    "3arRsJSioQkIGbLEgbAS7Dp8kkqlglARBvt6ODaUJplqY8++3Xh2G8LcNs5LHr2RhBPhJY/d"
    "YgyoSNyMzdpjNmFubycJ4l3s2nUr8UQzp8YLzO3tBClxXZfb9xwgpAQNbbFxaXRbV5P8yrx2"
    "OzVSUGy5eDU/vXIXzckwfc2C1vZetm1/PLowavorVMgQqRDCFBDQpu8EvmmhrkeV6uWHP/gS"
    "meHDHB4uM5Z32bl2EdfuPk7UqnByvJwbygZPEluWxwBuqost729TkRNZwUjGZ/P5veZjs37r"
    "IzmwbxdO1CaRTJFKpYjFkjixOKFQGADX8ygWixQLE2SzaTKZDIVymZWrL+LK33+H0kSG3990"
    "gjlNIbpTmuGMXz2R0buAC8Sly5IALQ7ep2o+Oy2FWjO3SbTG4OGPehatSQe35jKSLTGSzjOa"
    "zjKeyXMmmzct84OAUMiiOZUyf7SOtha625rpak0SsSNkSjW+85UPMJarcdvxovZ8/LDihyWs"
    "5wBpsWEDZ8NixB7dvKan2atN8LwXvQ1RyZjnXYaiiJCNtGwThRXBtENIU35Teq9qHtfAq0zG"
    "KjLZzUfe9Xwsy+GPtw9n6Ki0A95sHyPPFyIqpZx80VgIqQyZimrqfxAxj5qMJEwUyhgy+1Pn"
    "ZX2MECaXVJJG7inx2QxgacYK5QqWssiMDyNCUZMAQwzNmABz88AzEYKZZ4yx9NgpLCtEsVwz"
    "ue/+cyz0T4bOFF0vgKv/9isspwVzi4ZQg35tutTVQp0TJtbnZt3sBy4CUIk2rv7TjwkCOJ0p"
    "uo3czIBiJqrWnYWC+7S+9mQ0lx3FUpK+ReeDVzMGYKoavpmb9UlThn7VPK6hVCc3XPVLbrvp"
    "bwQizJ1Hcnlf8QQgz1kQGxbbnAOviDnqjefPb4nLoMqCJavZ+sDH4zgx8zrVweQHSQgMhEQ0"
    "qELIiEO5WuUPP/sK++68Hq0i3HQwXSgU/bcB72UGBP+IEGCvXRz9XNy2HrJqMOmEqKKUxfzF"
    "K1ixZi3t3YPEEq1YkQgg8DyXUj7N2PBx7rzlSg7svhnf93CJcPvRfGmiVPvlVQeqzwcqQNXE"
    "WQzYk4w24oXzIs9PRK3n9rZErb4229J+hZCSCCnxTRWmsyipCHSA5wVIZXMyU/WOj5W8XKH2"
    "+ZuPuZ/BiBqWJ2MJ0PIcFZFTvPFw9Ut7T1Yec3C4cOWVu9O13ae98umcJl8WeETQ0tCM8xXB"
    "cA7qZyp/2512953MXbvrRPmpdfGvA3IGYdK+OIeBCOAAthlPxmRMzelrstYlHbFOKb1QIlt8"
    "RBhAoF0I0p6rD+XK4qqTGe/qibI/DlTP4tTtC2Y+LTgrFBCebosZW2dRAsJw+kYB4AE+4BrR"
    "adbM/gwI7h3ElPAMagyMgJ6O/wH4OzVRu8jWSr4VAAAAAElFTkSuQmCC")


#- __main__ -------------------------------------------------------------------


if __name__ == '__main__':
    import sys
    print('Python %s.%s.%s %s' % sys.version_info[0:4])
    print('wxPython %s' % wx.version())
    app = wx.App(False)
    frame = wx.Frame(None, title="PlateButton Test")
    sizer = wx.BoxSizer(wx.HORIZONTAL)
    sizer.Add(TestPanel(frame, TestLog()), 1, wx.EXPAND)
    frame.CreateStatusBar()
    frame.SetSizer(sizer)
    frame.SetInitialSize()
    frame.Show()
    app.MainLoop()
