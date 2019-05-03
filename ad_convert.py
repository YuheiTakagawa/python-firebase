import time
import spidev
import sys

class SPI:
    def __init__(self, no, num):
        this.spi = spidev.SpiDev()
        this.spi.open(no, num)

    def convertVolts(self):
        v = (this.data * 3.3) / float(1023)
        self.volts = round(v, 4)
        return self.volts

    def readAdc(self, channel):
        adc = this.spi.xfer2([0x01,0x80,0x00])
        self.data = ((adc[1]&3) << 8) | adc[2]
        print(str(adc[0] + "," + str(adc[1]) + "," + str(adc[2]))
        return self.data

while True:
    spi = SPI()
    data = spi.readAdc(0)
    print("adc: {:8}".format(data))
    volts = spi.convertVolts()
    print("volts: {:8.2f}".format(volts))

    time.sleep(0.5)
