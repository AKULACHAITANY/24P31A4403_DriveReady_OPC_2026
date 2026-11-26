# Day 2 – Introduction to AI Agents

## Overview

Day 2 focuses on understanding how to create an AI Agent using LangChain.

Unlike a basic LLM interaction, an AI Agent can be configured with a system prompt and tools to handle user requests.

The goal was to understand agent creation, model integration, and how an agent processes user queries.

## Technologies Used

- Python
- LangChain
- Groq LLM
- Google Colab

## What I Implemented

### 1. Agent Creation

Used LangChain's `create_agent()` function to create an AI Agent.

```python
from langchain.agents import create_agent

agent_order = create_agent(
    model=llm,
    tools=[],
    system_prompt=SYSTEM
)
```

### 2. System Prompt

Configured a system prompt to define the agent's role and behavior.

### 3. Agent Invocation

Passed a user query to the agent.

```python
result_order = agent_order.invoke({
    "messages": [
        {
            "role": "user",
            "content": "Do you make eggless cakes?"
        }
    ]
})
```

### 4. Understanding Agent Workflow

1. User submits a query.
2. The query is passed to the agent.
3. The agent processes the conversation using the configured LLM.
4. The model generates a response.
5. The response is returned to the user.

## Key Learnings

- Understanding AI Agents.
- Introduction to LangChain `create_agent()`.
- Configuring an agent with an LLM.
- Understanding system prompts.
- Passing messages using agent invocation.
- Understanding the difference between a basic LLM call and an agent.

## Tools Integration

The agent was initially created with an empty tools list (`tools=[]`).

Tool integration was kept for the upcoming implementation.

## Project Structure

```text
Day2/
│
├── day2.py
└── README.md
```

## Outcome

Successfully created a basic AI Agent using LangChain and Groq.

Learned how to configure an agent, provide instructions through a system prompt, and process user queries using agent invocation.

---

**Learning Journey:** Agentic AI – Day 2

**Author:** AKULACHAITANY
