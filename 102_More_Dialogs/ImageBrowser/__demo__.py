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
    image = moredialog16 = PyEmbeddedImage(
    "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAABtklEQVR4nJ2STWsTURSGn5NM"
    "W8Gv0pYuagmiNoiiDajoDOnCrRsVlBbdG/oDuroEAmXEhTsXIqV0XfADd67cmGQWIkhBrGJD"
    "60JBMWiwX0NvjwvjMGkmVD2bc+89vM95z73XUVV2C+dM+mrf5f0lEOpPG6WtV/ZJVPOn/V0J"
    "N87d5PSlk1i1vP387rE/7QNgikac5gIRvyNgz6Bl5FaIVcv8I8v6F4OIYIoGB+ggDptZIG1Z"
    "s1+xapG0RaT0uyKy1wFQNW3ywzPDnB3OkRKlW0GdLlQtV2a/s0qZ5ZVjLG2vfHLioqAc4OZd"
    "gnLA0f5BvJEjkArZYpVva3VULaeyvYRWOZHp49mb8ICTJHbzLi8LH1h+/YON9Q02U5tcG8+g"
    "bDMzFzCwb4BarQZd1CNAXByUAxoPGtF+6vYUPw/eR1DunL9L7lAOb8xDVfs7OojnocwQ3b2j"
    "ILD4fpHJ8clo7BYH8eyNeVRfVHHzLpWlCs8XPpISeHivysTFiXbAzs7xsQrXC4wu5Mgez1Lp"
    "uRDV2xyISMtT/oElnSc6UNXEO0g6bwHs7PAv4ZiiEVNs/4l/DfhvZTN+AbNUzvDHFuq4AAAA"
    "AElFTkSuQmCC")

    # Return the bitmap to use in the wxPython demo tree control.
    return image


def GetDemos():
    """
    Returns all the demo names in the package, together with the
    tree item name which will go in the wxPython demo tree control.
    """

    # The tree item text.
    TreeItemText = "ImageBrowser"

    # The tree item's demos.
    TreeItemDemos = (
        'ImageBrowser_extended.py',
        'ImageBrowser_minimal.py',
        )

    return TreeItemText, TreeItemDemos


def GetOverview():
    """
    Creates the wxHTML code to display on the tree item's Overview tab.
    """

    wxHtmlOverviewStr = '''\
    <html><body>
    <center><h2>ImageBrowser</h2></center>
    <p>ImageBrowser demos.
    </body></html>
    '''

    return wxHtmlOverviewStr

