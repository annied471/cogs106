import unittest
import scipy.stats
import numpy as np
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
    
    # plot ROC curve
    def plot_roc(self):
        plt.plot([0, self.farate(), 1], [0, self.hitrate(), 1], color ='red', marker ='o', markersize = 5, label ='ROC')
        plt.plot([0, 1], [0, 1], color='darkblue', linestyle='--', label ="Baseline/Random")
        plt.xlabel('False Alarm Rate')
        plt.ylabel('Hit Rate')
        plt.title('Receiver Operating Characteristic (ROC) Curve')
        plt.legend()
        plt.show()

    # plot SDT plot
    def plot_sdt(self):
        x = np.linspace(-4, 4, 100)
        # variance = std ^ 2
        noise = scipy.stats.norm.pdf(x, loc = 0, scale = np.square(1))
        signal = scipy.stats.norm.pdf(x, loc = self.d_prime(), scale = np.square(1))

        c = (self.d_prime() / 2) + self.criterion()
        n_y = np.max(noise) # y max for noise
        n_x = x[np.where(noise == n_y)][0] # x value for noise
        s_y = np.max(signal) # y max for signal
        s_x = x[np.where(signal == s_y)][0] # x value for signal

        fig, ax = plt.subplots()
        ax.plot(x, noise, label='Noise')
        ax.plot(x, signal, label='Signal')
        ax.axvline(x=c, linestyle='--', color='gray', label = "Criterion")
        ax.plot([n_x, s_x],[n_y, s_y], linestyle=':', color='green', label = "d'")

        ax.set_xlabel('Decision Variable')
        ax.set_ylabel('Probability')
        ax.set_title('Signal Detection Theory (SDT) Plot')
        ax.legend()
        plt.show()

sd = SignalDetection(2, 2, 3, 1)
sd.plot_roc()
sd.plot_sdt()
