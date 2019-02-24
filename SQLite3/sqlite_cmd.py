#!/usr/bin/python3
# encoding: utf-8

import os, sqlite3


# sqlite3 test.db .dump > test.sql
os.system("sqlite3 ./db/demo.db .dump > ./db/demo.sql")
# print("finish")
# sqlite3 test.sql > test.db
# os.system("sqlite3 ./db/demo.db < ./db/demo.sql")
print("finish")