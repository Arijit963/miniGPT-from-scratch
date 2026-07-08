import random

from generators.helper import add_sample

from generators.templates import *

from generators.sql_templates import (
    last_30_min_query,
    last_hour_query,
    last_6_hours_query,
    last_day_query,
    today_query,
    last_week_query,
    last_month_query
)


def generate_time_queries():

    dataset = []

    mappings = [

        (LAST_30_MIN_PATTERNS, last_30_min_query()),

        (LAST_HOUR_PATTERNS, last_hour_query()),

        (LAST_6_HOURS_PATTERNS, last_6_hours_query()),

        (LAST_DAY_PATTERNS, last_day_query()),

        (TODAY_PATTERNS, today_query()),

        (LAST_WEEK_PATTERNS, last_week_query()),

        (LAST_MONTH_PATTERNS, last_month_query())
    ]

    for patterns, sql in mappings:

        for pattern in patterns:

            add_sample(
                dataset,
                pattern,
                sql
            )

    random.shuffle(dataset)

    return dataset