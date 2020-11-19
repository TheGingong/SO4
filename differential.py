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

    #Her differentiere vi deltaX til at gå imod x0 indtil den er så tæt på nul som muligt
    #Og dermed får vi hældningskoefficienten.
    def Differential(self, xZero, xOne):
        self.xZero = xZero
        self.xOne = xOne

        loop = 0
        while loop < 50:
            loop += 1
            self.formel = (self.func(self.xZero + self.xOne) - self.func(self.xZero)) / ((self.xZero + self.xOne) - self.xZero)

            self.xOne = self.xOne / 2

            print(self.formel)

            if loop == 100:
                break

objectDiff = differential(10, 50, 100)
objectDiff.Differential(3, 10)