#!/usr/bin/python3
# encoding: utf-8

import OPi.GPIO as GPIO, tkinter as tk
from time import sleep


# 事件触发方式等待
def button_event(channel):
    if GPIO.input(channel) == GPIO.HIGH:
        GPIO.output(16, 1)
    else:
        GPIO.output(16, 0)


def gpio_init():
    GPIO.setboard(GPIO.PCPCPLUS)
    GPIO.setmode(GPIO.BOARD)
    # 这个接口接到LED的正极，LED的负极接到GND即可
    GPIO.setup(16, GPIO.OUT)
    GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(18, GPIO.RISING, button_event, bouncetime=200)
    print("GPIO init success!")


if __name__ == '__main__':
    try:
        gpio_init()
        app = tk.Tk()
        app.mainloop()
    except Exception as err:
        print(err)
    finally:
        GPIO.cleanup()
        print("GPIO clean up")