from sql_executor import execute_sql


sql = """
SELECT *
FROM devices
WHERE status='active';
"""

columns, rows = execute_sql(sql)

print(columns)

for row in rows:

    print(row)