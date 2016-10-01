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


#-Imports---------------------------------------------------------------------
#--wxPython Imports.
import wx
from wx.lib.embeddedimage import PyEmbeddedImage


def GetDemoBitmap():
    """
    Returns the bitmap to be used for the demo tree item's bitmap.
    """

    # Get the image as PyEmbeddedImage
    image = process16 = PyEmbeddedImage(
    "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABGdBTUEAAK/INwWK6QAAABl0"
    "RVh0U29mdHdhcmUAQWRvYmUgSW1hZ2VSZWFkeXHJZTwAAAO1SURBVHjaYmBAA8LC5gyMjOwM"
    "urpB011dWz7z8ytHCgoquYaGdt7Iypp4gJGRVQRZPUAAMaIbIChozCAqqjRVRcU8i5+fk4GF"
    "hY2Bh4cbKMbLICUlynDs2M5jixY1BTMw/H0BUg8QQHAD2NmFdIyMIhd/+/aXSUhIRk9JSYyB"
    "n58HrJmTk4OBlZWZQVlZjOHvX1aG0tLyfffvb/IGavsJEEDMMAO0tSN38/DI6UtKioqHhdkx"
    "uLgYMKiqSjFwcXECNf0D0uwMTEyMQO+BLOMUvnHjzNGfP7/cBwggZoTTdTKVlBTF09LcgeHA"
    "x3DixD2GI0duAulLDJKSAgwyMiIMzMxMDEJCXAzOzmbsLCyyVidP7j8IEEBgAxQUXCepq1t6"
    "RkTYM3NzczHs2XMd6NfTvy9dOnH3yJGpJZ8//2GxsnJU4+dnB3qHhQFE///PI3zkyNGPAAHE"
    "oq8fMkNNzSldVlaQQU5OhGHv3hsM589f+X3s2NyeL18ebQCaf+nbt896rKysDAICkLB49uwD"
    "0DX/GCwsIkoAAohFTc05XVSUh0FeXpzh/fvvDJcv32I4fHjGhG/fHq8CaRYSUjSPjEwKkpDg"
    "BGpmYnj8+D3D9etPgYa8Z/jw4f13gABi+vjx/mF2dnZwQH38+A1oyAeGb9+enARqviAgIGdS"
    "UzNjh7e3rbyAABvDnz9/Ga5de8pw4cI9hpMnz3w5dWpeE0AAMR06tKCegYEJHNq/fv0FBhLv"
    "D3Z2YHIyj+iqqpq8xdXVhI+R8TcwOtmB6YCf4dOnbwy3bl3/ePv2mtYvX55uBQggFmVlbXUB"
    "AS5g1LAAA4iVwd/fhkVRsa/F2dleVEyMg4Gbm5GBg4Mb6H9QdP4HqmNkuHNn69z37+9tArry"
    "GUAAMYeH53Vqa+sqiovzgAOIn5+LSU9PnVtEhA2YChkZfvz4DYxWbqDz/zEcPHiH4d8/FoY3"
    "b34IPXhwci7QgLcAAcR86tTuzdzc4uaqqnoKIA3i4vxAlzABNTMx3L79CujXe8BYeczw7t0v"
    "hpcvvwDZ9xiuXr30/c2by6BAfg8QQNCkzCRqaBi3QU1N3yIlxf2fsbEqy9WrjxmOH7/LcPHi"
    "PaBBN7/z87O8ePfuHdP37z8ZHzzYAYyl11uAGh8ABBA8LwBzmTIHh0SArKwkR3FxX4ugIB8w"
    "MV0HhfbXO3fWNr9+fW83UNkfaP75BsSgzPQZIIDQMyMbEHOJiekVBAX1f3Z0rH3HxSVeChTT"
    "BKV2qDwIs8A0AAQYAAWOPI69PFvBAAAAAElFTkSuQmCC")

    # Return the bitmap to use in the wxPython demo tree control.
    return image


def GetDemos():
    """
    Returns all the demo names in the package, together with the
    tree item name which will go in the wxPython demo tree control.
    """

    # The tree item text.
    TreeItemText = "Process and Events"

    # The tree item's demos.
    TreeItemDemos = ()

    return TreeItemText, TreeItemDemos


def GetOverview():
    """
    Creates the wxHTML code to display on the tree item's Overview tab.
    """

    wxHtmlOverviewStr = '''\
    <html><body>
    <center><h2>Process and Events</h2></center>
    <p>Process and Events demos.
    </body></html>
    '''

    return wxHtmlOverviewStr


