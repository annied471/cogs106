import unittest
import scipy.stats


class SignalDetection: 
    def __init__ (self, hits, misses, falseAlarms, correctRejections):
        self.hits = hits
        self.misses = misses 
        self.falseAlarms = falseAlarms
        self.correctRejections = correctRejections 
    def hitrate(self):
        return self.hits/(self.hits + self.misses)
    def farate(self):
        return self.falseAlarms/(self.falseAlarms+self.correctRejections)
    def d_prime(self):
        return scipy.stats.norm.ppf(self.hitrate()) - scipy.stats.norm.ppf(self.farate())
    def criterion(self):
        return  -0.5 * (scipy.stats.norm.ppf(self.hitrate()) + scipy.stats.norm.ppf(self.farate()))

    # overload + and *
    def __add__(self, o):
        hits = self.hits + o.hits
        misses = self.misses + o.misses
        falseAlarms = self.falseAlarms + o.falseAlarms
        correctRejections = self.correctRejections + o.correctRejections
        return SignalDetection(hits, misses, falseAlarms, correctRejections)

    def __mul__(self, o):
        hits = self.hits * o
        misses = self.misses * o
        falseAlarms = self.falseAlarms * o
        correctRejections = self.correctRejections * o
        return SignalDetection(hits, misses, falseAlarms, correctRejections)
