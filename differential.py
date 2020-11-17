import math

class differential():

    #Vi har fået hjælp af david til at lave differentialregningen i python

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def func(self, x):
        #Her laver vi selve funktionsforskriften fra a, b og c.
        return ((self.a * x**2) + (self.b*x) + self.c)

    def Differential(self, xZero, deltaX):
        self.xZero = xZero
        self.deltaX = deltaX

        loop = 0
        while loop < 50:
            loop += 1
            self.formel = (self.func(self.xZero + self.deltaX) - self.func(self.xZero)) / ((self.xZero + self.deltaX) - self.xZero)

            self.deltaX = self.deltaX / 2

            print(self.formel)

            if loop == 100:
                break

object = differential(5, 6, 10)
object.Differential(3, 10)