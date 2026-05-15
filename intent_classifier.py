import re

class IntentClassifier:
    def __init__(self, confidence_threshold=0.6):
        self.confidence_threshold = confidence_threshold
        self.intent_keywords = {
            "top_performers": ["top performer", "top performers", "highest", "best", "top ", "top\s*\d+"],
            "average_marks": ["average", "mean", "avg", "class average"],
            "count_students": ["how many", "count", "number of", "total students", "students count"],
            "filter_by_marks": ["above", "below", "greater than", "less than", "at least", "at most", "minimum", "maximum", "equal", "equals", "exactly"],
            "get_all_students": ["list all", "all students", "show students", "display students", "student list"],
        }

    def train(self):
        """No-op training step for compatibility with app startup."""
        return None

    def predict(self, text):
        text_lower = text.lower()

        # Direct pattern-based intent detection for higher accuracy on short queries.
        if re.search(r"\b(top performers?|highest|best|top\s*\d+)\b", text_lower):
            return "top_performers", 1.0, False, "Intent inferred as top performers."

        if re.search(r"\b(average|mean|avg|class average)\b", text_lower):
            return "average_marks", 1.0, False, "Intent inferred as average marks."

        if re.search(r"\b(how many|count of|number of|total students|students count)\b", text_lower):
            return "count_students", 1.0, False, "Intent inferred as count students."

        if re.search(r"\b(above|below|greater than|less than|at least|at most|minimum|maximum|equal to|equals|exactly)\b", text_lower):
            return "filter_by_marks", 1.0, False, "Intent inferred as filter by marks."

        if re.search(r"\b(list all|all students|show students|display students|student list)\b", text_lower):
            return "get_all_students", 1.0, False, "Intent inferred as get all students."

        # Fallback to keyword scoring only if no direct pattern matched.
        scores = {}
        for intent, keywords in self.intent_keywords.items():
            intent_score = 0
            for keyword in keywords:
                if re.search(re.escape(keyword), text_lower):
                    intent_score += 1
            scores[intent] = intent_score

        best_intent = max(scores, key=scores.get)
        best_score = scores[best_intent]
        confidence = min(1.0, best_score / 2.0) if best_score > 0 else 0.0

        if best_score == 0 or confidence < self.confidence_threshold:
            return "fallback", confidence, True, "The query was too vague for offline intent classification."

        return best_intent, confidence, False, "Intent inferred from keyword matching."
