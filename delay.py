import numpy as np

def delay(signal, time, delay):
    if delay != 0:
        delaysample = int(np.round(delay / (time[1] - time[0])))
        signal = np.append(np.full(delaysample, 0), signal[:-delaysample])
    return signal