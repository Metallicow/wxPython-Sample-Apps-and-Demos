#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-Imports----------------------------------------------------------------------

#--wxPython Imports.
import wx
if not 'phoenix' in wx.version():
    wx.adv = wx
else:
    import wx.adv

if __name__ == '__main__':
    app = wx.App()

    info = wx.adv.AboutDialogInfo()
    info.Name = "Hello World"
    info.Version = "1.2.3"
    info.Copyright = "(C) 2006 Programmers and Coders Everywhere"
    info.Description = """\
A \"hello world\" program is a software program that prints out
\"Hello world!\" on a display device. It is used in many introductory
tutorials for teaching a programming language.

Such a program is typically one of the simplest programs possible
in a computer language. A \"hello world\" program can be a useful
sanity test to make sure that a language's compiler, development
environment, and run-time environment are correctly installed.
        """
    info.WebSite = ("http://en.wikipedia.org/wiki/Hello_world",
                    "Hello World home page")
    info.Developers = ("Joe Programmer",
                       "Jane Coder",
                       "Vippy the Mascot")

    info.License = "blah " * 250 + "\n\n" + "yadda " * 100

    # Then we call wx.AboutBox giving it that info object
    wx.adv.AboutBox(info)

    app.MainLoop()
