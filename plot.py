import math
from differential import *
from Integralregning import *
import matplotlib.pyplot as plt
from matplotlib import *
import numpy as np
""""
class Plot():
    def __init__(self, objektet):
        self.funktionsforskrift = objektet.fn
        self.lower = objektet.lowerBound
        self.upper = objektet.upperBound
        self.plot_Differentialregning()

    def plot_Integralregning(self):
        #Plot af integralregning
        xer = np.linspace(-15, 15, 1000)
        yer = f(objectIntegralregning.a, xer, objectIntegralregning.b, objectIntegralregning.c)
        filx1 = np.linspace(lower, upper, 100)
        fily = f(objectIntegralregning.a, filx1, objectIntegralregning.b, objectIntegralregning.c)
        ax = plt.subplot()
        plt.plot(xer, yer)
        #plt.fill_between(xer, yer, 0, color="red", alpha=0.5)
        plt.vlines(x=[lower,upper],ymin=0,ymax=[f(objectIntegralregning.a, lower, objectIntegralregning.b, objectIntegralregning.c),f(objectIntegralregning.a, upper, objectIntegralregning.b, objectIntegralregning.c)], color= "green")
        plt.fill_between(filx1, fily, 0, color="red", alpha=0.5)
        ax.text(0, 500, "Arealet er: " + str(objectIntegralregning.sum), ha = "center", fontsize= 14 )
        plt.show()

    def plot_Differentialregning(self):
        #Plot af differentialregningen
        xerDiff = np.linspace(-15, 15, 1000)
        yerDiff = self.tangentPåLinjen(xerDiff)
        plt.plot(xerDiff, yerDiff)
        plt.plot(xerDiff, self.funktionsforskrift(xerDiff))
        plt.show()
"""""