import json
import random


evaluation_set = []


# ==========================================================
# WHERE QUERIES (40)
# ==========================================================

statuses = [
    "active",
    "inactive",
    "online",
    "offline",
    "maintenance"
]

for status in statuses:

    evaluation_set.append({
        "query": f"show {status} devices",
        "expected": f"select * from devices where status = ' {status} ' ;"
    })

for battery in [10, 20, 30, 40, 50, 60, 70, 80]:

    evaluation_set.append({
        "query": f"show devices with battery below {battery}",
        "expected": f"select * from devices where battery < {battery} ;"
    })

    evaluation_set.append({
        "query": f"show devices with battery above {battery}",
        "expected": f"select * from devices where battery > {battery} ;"
    })

for humidity in [40, 50, 60, 70, 80]:

    evaluation_set.append({
        "query": f"show sensors with humidity above {humidity}",
        "expected": f"select * from sensors where humidity > {humidity} ;"
    })

for temp in [20, 30, 40, 50, 60]:

    evaluation_set.append({
        "query": f"show sensors with temperature above {temp}",
        "expected": f"select * from sensors where temperature > {temp} ;"
    })


# ==========================================================
# GROUP BY (15)
# ==========================================================

evaluation_set.extend([

    {
        "query": "count devices by status",
        "expected":
        "select status , count ( * ) from devices group by status ;"
    },

    {
        "query": "show average battery by location",
        "expected":
        "select location , avg ( battery ) from devices group by location ;"
    },

    {
        "query": "show average humidity by room",
        "expected":
        "select room , avg ( humidity ) from sensors group by room ;"
    },

    {
        "query": "show average temperature by room",
        "expected":
        "select room , avg ( temperature ) from sensors group by room ;"
    }
])


# ==========================================================
# HAVING (10)
# ==========================================================

for threshold in [2, 5, 10, 20, 30]:

    evaluation_set.append({

        "query":
        f"show rooms having more than {threshold} sensors",

        "expected":
        f"select room , count ( * ) from sensors "
        f"group by room having count ( * ) > {threshold} ;"
    })

    evaluation_set.append({

        "query":
        f"show locations where average battery exceeds {threshold}",

        "expected":
        f"select location , avg ( battery ) "
        f"from devices group by location "
        f"having avg ( battery ) > {threshold} ;"
    })


# ==========================================================
# ORDER BY (15)
# ==========================================================

for top_n in [5, 10, 20]:

    evaluation_set.append({

        "query":
        f"show top {top_n} devices with highest battery",

        "expected":
        f"select * from devices "
        f"order by battery desc limit {top_n} ;"
    })

    evaluation_set.append({

        "query":
        f"show top {top_n} devices with lowest battery",

        "expected":
        f"select * from devices "
        f"order by battery asc limit {top_n} ;"
    })


# ==========================================================
# BETWEEN (10)
# ==========================================================

ranges = [

    (20, 40),
    (30, 50),
    (40, 60),
    (50, 80),
    (10, 30)
]

for low, high in ranges:

    evaluation_set.append({

        "query":
        f"show sensors with temperature between {low} and {high}",

        "expected":
        f"select * from sensors "
        f"where temperature between {low} and {high} ;"
    })

    evaluation_set.append({

        "query":
        f"show devices with battery between {low} and {high}",

        "expected":
        f"select * from devices "
        f"where battery between {low} and {high} ;"
    })


# ==========================================================
# TIME (10)
# ==========================================================

evaluation_set.extend([

    {
        "query":
        "show devices connected today",

        "expected":
        "select * from devices "
        "where date ( last_connected ) = current_date ;"
    },

    {
        "query":
        "show devices connected in the last 24 hours",

        "expected":
        "select * from devices "
        "where last_connected >= now ( ) - interval 1 day ;"
    },

    {
        "query":
        "show devices connected in last day",

        "expected":
        "select * from devices "
        "where last_connected >= now ( ) - interval 1 day ;"
    },

    {
        "query":
        "show devices connected in last week",

        "expected":
        "select * from devices "
        "where last_connected >= now ( ) - interval 7 day ;"
    }
])


# ==========================================================
# MULTI CONDITION (20+)
# ==========================================================

for battery in [20, 40, 60, 80]:

    evaluation_set.append({

        "query":
        f"show active devices with battery above {battery}",

        "expected":
        f"select * from devices "
        f"where status = ' active ' "
        f"and battery > {battery} ;"
    })

    evaluation_set.append({

        "query":
        f"show online devices with battery above {battery}",

        "expected":
        f"select * from devices "
        f"where status = ' online ' "
        f"and battery > {battery} ;"
    })


# ==========================================================
# SHUFFLE
# ==========================================================

random.shuffle(
    evaluation_set
)

print(
    "Generated:",
    len(evaluation_set),
    "evaluation queries"
)


# ==========================================================
# SAVE
# ==========================================================

with open(
    r"data/evaluation_queries.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        evaluation_set,
        f,
        indent=4
    )

print(
    "Saved to data/evaluation_queries.json"
)