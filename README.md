# Build a Python Chatbot with the OpenAI API

This project walks through how to build a simple chatbot using the OpenAI API (or the Together API) in pure Python. Each file demonstrates one logical step in building up the final chatbot, from a single message to a full multi-turn conversation with memory and token management.

## Who This Is For

This project is great for:
- Anyone new to LLMs who wants to learn how to use an API instead of a chat interface
- Beginners learning how to structure Python scripts
- Developers looking to understand how chat history and token limits work

---

## Project Files

| File | Description |
|------|-------------|
| `part1_basic_chat.py` | Minimal working example: send one message and get a reply. |
| `part2_functional_chat.py` | Wraps the interaction in a function and uses variables for model and config. |
| `part3_chat_loop.py` | Adds a chat loop with memory (multi-turn conversations). |
| `part4_final.py` | Full chatbot with token budgeting using `tiktoken` to prevent runaway costs. |
| `oop_chatbot.py` | Full chatbot refactored to use OOP. |

---

## Requirements

You'll need to install a couple of packages:

```bash
pip install openai tiktoken
````

If you're using the Together API:

```bash
pip install together
```

---

## API Key Setup

Set your API key in your environment variables. You can use either OpenAI or Together:

```bash
# For OpenAI
export OPENAI_API_KEY="your-api-key"

# OR for Together
export TOGETHER_API_KEY="your-api-key"
```

> Never hardcode your API key in your script. Use environment variables to keep them secure.

---

## What You'll Learn

* How to connect to an LLM using the OpenAI or Together API
* How to format a `messages` list for conversation
* How to manage chat history to support memory
* What temperature and max tokens control
* How to estimate and manage token usage with `tiktoken`

---

## Model Notes

This project uses:

* `"gpt-4.1-nano-2025-04-14"` — A cheap, fast OpenAI-compatible model
* `"meta-llama/Llama-3.3-70B-Instruct-Turbo-Free"` — A free model on Together (slower but costs \$0)

You can swap either one in the `MODEL` variable.
