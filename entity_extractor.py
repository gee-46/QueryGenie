import re

class EntityExtractor:
    def extract(self, text):
        text_lower = text.lower()
        entities = {"marks": None, "condition": None, "limit": None}

        # Detect a numerical limit for top performers or explicit limits.
        limit_match = re.search(r"\b(?:top|first|highest|show|display)\s+(\d+)\b", text_lower)
        if not limit_match:
            limit_match = re.search(r"\blimit\s+(\d+)\b", text_lower)
        if not limit_match:
            limit_match = re.search(r"\b(\d+)\s+(?:students|performers|results|records)\b", text_lower)

        if limit_match:
            entities["limit"] = int(limit_match.group(1))

        if re.search(r"\b(at least|minimum|greater than or equal to|>=)\b", text_lower):
            entities["condition"] = ">="
        elif re.search(r"\b(at most|maximum|less than or equal to|<=)\b", text_lower):
            entities["condition"] = "<="
        elif re.search(r"\b(above|greater than|more than)\b", text_lower):
            entities["condition"] = ">"
        elif re.search(r"\b(below|less than|under)\b", text_lower):
            entities["condition"] = "<"
        elif re.search(r"\b(equal to|equals|exactly|=)\b", text_lower):
            entities["condition"] = "="

        numeric_values = [int(num) for num in re.findall(r"\b(\d{1,3})\b", text_lower)]
        if numeric_values:
            if entities["condition"] is not None:
                entities["marks"] = numeric_values[0]
            elif entities["limit"] is not None and not any(cond in text_lower for cond in ["above", "below", "greater", "less", "minimum", "maximum", "equal", "exactly"]):
                pass
            elif any(word in text_lower for word in ["marks", "score", "grade"]):
                entities["marks"] = numeric_values[0]
                if entities["condition"] is None:
                    entities["condition"] = "="

        return entities
