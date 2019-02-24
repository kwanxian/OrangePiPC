#!/usr/bin/python3
# encoding: utf-8

import socket
from time import sleep


class sock:
    def __init__(self, addr):
        self.bind_target = (addr, 6666)

    def listen_conn(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(self.bind_target)
            s.listen(5)
            try:
                s.settimeout(1)
                client, addr = s.accept()
                print("conn from: %s" % str(addr))
                recv_data = client.recv(1024).decode("utf8")
                print(recv_data)
            except Exception as err:
                print(err)


if __name__ == '__main__':
    my_server = sock("127.0.0.1")
    while True:
        my_server.listen_conn()
        sleep(1)

