import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="movies",
    user="postgres",
    password="",
)

cursor = conn.cursor()


# create_table_query = """
# CREATE TABLE rating (
#   title text NOT NULL,
#   rate FLOAT(2),
#   release_year text NOT NULL
# )
# """
# cursor.execute(create_table_query)

title = input()
rate = input()
release_year = input()
insert = "INSERT INTO rating VALUES (%s, %s, %s);"
cursor.execute(insert, (title, rate, release_year))


conn.commit()
cursor.close()
conn.close()