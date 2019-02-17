#!/usr/bin/python3
# encoding: utf-8

import OPi.GPIO as GPIO
from time import sleep


def gpio_init():
    GPIO.setboard(GPIO.PCPCPLUS)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(16, GPIO.OUT)
    print("GPIO init success!")


if __name__ == '__main__':
    try:
        gpio_init()
        while True:
            GPIO.output(16, 1)
            sleep(1)
            GPIO.output(16, 0)
    except KeyboardInterrupt:
        exit(1)
    except Exception as err:
        print(err)
    finally:
        GPIO.cleanup()
