class Bayes:
    def __init__(self, priorA, probBdadoA):
        self.priorA = priorA
        self.probBdadoA = probBdadoA
        self.probNoA = 1 - priorA
        self.probBnoA = 1 - probBdadoA
        self.probB = (probBdadoA * priorA) + (self.probBnoA * self.probNoA)

    def probabilityB(self):
        return self.probB

    def givenAandB(self):
        return round(((self.priorA * self.probBdadoA) / self.probB) * 100, 2)