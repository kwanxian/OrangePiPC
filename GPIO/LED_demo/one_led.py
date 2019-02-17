#!/usr/bin/python3
# encoding: utf-8

import OPi.GPIO as GPIO


def gpio_init():
    pass


if __name__ == '__main__':
    try:
        gpio_init()
    except Exception as err:
        print(err)
    finally:
        GPIO.clean()
