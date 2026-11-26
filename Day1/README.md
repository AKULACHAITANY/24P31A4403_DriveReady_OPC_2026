# Day 1 – Introduction to Agentic AI

## Overview
Day 1 focuses on understanding the fundamentals of building an AI-powered chatbot using Groq and LangChain.

The goal was to configure an LLM, send user questions to the model, and retrieve AI-generated responses.

## Technologies Used
- Python
- Groq – Large Language Model (LLM) provider
- LangChain – Framework for interacting with language models
- Google Colab – Development environment

## What I Implemented

### 1. LLM Configuration
- Configured the Groq LLM.
- Established a connection between Python and the language model.
- Understood how an LLM processes user prompts.

### 2. Chatbot Function
Created an `ask(question)` function to interact with the model.

```python
def ask(question):
    response = model.invoke(question)
    return response.content
```

### 3. Understanding the Workflow

1. User enters a question.
2. The question is passed to the `ask()` function.
3. `model.invoke()` sends the question to the LLM.
4. The model generates a response.
5. `response.content` extracts the text.
6. The chatbot returns the answer.

## Key Learnings
- Understanding Large Language Models (LLMs).
- Introduction to Groq.
- Understanding LangChain.
- Configuring and invoking an LLM.
- Creating a basic chatbot function.
- Understanding the request-response workflow.

## Project Structure

```text
Day1/
│
├── day1.py
└── README.md
```

## Outcome

Successfully explored the fundamentals of LLM integration and implemented a basic question-answering chatbot using Groq and LangChain.

This implementation serves as the foundation for learning more advanced Agentic AI concepts in the upcoming days.

---

**Learning Journey:** Agentic AI – Day 1  
**Author:** AKULACHAITANY
