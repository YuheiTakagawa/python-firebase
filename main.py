import RPi.GPIO as GPIO
import time
import fs
import setup_gpio

def switch_callback(gpio_pin):
    print("14")
    db.collection('messages').add({
        'name': u'RPI',
        'text': u'14',
        'timestamp': firestore.SERVER_TIMESTAMP
    })


#pin, io, func, event
a = [
    {"pin":14, "io":GPIO.IN, "func":switch_callback, "event": GPIO.FALLING},
]

setup_gpio.setup(a)

db = fs.firestore_init()

try:
    while True:
        time.sleep(0.1)

except KeyboardInterrupt:
    pass
    GPIO.cleanup()
