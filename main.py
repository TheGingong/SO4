import math
from Integralregning import *
from differential import *
import tkinter as tk
from tkinter import messagebox
from plot import *

class main(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        window.title("Menu")
        window.geometry("1000x666")
        self.theHub()
        self.pack()

    def theHub(self):
        #Den øverste tekst som bliver vist i GUI'en.
        tk.Label(self.master, font="Helvetica 12",
                 text="Herunder skal du indtaste din funktionsforskrift\n For eksempel: 5*x **2 + 5*x + 5\n"
                      "** HUSK AT LAVE '*' MELLEM TAL OG X **").pack()

        #Entry boks til funktionsforskrift
        self.InputFuncRaw = tk.Entry(self.master)
        self.InputFuncRaw.pack()

        #Tekst felt der forklarer hvad man skal indputte
        tk.Label(self.master, font="Helvetica 12", text="Herunder skal du indtaste din første x værdi (x0)").pack()
        #Første entryboks til X0 (lower)
        self.InputLowerRaw = tk.Entry(self.master)
        self.InputLowerRaw.pack()

        #Tekst felt der forklarer hvad man skal indputte
        tk.Label(self.master, font="Helvetica 12",text="Herunder skal du indtaste din sidste x værdi (x1)").pack()
        #Anden entryboks til X1 (upper)
        self.InputUpperRaw = tk.Entry(self.master)
        self.InputUpperRaw.pack()

        # Tekst felt der forklarer hvad man skal indputte
        tk.Label(self.master, font="Helvetica 14", text="Herunder skal du vælge om du vil plotte en differential- eller integral kurve").pack()
        #Differentionsknap hvor man vælger at plotte diff
        self.diffknap = tk.Button(self)
        self.diffknap ["text"] = "Differentiering plot"
        self.diffknap["command"] = self.onPressDiff
        self.diffknap.pack(side=tk.TOP)

        #Integral knap hvor man vælger at plotte integralregningen
        self.intknap = tk.Button(self)
        self.intknap["text"] = "Integral plot"
        self.intknap["command"] = self.onPressInt
        self.intknap.pack(side=tk.TOP)

        #Afslut knap
        self.afslut = tk.Button(self, text="Afslut Program", padx=10, pady=10, fg="coral1",
                                command=self.master.destroy)
        self.afslut.pack(side=tk.BOTTOM)

    #Funktionen der bliver kørt når man sender tal ind igennem en entryboks.
    #Den tjekker om visse krav bliver overholdt.
    #Den laver også en objekt af den valgte metode, og sender objektet til behandling i de forskellige klasser (DIFF)
    def onPressDiff(self):
        self.InputLower = float(self.InputLowerRaw.get())
        self.InputUpper = float(self.InputUpperRaw.get())
        self.InputFunc = str(self.InputFuncRaw.get())
        if len(self.InputFunc) == 0:
            messagebox.showwarning("Fejl", "Det indtastede tal, skal være enten et tal eller decimaltal (brug punktum ikke komma)")
        else:
            self.objectDiff = Diff(self.InputFunc, self.InputLower, self.InputUpper)
            # Vælg en af de to til test underneden. Så COMMENT den du ikke bruger.
            self.objectDiff.Differentialudregner()
            # self.objectDiff.slopeFunction()
            plotObjectDiff = plot(self.objectDiff, self.InputLower, self.InputUpper)
            plotObjectDiff.plotDifferential()

    # Funktionen der bliver kørt når man sender tal ind igennem en entryboks.
    # Den tjekker om visse krav bliver overholdt.
    # Den laver også en objekt af den valgte metode, og sender objektet til behandling i de forskellige klasser (INT)
    def onPressInt(self):
        self.InputLower = float(self.InputLowerRaw.get())
        self.InputUpper = float(self.InputUpperRaw.get())
        self.InputFunc = str(self.InputFuncRaw.get())
        if len(self.InputFunc) == 0:
            messagebox.showwarning("Fejl", "Det indtastede tal, skal være enten et tal eller decimaltal (brug punktum ikke komma)")
        else:
            self.objectInt = integralregning(self.InputFunc, self.InputLower, self.InputUpper, 1000)
            self.objectInt.integral()
            plotObjectInt = plot(self.objectInt, self.InputLower, self.InputUpper)
            plotObjectInt.plotIntegral()

window = tk.Tk()
app = main(master=window)
app.mainloop()