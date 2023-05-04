import psycopg2
import csv



conn = psycopg2.connect(
    host="localhost",
    database="create table",
    user="postgres",
    password=""
)

cur = conn.cursor()

#1 ex
# cur.execute("CREATE TABLE phonebook (id SERIAL PRIMARY KEY, name text NOT NULL, number text NOT NULL)")




# 2 ex
# id = input("input the id: ")
# name = input("input the name: ")
# number = input("input the number: ")
# insert = "INSERT INTO phonebook VALUES (%s, %s, %s);"
# cur.execute(insert, (id, name, number))




#2 ex
# array =[]
# with open ("1.csv") as f:
#     reader = csv.reader(f, delimiter = ",")
#     for row in reader:
#         row[0] = int(row[0])
#         array.append(row)
# insert = "INSERT INTO phonebook VALUES (%s, %s, %s) RETURNING *;"
# for row in array:
#     cur.execute(insert, row)
# final = cur.fetchall()
# print(final)




#3 ex
#Реализация обновления данных в таблице (изменение имени пользователя или телефона)
# field = input("Enter the field to update (name or number): ")
# name = input("Enter the name or number to update: ")
# new_value = input("Enter the new value: ")
# sql = "UPDATE phonebook SET {} = %s WHERE name = %s".format(field)
# cur.execute(sql, (new_value, name))




#4 ex
# Запрос данных из таблиц 
# x = input("Which person's number do you want? ")
# select = "SELECT number FROM phonebook WHERE name = %s"
# cur.execute(select, (x,)) #Python will interpret the expression (x) as just the value of x, without creating a tuple. 
# final = cur.fetchall()
# print(final)




#5 ex 
# x = input("Which person's data do you want to delete? ")
# delete = "DELETE FROM phonebook WHERE name = %s "
# cur.execute(delete, (x,))




conn.commit()
cur.close()
conn.close()