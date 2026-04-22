from llm.hf_model import generate
from core.global_memory import memory   # ✅ FIX

class ChatAgent:

    def respond(self, message):

        memory.add("user", message)

        history = memory.get_context()

        prompt = "Conversation:\n"

        for msg in history:
            prompt += f"{msg['role']}: {msg['content']}\n"

        prompt += "assistant:"

        response = generate(prompt)

        memory.add("assistant", response)

        return response