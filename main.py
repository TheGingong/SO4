import math
from Integralregning import *
from differential import *
import tkinter as tk

class main(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        window.title("Menu")
        window.geometry("1000x666")
        self.theHub()
        self.pack()

    def theHub(self):
        self.differentiering  = tk.Button(self)
        self.differentiering ["text"] = "Differentiering"
        #self.differentiering["command"] =
        self.differentiering.pack(side=tk.TOP)

        self.integration = tk.Button(self)
        self.integration["text"] = "Integration"
        self.integration["command"] = self.InputIntegral
        self.integration.pack(side=tk.TOP)

    def InputIntegral(self):
        self.InputIntegralWindow = tk.Toplevel()
        self.InputIntegralWindow.title("Integral vindue")
        self.InputIntegralWindow.geometry("600x400")
        tk.Label(self.InputIntegralWindow, font="Helvetica 10 bold",
                 text="Herunder skal du indtaste hvad din 'a', 'b', 'c' og 'potens' værdierne, herefter tryk confirm").pack()
        self.InputARaw = tk.Entry(self.InputIntegralWindow)
        self.InputARaw.pack()

        self.confirm = tk.Button(self.InputIntegralWindow, text="Acceptér valg.", padx=10, pady=10, fg="dark green",
                                 command=self.onPress)
        self.confirm.pack()

        tk.Button(self.InputIntegralWindow, text="Tilbage til menuen.", padx=10, pady=10, fg="coral1",
                  command=self.InputIntegralWindow.destroy).pack()

    def onPress(self):
        self.InputA = self.InputARaw.get()

window = tk.Tk()
app = main(master=window)
app.mainloop()