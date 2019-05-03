import serial
from micropyGPS import MicropyGPS
import time

class GPS:
    def __init__():
        self.gps = MicropyGPS(9, "dd")
        self.s = serial.Serial('/dev/serial0', 9600, timeout=10)

    def rungps():
        for x in self.s.readline().decode('utf-8'):
            self.gps.update(x)


gps = GPS()
while True:
    gps.rungps()
    gps.gps.latitude
    gps.gps.longitude
    time.sleep(1)
