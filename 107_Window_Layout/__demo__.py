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
    image = layout16 = PyEmbeddedImage(
    "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABGdBTUEAAK/INwWK6QAAABl0"
    "RVh0U29mdHdhcmUAQWRvYmUgSW1hZ2VSZWFkeXHJZTwAAAGZSURBVBgZpcHPi41hHMbhz/P2"
    "oJijzEKSQn4uFRsNK8lKKWZtFvMPKFulrKxZKGzs2MhismI3S5Qpg0YNZUFiaso5Z973e9+e"
    "J45mYWo015VssxGZYur2qyvAXuAUcBxsTEKmaRJNAkkoWNqUvXBkz/YTyFy9eDRhm8u3Xt71"
    "f7r56I0LMr+dprg/+50Rs7bpiXHefloaUmQqeRd/HNq5hSol/undlyFVf9BupsgUtrdSGHj/"
    "dch6OCJRZArLmWJ6Ypz1UogqU1hOFJPXnzGQkGHmxlnO3ztHr9dDEpKQRETweGoGK6gyhSWq"
    "b/2WM8d2M/PiM1WvN8bBA/uobGOL13PzVO6CqqGwTLU8CFqbn8OOKkIkEqt1EVRSR5UpkkQ1"
    "HLb02yAGLZUkbAMGG9tEF1TuVqgyhTEjNn91XSAHlW1kEwoqu6PKFOpkIFE8nV1kpDe2jYUP"
    "H2nblpW2JbqgSQ2VZVNkipAWgf1zdy6w2oNLD1mL7R8UmSr0ZPLa88O2TyLtkDqwsAKrAweW"
    "sA3YoGVo5imSbTbiFyrGMBGmEu5TAAAAAElFTkSuQmCC")

    # Return the bitmap to use in the wxPython demo tree control.
    return image


def GetDemos():
    """
    Returns all the demo names in the package, together with the
    tree item name which will go in the wxPython demo tree control.
    """

    # The tree item text.
    TreeItemText = "Window Layout"

    # The tree item's demos.
    TreeItemDemos = ()

    return TreeItemText, TreeItemDemos


def GetOverview():
    """
    Creates the wxHTML code to display on the tree item's Overview tab.
    """

    wxHtmlOverviewStr = '''\
    <html><body>
    <center><h2>Window Layout</h2></center>
    <p>Window Layout demos.
    </body></html>
    '''

    return wxHtmlOverviewStr
