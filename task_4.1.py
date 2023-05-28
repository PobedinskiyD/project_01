# Задача 4.1.
# Домашнее задание на SQL

# В базе данных teacher создайте таблицу Students

# Структура таблицы: Student_Id - Integer, Student_Name - Text, School_Id - Integer (Primary key)

# Наполните таблицу следующими данными:

# 201, Иван, 1
# 202, Петр, 2
# 203, Анастасия, 3
# 204, Игорь, 4

# Напишите программу, с помощью которой по ID студента можно получать информацию о школе и студенте.

# Формат вывода:

# ID Студента:
# Имя студента:
# ID школы:
# Название школы:


import sqlite3

def get_student(student_id):
  connection = sqlite3.connect("teachers.db")
  cursor = connection.cursor()
  query = "SELECT * FROM School JOIN Students ON School.School_Id = Students.School_Id WHERE Students.Student_id = ?"
  cursor.execute(query,(student_id,))
  records = cursor.fetchall()
  print(records)
  for row in records:
    print('ID Студента:', row[3])
    print('Имя Студента:', row[4])
    print('ID школы:', row[0])
    print('Название школы:', row[1])

get_student(201)