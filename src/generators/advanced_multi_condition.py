import random

from generators.helper import add_sample

from generators.config import (
    STATUS,
    LOCATIONS,
    ROOMS
)

from generators.templates import (
    VERBS,
    ADVANCED_DEVICE_PATTERNS,
    ADVANCED_SENSOR_PATTERNS
)

from generators.sql_templates import (
    where_and
)


def generate_advanced_multi_condition_queries():

    dataset = []

    # =====================================================
    # Devices
    # =====================================================

    battery_values = [20, 40, 60, 80]

    for status in STATUS:

        for location in LOCATIONS:

            for battery in battery_values:

                for pattern in ADVANCED_DEVICE_PATTERNS[:2]:

                    query = pattern.format(
                        verb=random.choice(VERBS),
                        status=status,
                        battery=battery,
                        location=location
                    )

                    sql = where_and(
                        "devices",
                        [
                            ("status", "=", status, True),
                            ("battery", ">", battery, False),
                            ("location", "=", location, True)
                        ]
                    )

                    add_sample(
                        dataset,
                        query,
                        sql
                    )

    # =====================================================
    # Sensors
    # =====================================================

    humidity_values = [40, 60, 80]

    temperature_values = [20, 40, 60]

    for room in ROOMS:

        for humidity in humidity_values:

            for temperature in temperature_values:

                for pattern in ADVANCED_SENSOR_PATTERNS[:2]:

                    query = pattern.format(
                        verb=random.choice(VERBS),
                        room=room,
                        humidity=humidity,
                        temperature=temperature
                    )

                    sql = where_and(
                        "sensors",
                        [
                            ("room", "=", room, True),
                            ("humidity", ">", humidity, False),
                            ("temperature", "<", temperature, False)
                        ]
                    )

                    add_sample(
                        dataset,
                        query,
                        sql
                    )

    random.shuffle(dataset)

    return dataset