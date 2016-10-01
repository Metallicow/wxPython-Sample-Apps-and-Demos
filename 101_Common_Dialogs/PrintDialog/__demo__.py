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
    image = dialog16 = PyEmbeddedImage(
    "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABHNCSVQICAgIfAhkiAAAAKRJ"
    "REFUeJytk0EOwjAMBGdRH+DvVOJVqLfCBZVbxadaJc8yB5RCSguEMhdLK3uzshWZGVuomkPj"
    "vw73114VQHtqkS5fD7q3SMLM2AFFw/P+KjmWIh0B7gkScYxFFYDu3Lm7exhCUQXczB4GpSYv"
    "Bn9J8AwwNS/pyWBa4tKC6n29qmdnTKKk7FRxjKt6Ikvg7oQhTDUlWNKzBPMXStDW37j73PKe"
    "G2AyEYLJPQvVAAAAAElFTkSuQmCC")

    # Return the bitmap to use in the wxPython demo tree control.
    return image


def GetDemos():
    """
    Returns all the demo names in the package, together with the
    tree item name which will go in the wxPython demo tree control.
    """

    # The tree item text.
    TreeItemText = "PrintDialog"

    # The tree item's demos.
    TreeItemDemos = (
        'PrintDialog_extended.py',
        'PrintDialog_minimal.py',
        )

    return TreeItemText, TreeItemDemos


def GetOverview():
    """
    Creates the wxHTML code to display on the tree item's Overview tab.
    """

    wxHtmlOverviewStr = '''\
    <html><body>
    <center><h2>PrintDialog</h2></center>
    <p>PrintDialog demos.
    </body></html>
    '''

    return wxHtmlOverviewStr
