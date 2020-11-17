import math
from differential import *
from Integralregning import *
import matplotlib.pyplot as plt
import numpy as np

#print(object.a, object.b, object.c, object.xZero, object.formel)

class plot(differential):
    def __init__(self):
        print(object.b)
        plt.plot([5,object.b])
        plt.show()

plot()




"""
# laver graf fra x -3 til 3, og laver 1000 mellem tal imellem de 2 punkter.
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
