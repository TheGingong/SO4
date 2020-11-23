import math
from Integralregning import *
from differential import *
import tkinter as tk
from tkinter import messagebox

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
        self.differentiering["command"] = self.InputDifferentiering
        self.differentiering.pack(side=tk.TOP)

        self.integration = tk.Button(self)
        self.integration["text"] = "Integral"
        self.integration["command"] = self.InputIntegral
        self.integration.pack(side=tk.TOP)

        self.afslut = tk.Button(self, text="Afslut Program", padx=10, pady=10, fg="coral1",
                                command=self.master.destroy)
        self.afslut.pack(side=tk.BOTTOM)

    def InputIntegral(self):
        self.InputIntegralWindow = tk.Toplevel()
        self.InputIntegralWindow.title("Integral vindue")
        self.InputIntegralWindow.geometry("600x400")
        tk.Label(self.InputIntegralWindow, font="Helvetica 10 bold",
                 text="Herunder skal du indtaste hvad din 'a', 'b', 'c' og 'potens' værdierne, herefter tryk confirm").pack()

        tk.Label(self.InputIntegralWindow, font="Helvetica 10 bold",
                 text="Herunder skal du indtaste hvad din 'a' værdi skal være").pack()
        self.InputARaw = tk.Entry(self.InputIntegralWindow)
        self.InputARaw.pack()

        tk.Label(self.InputIntegralWindow, font="Helvetica 10 bold",
                 text="Herunder skal du indtaste hvad din 'potens' værdi for 'a'").pack()

        self.InputPRaw = tk.Entry(self.InputIntegralWindow)
        self.InputPRaw.pack()

        tk.Label(self.InputIntegralWindow, font="Helvetica 10 bold",
                 text="Herunder skal du indtaste hvad din 'b' værdi skal være").pack()

        self.InputBRaw = tk.Entry(self.InputIntegralWindow)
        self.InputBRaw.pack()

        tk.Label(self.InputIntegralWindow, font="Helvetica 10 bold",
                 text="Herunder skal du indtaste hvad din 'c' værdi skal være").pack()

        self.InputCRaw = tk.Entry(self.InputIntegralWindow)
        self.InputCRaw.pack()



        self.confirm = tk.Button(self.InputIntegralWindow, text="Confirm", padx=10, pady=10, fg="dark green",
                                 command=self.onPress)
        self.confirm.pack()

        tk.Button(self.InputIntegralWindow, text="Tilbage til menuen.", padx=10, pady=10, fg="coral1",
                  command=self.InputIntegralWindow.destroy).pack()


    def InputDifferentiering(self):
        self.DifferentieringWindow = tk.Toplevel()
        self.DifferentieringWindow.title("Differentiering")
        self.DifferentieringWindow.geometry("600x400")

        tk.Label(self.DifferentieringWindow, font="Helvetica 10 bold",
              text="Herunder skal du indtaste hvad din 'a' værdi skal være").pack()
        self.InputARaw = tk.Entry(self.DifferentieringWindow)
        self.InputARaw.pack()

        tk.Label(self.DifferentieringWindow, font="Helvetica 10 bold",
                 text="Herunder skal du indtaste hvad din 'potens' værdi for 'a'").pack()
        self.InputPRaw = tk.Entry(self.DifferentieringWindow)
        self.InputPRaw.pack()

        tk.Label(self.DifferentieringWindow, font="Helvetica 10 bold",
                 text="Herunder skal du indtaste hvad din 'b' værdi skal være").pack()
        self.InputBRaw = tk.Entry(self.DifferentieringWindow)
        self.InputBRaw.pack()

        tk.Label(self.DifferentieringWindow, font="Helvetica 10 bold",
                 text="Herunder skal du indtaste hvad din 'c' værdi skal være").pack()
        self.InputCRaw = tk.Entry(self.DifferentieringWindow)
        self.InputCRaw.pack()

        self.confirm = tk.Button(self.DifferentieringWindow, text="Confirm", padx=10, pady=10, fg="dark green",
                            command=self.onPress)
        self.confirm.pack()

        tk.Button(self.DifferentieringWindow, text="Tilbage til menuen.", padx=10, pady=10, fg="coral1",
                  command=self.DifferentieringWindow.destroy).pack()

    def onPress(self):
        try:
            self.InputA = float(self.InputARaw.get())
            self.InputP = int(self.InputPRaw.get())
            self.InputB = float(self.InputBRaw.get())
            self.InputC = float(self.InputCRaw.get())
        except:
            messagebox.showwarning("Fejl", "Det indtastede tal, skal være enten et tal eller decimaltal (brug punktum ikke komma)")


window = tk.Tk()
app = main(master=window)
app.mainloop()