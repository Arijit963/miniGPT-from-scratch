import json

from generate import generate


# =====================================================
# Normalize SQL
# =====================================================

def normalize(text):

    return " ".join(
        text.lower().split()
    )


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
# Evaluation Loop
# =====================================================

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