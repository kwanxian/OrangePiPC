#!/usr/bin/python3
# encoding: utf-8


import sqlite3
from datetime import datetime
from os import system


class my_db:
    def __init__(self,db_file):
        self.file = db_file
        self.db_conn = sqlite3.connect(self.file)
        self.db_cursor = self.db_conn.cursor()

    def db_backup(self):
        with sqlite3.connect("./db/backup.db") as bck:
            self.db_conn.backup(bck)

    def db_export(self, db_name, target_name):
        cmd = "sqlite3 ./db/{} .dump > ./db/{}".format(db_name, target_name)
        system(cmd)

    def db_import(self, db_name, file_name):
        cmd = "sqlite3 ./db/{} < ./db/{}".format(db_name, file_name)
        system(cmd)

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

    def get_table_name(self):
        result = self.db_cursor.execute("select name from sqlite_master where type = 'table").fetchall()
        result = [tuple[0] for tuple in result]
        return result

    def get_table_title(self):
        result = self.db_cursor.execute("select * from students").description
        result = [tuple[0] for tuple in result]
        return result

    def format_result(self,data):
        title = self.get_table_title()
        data = [dict(zip(title, i)) for i in data]
        for i in data:
            print(i)

    def insert_data(self, data):
        self.db_cursor.execute("insert into students (name,sex,age,note,update_time) "
                               "values (?,?,?,?,?)",
                               (data.name, data.sex, data.age, data.note, data.update_time))
        self.db_conn.commit()

    def delete_data(self, name):
        self.db_cursor.execute("delete from students where name = (?)", (name,))
        self.db_conn.commit()

    def update_data(self, name, age):
        self.db_cursor.execute("update students set age = (?) where name = (?)", (age, name))
        self.db_conn.commit()

    def search_data(self, name):
        result = self.db_cursor.execute("select * from students where name = (?)", (name,))
        result = result.fetchall()
        self.format_result(result)

    def reset_table(self):
        self.db_cursor.execute("delete from students")
        self.db_cursor.execute("update sqlite_sequence set seq = 0 where name = 'students'")
        self.db_conn.commit()

    def select_time_data(self, time_value):
        result = self.db_cursor.execute("select * from students where update_time > (?)",(time_value,))
        result = result.fetchall()
        print("-" * 100)
        self.format_result(result)

    def select_order_result(self):
        # asc | desc
        result = self.db_cursor.execute("select * from students order by id desc")
        result = result.fetchall()
        print("-" * 100)
        self.format_result(result)

    def insert_big_data(self, data_list):
        for i in data_list:
            self.db_cursor.execute("insert into students (name,sex,age,note,update_time) "
                                   "values (?,?,?,?,?)",
                                   (i.name, i.sex, i.age, i.note, i.update_time))
        self.db_conn.commit()


class student_obj:
    def __init__(self,name, sex, age, note):
        self.name = name
        self.sex = sex
        self.age = age
        self.note = note
        self.update_time = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")


if __name__ == '__main__':
    Mike = student_obj("Mick","boy",12,"")
    demo_db = my_db("./db/demo.db")
    demo_db.create_student_table()
    demo_db.insert_data(Mike)
    demo_db.update_data("Mick", 20)
    demo_db.search_data("Mick")
    demo_db.delete_data("Jack")
    demo_db.select_time_data("2019-02-24 16:00:00")
    demo_db.select_order_result()
    demo_db.db_conn.close()
