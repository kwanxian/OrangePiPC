#!/usr/bin/python3
# encoding: utf-8

import socket
from time import sleep


class sock:
    def __init__(self, target):
        self.target = (target, 6666)
        self.flag = "alive"

    def keep_conn(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.connect(self.target)
                s.send(self.flag.encode("utf8"))
                print("conn success!")
            except Exception as err:
                print(err)


if __name__ == '__main__':
    client_sock = sock("127.0.0.1")
    try:
        print("Press Ctrl + C to stop")
        while True:
            client_sock.keep_conn()
            sleep(1)
    except KeyboardInterrupt:
        print("stop")
        exit(1)
    except Exception as err:
        print(err)
