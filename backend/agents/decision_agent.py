class DecisionAgent:
# trigger redeploy
    def decide(self, message: str):

        msg = message.lower()

        print("DECISION INPUT:", msg)  # debug

        # ✅ PRIORITY 1 → AUTOMATION
        if any(word in msg for word in ["play", "song", "music"]):
            return "automation"

        # ✅ PRIORITY 2 → RAG
        if any(word in msg for word in ["pdf", "document", "summarize"]):
            return "rag"

        # ✅ PRIORITY 3 → BROWSER
        if any(word in msg for word in ["search", "google"]):
            return "browser"

        return "chat"