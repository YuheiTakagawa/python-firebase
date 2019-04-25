import time
import spidev
import sys

spi = spidev.SpiDev()
spi.open(0,0)

def readAdc(channel):
	adc = spi.xfer2([0x01,0x80,0x00])
	data = ((adc[1]&3) << 8) | adc[2]
	print(str(adc[0])+","+str(adc[1])+ ","+str(adc[2]))
	return data

def convertVolts(data):
	volts = (data * 3.3) / float(1023)
	volts = round(volts,4)
	return volts

while True:
	data = readAdc(0)
	print("adc : {:8}".format(data))
	volts = convertVolts(data)
	print("volts: {:8.2f}".format(volts))

	time.sleep(0.5)
