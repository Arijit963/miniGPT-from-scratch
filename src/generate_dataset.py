import random

from generators import categorical
from generators.config import OUTPUT_FILE
from generators.numeric import generate_numeric_queries
from generators.helper import save_dataset
from generators.categorical import generate_categorical_queries
from generators.aggregation import generate_aggregation_queries
from generators.sorting import generate_sorting_queries
from generators.advanced_multi_condition import (
    generate_advanced_multi_condition_queries
)
from generators.multi_condition import (
    generate_multi_condition_queries
)


def main():

    random.seed(42)

    dataset = []

    # =====================================================
    # Numeric
    # =====================================================

    print("=" * 50)
    print("Generating Numeric Queries...")
    print("=" * 50)

    numeric = generate_numeric_queries()

    print(f"Generated : {len(numeric)}")

    dataset.extend(numeric)

    print()

    # =====================================================
    # Categorical
    # =====================================================

    print("=" * 50)
    print("Generating Categorical Queries...")
    print("=" * 50)

    categorical = generate_categorical_queries()

    print(f"Generated : {len(categorical)}")

    dataset.extend(categorical)

    print()

    # =====================================================
    # Aggregation
    # =====================================================

    print("=" * 50)
    print("Generating Aggregation Queries...")
    print("=" * 50)

    aggregation = generate_aggregation_queries()

    print(f"Generated : {len(aggregation)}")

    dataset.extend(aggregation)

    print()
    
    # =====================================================
    # Sorting
    # =====================================================

    print("=" * 50)
    print("Generating Sorting Queries...")
    print("=" * 50)

    sorting = generate_sorting_queries()

    print(f"Generated : {len(sorting)}")

    dataset.extend(sorting)

    print()
    
    # =====================================================
    # Multi condition queries
    # =====================================================
    
    print("=" * 50)
    print("Generating Multi Condition Queries...")
    print("=" * 50)

    multi_condition = generate_multi_condition_queries()

    print(f"Generated : {len(multi_condition)}")

    dataset.extend(multi_condition)

    print()
    
    # =====================================================
    # Advanced Multi condition queries
    # =====================================================

    print("=" * 50)
    print("Generating Advanced Multi Condition Queries...")
    print("=" * 50)

    advanced_multi = (
        generate_advanced_multi_condition_queries()
    )

    print(f"Generated : {len(advanced_multi)}")

    dataset.extend(advanced_multi)

    print()

    # =====================================================
    # Summary
    # =====================================================

    print("=" * 50)
    print("Dataset Summary")
    print("=" * 50)

    print(f"Numeric Queries          : {len(numeric)}")
    print(f"Categorical Queries      : {len(categorical)}")
    print(f"Aggregation Queries      : {len(aggregation)}")
    print(f"Multi Condition Queries  : {len(multi_condition)}")
    print(f"Advanced Multi Condition : {len(advanced_multi)}")
    print(f"Sorting Queries          : {len(sorting)}")
    print(f"Total Samples            : {len(dataset)}")

    print()

    # =====================================================
    # Save
    # =====================================================

    print("Saving dataset...")

    save_dataset(
        dataset,
        OUTPUT_FILE
    )

    print(f"Saved to : {OUTPUT_FILE}")

    print()

    # =====================================================
    # Preview
    # =====================================================

    print("=" * 50)
    print("Preview")
    print("=" * 50)

    print(dataset[0])
    
    
if __name__ == "__main__":
    main()