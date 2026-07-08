import random

from generators.helper import add_sample

from generators.templates import (
    GROUP_COUNT_PATTERNS,
    GROUP_AVG_PATTERNS
)

from generators.sql_templates import (
    group_by_count,
    group_by_avg
)


def generate_group_by_queries():

    dataset = []

    # ==========================================
    # COUNT GROUPS
    # ==========================================

    count_groups = [

        ("sensors", "room"),

        ("devices", "status"),

        ("devices", "location")
    ]

    for table, field in count_groups:

        for pattern in GROUP_COUNT_PATTERNS:

            query = pattern.format(
                table=table,
                field=field
            )

            sql = group_by_count(
                table,
                field
            )

            add_sample(
                dataset,
                query,
                sql
            )

    # ==========================================
    # AVG GROUPS
    # ==========================================

    avg_groups = [

        ("sensors", "room", "temperature"),

        ("sensors", "room", "humidity"),

        ("sensors", "room", "pressure"),

        ("devices", "location", "battery")
    ]

    for table, group_field, value_field in avg_groups:

        for pattern in GROUP_AVG_PATTERNS:

            query = pattern.format(
                value_field=value_field,
                group_field=group_field
            )

            sql = group_by_avg(
                table,
                group_field,
                value_field
            )

            add_sample(
                dataset,
                query,
                sql
            )

    random.shuffle(dataset)

    return dataset