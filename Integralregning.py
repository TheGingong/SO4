import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


#Vi har snakket med Casper, Frederik og David omkring hvordan de gjorde deres matematiske regneregler, og
#brugte den viden til at komme videre da vi sad fast.

#Vi har valgt at følge lidt den samme stil som vi skrev i differentialregning da vi følte at det gav mere mening i forhold til
#formlerne som vi fik vidst i matematik.

class integralregning():
    #I init funktionen modtager vi en a-, b-, c værdi samt en værdi for hvor mange søjler der skal være
    #for at regne det mest præcise areal ud.
    def __init__(self, a, b, c, columns):
        self.a = a
        self.b = b
        self.c = c
        self.columns = columns

    #I denne funktion bliver vores funktionsforskrift skrevet udfra hvad a, b, c,
    def func(self, x):
        # Her laver vi selve funktionsforskriften vha. a, b og c som også ses i "differential.py".
        return ((self.a * x ** 2) + (self.b * x) + self.c)

    #Denne funktion benytter vi det princip omkring integralregning og hvordan vi definere hvordan
    #arealet skal udregnes.
    def integral(self, xZero, xOne):
        self.xZero = xZero
        self.xOne = xOne

        self.deltaX = (self.xOne - self.xZero) / self.columns

        self.sum = 0
        n = 0
        while True:
            n += 1
            self.xZero += self.deltaX
            self.yZero = self.func(self.xZero)

            self.areal = self.deltaX * self.yZero

            self.sum += self.areal

            if n == self.columns:
                print(self.sum)
                break

object = integralregning(5, 6, 10, 10000)
object.integral(3, 10)