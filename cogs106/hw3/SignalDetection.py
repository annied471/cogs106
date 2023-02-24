import unittest
import scipy.stats
import matplotlib.pyplot as plt 

class SignalDetection: 
    def __init__ (self, hits = 0, misses = 0, falseAlarms = 0, correctRejections = 0):
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

    # generates a plot of the Receiver Operating Characteristic (ROC)
    # for one hit rate and false alarm rate

    def plot_roc(self):
        # Plot the ROC curve using matplotlib
        plt.plot([0, self.farate(), 1], [0, self.hitrate(), 1], color ='red', marker ='o', markersize = 10, label ='ROC')
        plt.plot([0, 1], [0, 1], color='darkblue', linestyle='--', label ="Chance Line")
        plt.xlabel('False Alarm Rate')
        plt.ylabel('Hit Rate')
        plt.title('Receiver Operating Characteristic (ROC) Curve')
        plt.legend()
        plt.show()

sd = SignalDetection(2, 2, 3, 1)
sd.plot_roc()
