import json
import pandas as pd
import streamlit as st
import sys
sys.path.append("src")
from src.inference import query_to_sql
from src.sql_executor import execute_sql



# =====================================================
# Page Config
# =====================================================

st.set_page_config(
    page_title="IoTQueryGPT",
    page_icon="🤖",
    layout="wide"
)


# =====================================================
# Load Metrics
# =====================================================

with open(
    r"data/evaluation_report.json",
    "r",
    encoding="utf-8"
) as f:

    report = json.load(f)

# =====================================================
# Side bar
# =====================================================

with st.sidebar:

    st.title("IoTQueryGPT v2")

    st.metric(
        "Accuracy",
        f"{report['accuracy']}%"
    )

    st.metric(
        "Parameters",
        "4.9M"
    )

    st.metric(
        "Vocabulary",
        "283"
    )


# =====================================================
# Header
# =====================================================

st.title("🤖 IoTQueryGPT v2")

st.markdown(
    f"""
**Accuracy:** {report['accuracy']}%

Natural Language → SQL → SQLite
"""
)


# =====================================================
# Examples
# =====================================================

st.subheader("Example Queries")

examples = [

    "show active devices",

    "count devices by status",

    "show top 10 devices with highest battery",

    "show devices with battery below 30",

    "show locations where average battery exceeds 60"
]

st.subheader(
    "Example Queries"
)

for ex in examples:

    st.markdown(
        f"• {ex}"
    )

# =====================================================
# User Query
# =====================================================

query = st.text_input(
    "Enter IoT Query"
)


# =====================================================
# Generate
# =====================================================

if st.button("Generate SQL"):

    if query.strip():

        sql = query_to_sql(
            query
        )

        st.subheader(
            "Generated SQL"
        )

        st.text_area(
            "Copy SQL",
            sql,
            height=120
        )

        columns, rows = execute_sql(
            sql
        )

        st.subheader(
            "Query Results"
        )

        if columns is None:

            st.error(rows)

        else:

            df = pd.DataFrame(
                rows,
                columns=columns
            )

            st.dataframe(
                df,
                use_container_width=True
            )