#!/usr/bin/python3
# encoding: utf-8

import serial


class printer(serial.Serial):
    def __init__(self, port):
        serial.Serial.__init__(self)
        self.name = "printer"
        self.port = port
        self.baudrate = 9600
        self.bytesize = 8
        self.stopbits = 1
        self.timeout = 1

    def enable(self):
        try:
            self.open()
        except Exception as err:
            print(err)

    # convert string to hex_code
    def __str_to_hex(self, source_str):
        # 转换成十六进制,原字符串的1个字符对应2位十六位字符，大写显示
        s_str = source_str.encode('ascii').hex().upper()
        result_format = []
        # 获取字符串元素及下标，当下标为奇数时，添加' '空格，因为打印格式要求
        for i in enumerate(s_str):
            obj = i[1]
            if i[0] == 0 or i[0] % 2 != 0:
                result_format.append(obj)
            else:
                result_format.append(' ' + obj)
        # 重新拼接字符串
        result_format = ''.join(result_format)
        return result_format

    def print_test(self):
        # hex code 0x1B 0x40 0x12 0x54
        test_cmd = "1B 40 12 54"
        self.write(bytearray.fromhex(test_cmd))

    def print_text_format(self, text_info):
        # printer init
        l1 = '1B 40'
        # line height 10,20,30,40,50,60
        l2 = '1B 33 20'
        # font size 00,11,10,01
        l3 = '1D 21 00'
        # text alignment 00:left 01:center 02:right
        l4 = '1B 61 00'
        # your data
        l5 = '{}'.format(self.__str_to_hex(text_info))
        # tell printer finish 0A: new line
        l6 = '0D 0A 0D'
        # b_data = bytearray(tick_info,encoding='gb2312')
        # self.printer.write(b_data)
        tick_info = " ".join([l1, l2, l3, l4, l5, l6])
        self.write(bytearray.fromhex(tick_info))

    def print_qrcode_format(self, qrcode_info):
        def check_qrcode_len(str_info):
            qrcode_len = len(str_info)
            if qrcode_len <= 15:
                info_length = "0" + hex((qrcode_len + 3)).upper().split('x')[1]
            else:
                info_length = hex((qrcode_len + 3)).upper()[2:]
            return info_length

        info_length = check_qrcode_len(qrcode_info)
        info = self.__str_to_hex(qrcode_info)

        # init
        l1 = '1B 40'
        # qr_code size: 43 02、43 03、43 04、43 05、43 06、43 07、43 08
        l2 = '1D 28 6b 03 00 31 43 05'
        # limit
        l3 = '1D 28 6b 03 00 31 45 30'
        # data length & your date
        l4 = '1D 28 6b {} 00 31 50 30 {}'.format(info_length, info)
        # qr_code position 00:left 01:middle 10:right
        l5 = '1B 61 01'
        # limit
        l6 = '1D 28 6b 03 00 31 52 30'
        l7 = '1D 28 6b 03 00 31 51 30'
        # tell printer finish
        l8 = '0D 0A 0A'
        qrcode_info = " ".join([l1, l2, l3, l4, l5, l6, l7, l8])
        self.write(bytearray.fromhex(qrcode_info))


if __name__ == '__main__':
    my_printer = printer("COM3")
    my_printer.enable()
    my_printer.print_test()
    my_printer.print_text_format("Hello World!")
    my_printer.print_qrcode_format("Hello World!")
