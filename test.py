# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
from time import sleep
import spidev

#GPIOのピン番号
pin = 22

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

#GPIOの指定したピン番号を出力端子に設定
GPIO.setup(pin, GPIO.OUT)

#出力用関数
def output_fromGPIO(pin, output):
        GPIO.output(pin, output)
        sleep(0.1)

#MCP3002動作用関数
def readadc_spidev(adcnum):
        if ((adcnum > 1) or (adcnum < 0)):
            return -1
        #0x68は1chを使う場合です。2chは0x78を使います。
        ret = spi.xfer2([0x68,0x00])    
        #データは8ビットずつに分かれているので、最初の8ビットを上位データとして8ビットシフトし、下位データと結合する
        #MCP3002は10ビット目までがデータなので、10ビット目までを残して他のデータを消す
        adcout = ((ret[0]<<8) + ret[1])&0x3ff
        return adcout

#SPI通信開始
spi=spidev.SpiDev()
spi.open(0, 0) # bus0, CE0

#データ取得前にYL-69に電圧を印可
output_fromGPIO(pin,True)

try:
    while True:
        #先ほど定義したMCP3002の関数を呼び出す
        getValue = readadc_spidev(0)
        #値がちゃんと取れたらデータを出力。取れるまでトライ
        if getValue != -1:
            print(getValue)
     #       break;
        sleep(1)

except KeyboardInterrupt:
    pass

#YL-69の印加電圧をとめる
output_fromGPIO(pin,False)
#SPI通信終了
spi.close()
