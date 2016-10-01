#!/usr/bin/env python


import wx
if 'phoenix' in wx.version():
    import wx.adv
    from wx.adv import Wizard
    from wx.adv import WizardPage, WizardPageSimple
    xwx = wx.adv
else: # Classic
    from wx.wizard import Wizard
    from wx.wizard import PyWizardPage as WizardPage
    from wx.wizard import WizardPageSimple
    xwx = wx.wizard


class MyWizardPage(WizardPage):
    """
    An extended panel obj with a few methods to keep track of its siblings.
    This should be modified and added to the wizard.
    Season to taste.
    """
    def __init__(self, parent, title):
        WizardPage.__init__(self, parent)

        self.next = self.prev = None
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        title = wx.StaticText(self, -1, title)
        title.SetFont(wx.Font(18, wx.FONTFAMILY_SWISS,
                                  wx.FONTSTYLE_NORMAL,
                                  wx.FONTWEIGHT_BOLD))
        self.sizer.Add(title, 0, wx.ALIGN_LEFT | wx.ALL, 5)
        self.sizer.Add(wx.StaticLine(self, -1), 0, wx.EXPAND | wx.ALL, 5)
        self.SetSizer(self.sizer)

    def add_stuff(self, stuff):
        """Add additional widgets to the bottom of the page."""
        self.sizer.Add(stuff, 0, wx.EXPAND | wx.ALL, 5)

    def SetNext(self, next):
        """Set the next page."""
        self.next = next

    def SetPrev(self, prev):
        """Set the previous page."""
        self.prev = prev

    def GetNext(self):
        """Return the next page."""
        return self.next

    def GetPrev(self):
        """Return the previous page."""
        return self.prev


class MyWizard(Wizard):
    """Add pages to this wizard object to make it useful."""
    def __init__(self, title, img_filePath=""):
        # img could be replaced by a py string of bytes
        if img_filePath and os.path.exists(img_filePath):
            img = wx.Bitmap(img_filePath)
        else:
            img = wx.NullBitmap
        Wizard.__init__(self, None, -1, title, img)
        self.pages = []
        # Lets catch the events
        self.Bind(xwx.EVT_WIZARD_PAGE_CHANGED, self.OnWizardPageChanged)
        self.Bind(xwx.EVT_WIZARD_PAGE_CHANGING, self.OnWizardPageChanging)
        self.Bind(xwx.EVT_WIZARD_CANCEL, self.OnWizardCancel)
        self.Bind(xwx.EVT_WIZARD_FINISHED, self.OnWizardFinished)

    def DoAddWizardPage(self, page):
        """Add a wizard page to the list."""
        if self.pages:
            previous_page = self.pages[-1]
            page.SetPrev(previous_page)
            previous_page.SetNext(page)
        self.pages.append(page)

    def DoRunWizard(self):
        self.RunWizard(self.pages[0])

    def OnWizardPageChanged(self, event):
        """Executed after the page has changed."""
        if event.GetDirection():
            dir = "forward"
        else:
            dir = "backward"
        page = event.GetPage()
        print("page_changed: %s, %s\n" % (dir, page.__class__))

    def OnWizardPageChanging(self, event):
        """Executed before the page changes, so we might veto it."""
        if event.GetDirection():
            dir = "forward"
        else:
            dir = "backward"
        page = event.GetPage()
        print("page_changing: %s, %s\n" % (dir, page.__class__))

    def OnWizardCancel(self, event):
        """
        Cancel button has been pressed.
        Clean up and exit without continuing.
        """
        page = event.GetPage()
        print("OnWizardCancel: %s\n" % page.__class__)

        # Prevent cancelling of the wizard.
        if page is self.pages[0]:
            wx.MessageBox("Cancelling on the first page has been prevented.",
                          "Sorry")
            event.Veto()

    def OnWizardFinished(self, event):
        """Finish button has been pressed.  Clean up and exit."""
        print("OnWizFinished\n")


if __name__ == '__main__':
    import os
    import sys
    try:
        gFileDir = os.path.dirname(os.path.abspath(__file__))
    except:
        gFileDir = os.path.dirname(os.path.abspath(sys.argv[0]))

    app = wx.App()  # Start the application

    # Create wizard and add any kind pages you'd like
    imgPath = gFileDir + os.sep + 'bitmaps' + os.sep + 'wiztest1.bmp'
    mywiz = MyWizard('Simple Wizard', img_filePath=imgPath)
    page1 = MyWizardPage(mywiz, 'Page 1')  # Create a first page
    page1.add_stuff(wx.TextCtrl(page1, -1,
            ('Hello from wxPython %s ' % wx.version() +
             'running on Python %d.%d.%d.%s' % sys.version_info[:-1]),
             style=wx.TE_MULTILINE | wx.TE_READONLY))
    mywiz.DoAddWizardPage(page1)

    # Add some more pages
    mywiz.DoAddWizardPage(MyWizardPage(mywiz, 'Page 2'))
    mywiz.DoAddWizardPage(MyWizardPage(mywiz, 'Page 3'))

    mywiz.DoRunWizard() # Show the main window

    # Cleanup
    mywiz.Destroy()
    app.MainLoop()
