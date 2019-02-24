#!/usr/bin/python3
# encoding: utf-8


import sqlite3
from datetime import datetime


class my_db:
    def __init__(self,db_file):
        self.file = db_file
        self.db_conn = sqlite3.connect(self.file)
        self.db_cursor = self.db_conn.cursor()

    def create_student_table(self):
        # 如果表存在就删除旧表
        # drop table if exists students
        # 如果表不存在就重新建立
        # create table if not exists students
        script = '''create table if not exists students(
        id integer primary key autoincrement,
        name text not null,
        sex text not null,
        age int not null,
        note text,
        update_time text);'''
        self.db_cursor.executescript(script)
        self.db_conn.commit()

    def format_result(self,data):
        title = ("id", "name", "sex", "age", "note", "update_time")
        for i in data:
            data = dict(zip(title, i))
            print(data)

    def insert_data(self, data):
        try:
            update_time = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")
            self.db_cursor.execute("insert into students (name,sex,age,note,update_time) "
                                   "values (?,?,?,?,?)",
                                   (data.name, data.sex, data.age, data.note, update_time))
            self.db_conn.commit()
        except Exception as err:
            print("Insert Error: %s" % str(err))

    def delete_data(self, name):
        try:
            self.db_cursor.execute("delete from students where name = (?)", (name,))
            self.db_conn.commit()
        except Exception as err:
            print("Delete Error: %s" % str(err))

    def update_data(self, name, age):
        try:
            self.db_cursor.execute("update students set age = (?) where name = (?)", (age, name))
            self.db_conn.commit()
        except Exception as err:
            print("Update Error: %s" % str(err))

    def search_data(self, name):
        try:
            result = self.db_cursor.execute("select * from students where name = (?)", (name,))
            result = result.fetchall()
            self.format_result(result)
        except Exception as err:
            print("Search Error: %s" % str(err))

    def reset_table(self):
        try:
            self.db_cursor.execute("delete from students")
            self.db_cursor.execute("update sqlite_sequence set seq = 0 where name = 'students'")
            self.db_conn.commit()
        except Exception as err:
            print("Reset Error: %s" % str(err))

    def select_time_data(self, time_value):
        try:
            result = self.db_cursor.execute("select * from students where update_time > (?)",
                                            (time_value,))
            result = result.fetchall()
            print("-" * 40)
            self.format_result(result)
        except Exception as err:
            print("Search Error: %s" % str(err))


class student_obj:
    def __init__(self,name, sex, age, note):
        self.name = name
        self.sex = sex
        self.age = age
        self.note = note


if __name__ == '__main__':
    Mike = student_obj("Mick","boy",12,"")
    demo_db = my_db("./db/demo.db")
    demo_db.create_student_table()
    demo_db.insert_data(Mike)
    demo_db.update_data("Mick", 20)
    demo_db.search_data("Mick")
    demo_db.delete_data("Jack")
    demo_db.select_time_data("2019-02-23 23:50:50")
    demo_db.db_conn.close()
