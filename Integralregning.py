import math
from Equation import Expression

# Vi har snakket med Casper, Frederik og David omkring hvordan de gjorde deres matematiske regneregler, og
# brugte den viden til at komme videre da vi sad fast.

# Vi har valgt at følge lidt den samme stil som vi skrev i differentialregning da vi følte at det gav mere mening i forhold til
# formlerne som vi fik vidst i matematik.

class integralregning():
    # I init funktionen modtager vi en a-, b-, c værdi samt en værdi for hvor mange søjler der skal være
    # for at regne det mest præcise areal ud.
    def __init__(self, expr, lower, upper, columns):
        self.fn = Expression(expr, "x")
        self.lowerBound = lower
        self.upperBound = upper
        self.columns = columns

        #Disse nedenstående værdier bruger vi til at plotte med rigtig mellemrum, da disse værdier ikke bliver ændret.
        self.lowerBoundKOPI = lower
        self.upperBoundKOPI = upper

    # I denne funktion bliver vores funktionsforskrift skrevet udfra hvad a, b, c,
    def func(self, x):
        # Her laver vi selve funktionsforskriften vha. a, b og c som også ses i "differential.py".
        return ((self.a * x ** 2) + (self.b * x) + self.c)

    # Denne funktion benytter vi det princip omkring integralregning og hvordan vi definere hvordan
    # arealet skal udregnes.

    def integral(self):
        #Disse to variabler bliver brugt til plot funktionen og til at sætte linjerne korrekt.
        #Det kan nemlige ikke være de andre to, da de bliver opdateret i et "while loop" herunder.

        self.deltaX = (self.upperBound - self.lowerBound) / self.columns

        self.sum = 0
        n = 0
        while True:
            n += 1
            self.lowerBound += self.deltaX
            self.yZero = self.fn(self.lowerBound)

            self.areal = self.deltaX * self.yZero

            self.sum += self.areal

            if n == self.columns:
                print(self.sum)
                break