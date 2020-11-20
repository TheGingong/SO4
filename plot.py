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

        a = objectIntegralregning.xZero
        b = objectIntegralregning.xOne
        print(a,b)

        xer = np.linspace(-15, 15, 1000)
        yer = f(objectIntegralregning.a, xer, objectIntegralregning.b, objectIntegralregning.c)
        #ax = plt.subplots()
        plt.plot(xer, yer)
        plt.fill_between(xer, yer, 0, color="red", alpha=0.5)
        plt.vlines(x=[a,b],ymin=0,ymax=[100,100])
        plt.show()
plot()