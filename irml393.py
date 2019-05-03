import setup_gpio
import RPi.GPIO as GPIO

list = [
    {"pin":12, "io": GPIO.INPUT}
]

setup_gpio.setup(list)
while True:
    if GPIO.input(12) == GPIO.HIGH:
        print("detected!!")

        