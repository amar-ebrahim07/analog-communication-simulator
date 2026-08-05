import signals
import plotter
import ammodulation
import amdemodulation
import channel
import matplotlib.pyplot as plt
import numpy as np
import analysis
import simulator

def main():
    
    while True:
        try:
            choice = int(input("===== Analog Communication Simulator =====\n\n" \
                            "Select the message signal:\n" \
                            "1. Sine Wave\n" \
                            "2. Square Wave\n" \
                            "3. Triangle Wave\n" \
                            "4. Sawtooth Wave\n" \
                            "5. PWM Wave\n" \
                            "6. DC Wave\n"  \
                            "7. Exit\n\n" \
                            "Choice: " ))
            
            if choice < 1 or choice> 7:
                print("Please enter a choice between 1 and 7.")
                continue

            if choice == 7:
                break

            duration = float(input("Please enter the duration: "))
            rate = int(input("Please enter the sampling rate: "))
            time = signals.generate_time(duration, rate)

            amplitude = int(input("Please enter the amplitude: "))

            if choice == 6:
                signal = signals.generate_dc(time, amplitude)
            else:
                frequency = int(input("Please enter the frequency: "))
                phase = int(input("Please enter the phase: "))
                while True:
                    if choice == 5:
                        duty = float(input("Please enter the duty cycle (Between 0 and 1): "))
                        if duty > 1 or duty < 0:
                            print("Invalid duty cycle, try again.")
                            continue
                    break

        except ValueError:
            print("Invalid input, try again.")
            continue



        if choice == 1:
            signal = signals.generate_sine(time, amplitude, frequency, phase)

        elif choice == 2:
            signal = signals.generate_square(time, amplitude, frequency, phase)

        elif choice == 3:
            signal = signals.generate_triangle(time, amplitude, frequency, phase)

        elif choice == 4:
            signal = signals.generate_sawtooth(time, amplitude, frequency, phase)

        elif choice == 5:
            signal = signals.generate_pwm(time, amplitude, frequency, phase, duty)


        while True:
                try:
                    choice = int(input("Select the modulation type:\n" \
                                    "1. AM \n" \
                                    "2. FM \n" \
                                    "3. Back\n" ))
                    
                    if choice < 1 or choice> 3:
                        print("Please enter a choice between 1 and 3.")
                        continue
        
                    if choice == 3:
                        break

                    if choice == 1:
                        simulator.runAM(signal, time, rate)

                    elif choice == 2:
                        simulator.runFM(signal, time, rate, frequency)

                except ValueError:
                    print("Invalid input, try again.")
                    continue






if __name__ == "__main__":
    main()