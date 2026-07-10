import sqlite3

import re


def clean_sql(sql):

    sql = sql.replace(
        "> =",
        ">="
    )

    sql = sql.replace(
        "< =",
        "<="
    )

    sql = sql.replace(
        "! =",
        "!="
    )

    sql = re.sub(
        r"'\s*(.*?)\s*'",
        r"'\1'",
        sql
    )

    return sql


def execute_sql(sql):

    sql = clean_sql(sql)
    
    try:

        conn = sqlite3.connect(
            r"data/iot.db"
        )

        cursor = conn.cursor()

        cursor.execute(sql)

        rows = cursor.fetchall()

        columns = [
            desc[0]
            for desc in cursor.description
        ] if cursor.description else []

        conn.close()

        return columns, rows

    except Exception as e:

        return None, str(e)