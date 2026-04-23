from workflows.engine import WorkflowEngine
import urllib.parse   # ✅ add this

class AutomationAgent:

    def __init__(self):
        self.engine = WorkflowEngine()

    def respond(self, message: str):

        msg = message.lower()

        # ✅ EMAIL
        if "email" in msg:

            task = {
                "type": "email",
                "to": "test@example.com",
                "subject": "Auto Email",
                "body": message
            }

            return self.engine.run(task)

        # ✅ MUSIC (ADD THIS BLOCK)
        if "play" in msg or "song" in msg or "music" in msg:

            query = message.replace("play", "").replace("song", "").strip()
            q = urllib.parse.quote_plus(query)

            return {
                "type": "music",
                "url": f"https://www.youtube.com/results?search_query={q}"
            }

        return "No automation matched"