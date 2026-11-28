# Day 5 – Building an AI Agent with Memory and RAG

## Project: Sweet Crumbs Home Bakery AI Assistant

### Overview
On Day 5, I enhanced my Sweet Crumbs Home Bakery AI Assistant by integrating **Memory and Retrieval-Augmented Generation (RAG)**.

The assistant can now remember previous conversations with customers and retrieve relevant bakery information from an FAQ knowledge base before answering policy-related questions.

### Technologies Used
- Python
- LangChain
- LangGraph
- Groq LLM
- Google Colab
- Google Sheets
- Pydantic

### Features Implemented

**1. AI Agent**
- Created an AI agent using LangChain's `create_agent()`.
- Connected the LLM with multiple custom tools.
- Added system instructions to guide the agent's behavior.

**2. Memory using LangGraph**
- Implemented `InMemorySaver()` as a checkpointer.
- Used customer-specific `thread_id` values to maintain conversation history.
- Enabled the assistant to remember details shared earlier in a conversation.

**3. RAG – FAQ Retrieval**
- Created a bakery FAQ knowledge base.
- Implemented a `search_faq` tool to retrieve relevant information.
- Instructed the agent to use retrieved FAQ information when answering policy-related questions.
- If the information is unavailable, the assistant responds that it will check with the owner instead of guessing.

**4. Tool Integration**
The agent uses four tools:

| Tool | Purpose |
|---|---|
| `get_price` | Retrieves cake prices |
| `is_open` | Checks bakery opening hours |
| `log_order` | Saves customer orders to Google Sheets |
| `search_faq` | Retrieves answers from the FAQ knowledge base |

**5. Google Sheets Integration**
- Stores customer order details.
- Records customer name, cake item, quantity, pickup date, eggless preference, and total price.

### Conversation Testing

Tested the assistant with multiple conversations:

- Asked about bakery delivery policies.
- Asked whether plum cake contains nuts.
- Asked about order cancellation policies.
- Checked whether the assistant could remember a customer's name from an earlier conversation.

### Key Learnings
- How to create an AI agent using LangChain.
- How conversation memory works with LangGraph.
- How to use `thread_id` to maintain separate customer conversations.
- How RAG helps an AI agent retrieve information from a knowledge base.
- How to connect multiple custom tools to a single AI agent.
- How to combine memory, RAG, and tool calling in one application.

### Day 5 Outcome
Successfully developed an AI bakery assistant that combines **LLM reasoning, tool calling, conversation memory, and FAQ retrieval**.

This makes the assistant more context-aware and helps it provide information based on the bakery's knowledge base rather than guessing.

---

**#AgenticAI #LangChain #LangGraph #RAG #AI #Python #Groq #GoogleColab #Day5**
