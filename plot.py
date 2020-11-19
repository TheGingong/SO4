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




        xer = np.linspace(-3, 3, 1000)
        yer = f(objectIntegralregning.a, xer, objectIntegralregning.b, objectIntegralregning.c)
        plt.plot(xer, yer)
        plt.fill_between(xer, yer, 0, color="red", alpha=0.5)
df
        ax = plt.subplots()
        #ax.text(0.5 * (objectIntegralregning.a + objectIntegralregning.b), 30, r"$\int_a^b f(x)\mathrm{d}x$",
         #       horizontalalignment='center', fontsize=20)
        ax.plot(xer, yer, 'r', linewidth=2)
        ax.set_ylim(bottom=0)

        plt.show()
plot()