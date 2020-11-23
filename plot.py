import math
from differential import *
from Integralregning import *
import matplotlib.pyplot as plt
from matplotlib import *
import numpy as np

class plot(differential, integralregning):
    def __init__(self):
        def f(a, x, b, c):
            # Her laver vi selve funktionsforskriften fra a, b og c.
            return ((a * x ** 2) + (b * x) + c)

        lower = objectIntegralregning.plotxZeroINT
        upper = objectIntegralregning.plotxOneINT

        #Plot af integralregning
        xer = np.linspace(-15, 15, 1000)
        yer = f(objectIntegralregning.a, xer, objectIntegralregning.b, objectIntegralregning.c)
        filx1 = np.linspace(lower, upper, 100)
        fily = f(objectIntegralregning.a, filx1, objectIntegralregning.b, objectIntegralregning.c)
        ax = plt.subplot()
        plt.plot(xer, yer)
        #plt.fill_between(xer, yer, 0, color="red", alpha=0.5) #Denne fil er blevet pillet ud da vi ikke ønsker at farve hele grafen men kun arealet.
        plt.vlines(x=[lower,upper],ymin=0,ymax=[f(objectIntegralregning.a, lower, objectIntegralregning.b, objectIntegralregning.c),f(objectIntegralregning.a, upper, objectIntegralregning.b, objectIntegralregning.c)], color= "green")
        plt.fill_between(filx1, fily, 0, color="red", alpha=0.5)
        ax.text(0, 0, "Arealet er: " + str(objectIntegralregning.sum), ha = 'center', va = 'center', fontsize= 14 )
        plt.show()


        #Plot af differentialregningen
        xerDiff = np.linspace(objectDiff.xZero, objectDiff.plotxOneDIFF, 1000)
        yerDiff = self.tangentPåLinjen(xer)
        plt.plot(xerDiff, yerDiff)
        plt.plot(xerDiff, f(objectDiff.a, xer, objectDiff.b, objectDiff.c))
        plt.show()
plot()
