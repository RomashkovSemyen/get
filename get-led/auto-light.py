import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

led = 26
GPIO.setup(led, GPIO.OUT)

phototransistor = 6
GPIO.setup(phototransistor, GPIO.IN)

while True:
    state = GPIO.input(phototransistor)
    if state == 0:
        GPIO.output(led, 1)
    else:
        GPIO.output(led, 0)
    time.sleep(0.1)