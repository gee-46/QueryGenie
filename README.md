# 🚀 QueryGenie — Intelligent Text-to-SQL Engine

An advanced NLP-powered system that converts natural language queries into executable SQL using Large Language Models (LLMs), with built-in schema awareness and automatic error correction.

---

## 📌 Overview

QueryGenie allows users to interact with databases using plain English instead of writing SQL queries manually. It leverages modern NLP techniques and LLM capabilities to understand user intent, generate SQL queries, execute them, and return structured results.

This project demonstrates how natural language interfaces can simplify database interactions and improve accessibility for non-technical users.

---

## ✨ Key Features

### 🔍 Natural Language to SQL

* Converts user queries like:

  * *“Show students in Data Science class”*
  * into valid SQL queries automatically.

---

### 🧠 Schema-Aware Query Generation

* Dynamically reads database schema
* Ensures generated queries match actual table structure
* Reduces hallucinations and errors

---

### 🔁 Automatic SQL Error Correction

* Detects SQL execution failures
* Uses LLM to refine and fix incorrect queries
* Improves robustness and reliability

---

### 📊 Interactive UI (Streamlit)

* Clean and responsive interface
* Displays:

  * Generated SQL
  * Query results in table format
* Provides user-friendly interaction

---

### ⚡ Multi-Table Support

* Supports queries across:

  * `STUDENT`
  * `MARKS`
  * `COURSES`
* Handles JOIN operations automatically

---

## 🧠 NLP Concepts Implemented

This project is not just an API wrapper — it applies real NLP concepts:

* **Natural Language Understanding (NLU)**
  Interpreting user intent from free-text input

* **Semantic Parsing**
  Converting natural language → structured SQL queries

* **Prompt Engineering**
  Designing structured prompts for accurate LLM output

* **Context Injection (Schema Awareness)**
  Providing database schema to guide model reasoning

* **Iterative Refinement**
  Using error feedback to improve generated queries

---

## 🛠️ Tech Stack

| Component     | Technology Used   |
| ------------- | ----------------- |
| Language      | Python            |
| UI Framework  | Streamlit         |
| Database      | SQLite            |
| LLM Backend   | Google Gemini API |
| Data Handling | Pandas            |
| Environment   | python-dotenv     |

---

## 📂 Project Structure

```bash
QueryGenie/
│
├── app.py              # Main Streamlit application
├── sql.py              # Database utilities (if used)
├── student.db          # Sample SQLite database
├── requirements.txt    # Dependencies
├── .env                # API key (NOT included in repo)
├── README.md           # Project documentation
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/querygenie.git
cd querygenie
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Configure API Key

Create a `.env` file in the root directory:

```
GOOGLE_API_KEY=your_api_key_here
```

⚠️ Note: Do NOT upload `.env` to GitHub

---

### 4️⃣ Run the Application

```bash
streamlit run app.py
```

---

## 💡 Example Queries

Try asking:

* Show all students
* List students in Data Science class
* Show students with marks greater than 80
* Display student names along with their marks

---

## 🔄 System Workflow

1. User inputs a natural language query
2. Schema is extracted from the database
3. Prompt + schema + query → sent to LLM
4. SQL query is generated
5. Query is executed on SQLite
6. If error occurs → auto-correction triggered
7. Final result displayed to user

---

## 🎯 Use Cases

* Educational tools for learning SQL
* Natural language database querying
* Business analytics without SQL knowledge
* Rapid data exploration

---

## ⚠️ Limitations

* Dependent on LLM API availability and quota
* Performance may vary based on prompt quality
* Limited to predefined schema (can be extended)

---

## 🚀 Future Improvements

* Chat-style conversational interface
* Support for PostgreSQL / MySQL
* Query explanation in natural language
* Visualization (charts/graphs)
* Offline fallback models

---

## 👨‍💻 Author

**Gautam N Chipkar**
GitHub: [gee-46](https://github.com/gee-46)

---

## ⭐ Support

If you found this project useful:

* ⭐ Star the repository
* 🍴 Fork it
* 💡 Use it in your own projects

---

## 📜 License

This project is open-source and available under the MIT License.
