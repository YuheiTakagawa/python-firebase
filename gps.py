import serial
from micropyGPS import MicropyGPS
import time

class GPS:
    def __init__(self):
        self.gps = MicropyGPS(9, "dd")
        self.s = serial.Serial('/dev/serial0', 9600, timeout=10)

    def rungps(self):
        for x in self.s.readline().decode('utf-8'):
            self.gps.update(x)


gps = GPS()
while True:
    gps.rungps()
    print(str(gps.gps.latitude[0])+","+str(gps.gps.longitude[0]))
    time.sleep(1)
