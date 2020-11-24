import math
from Equation import Expression
import numpy as np

class Diff():
    #Vi har fået hjælp af david til at lave differentialregningen i python
    def __init__(self, expr, lower, upper):
        self.fn = Expression(expr, "x")
        self.lowerBound = lower
        self.upperBound = upper

        # Disse nedenstående værdier bruger vi til at plotte med rigtig mellemrum, da disse værdier ikke bliver ændret.
        self.lowerBoundKOPI = lower
        self.upperBoundKOPI = upper

    def tangentPåLinjen(self, x):
        return self.slope * x + self.tangentB

    #Her differentiere vi deltaX til at gå imod x0 indtil den er så tæt på nul som muligt
    #Og dermed får vi hældningskoefficienten.

    def Differentialudregner(self):
        self.loop = 0
        while self.loop < 50:
            self.loop += 1
            self.slope = (self.fn(self.lowerBound + self.upperBound) - self.fn(self.lowerBound)) / (
                        (self.lowerBound + self.upperBound) - self.lowerBound)

            self.upperBound = self.upperBound / 2
            self.tangentB = self.fn(self.lowerBound) - self.slope * self.lowerBound
            print(self.slope)

    def slopeFunction(self):
        self.loop = 0
        self.reps = 100
        self.list_slopes = []
        self.x_values = np.linspace(self.lowerBoundKOPI, self.upperBoundKOPI, num=self.reps)
        for x in self.x_values:
            while True:
                self.loop += 1
                self.slopeGraph = (self.fn(self.lowerBound + self.upperBound) - self.fn(self.lowerBound)) / ((self.lowerBound + self.upperBound) - self.lowerBound)

                self.upperBound = self.upperBound / 2
                self.tangentB = self.fn(self.lowerBound) - self.slopeGraph * self.lowerBound
                print(self.slopeGraph)

                if self.loop == 40:
                    self.lowerBound += self.reps / self.lowerBound
                    self.upperBound = self.upperBoundKOPI
                    self.list_slopes.append(self.slopeGraph)
                    print(self.list_slopes)
                    break