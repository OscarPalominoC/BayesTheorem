class Bayes:
    def __init__(self, priorA, probBdadoA,probBnoA):
        self.priorA = priorA
        self.probBdadoA = probBdadoA
        self.probNoA = 1 - priorA
        self.probBnoA = probBnoA
        self.probB = (probBdadoA * priorA) + (self.probBnoA * self.probNoA)

    def probabilityB(self):
        return self.probB

    def givenAandB(self):
        return round(((self.priorA * self.probBdadoA) / self.probB) * 100, 2)