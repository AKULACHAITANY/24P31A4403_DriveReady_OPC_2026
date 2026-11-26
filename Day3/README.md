# Day 3 – Building a Context-Aware Bakery Chatbot

## Overview

Day 3 focuses on building a more interactive and context-aware AI chatbot for Sweet Crumbs Home Bakery using LangChain and an LLM.

The implementation introduces prompt templates, conversation history, output parsing, automated CSV-based testing, and AI Agent creation.

## Technologies Used

- Python
- LangChain
- Groq LLM
- Google Colab
- CSV

## What I Implemented

### 1. Prompt Template Creation

Used `ChatPromptTemplate` to structure conversations between the user and the AI assistant.

Defined a system prompt containing:
- Bakery information and cake prices.
- Order notice requirements.
- Eggless cake availability.
- Rules for answering customer questions.
- Response formatting instructions.

### 2. Conversation History

Used `MessagesPlaceholder` to maintain previous conversation messages.

```python
history = []
```

Created an `ask()` function to:
- Accept user questions.
- Pass previous conversation history to the chain.
- Generate responses.
- Store user questions and AI answers for future interactions.

This allows the chatbot to remember conversational context.

### 3. Output Parsing

Used `StrOutputParser()` to convert the LLM response into a string.

```python
chain = prompt | llm | StrOutputParser()
```

This creates a processing pipeline connecting:
- Prompt Template
- LLM
- Output Parser

### 4. CSV-Based Automated Testing

Used Python's `csv` module to read test cases from a CSV file.

Created a `run_tests()` function that:
- Reads questions from the CSV file.
- Sends each question to the chatbot.
- Checks whether the expected keyword is present in the response.
- Displays PASS or FAIL for each test.
- Calculates the overall test pass percentage.

The CSV file contains:
- `question`
- `must_include`

### 5. LangChain Agent Creation

Used LangChain's `create_agent()` function to create an AI Agent.

Configured the agent with:
- Groq LLM
- System prompt
- Empty tools list (`tools=[]`)

Invoked the agent using a user message and retrieved the generated response.

## Key Learnings

- Understanding `ChatPromptTemplate`.
- Using `MessagesPlaceholder`.
- Maintaining conversation history.
- Building LLM chains using LCEL.
- Understanding `StrOutputParser`.
- Implementing CSV-based automated testing.
- Evaluating chatbot responses using expected keywords.
- Creating and invoking LangChain Agents.

## Project Structure

```text
Day3/
│
├── day3.py
├── day3csv.csv
└── README.md
```

## Outcome

Successfully implemented a context-aware bakery chatbot with conversation history and structured prompt handling.

Also explored automated response testing using CSV test cases and created a LangChain Agent using the configured LLM.

---

**Learning Journey:** Agentic AI – Day 3

**Project:** Sweet Crumbs Home Bakery Chatbot

**Author:** AKULACHAITANY
