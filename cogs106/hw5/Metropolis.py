import numpy as np
import scipy.stats as stats

class Metropolis:
    def __init__(self, logTarget, initialState):
        self.logTarget = logTarget
        self.initialState = initialState
        self.samples = []
        self.scale = 1

    def __accept(self, proposal):
        ratio = self.logTarget(proposal) - self.logTarget(self.initialState)
        acceptanceProbability = min(1, np.exp(ratio))
        return acceptanceProbability > np.random.uniform() 
    
    def adapt(self, blockLengths):
        for length in blockLengths:
            acceptances = 0
            for i in range(length):
                proposal = self.initialState + np.random.normal()
                if self.__accept(proposal):
                    acceptances += 1
                    self.initialState = proposal
            acceptanceRate = acceptances / length
            # adjustments based on the multiplicative factor
            if acceptanceRate > 0.4:
                self.scale *= (acceptanceRate / 0.4) ** 0.1
            else:
                self.scale /= (0.4 / acceptanceRate) ** 0.1
        return self

    def sample(self, nSamples):
        for i in range(nSamples):
            proposal = self.initialState + np.random.normal()
            if self.__accept(proposal):
                self.initialState = proposal
            self.samples.append(self.initialState)
        return self

    def summary(self):
        mean = np.mean(self.samples, axis = 0)
        credint = stats.mstats.mquantiles(self.samples, [0.025, 0.975], axis = 0)
        return {"mean": mean, "c025": credint[0], "c975": credint[1]}
