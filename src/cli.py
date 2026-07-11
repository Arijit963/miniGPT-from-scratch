import json
from inference import query_to_sql
import os
from sql_executor import execute_sql
'''from generate import (
    generate,
    extract_sql
)'''

# =====================================================
# Load Evaluation Report
# =====================================================

with open(
    r"data/evaluation_report.json",
    "r",
    encoding="utf-8"
) as f:

    report = json.load(f)


# =====================================================
# Load Training Info
# =====================================================

with open(
    r"data/training_info.json",
    "r",
    encoding="utf-8"
) as f:

    info = json.load(f)


# =====================================================
# Banner
# =====================================================

print()

print("=" * 50)

print("IoTQueryGPT v2")

print(
    f"Model Accuracy : {report['accuracy']}%"
)

print(
    f"Vocabulary Size: {info['vocab_size']}"
)

print(
    f"Layers         : {info['n_layer']}"
)

print(
    f"Heads          : {info['n_head']}"
)

print(
    f"Embedding Dim  : {info['n_embd']}"
)

print("=" * 50)

print()

print("Commands:")
print("help  -> show commands")
print("stats -> model statistics")
print("exit  -> quit")

print()


# =====================================================
# CLI Loop
# =====================================================

while True:

    query = input(
        "\nIoT Query > "
    ).strip()

    if not query:
        continue

    if query.lower() == "exit":

        print(
            "\nGoodbye!"
        )

        break


    if query.lower() == "clear":

        os.system(
            "cls" if os.name == "nt"
            else "clear"
        )

        continue

    if query.lower() == "help":

        print("\nExamples:")

        print(
            "show active devices"
        )

        print(
            "show top 10 devices with highest battery"
        )

        print(
            "count devices by status"
        )

        continue

    if query.lower() == "stats":

        print()

        print("=" * 40)

        print(
            f"Accuracy : {report['accuracy']}%"
        )

        print(
            f"Correct  : {report['correct']}"
        )

        print(
            f"Total    : {report['total']}"
        )

        print("=" * 40)

        continue

    prompt = f"""
### Instruction:
Convert the following IoT query into SQL.

### Input:
{query}

### Response:
"""

    sql = query_to_sql(query)

    print()

    print("Generated SQL:")

    print()

    print(sql)

    print()

    print("Query Results:")

    columns, rows = execute_sql(sql)

    if columns is None:

        print(rows)

    else:

        print(" | ".join(columns))

        print("-" * 60)

        for row in rows:

            print(
                " | ".join(
                    str(x)
                    for x in row
                )
            )