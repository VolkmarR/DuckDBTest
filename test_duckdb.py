import duckdb
import pandas
conn = duckdb.connect()
conn.execute("CREATE TABLE persons (id INTEGER, name STRING, street STRING, city STRING,email STRING)")
conn.execute("CREATE TABLE books (id INTEGER, isbn STRING, name STRING, category INTEGER, price DECIMAL)")
conn.execute("CREATE TABLE orderItems (id INTEGER, person_id INTEGER, book_id INTEGER, quantity INTEGER, date DATE)")

conn.execute("COPY persons From 'testData\\persons.csv' (HEADER)")
conn.execute("COPY books From 'testData\\books.csv' (HEADER)")
conn.execute("COPY orderItems From 'testData\\orderItems.csv' (HEADER)")

print(conn.execute("SELECT Count(*) FROM persons").fetchall())
print(conn.execute("SELECT Count(*) FROM books").fetchall())
print(conn.execute("SELECT Count(*) FROM orderItems").fetchall())
print(conn.execute("""SELECT Count(*) FROM orderItems 
inner Join persons on person_id = persons.id 
inner Join books on book_id = books.id""").fetchall())
