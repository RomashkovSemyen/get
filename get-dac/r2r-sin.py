import r2r_dac as r2r
import signal_generator as sg
import time

amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000

if __name__ == "__main__":
    dac = r2r.r2r_dac([16, 20, 21, 25, 26, 17, 27, 22], 3.11, True)
    try:
        start_time = time.time()
        sample_count = 0
        while True:
            current_time = sample_count / sampling_frequency
            normalized_amplitude = sg.get_sin_wave_amplitide(signal_frequency, current_time)
            voltage = amplitude * normalized_amplitude
            dac.set_voltage(voltage, [16, 20, 21, 25, 26, 17, 27, 22])
            sample_count += 1
            sg.wait_for_sampling_period(sampling_frequency)

            if sample_count % sampling_frequency == 0:
                elapsed_time = time.time() - start_time
                print(f"Прошло времени: {elapsed_time:.1f} сек, сгенерировано семплов: {sample_count}")
    except KeyboardInterrupt:
        print("\nГенерация прервана пользователем")
    finally:
        dac.deinit()
