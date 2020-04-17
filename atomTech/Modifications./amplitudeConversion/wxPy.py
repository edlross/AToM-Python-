import wx

class MyPanel(wx.Panel): 
     
   def __init__(self, parent): 
      super(MyPanel, self).__init__(parent)
      vbox = wx.BoxSizer(wx.VERTICAL)

      self.SetBackgroundColour((147, 136, 136))
		
      self.tbtn = wx.ToggleButton(self, -1, "Start/Stop Stream", pos = (200,200))
      t = self.tbtn
      vbox.Add(t,0,wx.EXPAND|wx.ALIGN_CENTER) 
      t.SetBackgroundColour((229, 18, 39))
      t.Bind(wx.EVT_TOGGLEBUTTON, self.btnclk) 
      self.Bind(wx.EVT_BUTTON, self.OnButtonClicked) 
		
   def OnButtonClicked(self, e): 
         
      print('Panel received click event. propagated to Frame class')
      e.Skip()  
		
   def btnclk(self,e): 
      print("Button received click event. propagated to Panel class")
      e.Skip()
		
class Example(wx.Frame):

   def __init__(self,parent): 
      super(Example, self).__init__(parent)  
         
      self.InitUI() 

   def InitUI(self):
	
      mpnl = MyPanel(self) 
      self.Bind(wx.EVT_BUTTON, self.OnButtonClicked)
		
      self.SetTitle('Event propagation demo') 
      self.SetSize((1000,500))
      self.Centre() 
      self.Show(True)
		
   def OnButtonClicked(self, e): 
         
      print('click event received by frame class') 
      e.Skip()
		
ex = wx.App() 
Example(None) 
ex.MainLoop()