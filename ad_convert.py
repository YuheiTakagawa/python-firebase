import time
import spidev
import sys

class SPI:
    def __init__(self, no, num):
        self.spi = spidev.SpiDev()
        self.spi.open(no, num)

    def convertVolts(self):
        v = (self.data * 3.3) / float(1023)
        self.volts = round(v, 4)
        return self.volts

    def readAdc(self, channel):
        spi = spidev.SpiDev()
        spi.open(0,0)
#        adc = self.spi.xfer2([0x01,(8+channel)<<4,0x00])
        adc = spi.xfer2([0x68,0x00])    
#        self.data = ((adc[0]&3) << 8) | adc[1]))
        self.data = ((adc[0]<<8) + adc[1])&0x3ff
        print(str(adc[0]) + "," + str(adc[1]))
        return self.data

while True:
    spi = SPI(0, 0)
    data = spi.readAdc(0)
    print("adc: {:8}".format(data))
    volts = spi.convertVolts()
    print("volts: {:8.2f}".format(volts))

    time.sleep(0.5)
