# import firebase_admin
from firebase_admin import firestore
import RPi.GPIO as GPIO
import time
import fs_init

input_list = [14]
output_list = []

def gpio_setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(input_list, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(output_list, GPIO.OUT)


gpio_setup()
db = fs_init.firestore_init()

try:
    while True:
        if GPIO.input(14) == GPIO.HIGH:
            print("14")
            db.collection('messages').add({
                'name': u'RPI',
                'text': u'14',
                'timestamp': firestore.SERVER_TIMESTAMP
            })
        time.sleep(0.2)

except KeyboardInterrupt:
    pass
    GPIO.cleanup()
