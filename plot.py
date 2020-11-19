import math
from differential import *
from Integralregning import *
import matplotlib.pyplot as plt
import numpy as np
#from sympy import *

#print(object.a, object.b, object.c, object.xZero, object.formel)

class plot(differential):
    def __init__(self):
        print(str(object.a) + ("x^2") + " + " + str(object.b) + "x" + " + " + str(object.c))

    #def funktionsforskrift(x):
    #    x = Symbol('x')
    #    return ((object.a * x**2) + (object.b*x) + object.c)

    def f(x):
        return x ** 2

    x = np.linspace(-3, 3, 1000)
    plt.plot(x, f(x))
    plt.show()

plot()


"""
# laver graf fra x -3 til 3, og laver 1000 mellem x værdiger imellem de 2 punkter.
x = np.linspace(-3, 3, 1000)


# her sætter vi vores x værdi
def f(self, xZero):
    self.xZero = xZero
    return self.xZero ** 2


# plotter funktion ind
plt.plot(x, f(self, xZero))

# viser vores funktion
plt.show()

# https://www.youtube.com/watch?v=u5VCZBUNOcA
"""