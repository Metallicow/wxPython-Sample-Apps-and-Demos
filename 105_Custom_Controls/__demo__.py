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
    image = customcontrol16 = PyEmbeddedImage(
    "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABGdBTUEAAK/INwWK6QAAAnRJ"
    "REFUeJylk09vVGUUxn/nfe/MtNOZtoy0pi3QNJHAQkwKRNCNuCJuSGBj3LkwIWHDJzDu3GCi"
    "iZ/AlW78AIbACmVhNEaNYpCQDDBAhcIwk7lz733POS5u+RPjxvhsTnKS8+T8Tp4D/1Oytnnh"
    "wvFjr3/gliQpJBVUQRWS7dQEas97poG8NO//+tnH2cGNXe+ce3djcTwpyQuYFrJToahgOoW8"
    "gKKEfCrkFVRVYHtk3Lu5+lbWXWgWayst1JqYgRkgQgTK5LgJ0+SoBcwcNcE9UGrGrd9jyhqN"
    "wOpKh+58+xnX/ccV3/Yrjq63mFTO4eUMcHDD3QEoq8jCnJAB7PQAuHJjyg8D5aEKl65t0ZyZ"
    "4Y31Nq8tCfuXA2VluNd4SbU2eFGXfxuy1erQ3H7Igz/63Bomrq7t48iBl/n0RMQF1LxGdSW8"
    "OLw9VvpFiz0vzXLm2DJffvgmn587zGrLuTJQPvk+oUnBHVPD7R8GQeDyzwOuXn9E3mgRxDny"
    "SpvzJ/eye1eHm0NDk2FWG5hbbSAiACy0I1+8t4deI/DnGC7eDvQfOXNzgQNLgjUytsZeb+AO"
    "pmQBIcZYp0qgN9/g2mDIjQcTjm50ebJ/nlHhzIeC767fJR7ajartHN7qI4ZYk7g7670m7x+a"
    "AVXuFDltm+Gbn7ZYXOzy0ds9em2YVoaZAEoWsyit5tMNhM5s4OyJJTDlqx/HhGnJqYNdhnli"
    "c+8sZkYWnRACEkSy4aiS7ZEQI2iqk2iqmDvHV9o1pwTcI8NRwswQgUleMB5NosTOq6dX922e"
    "CWJi9jRRhgEBMK3AFUxxEnhCUMqq5K/BL1//t9/9F/0NKrFMKr3z3WMAAAAASUVORK5CYII=")

    # Return the bitmap to use in the wxPython demo tree control.
    return image


def GetDemos():
    """
    Returns all the demo names in the package, together with the
    tree item name which will go in the wxPython demo tree control.
    """

    # The tree item text.
    TreeItemText = "Custom Controls"

    # The tree item's demos.
    TreeItemDemos = ()

    return TreeItemText, TreeItemDemos


def GetOverview():
    """
    Creates the wxHTML code to display on the tree item's Overview tab.
    """

    wxHtmlOverviewStr = '''\
    <html><body>
    <center><h2>Custom Controls</h2></center>
    <p>Custom controls demos.
    </body></html>
    '''

    return wxHtmlOverviewStr


