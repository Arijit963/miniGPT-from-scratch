import sqlite3


conn = sqlite3.connect(
    r"data/iot.db"
)

cursor = conn.cursor()

cursor.execute(
    "SELECT * FROM devices"
)

rows = cursor.fetchall()

for row in rows:

    print(row)

conn.close()