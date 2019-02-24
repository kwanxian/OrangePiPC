#!/usr/bin/python3
# encoding: utf-8

import random
from SQLite3.db_function import my_db, student_obj


def generate_students():
    name_len = random.choice(range(3, 10))
    s_name = "".join(random.choices(name_char, k=name_len)).capitalize()
    if s_name in name_list:
        generate_students()
    else:
        s_sex = random.choice(sex_choice)
        s_age = random.choice(age_choice)
        s_note = random.choice(note_choice)
        student_list.append(student_obj(s_name, s_sex, s_age, s_note))
        name_list.append(s_name)


def insert_students(count):
    start = 0
    while start < count:
        generate_students()
        start += 1
    demo_db.insert_big_data(student_list)


if __name__ == '__main__':
    # data_init
    name_char = [chr(i) for i in range(97, 123)]
    sex_choice = ("boy", "girl")
    age_choice = [i for i in range(6, 12)]
    note_choice = ("new", "old", "good", "normal", "")

    name_list = []
    student_list = []

    demo_db = my_db("./db/big_data.db")
    demo_db.create_student_table()
    # insert_students(1000)
    demo_db.select_order_result()
