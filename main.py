import math
from Integralregning import *
from differential import *
import tkinter as tk
from tkinter import messagebox
from sympy import *

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

        tk.Label(self.InputIntegralWindow, font="Helvetica 14 bold",
                 text="Herunder skal du indtaste din funktionsforskrift\n For eksempel: 5*x **2 + 5*x + 5\n"
                      "** HUSK AT LAVE '*' MELLEM TAL OG X **").pack()
        self.InputFRaw = tk.Entry(self.InputIntegralWindow)
        self.InputFRaw.pack()

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
              text="Herunder skal du indtaste din funktionsforskrift samt antallet af ").pack()
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

    #Funktionen der bliver kørt når man sender tal ind igennem en entryboks.
    #Den tjekker om visse krav bliver overholdt.
    def onPress(self):
        self.InputA = str(self.InputFRaw.get())
        if len(self.InputA) == 0:
            messagebox.showwarning("Fejl", "Det indtastede tal, skal være enten et tal eller decimaltal (brug punktum ikke komma)")
        else:
            if "0" in self.InputA:
                messagebox.showwarning("Fejl",
                                       "Det indtastede tal, må ikke være et 0. Hvis det var din intension, så lad være med at skriv noget")
            else:
                if "^" in self.InputA:
                    messagebox.showwarning("Fejl", "Når du skal opløfte en potens skal du benytte dig af ** istedet for ^.\n"
                                                   "Et eksempel på dette: a * x**2 + b * x + c")

window = tk.Tk()
app = main(master=window)
app.mainloop()