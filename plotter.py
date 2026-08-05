import matplotlib.pyplot as plt
import numpy as np

def plot_2signals(time, signal1, signal2):
    plt.plot(time, signal1)
    plt.plot(time, signal2)
    plt.xlim(0, 0.02)
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.title("Signal Comparison")
    plt.grid()
    plt.show()


def plot_signal(time, signal, title, x = "Time (s)", y = "Amplitude"):
    plt.plot(time, signal)
    plt.xlim(0, 0.02)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.title(title)
    plt.grid()
    plt.show()


def plot_fft(freq, fft, title, carrierf, x = "Time (s)", y = "Amplitude"):
    #plt.plot(time[1000:1100], signal[1000:1100])
    zoom = 0.25 * carrierf
    positive = freq >=0
    plt.plot(freq[positive], np.abs(fft)[positive])
    plt.xlim(carrierf - zoom, carrierf + zoom)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.title(title)
    plt.grid()
    plt.show()
