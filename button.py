import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import RPi.GPIO as GPIO
import time
import dht11

GPIO.cleanup()

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(13, GPIO.IN)
instance = dht11.DHT11(pin=26)

cred = credentials.Certificate(os.environ['FIREBASE_AUTH_KEY'])
firebase_admin.initialize_app(cred)

db = firestore.client()

p = GPIO.PWM(18, 1)

count = 0
try:
    while True:
        if GPIO.input(14) == GPIO.HIGH or GPIO.input(13) == GPIO.HIGH:
            p.start(50)
	    p.ChangeFrequency(260)
	    count += 1
            print(count)
	else:
	    if count != 0:
	        db.collection('messages').add({
                    'name': u'RPI',
                    'text': count,
                    'timestamp': firestore.SERVER_TIMESTAMP
                })
		count = 0
		result = instance.read()
		if result.is_valid():
			msg = u"{0:0.1f}".format(result.temperature) 
       			print(u"kion:" + msg + u"C " + u"sitsudo" + str(result.humidity) + u"%")
			db.collection('messages').add({
				'name': u'RPI tempe',
			'text': msg + u"C " + str(result.humidity) + u'%',
				'timestamp': firestore.SERVER_TIMESTAMP
			})

	    p.stop() 

        time.sleep(0.1)

except KeyboardInterrupt:
    pass

GPIO.cleanup()
