class DecisionAgent:

    def decide(self, message: str):

        msg = message.lower()

        if "pdf" in msg or "document" in msg:
            return "rag"

        if "email" in msg:
            return "automation"

        if "open" in msg or "search" in msg:
            return "browser"
        
        if "play" in message.lower() or "song" in message.lower():
            return "music"

        return "chat"