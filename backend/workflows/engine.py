

from automation.email import send_email

class WorkflowEngine:

    def run(self, task: dict):

        task_type = task.get("type")

        if task_type == "email":
            return send_email(
                task.get("to"),
                task.get("subject"),
                task.get("body")
            )

        return "Unknown task"