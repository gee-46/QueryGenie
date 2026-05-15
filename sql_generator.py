class SQLGenerator:
    def __init__(self):
        self.table_name = "STUDENT"

    def generate(self, intent, entities):
        """
        Maps an intent and extracted entities to a valid SQLite query.
        Returns the raw SQL string or None if fallback.
        """
        if intent == "fallback":
            return None
        # Base query components
        select_clause = f"SELECT * FROM {self.table_name}"
        where_clause = ""
        order_limit_clause = ""

        # Build WHERE clause based on entities
        if entities["marks"] is not None and entities["condition"] is not None:
            where_clause = f" WHERE MARKS {entities['condition']} {entities['marks']}"
        
        # Build ORDER/LIMIT based on intent and entities
        if intent == "top_performers":
            order_limit_clause = " ORDER BY MARKS DESC"
            limit = entities["limit"] if entities["limit"] else 5  # default to top 5 if not specified
            order_limit_clause += f" LIMIT {limit}"
        elif entities["limit"] is not None:
            # If the user specified a limit on a different query
            order_limit_clause += f" LIMIT {entities['limit']}"

        # Handle specific intents
        if intent == "get_all_students":
            query = select_clause + where_clause + order_limit_clause
        
        elif intent == "count_students":
            query = f"SELECT COUNT(*) as Student_Count FROM {self.table_name}" + where_clause
            
        elif intent == "top_performers":
            query = select_clause + where_clause + order_limit_clause
            
        elif intent == "average_marks":
            query = f"SELECT AVG(MARKS) as Average_Marks FROM {self.table_name}" + where_clause
            
        elif intent == "filter_by_marks":
            query = select_clause + where_clause + order_limit_clause
        else:
            return None

        return query + ";"
