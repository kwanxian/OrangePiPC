#!/usr/bin/python3
# encoding: utf-8

import OPi.GPIO as GPIO
from time import sleep


def gpio_init():
    GPIO.setboard(GPIO.PCPLUS)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12, GPIO.OUT, pull_up_down=GPIO.PUD_UP)


if __name__ == '__main__':
    try:
        gpio_init()
        while True:
            GPIO.output(12, 1)
            sleep(1)
            GPIO.output(12, 0)
    except Exception as err:
        print(err)
    finally:
        GPIO.clear()
