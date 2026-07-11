import random

from generators.helper import add_sample

from generators.templates import (
    HAVING_PATTERNS,
    HAVING_AVG_PATTERNS
)

from generators.sql_templates import (
    having_count,
    having_avg
)


def generate_having_queries():

    dataset = []

    # =====================================================
    # HAVING COUNT
    # =====================================================

    count_groups = [

        ("sensors", "room"),

        ("devices", "status"),

        ("devices", "location")
    ]

    count_thresholds = [1,2,3,5,10,15,20,25,50]

    for table, group_field in count_groups:

        for threshold in count_thresholds:

            for pattern in HAVING_PATTERNS:

                query = pattern.format(
                    group_field=group_field,
                    threshold=threshold
                )

                sql = having_count(
                    table,
                    group_field,
                    threshold
                )

                add_sample(
                    dataset,
                    query,
                    sql
                )

    # =====================================================
    # HAVING AVG
    # =====================================================

    avg_configs = [

        ("sensors", "room", "temperature",
         [25, 30, 35, 40, 45]),

        ("sensors", "room", "humidity",
         [40, 50, 60, 70]),

        ("devices", "location", "battery",
         [5, 10, 20, 30, 40, 50, 60, 70, 80, 90])
    ]

    for table, group_field, field, thresholds in avg_configs:

        for threshold in thresholds:

            for pattern in HAVING_AVG_PATTERNS:

                query = pattern.format(
                    group_field=group_field,
                    field=field,
                    threshold=threshold
                )

                sql = having_avg(
                    table,
                    group_field,
                    field,
                    threshold
                )

                add_sample(
                    dataset,
                    query,
                    sql
                )

    random.shuffle(dataset)

    return dataset