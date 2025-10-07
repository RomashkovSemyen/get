import smbus
import numpy as np
import time

def get_sin_wave_amplitide(freq: float, tima_val: float) -> float:
    sin_value = np.sin(2 * np.pi * freq * tima_val)
    shifted_value = sin_value + 1
    normalized_value = shifted_value / 2
    return normalized_value
def wait_for_sampling_period(sampling_frequency: float, start_time: float = None) -> float:
    sampling_period = 1.0 / sampling_frequency

    if start_time is None:
        time.sleep(sampling_period)
        return time.time()
    else:
        elapsed_time = time.time() - start_time
        sleep_time = sampling_period - elapsed_time

        if sleep_time > 0:
            time.sleep(sleep_time)
        return time.time()

