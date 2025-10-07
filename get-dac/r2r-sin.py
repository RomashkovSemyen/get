import r2r_dac as r2r
import signal_generator as sg
import time

amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000

if __name__ == "__main__":
    
    try:
        dac = r2r.r2r_dac([16, 20, 21, 25, 26, 17, 27, 22], 3.11, True)
        while True:
            dac.set_voltage(amplitude * sg.get_sin_wave_amplitide(signal_frequency, time.time()))
            sg.wait_for_sampling_period(sampling_frequency)
    except KeyboardInterrupt:
        print("\nГенерация прервана пользователем")
    finally:
        dac.deinit()
