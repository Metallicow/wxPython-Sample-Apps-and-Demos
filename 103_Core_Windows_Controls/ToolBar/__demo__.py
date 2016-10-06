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
    image = core16 = PyEmbeddedImage(
    "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAACXBIWXMAAAsTAAALEwEAmpwY"
    "AAAABGdBTUEAALGOfPtRkwAAACBjSFJNAAB6JQAAgIMAAPn/AACA6QAAdTAAAOpgAAA6mAAA"
    "F2+SX8VGAAACnUlEQVR42mJcsWLFfwYKAEAAmubYBmAYBIDgR2IBJLcszEJmJxo30MSSrRRp"
    "rj35GGOQmagqIkJEMOeku1lrUVWc8z8Pe7+YGe7OFYDDMbgBGAaBmNmAldh/DyagEqgRNPRl"
    "2fc52QdmRkTc4dDdZCZV9fty24zwHph+rguqirvzCSCwC8TExMAYGYBsBGFGRkagS34w/Pvz"
    "hoGH+RoDw59vDH95QsAuXblyJQNAALGg++nTp08M7969A9v+/v17hocPHzKcPnOBwUSHi8FA"
    "W5xBUt6a4c+XbwysrMxg9QABxISs+c2bNwwPHjwAOxuk+eXLlwz37t1jmDNrGkNUUhPDrRcK"
    "DKw8qgy/f/+E6wEIILgLQJouXrzIwMzMzPD8+XOw/0D0o0ePGH79/s3wB6jpwrkTDM6O1mCv"
    "MTFB7AYIILgBN27cYDh58iRY4vHjxwwvXrxgePLkCcPdu3fBAQwCq1atYkhMTGTg4OAAWwQC"
    "AAEEN+Dp06cMwBgBRw9IMwiDvPTr1y+IX4EGf//+HRw2oACEuQAggOAGCAsLM9y+fZvh8uXL"
    "YElQ1IEAGxsbAx8fHwMXFxeDoqIiAycnJzhmYAYABBCY/Pv3L4Ouri5DSEgIWBCkmZWVFZzA"
    "QJpUVVUZeHl5GQIDAxm4ubnhaQMEAAII7AKQiSBngVIWyOl79+4Fu0hcXBzsX5DiyMhIcErd"
    "vHkzSrQDBBALzH8gRSBDWltbGWxtbRmuXr0KVgCy2dramsHGxobh3LlzDOHh4WBxUCKKiIjg"
    "AQgglIQEcp6GhgaDtrY22JmgAAT5HRQOnz9/BqsB5Y2dO3eCNHOAYh8ggOAGgJyKbhgygAUa"
    "VDMjTBwggMAGTJ48+flvIJCWlpYjlH2RNYMAQIABANLKHICUilYLAAAAAElFTkSuQmCC")

    # Return the bitmap to use in the wxPython demo tree control.
    return image


def GetDemos():
    """
    Returns all the demo names in the package, together with the
    tree item name which will go in the wxPython demo tree control.
    """

    # The tree item text.
    TreeItemText = "ToolBar"

    # The tree item's demos.
    TreeItemDemos = (
        'ToolBar_extended.py',
        'ToolBar_minimal.py',
        )

    return TreeItemText, TreeItemDemos


def GetOverview():
    """
    Creates the wxHTML code to display on the tree item's Overview tab.
    """

    wxHtmlOverviewStr = '''\
    <html><body>
    <center><h2>ToolBar</h2></center>
    <p>ToolBar demos.
    </body></html>
    '''

    return wxHtmlOverviewStr
