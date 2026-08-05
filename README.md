# Analog Communication System Simulator

A Python-based simulator for exploring the fundamentals of analog communication systems.

This project was built to better understand how communication systems work by implementing the core concepts from scratch rather than relying on existing communications libraries. It includes signal generation, analog modulation and demodulation, channel effects, and signal analysis tools.

---

## Features

### Signal Generation

* Sine wave
* Square wave
* Triangle wave
* Sawtooth wave
* PWM signal
* DC signal

### Modulation

* Amplitude Modulation (AM)
* Frequency Modulation (FM)

### Demodulation

* AM Demodulation
* Custom FM Demodulation using zero-crossing frequency estimation

### Channel Simulation

* Additive noise
* Signal attenuation
* Signal delay

### Analysis

* Fast Fourier Transform (FFT)
* Signal-to-Noise Ratio (SNR)
* Time-domain signal visualization

---

## How It Works

The simulator follows the same processing chain used in a basic analog communication system:

```text
Message Generator
        │
        ▼
AM / FM Modulator
        │
        ▼
Communication Channel
 • Noise
 • Delay
 • Attenuation
        │
        ▼
AM / FM Demodulator
        │
        ▼
Signal Analysis
 • FFT
 • SNR
```

---

## FM Implementation

The FM modulator generates an instantaneous carrier frequency based on the message signal. Instead of assuming a constant carrier frequency, the simulator computes a frequency for every sample, converts these frequencies into phase increments, accumulates the phase, and generates the transmitted waveform.

The FM demodulator estimates the instantaneous frequency using zero-crossing detection, reconstructs the carrier frequency over time, removes the carrier component, and applies smoothing to recover the original message.

---

## Technologies Used

* Python
* NumPy
* Matplotlib

---

## Example Output

The simulator can visualize:

* Original message signal
* Modulated signal
* Demodulated signal
* FFT spectrum
* Channel effects

---

## Future Improvements

Some features planned for future versions include:

* Digital modulation schemes
* Additional channel models
* Better FM demodulation techniques
* Configurable filters
* GUI for interactive simulations
* Audio transmission support

---

## Purpose

This project was developed as a learning exercise alongside a Communications Engineering degree. The primary objective was to gain a practical understanding of analog communication systems by implementing the underlying algorithms rather than treating them as black boxes.

---

## Author

**Amar Ebrahim**

Communications Engineering Student
German University in Cairo (GUC)

https://github.com/amar-ebrahim07/analog-communication-simulator
