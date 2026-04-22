from rag.retriever import retrieve_context
from llm.hf_model import generate
from core.global_memory import memory   # ✅ FIX

class RAGAgent:

    def respond(self, question):

        memory.add("user", question)

        context = retrieve_context(question)

        history = memory.get_context()

        history_text = ""
        for msg in history:
            history_text += f"{msg['role']}: {msg['content']}\n"

        prompt = f"""
You are an AI assistant.

Use BOTH:
1. Conversation history
2. Document context

Rules:
- If context is available → prioritize it
- If context is empty → answer normally

Conversation History:
{history_text}

Document Context:
{context}

User Question:
{question}

Answer:
"""

        response = generate(prompt)

        memory.add("assistant", response)

        return response