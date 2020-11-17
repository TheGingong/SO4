import math
from differential import *
from Integralregning import *
import matplotlib.pyplot as plt
import numpy as np

class plot():
    def __init__(self):
        pass

#laver graf fra x -3 til 3, og laver 1000 mellem tal imellem de 2 punkter.
x = np.linspace (-3,3, 1000)
#her sætter vi vores x værdi
def f(x):
    return x**2

#plotter funktion ind
plt.plot(x,f(x))

#viser vores funktion
plt.show()

#https://www.youtube.com/watch?v=u5VCZBUNOcA
