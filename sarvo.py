#!/usr/bin/python
# coding: utf-8

import RPi.GPIO as GPIO
import time
import signal
import sys


def rotate_servo(servo, angle):
    #   0度の位置 0.5 ms / 20 ms * 100 = 2.5 %
    # 180度の位置 2.4 ms / 20 ms * 100 = 12 %
    #      変動幅 12% - 2.5% (9.5%)
    # angle * 9.5 / 180
    if -90 <= angle <= 90:
        d = ((angle + 90) * 9.5 / 180) + 2.5
        servo.ChangeDutyCycle(d)
    else:
        raise ValueError("angle")


def init_servo(gpios):
    """
    初期化します。gpiosは利用するGPIOをLISTで指定してください。
    :param gpios: GPIO番号(LIST)
    :return: GPIO.PWM (List)
    """
    pwms = []
    GPIO.setmode(GPIO.BCM)
    if isinstance(gpios, list):
        for gpio in gpios:
            GPIO.setup(gpio, GPIO.OUT)

            s = GPIO.PWM(gpio, 50)
            s.start(0.0)
            pwms.append(s)
    else:
        raise Exception("gpios isn't list object.")

    return pwms


if __name__ == "__main__":
    # GPIO 12番を使用
    GPIO_12 = 12

    # 初期化
    pwms = init_servo([GPIO_12])

    try:
        # -90°の位置まで動かし3秒停止します。
        rotate_servo(pwms[0], -90)
        time.sleep(3)

        # 0°の位置まで動かし3秒停止します。
        rotate_servo(pwms[0], 0)
        time.sleep(3)

        # 90°の位置まで動かし3秒停止します。
        rotate_servo(pwms[0], 90)
        time.sleep(3)

        for mm in range(4):
            # -90°の位置まで動かします。
            rotate_servo(pwms[0], -90)
            time.sleep(2)
            for i in range(-90, 91):
                # -90～90°まで20ミリ秒毎に動かします。
                rotate_servo(pwms[0], i)
                time.sleep(0.02)

    except KeyboardInterrupt as ki:
        # サーボの動作を停止します。
        pwms[0].stop()
        GPIO.cleanup()
