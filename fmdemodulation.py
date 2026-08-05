import numpy as np


def fm_demod(modulated, fs, frequency_dev, carrier_frequency, message_freq):
    crossing_indices = []

    for i in range(len(modulated)-1):
        if (modulated[i] >= 0 and modulated[i+1] <= 0) or (modulated[i] <= 0 and modulated[i+1] >= 0):
            crossing_indices.append(i)

    crossing_diff = np.diff(crossing_indices)
    period = (crossing_diff / fs) * 2
    periodArr = np.empty(len(modulated))
    periodArr[0:crossing_indices[0]] = period[0]
    periodArr[crossing_indices[-1]:] = period[-1]
    for i in range(len(crossing_diff)):
        periodArr[crossing_indices[i] : crossing_indices[i+1]] = period[i]
    
    frequency = 1 / periodArr
    carrier_dev = frequency - carrier_frequency
    demodulated = (carrier_dev / frequency_dev) * np.max(np.absolute(modulated))


    window = int(fs/(message_freq * 5))
    kernel = np.ones(window) / window
    filtered = np.convolve(demodulated, kernel, mode="same")
    return filtered
