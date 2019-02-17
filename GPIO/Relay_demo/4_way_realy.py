#!/usr/bin/python3
# encoding: utf-8

import OPi.GPIO as GPIO
from time import sleep


def gpio_init():
    GPIO.setboard(GPIO.PCPCPLUS)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(16, GPIO.OUT)
    GPIO.setup(18, GPIO.OUT)
    GPIO.setup(26, GPIO.OUT)
    GPIO.setup(27, GPIO.OUT)
    # 手上的继电器支持高低电平触发，这里以高电平触发演示，默认初始化时为低电平
    GPIO.output(16, 0)
    GPIO.output(18, 0)
    GPIO.output(26, 0)
    GPIO.output(27, 0)
    print("GPIO init success!")


def relay_ctrl(num):
    if num == 1:
        GPIO.output(16, 1)
        sleep(1)
        GPIO.output(16, 0)
    elif num == 2:
        GPIO.output(18, 1)
        sleep(1)
        GPIO.output(18, 0)
    elif num == 3:
        GPIO.output(26, 1)
        sleep(1)
        GPIO.output(26, 0)
    elif num == 4:
        GPIO.output(27, 1)
        sleep(1)
        GPIO.output(27, 0)


if __name__ == '__main__':
    try:
        gpio_init()
        print("Press Ctrl + C to stop")
        while True:
            num = int(input("Enter Relay Num:"))
            if num in (1,2,3,4):
                relay_ctrl(num)
            else:
                print("Input Error")
            sleep(1)

    except Exception as err:
        print(err)
    finally:
        GPIO.cleanup()
