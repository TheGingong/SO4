from differential import *
from Integralregning import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import numpy as np

class plot():
    def __init__(self, objektet, lowerBound, upperBound):
        self.objektet = objektet
        self.funktionsforskrift = objektet.fn
        self.lower = lowerBound
        self.upper = upperBound

    #Funktionen for at plotte differentialberegningerne
    def plotDifferential(self):
        # Sætter x og y værdierne til at blive plottet
        self.xerDiff = np.linspace(self.lower-15, self.lower+15, 1000)
        self.ligningYvals = self.funktionsforskrift(self.xerDiff)
        self.tangentYvals = self.objektet.tangentPåLinjen(self.xerDiff)

        #Herunder laver vi et vindue hvor vi gerne vil plotte resultatet ud på. Dette gør vi ved hjælp af tkinter og matplotlib
        self.diffPlot = tk.Toplevel()
        self.diffPlot.title("Differentialregning visualiserede")
        self.diffPlot.geometry("700x400")

        figure = plt.Figure(figsize=(6, 5), dpi=100)
        chart_type = FigureCanvasTkAgg(figure, self.diffPlot)
        chart_type.get_tk_widget().pack()
        ax = figure.add_subplot(111)
        #Herover slutter vores linjer til at plotte i et GUI vindue

        # Skriver funktionsforskriften ind på grafen, og skriver b værdien ind baseret på om det er plus eller minus.
        if self.objektet.B > 0:
            self.printFunktionsforskrift = "f(x) = " + str(self.objektet.slope) + "x" + " + " + str(self.objektet.B)
        else:
            self.printFunktionsforskrift = "f(x) = " + str(self.objektet.slope) + "x" + " " + str(self.objektet.B)

        ax.plot(self.xerDiff, self.ligningYvals) # optegner kurven på grafen
        ax.plot(self.xerDiff, self.tangentYvals) # optegner tangenten på grafen

        ax.text(0.5, 0.5, f"f(x) for tangenten er: {self.printFunktionsforskrift}", ha='center', va='center',
                transform=ax.transAxes, fontsize=14)  # ax.text, laver text på grafen
        ax.set_title("Differential plot") # Tilføjer en title over graf
        ax.set_ylabel("y-akse")  # Skriver text ud fra den venstre side af grafen
        ax.set_xlabel("x-akse")  # Skriver text ud fra den højre side af grafen

    #Funktionen for at plotte integralberegningerne
    def plotIntegral(self):
        #Sætter x og y værdierne til at blive plottet
        self.xerInt = np.linspace(self.lower - 15, self.lower + 15, 1000)
        self.ligningYvals = self.funktionsforskrift(self.xerInt)

        #Herunder laver vi et vindue hvor vi gerne vil plotte resultatet ud på. Dette gør vi ved hjælp af tkinter og matplotlib
        self.intPlot = tk.Toplevel()
        self.intPlot.title("Integralregning visualiserede")
        self.intPlot.geometry("700x400")

        figure = plt.Figure(figsize=(6, 5), dpi=100)
        chart_type = FigureCanvasTkAgg(figure, self.intPlot)
        chart_type.get_tk_widget().pack()
        ax = figure.add_subplot(111)
        #Herover slutter vores linjer til at plotte i et GUI vindue

        ax.plot(self.xerInt, self.ligningYvals) #Plotter kurven i vinduet.
        ax.text(0.5, 0.5, f"Arealet mellem punkt x0 og x1 er: {self.objektet.sum:.3f}", ha='center', va='center',
                transform=ax.transAxes, fontsize=14)# ax.text, laver text på grafen
        filx1 = np.linspace(self.lower, self.upper, 100) #Laver vores areal på grafen
        fily = self.funktionsforskrift(filx1)
        ax.fill_between(filx1, fily, 0, color="red", alpha=0.5) #Laver fill i vores areal
        ax.vlines(x=[self.lower, self.upper], ymin=0,
                  ymax=[self.funktionsforskrift(self.lower),
                        self.funktionsforskrift(self.upper)], color="blue") #Vlines laver nogle linjer som gør fra x aksen og på til funktionen.

        ax.set_title("Integral plot") #Tilføjer en title over graf
        ax.set_ylabel("y-akse") #Skriver text ud fra den venstre side af grafen
        ax.set_xlabel("x-akse") #Skriver text ud fra den højre side af grafen