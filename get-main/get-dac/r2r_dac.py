import RPi.GPIO as gpio
import time


def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

class R2R_DAC:
    def __init__(self, bits, dynamic_range, verbose = False):
        self.bits = bits
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        gpio.setmode(gpio.BCM)
        gpio.setup(self.bits, gpio.OUT, initial = 0)
    def deinit(self):
        gpio.output(self.bits, 0)
        gpio.cleanup()
    def setnumber(self, number):
        for i in range(8):
            gpio.output(self.bits[i], dec2bin(number)[i])
    def setvoltage(self, voltage):
        if not (0.0 <= voltage <= self.dynamic_range):
            print(f"voltage exceeds the DAC dynamic range (0.0 - {dynamic_range:.2}V)")
            print("voltage set to 0V")
            return 0
        self.setnumber( int(round(voltage / self.dynamic_range * 255)))

if __name__ == "__main__":
    try:
        dac = R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.183, True)

        while True:
            try:
                voltage = float(input("input voltage in Volts: "))
                dac.setvoltage(voltage)

            except ValueError:
                print("no correct input, try again\n")
    finally:
        dac.deinit()
#Vref - 3.186
#max voltage - 3.162