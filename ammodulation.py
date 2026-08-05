import numpy as np

def am_mod(message, carrier_amplitude, modulation_index, carrier_frequency, time):
    amsignal = carrier_amplitude * (1 + modulation_index*message)* np.cos(2 * np.pi * carrier_frequency * time)
    return amsignal