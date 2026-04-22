from core.models import Conversation

class Memory:

    def add(self, role, content):
        Conversation.objects.create(role=role, content=content)

    def get_context(self, limit=5):
        chats = Conversation.objects.all().order_by("-created_at")[:limit]

        chats = list(chats)[::-1]  # reverse for correct order

        return [
            {"role": c.role, "content": c.content}
            for c in chats
        ]