stimport streamlit as st
import sqlite3
import pandas as pd

# Import NLP Pipeline modules
from intent_classifier import IntentClassifier
from entity_extractor import EntityExtractor
from sql_generator import SQLGenerator
from response_generator import ResponseGenerator
from speech_handler import listen_to_voice

# ------------------ NLP INITIALIZATION ------------------ #
@st.cache_resource
def load_nlp_pipeline():
    """Initializes and trains the offline classical NLP models on startup."""
    classifier = IntentClassifier(confidence_threshold=0.6)
    classifier.train()  
    extractor = EntityExtractor()
    sql_gen = SQLGenerator()
    response_gen = ResponseGenerator()
    return classifier, extractor, sql_gen, response_gen

classifier, extractor, sql_gen, response_gen = load_nlp_pipeline()
DB_NAME = "student.db"

# ------------------ DATABASE OPERATIONS ------------------ #
def read_sql_query(sql, db):
    try:
        conn = sqlite3.connect(db)
        df = pd.read_sql_query(sql, conn)
        conn.close()
        return df, None
    except Exception as e:
        if 'conn' in locals(): conn.close()
        return None, str(e)

# ------------------ UI DESIGN ------------------ #
st.set_page_config(page_title="Offline NLP SQL Assistant", layout="wide")

# Add missing style rules for UI and DataFrame fixes previously noticed in logs
st.markdown("""
    <style>
    .main-title { text-align: center; font-size: 40px; font-weight: bold; color: #4CAF50; }
    .subtitle { text-align: center; font-size: 18px; color: grey; margin-bottom: 20px; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #4CAF50; color: white; }
    .debug-box { background-color: #f0f2f6; color: #333; padding: 15px; border-radius: 10px; border-left: 5px solid #4CAF50; font-family: monospace; }
    .debug-warn { background-color: #fff3cd; color: #333; padding: 15px; border-radius: 10px; border-left: 5px solid #ffc107; font-family: monospace; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🤖 Offline NLP DB Assistant</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Classical NLP Pipeline with Voice Input</div>', unsafe_allow_html=True)

# Session State for Voice Input
if "transcribed_text" not in st.session_state:
    st.session_state["transcribed_text"] = ""
if "voice_success" not in st.session_state:
    st.session_state["voice_success"] = False

col1, col2 = st.columns([2, 1])

with col1:
    # Voice Trigger
    if st.button("🎤 Use Voice Input"):
        with st.spinner("🎙️ Listening... Speak now!"):
            success, result = listen_to_voice(timeout=5, phrase_time_limit=5)
            if success:
                st.session_state["transcribed_text"] = result
                st.session_state["query_input"] = result
                st.session_state["voice_success"] = True
                st.success("Processing speech...")
            else:
                st.session_state["voice_success"] = False
                st.error(f"Voice input failed: {result} Please type your query in the box below.")

    if st.session_state["voice_success"] and st.session_state["transcribed_text"]:
        st.info(f"**Recognized Speech:** {st.session_state['transcribed_text']}")

    # User Query Input Box
    question = st.text_input("💬 Ask a question about the students:", key="query_input")
    
    # User Confirmation Button
    submit = st.button("🚀 Run Query")
    
with col2:
    st.info("💡 **Try asking:**\n- List all students\n- Who are the top 3 performers?\n- Show students who got above 80\n- What is the class average?")

st.markdown("---")
show_debug = st.checkbox("🔍 Show NLP Debug Info")


