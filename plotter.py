import matplotlib.pyplot as plt

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
    #plt.plot(time[1000:1100], signal[1000:1100])
    plt.plot(time, signal)
    plt.xlim(0, 0.02)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.title(title)
    plt.grid()
    plt.show()
