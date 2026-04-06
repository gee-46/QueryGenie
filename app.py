from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import sqlite3
import pandas as pd
from google import genai

# ------------------ CONFIG ------------------ #
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

# ------------------ GEMINI RESPONSE ------------------ #
def get_gemini_response(question, prompt, schema):
    try:
        full_prompt = f"""
        Database schema:
        {schema}

        {prompt}

        Question:
        {question}
        """

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=full_prompt
        )

        return response.text.strip()

    except Exception as e:
        return f"Error: {e}"

# ------------------ FIX SQL ------------------ #
def fix_sql_query(bad_sql, error, schema):
    try:
        fix_prompt = f"""
        You are an SQL expert.

        Wrong SQL:
        {bad_sql}

        Error:
        {error}

        Schema:
        {schema}

        Fix it and return ONLY SQL.
        """

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=fix_prompt
        )

        return response.text.strip()

    except Exception as e:
        return f"Error: {e}"

# ------------------ EXECUTE SQL ------------------ #
def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()

    try:
        cur.execute(sql)
        rows = cur.fetchall()
        conn.close()
        return rows, None
    except Exception as e:
        conn.close()
        return None, str(e)

# ------------------ GET SCHEMA ------------------ #
def get_schema(db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()

    tables = ["STUDENT", "MARKS", "COURSES"]
    schema_info = []

    for table in tables:
        try:
            cur.execute(f"PRAGMA table_info({table})")
            cols = cur.fetchall()
            col_names = ", ".join([col[1] for col in cols])
            schema_info.append(f"{table}({col_names})")
        except:
            pass

    conn.close()
    return "\n".join(schema_info)

# ------------------ PROMPT ------------------ #
prompt = """
You are an expert SQL generator.
Convert the user question into a valid SQLite SQL query.
Return ONLY SQL.
"""

# ------------------ UI DESIGN ------------------ #
st.set_page_config(page_title="AI Query Assistant", layout="wide")

st.markdown("""
    <style>
    .main-title {
        text-align: center;
        font-size: 42px;
        font-weight: bold;
        color: #4CAF50;
    }
    .subtitle {
        text-align: center;
        font-size: 18px;
        color: grey;
        margin-bottom: 30px;
    }
    .card {
        background-color: #f9f9f9;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🤖 AI Database Query Assistant</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Ask questions in natural language and get instant SQL results</div>', unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    question = st.text_input("💬 Enter your question:")
    submit = st.button("🚀 Generate & Run Query")
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### 💡 Example Queries")
    st.write("- Show all students")
    st.write("- Students in Data Science class")
    st.write("- Students with marks > 80")
    st.markdown("</div>", unsafe_allow_html=True)

# ------------------ MAIN LOGIC ------------------ #
if submit and question:
    with st.spinner("Thinking..."):
        schema = get_schema("student.db")
        sql_query = get_gemini_response(question, prompt, schema)

    st.subheader("🧾 Generated SQL")
    st.code(sql_query, language="sql")

    result, error = read_sql_query(sql_query, "student.db")

    if error:
        st.warning("⚠️ Fixing query automatically...")

        fixed_query = fix_sql_query(sql_query, error, schema)
        st.code(fixed_query, language="sql")

        result, error = read_sql_query(fixed_query, "student.db")

    if error:
        st.error(f"❌ Error: {error}")
    else:
        st.success("✅ Query executed successfully")
        df = pd.DataFrame(result)
        st.dataframe(df, use_container_width=True)

# ------------------ FOOTER ------------------ #
st.markdown("""
<hr>
<div style='text-align: center; font-size: 16px;'>
    Built by GitHub ID <b>gee-46 (Gautam N Chipkar)</b>
</div>
""", unsafe_allow_html=True)
