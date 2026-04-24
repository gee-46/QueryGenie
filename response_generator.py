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
             return f"There are a total of {total} students."
            
        elif intent == "top_performers":
            if count == 1:
                return f"Here is the top performer from the class:"
            else:
                return f"Here are the top {count} performers based on their marks:"
                
        elif intent == "average_marks":
            avg = float(df.iloc[0, 0])
            return f"The average mark of the students is {avg:.2f}."
            
        elif intent == "filter_by_marks":
            return f"I found {count} students who match your marks criteria."
            
        return f"Here are the {count} retrieved records:"
