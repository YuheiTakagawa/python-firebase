import RPi.GPIO as GPIO

# def callback1():
#     print("Hello")

#pin, io(IN or OUT), event
# a = [
#     {"pin":14, "io":GPIO.IN, "func":callback1, "event":GPIO.FALLING},
#     {"pin":15, "io":GPIO.OUT, "pull_up":GPIO.PUD_DOWN}
# ]

def setup(ab):
    GPIO.setmode(GPIO.BCM)
    for item in ab:
        if "pull_up" in item:
            GPIO.setup(item["pin"], item["io"], item["pull_up"])
        else:
            GPIO.setup(item["pin"], item["io"])
        if "event" in item and "func" in item:
            GPIO.add_event_detect(item["pin"], item["event"], bouncetime=100)
            GPIO.add_event_callback(item["pin"], item["func"])


