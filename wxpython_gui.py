import wx

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="My To-Do App")
        panel = wx.Panel(self)

        vbox = wx.BoxSizer(wx.VERTICAL)

        self.entry = wx.TextCtrl(panel)
        self.listbox = wx.ListBox(panel)

        button = wx.Button(panel, label="Add")
        button.Bind(wx.EVT_BUTTON, self.add_todo)

        vbox.Add(wx.StaticText(panel, label="Type in to-do"))
        vbox.Add(self.entry, flag=wx.EXPAND)
        vbox.Add(button)
        vbox.Add(self.listbox, proportion=1, flag=wx.EXPAND)

        panel.SetSizer(vbox)
        self.Show()

    def add_todo(self, event):
        todo = self.entry.GetValue()
        if todo:
            self.listbox.Append(todo)
            self.entry.Clear()

app = wx.App()
MyFrame()
app.MainLoop()
