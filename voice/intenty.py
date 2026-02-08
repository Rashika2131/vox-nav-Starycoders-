class IntentParser:
    def parse(self, text):
        t = text.lower()

        if "analyze" in t:
            return "analyze"
        if "dry" in t and "bush" in t:
            return 2
        if "sand" in t:
            return 3
        if "rock" in t or "stone" in t:
            return 4
        if "tree" in t:
            return 6
        if "vegetation" in t or "grass" in t:
            return 1
        return None
