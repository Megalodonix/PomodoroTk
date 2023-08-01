import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk


def readText(textFile):
        with open(textFile) as text:
            value = text.read()
            return value

class HelpMenuCommands():
    def __init__(self, root, pathToPic, txtFile, title):
         
        self.textpath = readText(txtFile)
        self.helpwin = tk.Toplevel(root)
        self.helpwin.geometry("500x300")
        self.helpwin.config(bg="#f7f6f7")
        self.helpwin.title(title)
        self.helpwin.resizable(False, False)
        self.path = pathToPic
        self.imagefile = Image.open(self.path)
        self.img = ImageTk.PhotoImage(image=self.imagefile)        
        self.pic = ttk.Label(self.helpwin, image=self.img)
        self.pic.photo = self.img
        self.pic.place(x=300)
        self.label = ttk.Label(self.helpwin,
                        text=(f"{self.textpath}"),
                        justify='left').place(x=10, y=80)

