import math

import tkinter as tk

from tkinter import *



class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
    
    def fu(self):
        	self.fau
    
    def fau(self):	
    	res = 1
    	print(1)

    def create_widgets(self):
        
        self.widget1 = tk.Frame(self)
        self.widget1.pack()
        self.msg = Label(self.widget1, text="Calculadora master power zica das calculation\n")
        self.msg.pack ()

        bot = Frame(root)
        bot.pack(side=BOTTOM)

        self.autenticar = Button(bot)
        self.autenticar["text"] = "7"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = ""
        self.autenticar.pack(side=LEFT,fill=None)

        self.autenticar = Button(bot)
        self.autenticar["text"] = "8"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = ""
        self.autenticar.pack(side=LEFT,fill=None)

        self.autenticar = Button(bot)
        self.autenticar["text"] = "9"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = ""
        self.autenticar.pack(side=LEFT,fill=None)

        bu = Frame(root)
        bu.pack(side=BOTTOM)

        self.autenticar = Button(bu)
        self.autenticar["text"] = "4"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = ""
        self.autenticar.pack(side=LEFT,fill=None)

        self.autenticar = Button(bu)
        self.autenticar["text"] = "5"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = ""
        self.autenticar.pack(side=LEFT,fill=None)

        self.autenticar = Button(bu)
        self.autenticar["text"] = "6"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = ""
        self.autenticar.pack(side=LEFT,fill=None)

        bom = Frame(root)
        bom.pack(side=BOTTOM)

        self.autenticar = Button(bom)
        self.autenticar["text"] = "1"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = ""
        self.autenticar.pack(side=LEFT,fill=None)

        self.autenticar = Button(bom)
        self.autenticar["text"] = "2"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = ""
        self.autenticar.pack(side=LEFT,fill=None)
        
       	self.autenticar = Button(bom)
        self.autenticar["text"] = "3"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = ""
        self.autenticar.pack(side=LEFT,fill=None)

        mult = Frame(root)
        mult.pack(side=BOTTOM)

        self.autenticar = Button(mult)
        self.autenticar["text"] = "*"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = ""
        self.autenticar.pack(side=LEFT,fill=None)

        self.autenticar = Button(mult)
        self.autenticar["text"] = "+"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = ""
        self.autenticar.pack(side=LEFT,fill=None)
        
       	self.autenticar = Button(mult)
        self.autenticar["text"] = "-"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.fu
        self.autenticar.pack(side=LEFT,fill=None)

        





    
root = tk.Tk()
app = Application(master=root)
app.mainloop()