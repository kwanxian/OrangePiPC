#!/usr/bin/python3
# encoding: utf-8


from smbus2 import SMBus
import time

bus = SMBus(1)
address = 0x14


def writeNumber(value):
    bus.write_byte(address, value)
    return -1


def readNumber():
    number = bus.read_byte(address)
    return number


def readBlockData(numBytes):
    res3 = []
    x = bus.read_i2c_block_data(address, 0, numBytes)
    res3.extend(x)
    return res3


def readBunchOfData(numBytes):
    # Send number of bytes we are requesting
    writeNumber(numBytes)
    # Receive data
    myDataHere = readBlockData(numBytes)
    # Show what we've got
    print("We received ", numBytes, " of data")
    for i in range(0, numBytes):
        print(myDataHere[i])


while True:
    # For now, hard-code 4 bytes of data
    print()
    print("We are requesting ", 4, " bytes of data")
    readBunchOfData(4)
    print()