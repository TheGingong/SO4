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

        lower = objectIntegralregning.xZero
        upper = objectIntegralregning.xOne
        print(lower,upper)
        xer = np.linspace(-15, 15, 1000)
        yer = f(objectIntegralregning.a, xer, objectIntegralregning.b, objectIntegralregning.c)
        #ax = plt.subplots()
        plt.plot(xer, yer)
        plt.fill_between(xer, yer, 0, color="red", alpha=0.5)
        plt.vlines(x=[lower,upper],ymin=0,ymax=[f(objectIntegralregning.a, lower, objectIntegralregning.b, objectIntegralregning.c),f(objectIntegralregning.a, upper, objectIntegralregning.b, objectIntegralregning.c)], color= "green")
        plt.show()
plot()