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
    image = book16 = PyEmbeddedImage(
    "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABGdBTUEAAK/INwWK6QAAABl0"
    "RVh0U29mdHdhcmUAQWRvYmUgSW1hZ2VSZWFkeXHJZTwAAAIASURBVDjLpVPPaxNREJ6Vt01c"
    "aH4oWk1T0ZKlGIo9RG+BUsEK4kEP/Q8qPXnpqRdPBf8A8Wahhx7FQ0GF9FJ6UksqwfTSBDGy"
    "B5HkkphC9tfb7jfbtyQQTx142byZ75v5ZnZWC4KALmICPy+2DkvKIX2f/POz83LxCL7nrz+W"
    "PNcll49DrhM9v7xdO9JW330DuXrrqkFSgig5iR2Cfv3t3gNxOnv5BwU+eZ5HuON5/PMPJZKJ"
    "+yKQfpW0S7TxdC6WJaWkyvff1LDaFRAeLZj05MHsiPTS6hua0PUqtwC5sHq9zv9RYWl+nu5c"
    "ETcnJ1M0M5WlWq3GsX6/T+VymRzHDluZiGYAAsw0TQahV8uyyGq1qFgskm0bHIO/1+sx1rFt"
    "chJhArwEyIQ1Gg2WD2A6nWawHQJVDIWgIJfLhQowTIeE9D0mKAU8qPC0220afsWFQoH93W6X"
    "7yCDJ+DEBeBmsxnPIJVKxWQVUwry+XyUwBlKMKwA8jqdDhOVCqVAzQDVvXAXhOdGBFgymYwr"
    "GoZBmUyGjxCCdF0fSahaFdgoTHRxfTveMCXvWfkuE3Y+f40qhgT/nMitupzApdvT18bu+YeD"
    "QwY9Xl4aG9/d/URiMBhQq/dvZMeVghtT17lSZW9/rAKsvPa/r9Fc2dw+Pe0/xI6kM9mT5vtX"
    "y+Nw2kU/5zOGRpvuMIu0YAAAAABJRU5ErkJggg==")

    # Return the bitmap to use in the wxPython demo tree control.
    return image


def GetDemos():
    """
    Returns all the demo names in the package, together with the
    tree item name which will go in the wxPython demo tree control.
    """

    # The tree item text.
    TreeItemText = "Treebook"

    # The tree item's demos.
    TreeItemDemos = (
        'Treebook_extended.py',
        'Treebook_minimal.py',
        )

    return TreeItemText, TreeItemDemos


def GetOverview():
    """
    Creates the wxHTML code to display on the tree item's Overview tab.
    """

    wxHtmlOverviewStr = '''\
    <html><body>
    <center><h2>Treebook</h2></center>
    <p>Treebook demos.
    </body></html>
    '''

    return wxHtmlOverviewStr

