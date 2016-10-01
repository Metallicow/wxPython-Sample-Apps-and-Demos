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
    image = images16 = PyEmbeddedImage(
    "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABGdBTUEAAK/INwWK6QAAABl0"
    "RVh0U29mdHdhcmUAQWRvYmUgSW1hZ2VSZWFkeXHJZTwAAAQHSURBVHjaYtx+7hMDBPxnYPjx"
    "iYGR4W+ZrARPKTMTIwMDQobh129Ghk9ffzDcvn1/05evn1JZWdj+ffn+mwEggFj+H21mYASp"
    "YGVl+K8Zw8DCJ8qnoSAkgtAOAZ9/MjA8ev6FQUdbPenWnXvf3r17nwsSBwgg5ijGYwwMd0D4"
    "MMPf2+sZWKT1rRTU1J3QDfgDtOTT198MgjwsDGoqsmbPX33g+Pj5216AAGJhYIeqAOr4+/AZ"
    "2689tdJPOB8w/Hh5n4GZS4CBiVucQVTbnoFLSoOBm5uL4cnTpwzcHCwMvLx8FQwv3v8ECCAW"
    "sB+Bpv/9zRDGpyScxaukZnL66isGBiZxBnUuVoZ/988wPD62hoFL1pBBNqCegZ2bn+HmnYcM"
    "X77/Yfj3n6EKIAAAQQC+/wT+/gAAAgEAhiBHTXkpWogAzvYiAKzDBwD9AwAAL/bjAF5R9gDt"
    "4NMA5raaAOeRXAAnZKIAFRUVAA/5+gDy8fD2AgBBAL7/A1knAGYRJSOJAAkQuvXjzOrs/Aod"
    "g7YUANDWAAAg97cAzxifAL8K3gD7HiMAKNrbANvY1QAULUkABgQAAOzu8PkCAEEAvv8EDR0W"
    "eQ8lJ/jInraFAQUAJEh/GDmVQfYA3trwAGE99ABO4sMA0gviAFPxLwB7SU4AoZWhAAFIcgAL"
    "DxcABAQDAAKIhUtcREYr2JuFi495LTPjf2ZJcSaGWJnjDAwaPxgYgHHf+0aD4dhTbga/PxIM"
    "bMK3GATYvjN8f/2AQVRKnoGViZkBIAAAQQC+/wTl1d67FcS7SSE1JhQAAfoAAOjhAAD39AAA"
    "+vcAAPn3AEP/+ABD3xgA/Qg9APLZtwAA9fEAAP/+AAYGAQACAwEAAojly/sf8fsmbfATkBZI"
    "MbBXt1BSFoQo+vkNmDK/Mvz985Xh3fZnDCIPHzG8ZnrM8NLoH4OimBQDEyjmGRkZAAKICeiK"
    "18CYmPv4zgevLYtPLnt0+QEDwz+g7d+Arvj+nYHp50+Gf+ofGB7yPGB4rfiL4Y+oEoOQhALI"
    "EUADGBgAAogJnIaAJDs7w/tvPxmydu+4feH3+/cQQ75/ZWD89I1B3PAvg3z6X4a7ogwMivZp"
    "DBzcHEBd/8CpDyCAmP7/ATKB4fXuI9jrH18ziOzYfvgjw7Pbrxh+fvjI8P/TD4b3r/8xrAWm"
    "9g9yjgxGAdkMv378huQwIAAIIBYWUREGQedIBjYGToa/v/4xiGha/VYU/MFwesd0hv8vbzMA"
    "0yLD298cDILuUQwR8fUMTECnfv/2j4GdlQkYjSzsAAHEuO3AVQZmfmlgamQC++nPr+9lv368"
    "L/355RPDly9fGP7+ZQApZOAWFANa8IPhFyhMgGmfGRh4T56/+gQQYADZtXRJ8ecNFwAAAABJ"
    "RU5ErkJggg==")

    # Return the bitmap to use in the wxPython demo tree control.
    return image


def GetDemos():
    """
    Returns all the demo names in the package, together with the
    tree item name which will go in the wxPython demo tree control.
    """

    # The tree item text.
    TreeItemText = "Using Images"

    # The tree item's demos.
    TreeItemDemos = ()

    return TreeItemText, TreeItemDemos


def GetOverview():
    """
    Creates the wxHTML code to display on the tree item's Overview tab.
    """

    wxHtmlOverviewStr = '''\
    <html><body>
    <center><h2>Using Images</h2></center>
    <p>Image demos.
    </body></html>
    '''

    return wxHtmlOverviewStr
