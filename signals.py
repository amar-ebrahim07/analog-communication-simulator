import numpy as np

def generate_time(duration, rate):
    samples = int(duration * rate)
    return np.linspace(0, duration, samples, False)

def generate_sine(time, amplitude, frequency, phase):
    sineArr = amplitude*np.sin(np.pi * 2 * frequency * time + phase)
    return sineArr

def generate_square(time, amplitude, frequency, phase):
    comp = generate_sine(time, amplitude, frequency, phase) > 0
    squareArr = np.where(comp, amplitude, -1 * amplitude)
    return squareArr

def generate_triangle(time, amplitude, frequency, phase):
    period = 1/frequency
    phase_time = (phase / (2 * np.pi)) * period
    position = (time +phase_time) % period
    triangleArray = np.where(position < period/2, 4 * amplitude * frequency * position - amplitude, -4 * amplitude * frequency * (position-period/2) + amplitude)
    return triangleArray

def generate_sawtooth(time, amplitude, frequency, phase):
    period = 1/frequency
    phase_time = (phase / (2 * np.pi)) * period
    position = (time +phase_time) % period
    sawtoothArr = 2 * amplitude * frequency * position - amplitude
    return sawtoothArr

def generate_pwm(time, amplitude, frequency, phase, duty):
    period = 1/frequency
    phase_time = (phase / (2 * np.pi)) * period
    position = (time +phase_time) % period
    pwmArr = np.where(position<duty*period, amplitude, -amplitude)
    return pwmArr

def generate_dc(time, amplitude):
    dcArr = np.full(len(time), amplitude)
    return dcArr


