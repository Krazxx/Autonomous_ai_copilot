class DecisionAgent:

    def decide(self, message: str):
        msg = message.lower()

        if "play" in msg and "song" in msg:
            return "automation"

        if "pdf" in msg or "document" in msg:
            return "rag"

        return "chat"