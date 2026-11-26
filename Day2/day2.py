{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNf2Nv0gCWKzgGKGFnwf1qv",
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
        "<a href=\"https://colab.research.google.com/github/AKULACHAITANY/24P31A4403_DriveReady_OPC_2026/blob/main/Day2/day2.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "yY7NanQUWBxs",
        "outputId": "1a8b22d1-66d9-4f69-de9a-a060cd58c32c"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting groq\n",
            "  Downloading groq-1.7.0-py3-none-any.whl.metadata (16 kB)\n",
            "Requirement already satisfied: anyio<5,>=3.5.0 in /usr/local/lib/python3.13/dist-packages (from groq) (4.16.0)\n",
            "Requirement already satisfied: distro<2,>=1.7.0 in /usr/local/lib/python3.13/dist-packages (from groq) (1.9.0)\n",
            "Requirement already satisfied: httpx<1,>=0.23.0 in /usr/local/lib/python3.13/dist-packages (from groq) (0.28.1)\n",
            "Requirement already satisfied: pydantic<3,>=1.9.0 in /usr/local/lib/python3.13/dist-packages (from groq) (2.14.2)\n",
            "Requirement already satisfied: sniffio in /usr/local/lib/python3.13/dist-packages (from groq) (1.3.1)\n",
            "Requirement already satisfied: typing-extensions<5,>=4.14 in /usr/local/lib/python3.13/dist-packages (from groq) (4.16.0)\n",
            "Requirement already satisfied: idna>=2.8 in /usr/local/lib/python3.13/dist-packages (from anyio<5,>=3.5.0->groq) (3.20)\n",
            "Requirement already satisfied: certifi in /usr/local/lib/python3.13/dist-packages (from httpx<1,>=0.23.0->groq) (2026.10.23)\n",
            "Requirement already satisfied: httpcore==1.* in /usr/local/lib/python3.13/dist-packages (from httpx<1,>=0.23.0->groq) (1.0.9)\n",
            "Requirement already satisfied: h11>=0.16 in /usr/local/lib/python3.13/dist-packages (from httpcore==1.*->httpx<1,>=0.23.0->groq) (0.16.0)\n",
            "Requirement already satisfied: annotated-types>=0.6.0 in /usr/local/lib/python3.13/dist-packages (from pydantic<3,>=1.9.0->groq) (0.8.0)\n",
            "Requirement already satisfied: pydantic-core==2.50.2 in /usr/local/lib/python3.13/dist-packages (from pydantic<3,>=1.9.0->groq) (2.50.2)\n",
            "Requirement already satisfied: typing-inspection>=0.4.4 in /usr/local/lib/python3.13/dist-packages (from pydantic<3,>=1.9.0->groq) (0.4.4)\n",
            "Downloading groq-1.7.0-py3-none-any.whl (143 kB)\n",
            "Installing collected packages: groq\n",
            "Successfully installed groq-1.7.0\n"
          ]
        }
      ],
      "source": [
        "!pip install groq"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from groq import Groq\n",
        "from groq import RateLimitError, APIConnectionError\n",
        "\n",
        "print(\"Groq installed successfully!\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "L2iaUNb5XWl4",
        "outputId": "645c4a7d-1aa1-47e5-fa61-0b1f292f70ab"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Groq installed successfully!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import os\n",
        "from getpass import getpass\n",
        "\n",
        "os.environ[\"sweetcrumbs\"] = getpass(\"Enter your NEW Groq API key: \")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "MmViqfL6Xaux",
        "outputId": "1def1e46-a258-42ea-9c7f-633be3fd8b85"
      },
      "execution_count": null,
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Enter your NEW Groq API key: ··········\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from groq import Groq\n",
        "\n",
        "client = Groq(\n",
        "    api_key=os.environ[\"GROQ_API_KEY\"]\n",
        ")\n",
        "\n",
        "print(\"Groq client initialized successfully!\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "msfPmZHZYAZ_",
        "outputId": "d3957255-6c16-445d-ff9b-5c2b9b483e57"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Groq client initialized successfully!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "response = client.chat.completions.create(\n",
        "    model=\"openai/gpt-oss-20b\",\n",
        "    messages=[\n",
        "        {\"role\": \"user\", \"content\": \"Say hello!\"}\n",
        "    ]\n",
        ")\n",
        "\n",
        "print(response.choices[0].message.content)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Nsw47oauYGAE",
        "outputId": "2483ae16-6fcf-4baa-ef3d-302a2e5cb02c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Hello! 👋\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "import os\n",
        "import json\n",
        "import functools\n",
        "from getpass import getpass\n",
        "\n",
        "from groq import (\n",
        "    Groq,\n",
        "    RateLimitError,\n",
        "    APIConnectionError,\n",
        "    AuthenticationError\n",
        ")\n",
        "\n",
        "# ==========================================\n",
        "# 1. API CONFIGURATION\n",
        "# ==========================================\n",
        "\n",
        "# Enter your Groq API key securely\n",
        "api_key = getpass(\"Enter your Groq API key: \").strip()\n",
        "\n",
        "client = Groq(api_key=api_key)\n",
        "\n",
        "MODEL = \"openai/gpt-oss-20b\"\n",
        "\n",
        "\n",
        "# ==========================================\n",
        "# 2. BAKERY MENU\n",
        "# ==========================================\n",
        "\n",
        "MENU = {\n",
        "    \"plum cake\": 500,\n",
        "    \"chocolate cake\": 650,\n",
        "    \"cupcake\": 80\n",
        "}\n",
        "\n",
        "\n",
        "# ==========================================\n",
        "# 3. SYSTEM PROMPT\n",
        "# ==========================================\n",
        "\n",
        "SYSTEM = f\"\"\"\n",
        "ROLE:\n",
        "You are a friendly AI assistant for Sweet Crumbs Home Bakery.\n",
        "\n",
        "FACTS:\n",
        "Menu with prices in rupees:\n",
        "{json.dumps(MENU)}\n",
        "\n",
        "- Orders require 24 hours' notice.\n",
        "- All cakes have eggless versions.\n",
        "\n",
        "RULES:\n",
        "1. Be friendly and helpful.\n",
        "2. Remember the customer's name and order during the conversation.\n",
        "3. Never invent menu items or prices.\n",
        "4. Use the price calculation tool when customers ask for\n",
        "   the total price.\n",
        "5. Never promise a delivery time.\n",
        "6. If information is unavailable, say:\n",
        "   \"I'll check with the owner.\"\n",
        "7. Respond in English or Telugu according to the customer.\n",
        "8. Keep responses under 50 words.\n",
        "\"\"\"\n",
        "\n",
        "\n",
        "# ==========================================\n",
        "# 4. LOGGING DECORATOR\n",
        "# ==========================================\n",
        "\n",
        "def log_call(func):\n",
        "\n",
        "    @functools.wraps(func)\n",
        "    def wrapper(*args, **kwargs):\n",
        "\n",
        "        result = func(*args, **kwargs)\n",
        "\n",
        "        print(f\"[LOG] {func.__name__} -> {result}\")\n",
        "\n",
        "        return result\n",
        "\n",
        "    return wrapper\n",
        "\n",
        "\n",
        "# ==========================================\n",
        "# 5. PRICE CALCULATION FUNCTION\n",
        "# ==========================================\n",
        "\n",
        "@log_call\n",
        "def get_price(item: str, qty: int = 1) -> dict:\n",
        "\n",
        "    item = item.lower().strip()\n",
        "\n",
        "    if item not in MENU:\n",
        "        return {\n",
        "            \"success\": False,\n",
        "            \"message\": \"Item not available in menu.\"\n",
        "        }\n",
        "\n",
        "    if not isinstance(qty, int) or isinstance(qty, bool) or qty < 1:\n",
        "        return {\n",
        "            \"success\": False,\n",
        "            \"message\": \"Quantity must be a positive integer.\"\n",
        "        }\n",
        "\n",
        "    total = MENU[item] * qty\n",
        "\n",
        "    return {\n",
        "        \"success\": True,\n",
        "        \"item\": item,\n",
        "        \"quantity\": qty,\n",
        "        \"unit_price\": MENU[item],\n",
        "        \"total_price\": total\n",
        "    }\n",
        "\n",
        "\n",
        "# ==========================================\n",
        "# 6. FUNCTION CALLING / TOOL DEFINITION\n",
        "# ==========================================\n",
        "\n",
        "tools = [\n",
        "    {\n",
        "        \"type\": \"function\",\n",
        "        \"function\": {\n",
        "            \"name\": \"get_price\",\n",
        "            \"description\": \"Calculate the total price of bakery items.\",\n",
        "            \"parameters\": {\n",
        "                \"type\": \"object\",\n",
        "                \"properties\": {\n",
        "                    \"item\": {\n",
        "                        \"type\": \"string\",\n",
        "                        \"enum\": list(MENU.keys())\n",
        "                    },\n",
        "                    \"qty\": {\n",
        "                        \"type\": \"integer\",\n",
        "                        \"description\": \"Number of items\"\n",
        "                    }\n",
        "                },\n",
        "                \"required\": [\"item\", \"qty\"],\n",
        "                \"additionalProperties\": False\n",
        "            }\n",
        "        }\n",
        "    }\n",
        "]\n",
        "\n",
        "\n",
        "# ==========================================\n",
        "# 7. CONVERSATION HISTORY\n",
        "# ==========================================\n",
        "\n",
        "history = [\n",
        "    {\n",
        "        \"role\": \"system\",\n",
        "        \"content\": SYSTEM\n",
        "    }\n",
        "]\n",
        "\n",
        "MAX_TURNS = 8\n",
        "\n",
        "\n",
        "def trim_history():\n",
        "\n",
        "    # Keep the latest 8 complete user conversations.\n",
        "    messages = history[1:]\n",
        "\n",
        "    user_positions = [\n",
        "        i for i, msg in enumerate(messages)\n",
        "        if msg[\"role\"] == \"user\"\n",
        "    ]\n",
        "\n",
        "    if len(user_positions) > MAX_TURNS:\n",
        "\n",
        "        start = user_positions[-MAX_TURNS]\n",
        "\n",
        "        history[:] = [history[0]] + messages[start:]\n",
        "\n",
        "\n",
        "# ==========================================\n",
        "# 8. CHAT FUNCTION\n",
        "# ==========================================\n",
        "\n",
        "def chat(user_text: str) -> str:\n",
        "\n",
        "    history.append({\n",
        "        \"role\": \"user\",\n",
        "        \"content\": user_text\n",
        "    })\n",
        "\n",
        "    try:\n",
        "\n",
        "        messages = history.copy()\n",
        "\n",
        "        response = client.chat.completions.create(\n",
        "            model=MODEL,\n",
        "            messages=messages,\n",
        "            tools=tools,\n",
        "            tool_choice=\"auto\",\n",
        "            temperature=0.3\n",
        "        )\n",
        "\n",
        "        message = response.choices[0].message\n",
        "\n",
        "        # Handle function calls\n",
        "        tool_rounds = 0\n",
        "        MAX_TOOL_ROUNDS = 5\n",
        "\n",
        "        while message.tool_calls:\n",
        "\n",
        "            tool_rounds += 1\n",
        "\n",
        "            if tool_rounds > MAX_TOOL_ROUNDS:\n",
        "                reply = \"Sorry, I couldn't complete that request.\"\n",
        "                history.append({\n",
        "                    \"role\": \"assistant\",\n",
        "                    \"content\": reply\n",
        "                })\n",
        "                trim_history()\n",
        "                return reply\n",
        "\n",
        "            # Save assistant tool-call message\n",
        "            history.append(\n",
        "                message.model_dump(exclude_none=True)\n",
        "            )\n",
        "\n",
        "            # Execute requested functions\n",
        "            for tool_call in message.tool_calls:\n",
        "\n",
        "                function_name = tool_call.function.name\n",
        "\n",
        "                arguments = json.loads(\n",
        "                    tool_call.function.arguments\n",
        "                )\n",
        "\n",
        "                if function_name == \"get_price\":\n",
        "\n",
        "                    result = get_price(**arguments)\n",
        "\n",
        "                else:\n",
        "\n",
        "                    result = {\n",
        "                        \"success\": False,\n",
        "                        \"message\": \"Unknown function.\"\n",
        "                    }\n",
        "\n",
        "                # Send function result back to LLM\n",
        "                history.append({\n",
        "                    \"role\": \"tool\",\n",
        "                    \"tool_call_id\": tool_call.id,\n",
        "                    \"content\": json.dumps(result)\n",
        "                })\n",
        "\n",
        "            # Ask the LLM to generate the final answer\n",
        "            response = client.chat.completions.create(\n",
        "                model=MODEL,\n",
        "                messages=history.copy(),\n",
        "                tools=tools,\n",
        "                tool_choice=\"auto\",\n",
        "                temperature=0.3\n",
        "            )\n",
        "\n",
        "            message = response.choices[0].message\n",
        "\n",
        "        reply = message.content or \"I'll check with the owner.\"\n",
        "\n",
        "    except AuthenticationError:\n",
        "\n",
        "        reply = \"Invalid API key. Please check your Groq API key.\"\n",
        "\n",
        "    except RateLimitError:\n",
        "\n",
        "        reply = \"We're a little busy. Please try again in a minute.\"\n",
        "\n",
        "    except APIConnectionError:\n",
        "\n",
        "        reply = \"I can't reach the server right now. Please try again shortly.\"\n",
        "\n",
        "    except (ValueError, TypeError, KeyError, json.JSONDecodeError):\n",
        "\n",
        "        reply = \"Sorry, something went wrong. Please try again.\"\n",
        "\n",
        "    history.append({\n",
        "        \"role\": \"assistant\",\n",
        "        \"content\": reply\n",
        "    })\n",
        "\n",
        "    trim_history()\n",
        "\n",
        "    return reply\n",
        "\n",
        "\n",
        "# ==========================================\n",
        "# 9. RUN THE CHATBOT\n",
        "# ==========================================\n",
        "\n",
        "print(\"=\" * 45)\n",
        "print(\"Welcome to Sweet Crumbs Home Bakery!\")\n",
        "print(\"=\" * 45)\n",
        "\n",
        "print(\"Type 'bye' to exit.\\n\")\n",
        "\n",
        "while True:\n",
        "\n",
        "    user_text = input(\"You: \").strip()\n",
        "\n",
        "    if user_text.lower() in (\"bye\", \"exit\", \"quit\"):\n",
        "\n",
        "        print(\"\\nBot: Thank you for visiting Sweet Crumbs!\")\n",
        "        break\n",
        "\n",
        "    if not user_text:\n",
        "        continue\n",
        "\n",
        "    response = chat(user_text)\n",
        "\n",
        "    print(\"Bot:\", response)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "n23mvJReaneP",
        "outputId": "a2a01afe-057a-424c-bb36-d9897b282dfd"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter your Groq API key: ··········\n",
            "=============================================\n",
            "Welcome to Sweet Crumbs Home Bakery!\n",
            "=============================================\n",
            "Type 'bye' to exit.\n",
            "\n",
            "You: do you have chocolate cakes available\n",
            "Bot: Yes, we have chocolate cakes available! How many would you like to order?\n",
            "You: do u have eggless versions\n",
            "Bot: Yes, all our cakes—including chocolate cake—are available in eggless versions.\n",
            "You: can u understand telugu\n",
            "Bot: Yes, I can understand Telugu. How can I help you today?\n",
            "You: chocolate cake cost entha\n",
            "Bot: చాక్లెట్ కేక్ ధర ₹650.\n",
            "You: ok sare bye\n",
            "Bot: Sure! May I know your name?\n",
            "You: bye\n",
            "\n",
            "Bot: Thank you for visiting Sweet Crumbs!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import os\n",
        "from getpass import getpass\n",
        "\n",
        "key = getpass(\"Paste your generated Groq secret key: \").strip()\n",
        "\n",
        "print(\"Key entered:\", bool(key))\n",
        "print(\"Starts with gsk_:\", key.startswith(\"gsk_\"))\n",
        "print(\"Key length:\", len(key))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "MTNubuSma-7H",
        "outputId": "e6c7e806-e1ea-4b57-eb26-21ef1da03f07"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Paste your generated Groq secret key: ··········\n",
            "Key entered: True\n",
            "Starts with gsk_: True\n",
            "Key length: 56\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from groq import Groq\n",
        "\n",
        "client = Groq(api_key=key)"
      ],
      "metadata": {
        "id": "qn-643XcbGlV"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "response = client.chat.completions.create(\n",
        "    model=\"openai/gpt-oss-20b\",\n",
        "    messages=[\n",
        "        {\"role\": \"user\", \"content\": \"Hello\"}\n",
        "    ]\n",
        ")\n",
        "\n",
        "print(response.choices[0].message.content)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "L0h6Vf9TbKc-",
        "outputId": "38acf6b3-049d-4557-cd10-f9f1b8a8315a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Hello! 👋 How can I assist you today?\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"Client ready:\", client is not None)\n",
        "print(\"Model:\", MODEL)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "EKZK0uPubY8u",
        "outputId": "180e4c75-c799-44dd-9e9f-27b49b36329b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Client ready: True\n",
            "Model: openai/gpt-oss-20b\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"Welcome to Sweet Crumbs Home Bakery!\")\n",
        "print(\"Type 'bye' to exit.\\n\")\n",
        "\n",
        "while True:\n",
        "    text = input(\"You: \").strip()\n",
        "\n",
        "    if text.lower() in (\"bye\", \"exit\", \"quit\"):\n",
        "        print(\"Bot: Thank you for visiting Sweet Crumbs!\")\n",
        "        break\n",
        "\n",
        "    if text:\n",
        "        print(\"Bot:\", chat(text))\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "IICa9iYIbbAY",
        "outputId": "5c3c73df-ef2c-4a00-a0f1-6a9d193df4bd"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Welcome to Sweet Crumbs Home Bakery!\n",
            "Type 'bye' to exit.\n",
            "\n",
            "You: do you have cakes available\n",
            "Bot: Yes, we have chocolate cake (₹650) and other cakes (plum cake ₹500, cupcake ₹80). All are egg‑less. Please give 24‑hour notice before ordering.\n",
            "You: do you have eggless versions available\n",
            "Bot: Yes, all our cakes—including chocolate, plum, and cupcakes—are available in egg‑less versions. Remember to give 24‑hour notice before placing an order.\n",
            "You: ok thankyou\n",
            "Bot: You’re welcome! Let me know if you’d like to place an order or need more details.\n",
            "You: bye\n",
            "Bot: Thank you for visiting Sweet Crumbs!\n"
          ]
        }
      ]
    }
  ]
}