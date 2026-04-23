from workflows.engine import WorkflowEngine
import urllib.parse

class AutomationAgent:

    def __init__(self):
        self.engine = WorkflowEngine()

    def respond(self, message: str):

        msg = message.lower()

        # 🎵 PLAY SONG FEATURE
        if "play" in msg and "song" in msg:
            query = message.replace("play song", "").strip()
            q = urllib.parse.quote_plus(query)

            return {
                "type": "music",
                "url": f"https://www.youtube.com/results?search_query={q}"
            }

        # EMAIL
        if "email" in msg:
            task = {
                "type": "email",
                "to": "test@example.com",
                "subject": "Auto Email",
                "body": message
            }
            return self.engine.run(task)

        return "No automation matched"