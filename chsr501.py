from datetime import datetime
import time
import RPi.GPIO as GPIO

INTERVAL = 3
SLEEPTIME = 5
GPIO_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PIN, GPIO.IN)

if __name__ == '__main__':
    try:
        cnt = 1
        while True:
            if(GPIO.input(GPIO_PIN) == GPIO.HIGH):
                print(datetime.now().strftime('%Y/%m/%d %H:%M:%S') +
                ":" + str("{0:05d}".format(cnt)))
                cnt = cnt + 1
                time.sleep(SLEEPTIME)
            else:
                print(GPIO.input(GPIO_PIN))
                time.sleep(INTERVAL)
    except KeyboardInterrupt:
        print("finishing")
    finally:
        GPIO.cleanup()
        print("finished")
