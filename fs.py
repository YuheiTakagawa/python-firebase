import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import RPi.GPIO as GPIO
import time
import dht11

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# read data using pin 7
instance = dht11.DHT11(pin=26)



cred = credentials.Certificate(os.environ['FIREBASE_AUTH_KEY'])
firebase_admin.initialize_app(cred)

db = firestore.client()

try:
	while True:
		if GPIO.input(14) == GPIO.HIGH:
			print("14")
			db.collection('messages').add({
				'name': u'RPI',
				'text': u'14',
				'timestamp': firestore.SERVER_TIMESTAMP
			})
			result = instance.read()
			if result.is_valid():
				msg = u"{0:0.1f}".format(result.temperature) 
        			print(u"kion:" + msg + u"C " + u"sitsudo" + str(result.humidity) + u"%")

		time.sleep(0.2)

except KeyboardInterrupt:
	pass

GPIO.cleanup()



