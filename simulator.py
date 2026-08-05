import ammodulation
import plotter
import channel
import amdemodulation
import analysis
import fmmodulation
import fmdemodulation

def runAM(message, time, fs):
    while True:
            plotter.plot_signal(time,message, "Message Signal")
            try:
                carrier_amplitude = int(input("Please enter the carrier amplitude: "))
                carrier_frequency = int(input("Please enter the carrier frequency: "))
                modulation_index = float(input("Please enter the modulation index: "))

            except ValueError:
                print("Invalid input, try again.")
                continue

            amsignal = ammodulation.am_mod(message, carrier_amplitude, modulation_index, carrier_frequency, time)
            plotter.plot_signal(time,amsignal, "Modulated Signal")
            break

    while True:
                try:
                    fading_frequency = int(input("Please enter the fading frequency: "))
                    delayt = float(input("Please enter the delay time: "))
                    stdev = float(input("Please enter the standard deviation of noise: "))
                    cutoff = int(input("Please enter the cutoff frequency: "))
    
                except ValueError:
                    print("Invalid input, try again.")
                    continue
    
                transmitted = channel.transmit(amsignal, time, fading_frequency, delayt, stdev)
                transmitteds = transmitted[0]
                noise = transmitted[1]
                plotter.plot_signal(time,amsignal, "Transmitted Signal")

                demodulated = amdemodulation.am_demod(transmitteds, fs, cutoff, carrier_amplitude, modulation_index)
                plotter.plot_signal(time, demodulated, "Demodulated Signal")
                break


    analyse(demodulated, amsignal, transmitteds, message, time, noise, fs)


def analyse(demodulated, amsignal, transmitteds, message, time, noise, fs):

    while True:
        try:
            choice = int(input("Analysis Options:\n\n" \
                            "1. Calculate error\n" \
                            "2. Message Power\n" \
                            "3. Transmitted Power\n" \
                            "4. Demodulated Power\n" \
                            "5. Calculate SNR\n" \
                            "6. Calculate gain \n"  \
                            "7. Display Spectrum\n" \
                            "8. Compare sent/recieved\n" \
                            "9. Back\n\n" \
                            "Choice:" ))
            
            if choice < 1 or choice> 9:
                print("Please enter a choice between 1 and 7.")
                continue

            if choice == 9:
                break

        except ValueError:
            print("Invalid input, try again.")
            continue


        if choice == 1:
             print("Error is", {analysis.calculate_error(message, demodulated)})

        elif choice == 2:
             print(analysis.signal_power(message))

        elif choice == 3:
             print(analysis.signal_power(transmitteds))

        elif choice == 4:
             print(analysis.signal_power(demodulated))

        elif choice == 5:
             print(analysis.snr(transmitteds, noise))

        elif choice == 6:
             print(analysis.gain(message, demodulated))

        elif choice == 7:
             fftset = analysis.spectrum(demodulated, fs)
             plotter.plot_signal(fftset[1], fftset[0], "Frequency Spectrum", "Frequencies (Hz), ")

        elif choice == 8:
             analysis.compare(time, message, demodulated)
      


def runFM(message, time, fs, message_freq):
    while True:
            plotter.plot_signal(time,message, "Message Signal")
            try:
                frequency_dev = int(input("Please enter the frequency deviation: "))
                carrier_frequency = int(input("Please enter the carrier frequency: "))
                # modulation_index = float(input("Please enter the modulation index: "))

            except ValueError:
                print("Invalid input, try again.")
                continue

            fmsignal = fmmodulation.fm_mod(message, time, carrier_frequency, frequency_dev)
            plotter.plot_signal(time,fmsignal, "Modulated Signal")
            break

    while True:
                try:
                    fading_frequency = int(input("Please enter the fading frequency: "))
                    delayt = float(input("Please enter the delay time: "))
                    stdev = float(input("Please enter the standard deviation of noise: "))
    
                except ValueError:
                    print("Invalid input, try again.")
                    continue
    
                transmitted = channel.transmit(fmsignal, time, fading_frequency, delayt, stdev)
                transmitteds = transmitted[0]
                noise = transmitted[1]
                plotter.plot_signal(time,fmsignal, "Transmitted Signal")

                demodulated = fmdemodulation.fm_demod(fmsignal, fs, frequency_dev, carrier_frequency, message_freq)
                plotter.plot_signal(time, demodulated, "Demodulated Signal")
                break


    analyse(demodulated, fmsignal, transmitteds, message, time, noise, fs)






            