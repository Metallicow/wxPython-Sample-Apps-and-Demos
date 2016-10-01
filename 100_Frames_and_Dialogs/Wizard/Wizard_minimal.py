#!/usr/bin/env python

#-Imports----------------------------------------------------------------------

#--wxPython Imports.
import wx
if 'phoenix' in wx.version():
    from wx.adv import Wizard, WizardPageSimple
else: # Classic
    from wx.wizard import Wizard, WizardPageSimple


if __name__ == '__main__':
    app = wx.App(False)

    mywiz = Wizard(None, -1, 'My Wizard')
    mywiz.pages = []

    for i in range(3):
        page = WizardPageSimple(mywiz)
        st = wx.StaticText(page, -1, 'Wizard Page %d' % (i + 1))

        if mywiz.pages:
            previous_page = mywiz.pages[-1]
            page.SetPrev(previous_page)
            previous_page.SetNext(page)
        mywiz.pages.append(page)

    mywiz.RunWizard(mywiz.pages[0])
    mywiz.Destroy()
    app.MainLoop()
