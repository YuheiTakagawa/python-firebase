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
    
    def read(self):
        rungps()
        return (self.gps.latitude[0], self.gps.longitude[0])


gps = GPS()
while True:
    result = gps.read()
    print(str(result)
    time.sleep(1)
