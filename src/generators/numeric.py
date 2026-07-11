import random
from generators.helper import add_sample
from generators.config import NUMERIC_FIELDS
from generators.sql_templates import where_numeric
from generators.templates import (
    VERBS,
    GREATER_THAN,
    LESS_THAN,
    NUMERIC_PATTERNS
)
from generators.helper import make_instruction


def generate_numeric_queries():
    """
    Generate instruction-tuning samples for all numeric IoT fields.

    Supports:
        - temperature
        - humidity
        - pressure
        - battery

    Simply add a new field to NUMERIC_FIELDS in config.py
    and this generator will automatically include it.
    """

    dataset = []

    for field, info in NUMERIC_FIELDS.items():

        table = info["table"]

        minimum = info["min"]

        maximum = info["max"]

        step = info["step"]

        unit = info["unit"]

        values = range(
            minimum,
            maximum + 1,
            step
        )

        # ----------------------------
        # Greater-than Queries
        # ----------------------------

        for value in values:

            for pattern in NUMERIC_PATTERNS:

                query = pattern.format(

                    verb=random.choice(VERBS),

                    table=table,

                    field=field,

                    comparison=random.choice(GREATER_THAN),

                    value=f"{value} {unit}".strip()

                )

                sql = where_numeric(table, field, ">", value)

                add_sample(
                    dataset,
                    query,
                    sql
                )

        # ----------------------------
        # Less-than Queries
        # ----------------------------

        for value in values:

            for pattern in NUMERIC_PATTERNS:

                query = pattern.format(

                    verb=random.choice(VERBS),

                    table=table,

                    field=field,

                    comparison=random.choice(LESS_THAN),

                    value=f"{value} {unit}".strip()

                )

                sql = where_numeric(table, field, "<", value)
                   
                for _ in range(3):

                    add_sample(
                        dataset,
                        query,
                        sql
                    )

    random.shuffle(dataset)

    return dataset

