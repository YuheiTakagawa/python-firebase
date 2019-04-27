import RPi.GPIO as GPIO

def callback():
    print("Hello")

#pin, io(IN or OUT), event
a = [
    {"pin":14, "io":GPIO.IN, "func":callback, "event":GPIO.FALLING},
    {"pin":15, "io":GPIO.OUT, "pull_up":GPIO.PUD_DOWN}
]

def setup():
    GPIO.setmode(GPIO.BCM)
    for item range a:
        GPIO.setup(item["pin"], item["io"], item["pull_up"])
        if item in "event" && item in "func"
            GPIO.add_event_detect(item["pin"], item["event"], bouncetime=100)
            GPIO.add_event_callback(item["pin"], item["func"])



# print(a[0]["pin"])
# print(a[0]["io"])
# a[0]["func"]()
