import os
from openai import OpenAI

api_key = os.getenv("OPENAI_API_KEY") or os.getenv("TOGETHER_API_KEY")

client = OpenAI(api_key=api_key)
MODEL = "gpt-4.1-nano-2025-04-14" # or "meta-llama/Llama-3.3-70B-Instruct-Turbo-Free"
TEMPERATURE = 0.7
MAX_TOKENS = 100
SYSTEM_PROMPT = "You are a fed up and sassy assistant who hates answering questions."


def chat(user_input):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_input}
        ],
        temperature=TEMPERATURE,
        max_tokens=MAX_TOKENS
    )

    reply = response.choices[0].message.content
    return reply

print(chat("Hello! How are you?"))