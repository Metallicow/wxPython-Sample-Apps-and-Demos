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
    image = morecontrols16 = PyEmbeddedImage(
    "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAACq0lEQVR4nIXSQUtbWRjG8f89"
    "9yRGTYj2SgKVzKIg46BZSCkUo0N3tQuZTYabwQ/QzQzDLAfapRSy6MYP0I3QSBcuhiEGKnYr"
    "LZmKCDpiXFhjhoQ0aGJ7bu49ZxZiY7rps3s58OPlPY8sFAqGb+Tft28RxSLGstALC3x/796X"
    "NwkwNjZGvV5ndHQUKSUbGxsUi0UuLy9ptVqEPI+/njyBIGDx2TPqz5+TSqXI5/NXQDqdpt1u"
    "4/s+WmuWlpbIZrP4vo9SivKbN9hKYXyfP37/jan7s4yMjFCtVq+ARCJBIpHoW7vdbgMghKBV"
    "Oca8/wfjd0nfjfDjgwfYtk2lUrkCbub8/Jxms8nfs7Pcnp4mUIrAGEilEN0uwasmWy9/QmvN"
    "ebncDzQaDarVKgMDAySSSaYnJhBKwefPXDabmCDgh/govjH4xtCJx3uAUoqdnR1s2+bs7IyN"
    "gwNeHx/j+z5Bp8OvMzPgebx4945QLIZtWfz38WMP2N/fZ3t7GyEEJycntB89Yv/DB46OjjCd"
    "Dn8eHIAxTD59ys+PHxONRllfX+8Bp6enFAoFUqkUtVqNWq1Go9HA8zzGgFszM1ha4336hJQS"
    "IUSvBwCO43B4eMju7i5CCLTWAITDYYakZKdSQdg2lhBYltUPBEFAOp0mm82yurqK1ppQKEQ8"
    "HsdxHCbu3OFlNMrCw4f8sriIUorBwcEeYFkWUkry+Ty1Wo3NzU0cxyGZTBKJRKg3m9zPZNDR"
    "KK+3tvq+XV6XRWuNlJLl5WXm5+fZ29sDIBaLkclkmJubo1wu47ouAGtra+RyuWhfD4aHh5mc"
    "nGRqagqlFJ7nMTQ0RDgc5uLiAoBWq0WpVCKXy0WMMeoLEIlE+Bq7meujlUolXNe1rjeRACsr"
    "K2fdbrc7Pj7+Hd+I67rWzfl/sCoi6Ch8JCoAAAAASUVORK5CYII=")

    # Return the bitmap to use in the wxPython demo tree control.
    return image


def GetDemos():
    """
    Returns all the demo names in the package, together with the
    tree item name which will go in the wxPython demo tree control.
    """

    # The tree item text.
    TreeItemText = "ContextHelp"

    # The tree item's demos.
    TreeItemDemos = (
        'ContextHelp_extended.py',
        'ContextHelp_minimal.py',
        )

    return TreeItemText, TreeItemDemos


def GetOverview():
    """
    Creates the wxHTML code to display on the tree item's Overview tab.
    """

    wxHtmlOverviewStr = '''\
    <html><body>
    <center><h2>ContextHelp</h2></center>
    <p>ContextHelp demos.
    </body></html>
    '''

    return wxHtmlOverviewStr
