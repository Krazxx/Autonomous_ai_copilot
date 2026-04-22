from groq import Groq
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate(prompt):

    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "user", "content": prompt}
        ],
        model="llama-3.1-8b-instant",   # ✅ UPDATED MODEL
        temperature=0.7,
        max_tokens=300
    )

    return chat_completion.choices[0].message.content