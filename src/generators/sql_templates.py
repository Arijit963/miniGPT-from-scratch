# ==========================================================
# Basic WHERE Queries
# ==========================================================

def where_numeric(table, field, operator, value):
    return (
        f"SELECT * FROM {table} "
        f"WHERE {field} {operator} {value};"
    )


def where_string(table, field, value):
    return (
        f"SELECT * FROM {table} "
        f"WHERE {field} = '{value}';"
    )


# ==========================================================
# Aggregation Queries
# ==========================================================

def count(table):
    return (
        f"SELECT COUNT(*) FROM {table};"
    )


def average(table, field):
    return (
        f"SELECT AVG({field}) FROM {table};"
    )


def maximum(table, field):
    return (
        f"SELECT MAX({field}) FROM {table};"
    )


def minimum(table, field):
    return (
        f"SELECT MIN({field}) FROM {table};"
    )


def summation(table, field):
    return (
        f"SELECT SUM({field}) FROM {table};"
    )


# ==========================================================
# ORDER BY
# ==========================================================

def order_by(table, field, descending=True, limit=None):

    sql = f"SELECT * FROM {table}"

    sql += f" ORDER BY {field}"

    sql += " DESC" if descending else " ASC"

    if limit is not None:
        sql += f" LIMIT {limit}"

    sql += ";"

    return sql


# ==========================================================
# Multi Condition Queries
# ==========================================================

def where_and(table, conditions):

    sql = f"SELECT * FROM {table} WHERE "

    clauses = []

    for field, operator, value, is_string in conditions:

        if is_string:
            clauses.append(
                f"{field} {operator} '{value}'"
            )
        else:
            clauses.append(
                f"{field} {operator} {value}"
            )

    sql += " AND ".join(clauses)

    sql += ";"

    return sql


# ==========================================================
# Three Condition Queries
# ==========================================================

def where_and(table, conditions):

    sql = f"SELECT * FROM {table} WHERE "

    clauses = []

    for field, operator, value, is_string in conditions:

        if is_string:
            clauses.append(
                f"{field} {operator} '{value}'"
            )
        else:
            clauses.append(
                f"{field} {operator} {value}"
            )

    sql += " AND ".join(clauses)

    sql += ";"

    return sql

# ==========================================================
# Time Queries
# ==========================================================

def last_hour_query():

    return (
        "SELECT * FROM devices "
        "WHERE last_connected >= NOW() - INTERVAL 1 HOUR;"
    )


def last_day_query():

    return (
        "SELECT * FROM devices "
        "WHERE last_connected >= NOW() - INTERVAL 1 DAY;"
    )


def today_query():

    return (
        "SELECT * FROM devices "
        "WHERE DATE(last_connected) = CURRENT_DATE;"
    )


def last_week_query():

    return (
        "SELECT * FROM devices "
        "WHERE last_connected >= NOW() - INTERVAL 7 DAY;"
    )
    
def last_30_min_query():

    return (
        "SELECT * FROM devices "
        "WHERE last_connected >= "
        "NOW() - INTERVAL 30 MINUTE;"
    )


def last_6_hours_query():

    return (
        "SELECT * FROM devices "
        "WHERE last_connected >= "
        "NOW() - INTERVAL 6 HOUR;"
    )


def last_month_query():

    return (
        "SELECT * FROM devices "
        "WHERE last_connected >= "
        "NOW() - INTERVAL 30 DAY;"
    )
# ==========================================================
# BETWEEN Queries
# ==========================================================

def between_query(
    table,
    field,
    lower,
    upper
):

    return (
        f"SELECT * FROM {table} "
        f"WHERE {field} BETWEEN {lower} AND {upper};"
    )
    
# ==========================================================
# GROUP BY Queries
# ==========================================================

def group_by_count(
    table,
    group_field
):

    return (
        f"SELECT {group_field}, COUNT(*) "
        f"FROM {table} "
        f"GROUP BY {group_field};"
    )


def group_by_avg(
    table,
    group_field,
    value_field
):

    return (
        f"SELECT {group_field}, AVG({value_field}) "
        f"FROM {table} "
        f"GROUP BY {group_field};"
    )


# ==========================================================
# HAVING Queries
# ==========================================================

def having_count(
    table,
    group_field,
    threshold
):

    return (
        f"SELECT {group_field}, COUNT(*) "
        f"FROM {table} "
        f"GROUP BY {group_field} "
        f"HAVING COUNT(*) > {threshold};"
    )

def having_avg(
    table,
    group_field,
    value_field,
    threshold
):

    return (
        f"SELECT {group_field}, "
        f"AVG({value_field}) "
        f"FROM {table} "
        f"GROUP BY {group_field} "
        f"HAVING AVG({value_field}) > {threshold};"
    )