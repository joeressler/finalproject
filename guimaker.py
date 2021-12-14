from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from simulator import *
import ntpath

class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Python Tkinter Dialog Widget")
        self.minsize(640, 400)
 
        self.labelFrame = ttk.LabelFrame(self, text = "Open File")
        self.labelFrame.grid(column = 0, row = 1, padx = 20, pady = 20)
 
        self.button()
        self.numrunsbutton = ttk.Entry(self.labelFrame, text="# of Runs").grid(column = 1, row = 3)
    
    def button(self):
        self.button = ttk.Button(self.labelFrame, text = "Browse A File",command = self.fileDialog)
        self.button.grid(column = 1, row = 1)
    
    def runbutton(self):
        self.numruns = self.numrunsbutton.get()
        self.filename = ntpath.basename(self.path)
        guiFunction(self.filename, self.numruns)
    
    def fileDialog(self):
        self.path = filedialog.askopenfilename(initialdir =  "/", title = "Select A File", filetype =
        (("json files","*.json"),("all files","*.*")) )
        self.label = ttk.Label(self.labelFrame, text = "")
        self.label.grid(column = 1, row = 2)
        self.label.configure(text = self.path)
        self.runbutton = ttk.Button(self.labelFrame, text="Run", width=25, command=self.runbutton())

root = Root()
root.mainloop()