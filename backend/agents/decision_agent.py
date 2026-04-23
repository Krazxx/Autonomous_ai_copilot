class DecisionAgent:

    def decide(self, message: str):

        msg = message.lower()

        # ✅ automation triggers
        if "play" in msg or "song" in msg or "music" in msg:
            return "automation"

        if "search" in msg or "google" in msg:
            return "browser"

        if "pdf" in msg or "document" in msg or "summarize" in msg:
            return "rag"

        return "chat"