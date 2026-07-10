import sqlite3


conn = sqlite3.connect(
    r"data/iot.db"
)

cursor = conn.cursor()


# ==========================================
# Devices
# ==========================================

devices = [

    (1, "ESP32-01", "active", 92, "warehouse", "2026-07-10"),

    (2, "ESP32-02", "inactive", 35, "building a", "2026-07-09"),

    (3, "ESP32-03", "online", 67, "building a", "2026-07-10"),

    (4, "Pi-Node-01", "active", 80, "warehouse", "2026-07-10"),

    (5, "Pi-Node-02", "online", 20, "building b", "2026-07-08")
]


cursor.executemany(
    """
    INSERT OR REPLACE INTO devices
    VALUES (?, ?, ?, ?, ?, ?)
    """,
    devices
)


# ==========================================
# Sensors
# ==========================================

sensors = [

    (1, "a", 25, 45, 1008),

    (2, "a", 32, 61, 1002),

    (3, "b", 18, 72, 998),

    (4, "warehouse", 40, 50, 1010),

    (5, "warehouse", 55, 68, 1005)
]


cursor.executemany(
    """
    INSERT OR REPLACE INTO sensors
    VALUES (?, ?, ?, ?, ?)
    """,
    sensors
)

conn.commit()

conn.close()

print("Database Populated!")