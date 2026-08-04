import numpy as np
import plotter

def calculate_error(message, demodulated):
    error = np.mean(np.abs(message[1000:-1000] - demodulated[1000:-1000]))
    return f"{error*100}%"

def signal_power(signal):
    power = np.mean(signal**2)
    return power

def snr(signal, noise):
    snr = 10 * np.log10(signal_power(signal) / signal_power(noise))
    return snr

def gain(message, demodulated):
    gain = 10* np.log10(signal_power(demodulated) / signal_power(message))
    return gain

def spectrum(demodulated, fs):
    fftmag = np.absolute(np.fft.fft(demodulated))
    frequencies = np.fft.fftfreq(len(demodulated), 1/fs)
    return fftmag,frequencies

def compare(time, signal1, signal2):
    plotter.plot_2signals(time, signal1, signal2)