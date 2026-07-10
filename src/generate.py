from inference import query_to_sql


if __name__ == "__main__":

    user_query = input(
        "Prompt: "
    )

    sql = query_to_sql(
        user_query
    )

    print("\nGenerated SQL:\n")

    print(sql)