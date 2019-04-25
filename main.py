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

def switch_callback(gpio_pin):
    print("14")
    db.collection('messages').add({
        'name': u'RPI',
        'text': u'14',
        'timestamp': firestore.SERVER_TIMESTAMP
    })


#pin, inout, event
a = [
    {"pin":14, "io":GPIO.IN, "func":switch_callback},
]

GPIO.add_event_detect(14, GPIO.FALLING, bouncetime=100)
GPIO.add_event_callback(a[0]["pin"], a[0]["func"]) 

gpio_setup()
db = fs_init.firestore_init()

try:
    while True:
        time.sleep(0.1)

except KeyboardInterrupt:
    pass
    GPIO.cleanup()
