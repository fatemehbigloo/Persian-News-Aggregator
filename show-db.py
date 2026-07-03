
import sqlite3

conn = sqlite3.connect('news.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM news')
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()



