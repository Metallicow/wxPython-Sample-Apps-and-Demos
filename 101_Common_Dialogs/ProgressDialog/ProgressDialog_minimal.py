#!/usr/bin/env python

#-Imports----------------------------------------------------------------------

#--wxPython Imports.
import wx


if __name__ == '__main__':
    app = wx.App()

    max = 10
    dlg = wx.ProgressDialog("Minimal ProgressDialog Demo",
                            "An informative message",
                            maximum=max,
                            parent=None,
                            style=0
                                | wx.PD_APP_MODAL
                                | wx.PD_CAN_ABORT
                                ## | wx.PD_CAN_SKIP
                                | wx.PD_ELAPSED_TIME
                                | wx.PD_ESTIMATED_TIME
                                | wx.PD_REMAINING_TIME
                                ## | wx.PD_AUTO_HIDE
                                )

    keepGoing = True
    count = 0

    while keepGoing and count < max:
        count += 1
        wx.MilliSleep(1000)
        wx.Yield()

        if count >= max:
            (keepGoing, skip) = dlg.Update(count, "Done.")
        elif count >= max / 2:
            (keepGoing, skip) = dlg.Update(count, "Half-time!")
        else:
            (keepGoing, skip) = dlg.Update(count)

    dlg.Destroy()

    app.MainLoop()
