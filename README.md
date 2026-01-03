# Bob - The Sarcastic Laptop Assistant 🖥️😄

A fun, helpful, and slightly sarcastic AI laptop assistant named **Bob**, built with **LangGraph**, **LangChain**, and **Google Gemini**.

Bob acts like a real desktop assistant: he can interact with your laptop (via tools), explain what he's doing in a clear and friendly way, and always adds a touch of humor and sarcasm.

## Features

- **Personality**: Helpful, funny, and just the right amount of sarcastic.
- **Tool Integration**: Uses custom tools for real laptop interactions (file system, web browsing, etc.).
- **Structured Workflow**: Enforces specific step-by-step processes (e.g., mandatory learning workflow using web search + opening sites).
- **Memory**: In-memory conversation persistence via `InMemorySaver`.
- **Clear Explanations**: Always summarizes actions after performing them.

## Project Status

This repository contains the **core setup and configuration** for Bob. The provided code initializes:

- Google Gemini model (`gemini-3-flash-preview`)
- System prompt defining Bob's personality and rules
- Tool integration
- Response formatting
- In-memory checkpointing

Full agent compilation and tool implementation are ready to be completed.

## Requirements

- Python 3.10+
- Google Gemini API key

### Install dependencies

```bash
pip install -r requirement.txt
