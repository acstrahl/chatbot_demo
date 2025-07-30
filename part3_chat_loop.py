# adding a chat loop to interact with the assistant

import os
from openai import OpenAI

api_key = os.getenv("OPENAI_API_KEY") or os.getenv("TOGETHER_API_KEY")

client = OpenAI(api_key=api_key)
MODEL = "gpt-4.1-nano-2025-04-14" # or "meta-llama/Llama-3.3-70B-Instruct-Turbo-Free"
TEMPERATURE = 0.7
MAX_TOKENS = 100
TOKEN_BUDGET = 1000
SYSTEM_PROMPT = "You are a fed up and sassy assistant who hates answering questions."

messages = [{"role": "system", "content": SYSTEM_PROMPT}]

def chat(user_input):
    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=TEMPERATURE,
        max_tokens=MAX_TOKENS
    )

    reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})

    return reply

while True:
    user_input = input("You: ")
    if user_input.strip().lower() in {"exit", "quit"}:
        break
    answer = chat(user_input)
    print("Assistant:", answer)