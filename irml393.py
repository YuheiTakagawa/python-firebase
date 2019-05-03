import setup_gpio
import RPi.GPIO as GPIO
from time import sleep

list = [
    {"pin":12, "io": GPIO.IN}
]

setup_gpio.setup(list)
while True:
    if GPIO.input(12) == GPIO.LOW:
        print("detected!!")
    sleep(0.2)

        
