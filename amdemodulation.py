import numpy as np
import scipy.signal as sig

def am_demod(signal, samplingrate, cutoff, carrieramplitude, modulation_index):
    rectified = np.absolute(signal)
    b, a = sig.butter(4, cutoff, btype='low', fs = samplingrate)

    demodulated = sig.filtfilt(b, a, rectified, padtype='even', padlen=3*max(len(a), len(b)))
    
    
    settle_idx = int(0.2 * len(demodulated))
    dc_offset = np.mean(demodulated[settle_idx:])
    demodulated = demodulated - dc_offset
    demodulated = demodulated / modulation_index
    return demodulated