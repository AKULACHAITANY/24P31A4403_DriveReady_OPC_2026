# Day 6 – Building Multiple Specialized AI Agents

## Project: Sweet Crumbs Home Bakery AI Assistant

### Overview
On Day 6, I explored how to create multiple specialized AI agents using LangChain.

Instead of making one agent handle every task, I created two separate agents: one for answering customer questions and another for handling cake orders.

### Technologies Used
- Python
- LangChain
- Groq LLM
- Google Colab
- Google Sheets

### Features Implemented

**1. FAQ Agent**

Created an agent dedicated to answering customer questions.

Responsibilities:
- Answer bakery-related questions.
- Retrieve policy information using the `search_faq` tool.
- Check cake prices using `get_price`.
- Check bakery timings using `is_open`.
- Avoid guessing when information is unavailable.

**2. Order Agent**

Created a separate agent for handling customer orders.

Responsibilities:
- Collect customer details.
- Identify the cake item and quantity.
- Ask for missing order information.
- Calculate the order total using `get_price`.
- Save orders using `log_order`.
- Read the order details back to the customer after saving.

**3. Separate System Prompts**

Created individual system prompts:

- `FAQ_PROMPT` – Defines the FAQ agent's responsibilities and rules.
- `ORDER_PROMPT` – Defines the order agent's responsibilities and rules.

**4. Agent Creation**

Used LangChain's `create_agent()` to create both agents independently.

```python
faq_agent = create_agent(
    model=llm,
    tools=[search_faq, get_price, is_open],
    system_prompt=FAQ_PROMPT
)

order_agent = create_agent(
    model=llm,
    tools=[get_price, log_order],
    system_prompt=ORDER_PROMPT
)
```

### Key Learnings
- How to create multiple AI agents.
- How to assign different responsibilities to different agents.
- How system prompts control agent behavior.
- How to assign specific tools to individual agents.
- How to separate customer support from order management.
- How specialized agents can make an AI application more organized and modular.

### Day 6 Outcome
Successfully created two specialized AI agents for Sweet Crumbs Home Bakery:

