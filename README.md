# Analog Communication Simulator

A Python-based simulator for fundamental analog communication systems. This project demonstrates the complete transmission chain of an Amplitude Modulation (AM) communication system, including signal generation, channel effects, demodulation, and performance analysis.

## Features

### Signal Generation

* Sine wave
* Square wave
* Triangle wave
* Sawtooth wave
* PWM wave
* DC signal

### Modulation

* Amplitude Modulation (AM)

### Channel Simulation

* Additive White Gaussian Noise (AWGN)
* Signal delay
* Framework for future channel effects such as attenuation and multipath fading

### Demodulation

* Envelope detection
* Low-pass filtering using Butterworth filters

### Analysis

* Mean Absolute Error (MAE) between transmitted and recovered message
* Signal power
* Signal-to-Noise Ratio (SNR)
* Channel gain/attenuation
* Frequency spectrum analysis using the Fast Fourier Transform (FFT)

## Technologies Used

* Python 3
* NumPy
* SciPy
* Matplotlib

## Project Structure

```text
```text
Analog Communication Simulator/
│
├── main.py                  # Entry point
├── simulator.py             # Simulation workflow
├── signals.py               # Message and carrier signal generation
├── modulation.py            # AM modulation
├── demodulation.py          # AM demodulation
├── channel.py               # Channel model
├── noise.py                 # Noise models
├── delay.py                 # Signal delay functions
├── attenuation.py           # Attenuation models
├── analysis.py              # Error, SNR, power, FFT, gain
├── plotter.py               # Visualization utilities
└── README.md
```

```

## Learning Objectives

This project was built to strengthen understanding of:

* Analog communication systems
* Amplitude Modulation (AM)
* Envelope detection
* Digital signal processing fundamentals
* Frequency-domain analysis using FFT
* Communication channel effects
* Scientific computing with Python

## Future Improvements

* Frequency Modulation (FM)
* Phase Modulation (PM)
* Multipath fading
* Automatic Gain Control (AGC)
* Audio signal transmission
* Interactive graphical user interface
* Performance comparison between modulation schemes

## Author

**Amar Ebrahim**

GitHub: https://github.com/amar-ebrahim07

