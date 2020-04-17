import random
import wx

########################################################################
class MyPanel(wx.Panel):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent)

        self.port = wx.StaticText(self, label="Port:")
        self.stream_status = wx.StaticText(self, label="Start Stream")
        self.dialing_status = wx.StaticText(self, label="no dial tone")
        self.SetBackgroundColour((147, 136, 136))
        self.tbtn = wx.ToggleButton(self, -1, "Start Stream", pos = (200,200))
        self.tbtn.Bind(wx.EVT_TOGGLEBUTTON, self.onUpdate)
        self.tbtn.SetBackgroundColour((229, 18, 39))

        # btn = wx.Button(self, label="Update")
        # btn.Bind(wx.EVT_BUTTON, self.onUpdate)
        # self.tbtn = wx.ToggleButton(self, -1, "Start Stream", pos = (200,200))
        # self.tbtn.Bind(wx.EVT_TOGGLEBUTTON, self.onUpdate)
        # self.tbtn.SetBackgroundColour((229, 18, 39))

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.port, 0, wx.ALL, 5)
        sizer.Add(self.stream_status, 0, wx.ALL, 5)
        sizer.Add(self.dialing_status, 0, wx.ALL, 5)
        sizer.Add(self.tbtn, 0, wx.ALL, 5)
        self.SetSizer(sizer)
    #----------------------------------------------------------------------
    def update_text(self, info):
        """"""
        # index = {
        #     "Port:":self.port,
        #     "stream status":self.stream_status,
        #     "dial status":self.dialing_status
        #     }
        # text = index[info]
        data = info[1]
        append = info[0]
        self.stream_status.SetLabel(data)
        self.port.SetLabel(append)
        self.tbtn.SetLabel("Stop Stream")

    #----------------------------------------------------------------------
    def onUpdate(self, event):
        """"""
        # info = random.choice(
        #     [("Port:", "mork89", 1),
        #      ("stream status", "Stop Stream", 0),
        #      ("dial status", "dialing", 1)
        #      ])
        info = ["hi", "hello"]
                # Active State
        if self.button.GetValue() == True:

            self.button.SetLabel('Stop')
        self.update_text(info)

########################################################################
class MainFrame(wx.Frame):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, title="A.T.O.M. Controller")
        panel = MyPanel(self)
        self.Show()

if __name__ == "__main__":
    app = wx.App(False)
    frame = MainFrame()
    app.MainLoop()