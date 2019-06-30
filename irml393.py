import RPi.GPIO as GPIO
from time import sleep

class ML393:
    __pin = 0
    def __init__(self, pin):
        GPIO.setmode(GPIO.BCM)
        self.__pin = pin

    def read(self):
        GPIO.setup(self.__pin, GPIO.IN)
        return GPIO.input(self.__pin)


ml = ML393(pin=12)
while True:
    if ml.read() == GPIO.LOW:
        print("detected!!")
    sleep(0.2)

        
