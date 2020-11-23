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

    def tangentPåLinjen(self, x):
        return objectDiff.formel * x + objectDiff.tangentB

    #Her differentiere vi deltaX til at gå imod x0 indtil den er så tæt på nul som muligt
    #Og dermed får vi hældningskoefficienten.
    def Differential(self, xZero, xOne):
        self.xZero = xZero
        self.xOne = xOne

        # Disse to variabler bliver brugt til plot funktionen og til at sætte linjerne korrekt.
        # Det kan nemlige ikke være de andre to, da de bliver opdateret i et "while loop" herunder.
        self.plotxOneDIFF = xOne


        loop = 0
        while loop < 50:
            loop += 1
            self.formel = (self.func(self.xZero + self.xOne) - self.func(self.xZero)) / ((self.xZero + self.xOne) - self.xZero)

            self.xOne = self.xOne / 2
            self.tangentB = self.func(objectDiff.xZero) - objectDiff.formel * objectDiff.xZero
            print(self.formel)
            if loop == 100:
                break

objectDiff = differential(5, 6, 10)
objectDiff.Differential(3, 10)
