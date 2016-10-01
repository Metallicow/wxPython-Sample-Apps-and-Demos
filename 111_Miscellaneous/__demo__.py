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
    image = miscellaneous16 = PyEmbeddedImage(
    "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAACk0lEQVR4nKWSWUiUYRSGn2/m"
    "G20axyWzbcoM0xaywougIEupixbIkOiicGunm+yqboQWpCiyhRajTJC86qKFaDMCKyrCQq3U"
    "tG0mG2uadKb5/XNm/v/rQgILo6Jz+Z5zngPveaVSiv8p+aeBYeu8c4TxOVevydr/TwDrRmPC"
    "lpKo+9iRsQgxlsQ1T6b3ns8u+itAckF1ad7+0rO9VisNvgFtRUV2YfL6rkn+M66cPwJspk3W"
    "x0J8KwSjgIKMJMjZ55ovYmfZVX+TPjQgXyzUMtPOyciu3QQh6ILsLrCng80Kl7qBupfzgZs/"
    "AczFIl6sXvlBVN5yOAxFxanrZ4sCA5ejI+BhN5gKVBSqCg7eiDmZWhbe4j4MIMMbki7ElB8s"
    "IBqFzscQNSjMTRCPaqs5sawU0wGGBlhh4uW7+OYEKCtcWxl3OnVGaKN7vTRkjJ03V+HFa5Bx"
    "YCgI9HB8zBi+VLTozTsr7Un1bczeXIZ9m4MHXWAKk8kLXOtksbNNarqJ3ReAUSnQ1A7xSbCk"
    "BEzFlNqjja3x7eN7tt5J84YzaWv1IG2SuVkzyUvI4UVPy2gZ+mYy0q8NOJI5FZQDWh6D/x26"
    "boI13I/PRhtvmJeRTcgIE+rtp8pbAxEDufX2l/Iryc6llkgEdMDfBUqBEGh9huVth+cpidYp"
    "CAvvNT+ePi9KmSDAZhjIqz7VmBojMp6vGtfhDIfg41c+RSwsagjWtRhqkyppDzm2j/6mTxPF"
    "ptOC+ioRQmBtDHoityM1EsAdVp1xQqQ0rkzz7biv3buomauUUt0/fq0d+lgSm+94Fbs8fc9w"
    "j1fvO+AriOjqGicHBSmk1GchhFRKGUOls/+itlcIcRl4ppQyh0zi75YH9Zt/1b4DIgMimftg"
    "s4wAAAAASUVORK5CYII=")

    # Return the bitmap to use in the wxPython demo tree control.
    return image


def GetDemos():
    """
    Returns all the demo names in the package, together with the
    tree item name which will go in the wxPython demo tree control.
    """

    # The tree item text.
    TreeItemText = "Miscellaneous"

    # The tree item's demos.
    TreeItemDemos = ()

    return TreeItemText, TreeItemDemos


def GetOverview():
    """
    Creates the wxHTML code to display on the tree item's Overview tab.
    """

    wxHtmlOverviewStr = '''\
    <html><body>
    <center><h2>Miscellaneous</h2></center>
    <p>Miscellaneous demos.
    </body></html>
    '''

    return wxHtmlOverviewStr
