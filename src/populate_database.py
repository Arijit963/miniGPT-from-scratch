import sqlite3
import random
from datetime import datetime, timedelta


conn = sqlite3.connect(
    r"data/iot.db"
)

cursor = conn.cursor()


# ==========================================
# Clear Existing Data
# ==========================================

cursor.execute(
    "DELETE FROM devices"
)

cursor.execute(
    "DELETE FROM sensors"
)


# ==========================================
# Devices
# ==========================================

statuses = [
    "active",
    "inactive",
    "online",
    "offline",
    "maintenance"
]

locations = [
    "building a",
    "building b",
    "building c",
    "warehouse",
    "lab",
    "factory",
    "office"
]

device_prefixes = [
    "ESP32",
    "RPI",
    "ARDUINO",
    "STM32",
    "JETSON"
]

devices = []

today = datetime.now()

for i in range(1, 101):

    device_name = (
        f"{random.choice(device_prefixes)}-{i:03d}"
    )

    status = random.choice(
        statuses
    )

    battery = random.randint(
        5,
        100
    )

    location = random.choice(
        locations
    )

    days_ago = random.randint(
        0,
        30
    )

    last_connected = (
        today - timedelta(days=days_ago)
    ).strftime("%Y-%m-%d")

    devices.append(
        (
            i,
            device_name,
            status,
            battery,
            location,
            last_connected
        )
    )

cursor.executemany(
    """
    INSERT INTO devices
    VALUES (?, ?, ?, ?, ?, ?)
    """,
    devices
)


# ==========================================
# Sensors
# ==========================================

rooms = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "warehouse",
    "lab",
    "server_room",
    "factory",
    "office"
]

sensors = []

for i in range(1, 501):

    room = random.choice(
        rooms
    )

    temperature = round(
        random.uniform(10, 80),
        1
    )

    humidity = round(
        random.uniform(20, 95),
        1
    )

    pressure = round(
        random.uniform(950, 1050),
        1
    )

    sensors.append(
        (
            i,
            room,
            temperature,
            humidity,
            pressure
        )
    )

cursor.executemany(
    """
    INSERT INTO sensors
    VALUES (?, ?, ?, ?, ?)
    """,
    sensors
)

conn.commit()

conn.close()

print("Database Populated!")
print("Devices :", len(devices))
print("Sensors :", len(sensors))