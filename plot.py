from differential import *
from Integralregning import *
import matplotlib.pyplot as plt
import numpy as np

class plot():
    def __init__(self, objektet, lowerBound, upperBound):
        self.objektet = objektet
        self.funktionsforskrift = objektet.fn
        self.lower = lowerBound
        self.upper = upperBound

    def plotDifferential(self):
        self.xerDiff = np.linspace(self.lower-15, self.lower+15, 1000)
        self.ligningYvals = self.funktionsforskrift(self.xerDiff)
        self.tangentYvals = self.objektet.tangentPåLinjen(self.xerDiff)
        plt.plot(self.xerDiff, self.ligningYvals)
        plt.plot(self.xerDiff, self.tangentYvals) # optegner linjerne på grafen

        plt.title("Differential plot") # Tilføjer en title over graf
        plt.ylabel("y-akse")  # Skriver text ud fra den venstre side af grafen
        plt.xlabel("x-akse")  # Skriver text ud fra den højre side af grafen
        plt.show()

    def plotIntegral(self):
        self.xerInt = np.linspace(self.lower - 15, self.lower + 15, 1000)
        self.ligningYvals = self.funktionsforskrift(self.xerInt)
        plt.plot(self.xerInt, self.ligningYvals)
        ax = plt.subplot() #hjælper til med text på grafen
        ax.text(0.5, 0.5, f"Arealet er: {self.objektet.sum:.3f}", ha='center', va='center',
                transform=ax.transAxes, fontsize=14)# ax.text, laver text på grafen
        filx1 = np.linspace(self.lower, self.upper, 100) #Laver vores areal på grafen
        fily = self.funktionsforskrift(filx1)
        plt.fill_between(filx1, fily, 0, color="red", alpha=0.5) #Laver fill i vores areal
        plt.vlines(x=[self.lower, self.upper], ymin=0,
                  ymax=[self.funktionsforskrift(self.lower),
                        self.funktionsforskrift(self.upper)], color="blue") #Vlines laver nogle linjer som gør fra x aksen og på til funktionen.

        plt.title("Integral plot") #Tilføjer en title over graf
        plt.ylabel("y-akse") #Skriver text ud fra den venstre side af grafen
        plt.xlabel("x-akse") #Skriver text ud fra den højre side af grafen
        plt.show()