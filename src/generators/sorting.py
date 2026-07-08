import random

from generators.helper import add_sample

from generators.sql_templates import (
    order_by
)

from generators.templates import (
    SORT_DESC_PATTERNS,
    SORT_ASC_PATTERNS
)


FIELDS = {

    "temperature": "sensors",

    "humidity": "sensors",

    "pressure": "sensors",

    "battery": "devices"
}


LIMITS = [5, 10, 20]


def generate_sorting_queries():

    dataset = []

    # =====================================================
    # DESCENDING
    # =====================================================

    for field, table in FIELDS.items():

        for limit in LIMITS:

            for pattern in SORT_DESC_PATTERNS:

                query = pattern.format(
                    field=field,
                    table=table,
                    limit=limit
                )

                sql = order_by(
                    table,
                    field,
                    descending=True,
                    limit=limit
                )

                add_sample(
                    dataset,
                    query,
                    sql
                )

    # =====================================================
    # ASCENDING
    # =====================================================

    for field, table in FIELDS.items():

        for limit in LIMITS:

            for pattern in SORT_ASC_PATTERNS:

                query = pattern.format(
                    field=field,
                    table=table,
                    limit=limit
                )

                sql = order_by(
                    table,
                    field,
                    descending=False,
                    limit=limit
                )

                add_sample(
                    dataset,
                    query,
                    sql
                )

    random.shuffle(dataset)

    return dataset