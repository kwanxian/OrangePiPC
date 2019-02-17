#!/usr/bin/python3
# encoding: utf-8

import OPi.GPIO as GPIO
from time import sleep
from threading import Thread


def gpio_init():
    GPIO.setboard(GPIO.PCPCPLUS)
    GPIO.setmode(GPIO.BOARD)
    # 这个接口接到LED的正极，LED的负极接到GND即可
    GPIO.setup(16, GPIO.OUT)
    GPIO.setup(18, GPIO.IN)
    print("GPIO init success!")


def button_event(channel):
    if GPIO.input(channel) == GPIO.HIGH:
        GPIO.output(16, 1)
    else:
        GPIO.output(16, 0)


def long_time_thread():
    while True:
        sleep(1)


if __name__ == '__main__':
    try:
        gpio_init()
        print("Press Ctrl + C to stop")
        # 事件触发方式等待
        GPIO.add_event_detect(18, GPIO.RISING, callback=button_event, bouncetime=200)
        t1 = Thread(target=long_time_thread)
        t1.setDaemon(True)
        t1.start()
    except KeyboardInterrupt:
        print("stop")
    except Exception as err:
        print(err)
    finally:
        GPIO.cleanup()
        print("GPIO clean up")