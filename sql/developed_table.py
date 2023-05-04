import psycopg2


conn = psycopg2.connect(
    host="localhost",
    database="create table",
    user="postgres",
    password=""
)

cur = conn.cursor()




# ex 1 lab 11
output = "SELECT name, id, number FROM phonebook"
cur.execute(output)
rows = cur.fetchall()
for row in rows:
    print(row)




#ex 2 lab 11
# name = input("Enter the user's name which num you would like to update: ")
# cur.execute("SELECT * FROM phonebook WHERE name = %s", (name,))
# result = cur.fetchone()
# if result is None:
#     print("User not found in phonebook.")
# else:
#     new_number = input("Enter the new phone number: ")
#     cur.execute("UPDATE phonebook SET number = %s WHERE name = %s", (new_number, name))
#     conn.commit()




#ex 3 lab 11
# cur.execute("""
#     CREATE OR REPLACE PROCEDURE insert_many_users(
#         IN name TEXT[],
#         IN number TEXT[]
#     )
#     LANGUAGE plpgsql
#     AS $$
#     BEGIN
#         FOR i IN 1..array_length(name, 1) LOOP
#             INSERT INTO phonebook(name, number)
#             VALUES (name[i], number[i]);
#         END LOOP;
#     END;
#     $$;
# """)
# name = ['Alibek', 'Nurken']
# number = ['87093457645', '87003485647']
# cur = conn.cursor()
# cur.execute('CALL insert_many_users(%s, %s)', [name, number])
# conn.commit()




#ex 4 lab 11
# table_name = 'phonebook'
# limit = input("input the limit: ")
# offset = input("input the offset: ")
# def get_data_with_pagination (table_name, limit, offset):
    
#     # Execute the SQL query with pagination
#     cur.execute(f"SELECT * FROM {table_name} LIMIT {limit} OFFSET {offset}")
#     results = cur.fetchall()
#     return results
# results = get_data_with_pagination('phonebook', limit, offset)
# print(results)




#ex 5 lab 11
# deleting = input("Enter the field to delete by (name/number/id): ")
# value = input("Enter the value: ")
# if deleting == "name":
#     cur.execute(
#         "DELETE FROM phonebook WHERE name = %s",
#         (value,)
#     )
# elif deleting == "number":
#     cur.execute(
#         "DELETE FROM phonebook WHERE number = %s",
#         (value,)
#     )
# elif deleting == "id":
#     cur.execute(
#         "DELETE FROM phonebook WHERE id = %s",
#         (value,)
#     )




conn.commit()
cur.close()
conn.close()