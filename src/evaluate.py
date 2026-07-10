import json

from generate import generate


import re

# =====================================================
# Normalize SQL
# =====================================================


def normalize(text):

    text = text.lower()

    text = re.sub(
        r"\s+",
        " ",
        text
    )

    # Fix split operators

    text = text.replace(
        "> =",
        ">="
    )

    text = text.replace(
        "< =",
        "<="
    )

    text = text.replace(
        "! =",
        "!="
    )

    text = text.replace(
        "= =",
        "=="
    )

    return text.strip()

# =====================================================
# Load Evaluation Dataset
# =====================================================

with open(
    r"data/evaluation_queries.json",
    "r",
    encoding="utf-8"
) as f:

    test_cases = json.load(f)


correct = 0

total = len(test_cases)


# =====================================================
# Auto detect SQL Categories
# =====================================================

def detect_category(sql):

    sql = sql.lower()

    if "having" in sql:
        return "having"

    if "group by" in sql:
        return "group_by"

    if "order by" in sql:
        return "order_by"

    if "between" in sql:
        return "between"

    if "last_connected" in sql:
        return "time"

    return "where"

# =====================================================
# Evaluation Loop
# =====================================================

category_results = {
    "where": [0, 0],
    "group_by": [0, 0],
    "having": [0, 0],
    "order_by": [0, 0],
    "between": [0, 0],
    "time": [0, 0]
}

for i, sample in enumerate(test_cases, start=1):

    query = sample["query"]

    expected = normalize(
        sample["expected"]
    )

    prompt = f"""
### Instruction:
Convert the following IoT query into SQL.

### Input:
{query}

### Response:
"""

    prediction = generate(
        prompt
    )

    prediction_lower = prediction.lower()

    marker = "# # # response :"

    if marker in prediction_lower:

        prediction = prediction_lower.split(
            marker
        )[-1]

    stop_marker = "# # # instruction"

    if stop_marker in prediction:

        prediction = prediction.split(
            stop_marker
        )[0]

    prediction = normalize(
        prediction
    )

    matched = prediction == expected
    
    category = detect_category(
        expected
    )

    category_results[
        category
    ][1] += 1

    if matched:

        category_results[
            category
        ][0] += 1

    if matched:

        correct += 1

        status = "PASS"

    else:

        status = "FAIL"

    print("\n" + "=" * 60)

    print(f"Test Case {i}")

    print()

    print("Query:")
    print(query)

    print()

    print("Expected:")
    print(expected)

    print()

    print("Predicted:")
    print(prediction)

    print()

    print("Result:", status)


# =====================================================
# Final Accuracy
# =====================================================

accuracy = (
    correct / total
) * 100

print("\n" + "=" * 60)

print(
    f"Correct : {correct}/{total}"
)

print(
    f"Accuracy: {accuracy:.2f}%"
)

print("=" * 60)

# =====================================================
# Build Evaluation Report
# =====================================================

report = {

    "accuracy": round(
        accuracy,
        2
    ),

    "correct": correct,

    "total": total,

    "categories": {}
}

print("\nCategory Accuracy")

print("=" * 60)

for category, values in category_results.items():

    correct_cat = values[0]

    total_cat = values[1]

    if total_cat == 0:
        continue

    acc = (
        correct_cat / total_cat
    ) * 100

    report[
        "categories"
    ][category] = {

        "accuracy": round(
            acc,
            2
        ),

        "correct": correct_cat,

        "total": total_cat
    }

    print(
        f"{category:10s}: "
        f"{correct_cat}/{total_cat} "
        f"({acc:.2f}%)"
    )
    
# =====================================================
# Save Report
# =====================================================

with open(
    r"data/evaluation_report.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        report,
        f,
        indent=4
    )

print()

print(
    "Evaluation report saved:"
)

print(
    "data/evaluation_report.json"
)

