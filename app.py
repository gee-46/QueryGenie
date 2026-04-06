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
