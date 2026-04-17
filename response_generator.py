import pandas as pd

class ResponseGenerator:
    def generate(self, intent, df):
        """
        Takes the executed dataframe result and the intent, generating a natural string.
        """
        if df is None or df.empty:
            return "No matching records found in the database."
            
        count = len(df)
        
        if intent == "get_all_students":
            return f"I found {count} students matching your request. Here are their records:"
            
        elif intent == "count_students":
            # the result is in the first row, first col
            total = int(df.iloc[0, 0])
