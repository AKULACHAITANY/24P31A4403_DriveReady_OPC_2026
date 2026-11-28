# Day 4 – Building an AI-Powered Bakery Order Assistant 🍰

## 📌 Project Overview
On Day 4 of my Agentic AI learning journey, I built an AI-powered order assistant for **Sweet Crumbs Home Bakery** using LangChain and Groq.

The assistant interacts with customers, answers questions about bakery timings and cake prices, collects order details, and saves confirmed orders directly into Google Sheets.

## 🛠️ Technologies Used
- **Python** – Core programming language.
- **LangChain** – Building an AI agent and integrating tools.
- **Groq** – Providing LLM capabilities using `openai/gpt-oss-20b`.
- **Google Colab** – Development environment.
- **Google Sheets** – Storing customer orders.
- **gspread** – Connecting Python with Google Sheets.
- **Pydantic** – Validating structured order information.

## ⚙️ Features Implemented

### 1. LLM Configuration
- Installed LangChain, LangChain-Groq, and gspread.
- Configured the Groq API key securely using Google Colab Secrets.
- Initialized the ChatGroq model.

### 2. Google Sheets Integration
- Authenticated Google account access.
- Created a Google Spreadsheet named `Sweet Crumbs Orders`.
- Configured columns to store:
  - Customer Name
  - Cake Item
  - Quantity
  - Pickup Date
  - Eggless Preference
  - Total Price

### 3. Structured Order Validation
Used Pydantic's `BaseModel` and `Field` to define an Order schema.

Validated:
- Customer name
- Menu item
- Quantity (minimum 1)
- Pickup date
- Eggless preference

Used `Literal` to restrict cake selections to available menu items.

### 4. Agent Tools

Implemented three custom tools using LangChain's `@tool` decorator:

**get_price()**
- Retrieves cake prices from the menu.
- Calculates the total price based on quantity.

**is_open()**
- Checks bakery opening hours for a given weekday.

**log_order()**
- Validates order information.
- Calculates the total amount.
- Saves confirmed orders into Google Sheets.

### 5. AI Agent Creation
Used LangChain's `create_agent()` to create an AI agent with:
- Groq LLM
- Custom bakery tools
- System instructions

The system prompt defines the agent's role, responsibilities, and response format.

### 6. Conversation Memory
Implemented conversation history using a Python list.

The agent maintains previous messages, allowing it to understand follow-up questions and remember customer-provided details during the conversation.

## 🔄 Workflow

1. Customer sends a message.
2. AI agent understands the customer's request.
3. Agent selects the appropriate tool.
4. Tool retrieves prices, checks timings, or saves an order.
5. Confirmed order details are stored in Google Sheets.
6. Agent responds with the order summary and total price.

## 🧪 Sample Test Cases

**Test Case 1: Checking Bakery Timings**

Input:
`Are you open on Sunday?`

Expected:
The agent uses `is_open()` and returns Sunday opening hours.

**Test Case 2: Checking Cake Prices**

Input:
`How much are 2 chocolate cakes?`

Expected:
The agent uses `get_price()` and calculates the total.

**Test Case 3: Placing an Order**

Input:
`I'm Ravi. Please book 2 eggless chocolate cakes for 24 Dec.`

Expected:
- Extracts customer details.
- Validates the order.
- Calculates the total price.
- Saves the order in Google Sheets.
- Confirms the order to the customer.

## 📚 Key Learnings

- Integrating Groq LLM with LangChain.
- Creating custom tools using `@tool`.
- Building AI agents using `create_agent()`.
- Understanding structured data validation with Pydantic.
- Connecting Python applications with Google Sheets.
- Maintaining conversation history.
- Understanding how AI agents select and execute tools.

## 🚀 Day 4 Outcome

Successfully developed an AI-powered bakery order assistant that can interact with customers, answer questions, use custom tools, validate order details, and store customer orders in Google Sheets.

**Learning Journey:** Agentic AI – Day 4

#AgenticAI #LangChain #Python #Groq #AI #GoogleSheets #GenerativeAI #LearningInPublic
