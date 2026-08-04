import noise
import attenuation
import delay

def transmit(signal, time, fadingfrequency, delayt, stdev):
    noises = noise.add_noise(signal, stdev)
    signal = noises[0]
    signal = attenuation.attenuate(signal, time, fadingfrequency)
    signal = delay.delay(signal, time, delayt)
    return signal, noises[1]
    