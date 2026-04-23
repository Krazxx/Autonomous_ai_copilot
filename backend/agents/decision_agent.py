class DecisionAgent:

    def decide(self, message: str):
        msg = message.lower()

        # 🎵 MUSIC AUTOMATION
        if "play" in msg and "song" in msg:
            return "automation"

        # 📄 RAG
        if "pdf" in msg or "document" in msg:
            return "rag"

        return "chat"