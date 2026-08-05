import numpy as np
import signals
import matplotlib.pyplot as plt
import plotter

def fm_mod(message, time, carrier_frequency, frequency_dev):
    carrier_dev = (message / np.max(np.absolute(message))) * np.full(len(time), frequency_dev)
    carrier = carrier_frequency + carrier_dev
    phaseinc = carrier * 2 * np.pi * (time[1]-time[0])
    phaseArr = np.cumsum(phaseinc)
    modulated = np.max(np.absolute(message)) * np.sin(phaseArr)
    return modulated
