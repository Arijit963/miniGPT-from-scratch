import sqlite3


conn = sqlite3.connect(
    r"data/iot.db"
)

cursor = conn.cursor()


# ==========================================
# Devices Table
# ==========================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS devices (

    id INTEGER PRIMARY KEY,

    device_name TEXT,

    status TEXT,

    battery INTEGER,

    location TEXT,

    last_connected TEXT
)
""")


# ==========================================
# Sensors Table
# ==========================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS sensors (

    id INTEGER PRIMARY KEY,

    room TEXT,

    temperature REAL,

    humidity REAL,

    pressure REAL
)
""")


conn.commit()

conn.close()

print("Database Created!")