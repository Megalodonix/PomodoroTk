import tkinter as tk
from PIL import Image, ImageTk
def readText(textFile):
        with open(textFile) as text:
            value = text.read()
            return value

class HelpMenuCommands():
    def __init__(self, root, pathToPic, txtFile, title):
         
        self.textpath = readText(txtFile)
        self.helpwin = tk.Toplevel(root)
        self.helpwin.geometry("600x300")
        self.helpwin.title(title)
        self.helpwin.resizable(False, False)
        self.path = pathToPic
        self.img = ImageTk.PhotoImage(Image.open(self.path))
        self.pic = tk.Label(self.helpwin, image=self.img)
        self.pic.photo = self.img
        self.pic.pack(side=tk.LEFT, padx=20)
        self.label = tk.Label(self.helpwin,
                        text=(f"{self.textpath}"),
                        justify='left').place(x=230, y=100)

