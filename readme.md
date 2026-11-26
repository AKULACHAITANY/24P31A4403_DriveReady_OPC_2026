#day2 🍰 Sweet Crumbs Home Bakery – AI Chatbot

An AI-powered customer support chatbot built using Python and Groq LLM. It helps customers explore the bakery menu, check cake prices, calculate order totals, and get information about eggless cakes.

## 🚀 Features

- **AI-Powered Conversations:** Uses Groq LLM (`openai/gpt-oss-20b`) to interact with customers.
- **Menu Information:** Provides available cakes and their prices.
- **Price Calculation:** Uses Python function calling to calculate the total price based on item and quantity.
- **Conversation Memory:** Maintains recent conversation history to remember customer details and orders during the chat.
- **Eggless Cake Information:** Informs customers about eggless cake availability.
- **Order Guidelines:** Informs customers that orders require 24 hours' notice.
- **Error Handling:** Handles API authentication, rate-limit, and connection errors.
- **Telugu and English Support:** Responds according to the customer's language.

## 🛠️ Technologies Used

- Python
- Groq API
- OpenAI-compatible Chat Completions API
- JSON
- Python Decorators
- Function Calling

## 🍰 Bakery Menu

| Item | Price |
|---|---:|
| Plum Cake | ₹500 |
| Chocolate Cake | ₹650 |
| Cupcake | ₹80 |

*All cakes are available in eggless versions.*

## 📁 Project Structure

```text
Sweet-Crumbs-AI-Chatbot/
│
├── bakery.py
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd Sweet-Crumbs-AI-Chatbot
```

### 2. Install dependencies

```bash
pip install groq
```

### 3. Get your Groq API Key

Visit [Groq Console](https://console.groq.com/keys) and generate an API key.

### 4. Configure API Key

Set your API key as an environment variable.

**Windows PowerShell:**

```powershell
$env:GROQ_API_KEY="your_api_key"
```

### 5. Run the chatbot

```bash
python bakery.py
```

The program will securely request your API key if using the interactive `getpass` version of the code.

## 💬 Sample Interaction

```text
Welcome to Sweet Crumbs Home Bakery!

You: What cakes are available?

Bot: We have plum cake for ₹500,
chocolate cake for ₹650, and cupcakes for ₹80!

You: What is the price of 6 cupcakes?

Bot: 6 cupcakes will cost ₹480.

You: Do you have eggless cakes?

Bot: Yes! All our cakes are available
in eggless versions.

You: bye

Bot: Thank you for visiting Sweet Crumbs!
```

## 🧠 Key Concepts Implemented

1. Large Language Model (LLM) Integration
2. Prompt Engineering
3. Python Function Calling
4. Conversation History Management
5. Decorators and Logging
6. Exception Handling
7. API Integration

## 🔮 Future Improvements

- Store customer orders using a database.
- Add an order placement feature.
- Integrate WhatsApp customer support.
- Add order confirmation and notifications.
- Build a web-based chatbot interface.
- Add a bakery order management dashboard.

## 👩‍💻 Author

**Chaitanya Akula**

## 📌 Project Status

Completed – Basic AI Bakery Chatbot with LLM integration and function calling.

---

⭐ If you find this project interesting, feel free to explore and contribute!
