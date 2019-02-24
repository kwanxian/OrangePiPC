#!/usr/bin/python3
# encoding: utf-8

import serial
from time import sleep


class scanner(serial.Serial):
    def __init__(self, port):
        serial.Serial.__init__(self)
        self.name = "scanner"
        self.port = port
        self.baudrate = 9600
        self.bytesize = 8
        self.stopbits = 1
        self.timeout = 1

    def scan_init(self):
        try:
            self.open()
            print("scanner init success!")
        except Exception as err:
            print(err)
            exit(1)

    def scan_begin(self):
        data = self.read_all().decode("ascii")
        return data


if __name__ == '__main__':
    my_scanner = scanner("COM3")
    my_scanner.scan_init()
    try:
        while my_scanner.is_open:
            data = my_scanner.scan_begin()
            if data == "":pass
            else:
                print(data)
            sleep(0.2)
    except KeyboardInterrupt:
        print("stop!")
        my_scanner.close()
    except Exception as err:
        print(err)
