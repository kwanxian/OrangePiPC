#!/usr/bin/python3
# encoding: utf-8

import OPi.GPIO as GPIO
from time import sleep


def gpio_init():
    GPIO.setboard(GPIO.PCPCPLUS)
    GPIO.setmode(GPIO.BOARD)
    # 这个接口接到LED的正极，LED的负极接到GND即可
    GPIO.setup(16, GPIO.OUT)
    GPIO.setup(18, GPIO.IN)
    print("GPIO init success!")


def button_event(channel):
    if GPIO.input(18) == GPIO.HIGH:
        GPIO.output(16, 1)
    else:
        GPIO.output(16, 0)


if __name__ == '__main__':
    try:
        gpio_init()
        print("Press Ctrl + C to stop")
        # 事件触发方式等待
        GPIO.add_event_detect(18, GPIO.RISING, callback=button_event, bouncetime=200)
        while True:
            print("waiting")
            sleep(1)
    except KeyboardInterrupt:
        print("stop")
    except Exception as err:
        print(err)
    finally:
        GPIO.cleanup()
        print("GPIO clean up")