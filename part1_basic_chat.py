# setting up basic chatbot functionality with OpenAI's API
# This script initializes the OpenAI client, sets up a chat model, and tests the chat functionality.
import os
from openai import OpenAI

api_key = os.getenv("OPENAI_API_KEY") or os.getenv("TOGETHER_API_KEY")

client = OpenAI(api_key=api_key)

response = client.chat.completions.create(
    model="gpt-4.1-nano-2025-04-14", # or "meta-llama/Llama-3.3-70B-Instruct-Turbo-Free"
    messages=[
        {"role": "system", "content": "You are a fed up and sassy assistant who hates answering questions."},
        {"role": "user", "content": "What is the weather like today?"}
    ],
    temperature=0.7,
    max_tokens=100
)

reply = response.choices[0].message.content
print("Assistant:", reply)