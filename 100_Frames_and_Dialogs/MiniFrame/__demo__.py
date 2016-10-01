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
    """ Returns the bitmap to be used in the demo tree for the User's package. """

    # Get the image as PyEmbeddedImage
    image = frame16 = PyEmbeddedImage(
    "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABHNCSVQICAgIfAhkiAAAAH5J"
    "REFUeJztkzEOgmAUg79H/gP0rIYNXQxuxEth4Fh1+IOSmIgPVrt0aZsObUjiCEp7ar3XPNyH"
    "KADdpSPitmmwq65yIIkG+Mm81q31ZUnOIuIMUBssmB9zigHor71texqnFAOW9A7IhnwE/Bvs"
    "b1DqKCI9pNegjr6x2ZZ8xxMlwIa5mQGHJAAAAABJRU5ErkJggg==")

    # Return the bitmap to use in the wxPython demo tree control.
    return image


def GetDemos():
    """
    Returns all the demo names in the package, together with the
    tree item name which will go in the wxPython demo tree control.
    """

    # The tree item text.
    TreeItemText = "MiniFrame"

    # The tree item's demos.
    TreeItemDemos = (
        'MiniFrame_minimal',
        'MiniFrame_extended',
        )

    return TreeItemText, TreeItemDemos


def GetOverview():
    """
    Creates the wxHTML code to display on the tree item's Overview tab.
    """

    wxHtmlOverviewStr = '''\
    <html><body>
    <center><h2>MiniFrame</h2></center>
    <p>MiniFrame demos.
    </body></html>
    '''

    return wxHtmlOverviewStr


