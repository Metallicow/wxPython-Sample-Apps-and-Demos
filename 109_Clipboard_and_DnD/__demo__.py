#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-MetaData --------------------------------------------------------------------
__doc__ = """
This module contains the meta data needed for integrating the samples
in the directory into the wxPython demo framework. Once imported,
this module returns the following information:

* GetDemoBitmap: returns the bitmap used in the wxPython tree control
  to characterize the package;
* GetDemos: returns all the demos in the package;
* GetOverview: returns a wx.html-ready representation of the package's docs.

These meta data are merged into the wxPython demo tree at startup.

Last updated: User's Name @ 08 Aug 20xx, 21.00 GMT.
Version 0.0.1

"""

__version__ = "0.0.1"
__author__ = "wxPython Team"


#-Imports----------------------------------------------------------------------
#--wxPython Imports.
import wx
from wx.lib.embeddedimage import PyEmbeddedImage


def GetDemoBitmap():
    """
    Returns the bitmap to be used for the demo tree item's bitmap.
    """

    # Get the image as PyEmbeddedImage
    image = clipboard16 = PyEmbeddedImage(
    "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAK3RFWHRDcmVhdGlvbiBUaW1l"
    "AE1pIDEzIEZlYiAyMDAyIDEzOjEyOjIxICswMTAwF71J4AAAAAd0SU1FB9MEGBAXK41KwzcA"
    "AAAJcEhZcwAACvAAAArwAUKsNJgAAAAEZ0FNQQAAsY8L/GEFAAACDUlEQVR42q1Sz2sTQRT+"
    "ZrJbm2wMrCkWyiYUlOhBBUU8KtiTF/Ef8CL4HwTswR9XoRBSPHiyR0/iX2DFk4fioSKi1oBY"
    "pVgDjRvTrrs788Y3myYYE73owOzbN++9733vB/CPR/zJ0Gg0jpVKpUfGGB2G4eV6vb75V4D0"
    "3okF+JW7BqLWpnJu5+jVfGH2iHRdFzutNe2/uf/DV1vaKGzE0e7i4ZubqzbOGULNVJdkuXxa"
    "zhTxtn0JF85dRJqmmWlu7kruWex4C3oFai86qz99WOLnMyMARKLmHCriwYuTePX6CZ6vvYTW"
    "OrNJKdH+2sbH4+dxLXgKlVBtEDcEMJoAnSJf8NBsLo/UaXGUAm7fWgQqgnWFMQAylHkZlr2e"
    "Qqu1h1zOQbe7jTDcQhAEbMuoIt1nNgqQJBkDIoNi0UG1egBCSMTxLKLIx/T0wQFX0EQArSS4"
    "DB4bOh2N9fUIU1Mus9lmFp8xP18ZBiVKm/EeUCxsCZptmoGkjBlMsyQuBRkbmz1LQrZhvwFo"
    "OzKmZhlEUcpZv8B1HR7lLpLkO99kMC7uAU0ogVL0GQjOWoDve5xZ8pODfN6B55X7TeQP0YQp"
    "QPUZIO5guXmj7/zLsXql7GU+NJGBUhtx2D11PVjNZm2pDlHs/77e4YVi+X4MoNf9docX/bFW"
    "RtjmWWfFQbahirPaazdTkX4novgh/tf5CTJiK2HHBHfoAAAAAElFTkSuQmCC")

    # Return the bitmap to use in the wxPython demo tree control.
    return image


def GetDemos():
    """
    Returns all the demo names in the package, together with the
    tree item name which will go in the wxPython demo tree control.
    """

    # The tree item text.
    TreeItemText = "Clipboard and DnD"

    # The tree item's demos.
    TreeItemDemos = ()

    return TreeItemText, TreeItemDemos


def GetOverview():
    """
    Creates the wxHTML code to display on the tree item's Overview tab.
    """

    wxHtmlOverviewStr = '''\
    <html><body>
    <center><h2>Clipboard and DnD</h2></center>
    <p>Clipboard and Drag and Drop(DnD) demos.
    </body></html>
    '''

    return wxHtmlOverviewStr
