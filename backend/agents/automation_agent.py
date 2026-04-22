

from workflows.engine import WorkflowEngine

class AutomationAgent:

    def __init__(self):
        self.engine = WorkflowEngine()

    def respond(self, message: str):

        msg = message.lower()

        # simple parsing (we improve later)
        if "email" in msg:

            task = {
                "type": "email",
                "to": "test@example.com",
                "subject": "Auto Email",
                "body": message
            }

            return self.engine.run(task)

        return "No automation matched"