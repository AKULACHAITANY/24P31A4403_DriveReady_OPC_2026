{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNyPzgSXnB+cBtYvTYfwIuu",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/AKULACHAITANY/24P31A4403_DriveReady_OPC_2026/blob/main/Day5/task.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "myxYdjwiA-PF",
        "outputId": "a450a453-2b14-4009-f147-1a39a4005c78"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "12 facts stored\n",
            "['A message on the cake is free, up to 20 letters.', \"Photo cakes and custom designs need 48 hours' notice.\"]\n"
          ]
        }
      ],
      "source": [
        "!pip install -q chromadb opentelemetry-api==1.45.2 opentelemetry-sdk==1.45.2 opentelemetry-exporter-otlp-common==0.66b2\n",
        "import chromadb\n",
        "\n",
        "FAQS = {\n",
        "    \"delivery\":     \"We deliver within 5 km of the bakery. Delivery is Rs 50, free for orders above Rs 1,000.\",\n",
        "    \"payment\":      \"We accept UPI and cash. Orders above Rs 1,000 need a 50% advance by UPI.\",\n",
        "    \"cancellation\": \"Cancellation is free up to 12 hours before pickup. After that, the advance is not refunded.\",\n",
        "    \"photo_cake\":   \"Photo cakes and custom designs need 48 hours' notice.\",\n",
        "    \"notice\":       \"Regular orders need 24 hours' notice.\",\n",
        "    \"eggless\":      \"All our cakes have eggless versions at the same price.\",\n",
        "    \"allergens\":    \"Plum cake contains nuts and dried fruit. Cupcakes and chocolate cake are nut-free.\",\n",
        "    \"storage\":      \"Keep cakes in the fridge and eat them within 3 days.\",\n",
        "    \"message\":      \"A message on the cake is free, up to 20 letters.\",\n",
        "    \"candles\":      \"Candles are free with every cake.\",\n",
        "    \"discounts\":    \"Bulk-order discounts need the owner's approval.\",\n",
        "    \"pickup\":       \"Pickup is during opening hours: Monday to Saturday 9 am to 8 pm, Sunday 10 am to 6 pm.\",\n",
        "}\n",
        "\n",
        "client = chromadb.Client()\n",
        "faq = client.get_or_create_collection(name=\"sweet_crumbs_faq\")\n",
        "faq.upsert(ids=list(FAQS.keys()), documents=list(FAQS.values()))   # upsert = add or update\n",
        "print(faq.count(), \"facts stored\")\n",
        "print(faq.query(query_texts=[\"Can you send the cake to my house?\"], n_results=2)[\"documents\"][0])"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from langchain.tools import tool"
      ],
      "metadata": {
        "id": "LFiygjbMBqgH"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "@tool\n",
        "def search_faq(question: str) -> str:\n",
        "    \"\"\"Search Sweet Crumbs' policies and FAQs: delivery, payment, cancellation,\n",
        "    photo cakes, allergens, storage, candles and messages on cakes.\n",
        "    Use for any question about rules or policies, not for prices or opening hours.\"\"\"\n",
        "    results = faq.query(query_texts=[question], n_results=3)\n",
        "    return \"\\n\".join(results[\"documents\"][0])"
      ],
      "metadata": {
        "id": "MyNuCAhJBTV1"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import os\n",
        "from google.colab import userdata\n",
        "from langchain_groq import ChatGroq\n",
        "\n",
        "os.environ[\"GROQ_API_KEY\"] = userdata.get(\"GROQ_API_KEY\")\n",
        "\n",
        "llm = ChatGroq(\n",
        "    model=\"openai/gpt-oss-20b\",\n",
        "    temperature=0.2,\n",
        "    max_retries=3\n",
        ")\n",
        "\n",
        "print(\"LLM initialized successfully!\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "o6UR1CNbEgtM",
        "outputId": "ae5b5711-d046-4377-d98b-c96a70dedb69"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "LLM initialized successfully!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from langchain.tools import tool\n",
        "\n",
        "@tool\n",
        "def get_price(item: str, qty: int = 1) -> str:\n",
        "    \"\"\"Get the total price in rupees for a menu item.\"\"\"\n",
        "\n",
        "    price = MENU.get(item.lower().strip())\n",
        "\n",
        "    if price is None:\n",
        "        return f\"{item} is not on the menu.\"\n",
        "\n",
        "    return f\"{qty} x {item} = Rs {price * qty}\""
      ],
      "metadata": {
        "id": "F6Rf3lT1E25t"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from langchain.tools import tool\n",
        "\n",
        "@tool\n",
        "def is_open(day: str) -> str:\n",
        "    \"\"\"Check bakery opening hours for a day of the week.\"\"\"\n",
        "\n",
        "    hours = HOURS.get(day.lower().strip())\n",
        "\n",
        "    if hours:\n",
        "        return f\"Open {hours} on {day}.\"\n",
        "\n",
        "    return f\"{day} is not a valid day of the week.\""
      ],
      "metadata": {
        "id": "vzaz6us3FCmS"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "HOURS = {\n",
        "    \"monday\": \"9 am to 8 pm\",\n",
        "    \"tuesday\": \"9 am to 8 pm\",\n",
        "    \"wednesday\": \"9 am to 8 pm\",\n",
        "    \"thursday\": \"9 am to 8 pm\",\n",
        "    \"friday\": \"9 am to 8 pm\",\n",
        "    \"saturday\": \"9 am to 8 pm\",\n",
        "    \"sunday\": \"10 am to 6 pm\"\n",
        "}"
      ],
      "metadata": {
        "id": "sHp1Jd6kFFzq"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from langchain.tools import tool\n",
        "\n",
        "@tool\n",
        "def log_order(\n",
        "    name: str,\n",
        "    item: str,\n",
        "    qty: int,\n",
        "    date: str,\n",
        "    eggless: bool\n",
        ") -> str:\n",
        "    \"\"\"Save a confirmed cake order to Google Sheets.\"\"\"\n",
        "\n",
        "    try:\n",
        "        order = Order(\n",
        "            name=name,\n",
        "            item=item.lower().strip(),\n",
        "            qty=qty,\n",
        "            date=date,\n",
        "            eggless=eggless\n",
        "        )\n",
        "\n",
        "    except Exception as e:\n",
        "        return f\"Could not save order: {e}\"\n",
        "\n",
        "    total = MENU[order.item] * order.qty\n",
        "\n",
        "    ws.append_row([\n",
        "        order.name,\n",
        "        order.item,\n",
        "        order.qty,\n",
        "        order.date,\n",
        "        \"yes\" if order.eggless else \"no\",\n",
        "        total\n",
        "    ])\n",
        "\n",
        "    return (\n",
        "        f\"Saved: {order.qty} x {order.item} \"\n",
        "        f\"for {order.name} on {order.date}, Rs {total}.\"\n",
        "    )"
      ],
      "metadata": {
        "id": "GiaM9a5xFP4d"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from langgraph.checkpoint.memory import InMemorySaver\n",
        "from langchain.agents import create_agent\n",
        "\n",
        "SYSTEM = \"\"\"ROLE:   You are the friendly assistant for Sweet Crumbs Home Bakery.\n",
        "RULES:  Use get_price for prices and is_open for timings; never guess them.\n",
        "        For any policy question, use search_faq and answer ONLY from what it returns.\n",
        "        If the answer isn't there, say \"I'll check with the owner.\"\n",
        "        Before log_order, make sure you have name, item, quantity and pickup date; ask if missing.\n",
        "FORMAT: Under 60 words, friendly, English or Telugu matching the customer.\"\"\"\n",
        "\n",
        "agent = create_agent(model=llm, tools=[get_price, is_open, log_order, search_faq],\n",
        "                     system_prompt=SYSTEM, checkpointer=InMemorySaver())\n",
        "\n",
        "def chat(thread_id: str, text: str) -> str:\n",
        "    config = {\"configurable\": {\"thread_id\": thread_id}}\n",
        "    try:\n",
        "        result = agent.invoke({\"messages\": [{\"role\": \"user\", \"content\": text}]}, config)\n",
        "        return result[\"messages\"][-1].content\n",
        "    except Exception as e:\n",
        "        print(\"Agent error:\", e)\n",
        "        return \"Sorry, I'm a little busy. Please try again in a minute.\"\n",
        "\n",
        "print(chat(\"ravi\", \"Hi, I'm Ravi. Do you deliver? My order is about Rs 1,300.\"))\n",
        "print(chat(\"ravi\", \"Does the plum cake have nuts?\"))\n",
        "print(chat(\"sravani\", \"Can I cancel tomorrow morning if I pick up tomorrow evening?\"))\n",
        "print(chat(\"ravi\", \"What's my name, and will I pay for delivery?\"))   # memory + RAG together"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "J7AUvlXkDaCF",
        "outputId": "5fa30f2a-e9a8-430a-b96e-a29b2be4b54c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Hi Ravi! Yes, we deliver within 5 km of the bakery. Delivery is Rs 50, but it’s free for orders above Rs 1,000. Just give us a 24‑hour notice. Let me know your address and pickup date, and we’ll get it ready!\n",
            "Yes, our plum cake contains nuts and dried fruit. If you need a nut‑free option, we can suggest cupcakes or chocolate cake instead. Let me know how I can help!\n",
            "Sure! You can cancel for free if you do it at least 12 hours before your pickup time. If it’s within 12 hours, the advance won’t be refunded. Let me know if you’d like to cancel.\n",
            "Your name is Ravi, and since your order is above Rs 1,000, delivery is free!\n"
          ]
        }
      ]
    }
  ]
}