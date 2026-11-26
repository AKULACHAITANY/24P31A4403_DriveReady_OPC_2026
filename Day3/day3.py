{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/AKULACHAITANY/24P31A4403_DriveReady_OPC_2026/blob/main/Day3/day3.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "boI3ttKy2x3i"
      },
      "outputs": [],
      "source": [
        "!pip install -q langchain langchain-groq"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install -U langchain langchain-core langchain-groq"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "TIAd8kERw2VU",
        "outputId": "dcd94fff-4fe1-45c0-f705-ab633333518f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: langchain in /usr/local/lib/python3.13/dist-packages (1.4.8)\n",
            "Collecting langchain\n",
            "  Downloading langchain-1.5.2-py3-none-any.whl.metadata (6.1 kB)\n",
            "Requirement already satisfied: langchain-core in /usr/local/lib/python3.13/dist-packages (1.8.5)\n",
            "Requirement already satisfied: langchain-groq in /usr/local/lib/python3.13/dist-packages (1.2.1)\n",
            "Requirement already satisfied: langgraph<1.3.0,>=1.2.12 in /usr/local/lib/python3.13/dist-packages (from langchain) (1.2.19)\n",
            "Requirement already satisfied: pydantic>=2.7.4 in /usr/local/lib/python3.13/dist-packages (from langchain) (2.14.2)\n",
            "Requirement already satisfied: certifi>=2026.10.19 in /usr/local/lib/python3.13/dist-packages (from langchain-core) (2026.10.23)\n",
            "Requirement already satisfied: httpx>=0.23.0 in /usr/local/lib/python3.13/dist-packages (from langchain-core) (0.28.1)\n",
            "Requirement already satisfied: jsonpatch>=1.33.0 in /usr/local/lib/python3.13/dist-packages (from langchain-core) (1.41)\n",
            "Requirement already satisfied: langchain-protocol>=0.0.22 in /usr/local/lib/python3.13/dist-packages (from langchain-core) (0.0.22)\n",
            "Requirement already satisfied: langsmith<1.0.0,>=0.14.9 in /usr/local/lib/python3.13/dist-packages (from langchain-core) (0.14.17)\n",
            "Requirement already satisfied: packaging>=23.2.0 in /usr/local/lib/python3.13/dist-packages (from langchain-core) (26.3)\n",
            "Requirement already satisfied: pyyaml>=5.3.0 in /usr/local/lib/python3.13/dist-packages (from langchain-core) (6.0.3)\n",
            "Requirement already satisfied: tenacity!=8.4.0,>=8.1.0 in /usr/local/lib/python3.13/dist-packages (from langchain-core) (9.1.4)\n",
            "Requirement already satisfied: typing-extensions>=4.7.0 in /usr/local/lib/python3.13/dist-packages (from langchain-core) (4.16.0)\n",
            "Requirement already satisfied: uuid-utils>=0.12.0 in /usr/local/lib/python3.13/dist-packages (from langchain-core) (0.19.0)\n",
            "Requirement already satisfied: langgraph-checkpoint<5.0.0,>=4.3.0 in /usr/local/lib/python3.13/dist-packages (from langgraph<1.3.0,>=1.2.12->langchain) (4.3.1)\n",
            "Requirement already satisfied: langgraph-prebuilt<1.2.0,>=1.1.0 in /usr/local/lib/python3.13/dist-packages (from langgraph<1.3.0,>=1.2.12->langchain) (1.1.1)\n",
            "Requirement already satisfied: langgraph-sdk<0.5.0,>=0.4.6 in /usr/local/lib/python3.13/dist-packages (from langgraph<1.3.0,>=1.2.12->langchain) (0.4.12)\n",
            "Requirement already satisfied: xxhash>=3.5.0 in /usr/local/lib/python3.13/dist-packages (from langgraph<1.3.0,>=1.2.12->langchain) (4.0.2)\n",
            "Requirement already satisfied: ormsgpack>=1.12.0 in /usr/local/lib/python3.13/dist-packages (from langgraph-checkpoint<5.0.0,>=4.3.0->langgraph<1.3.0,>=1.2.12->langchain) (1.13.0)\n",
            "Requirement already satisfied: orjson>=3.11.5 in /usr/local/lib/python3.13/dist-packages (from langgraph-sdk<0.5.0,>=0.4.6->langgraph<1.3.0,>=1.2.12->langchain) (3.13.0)\n",
            "Requirement already satisfied: websockets>=14 in /usr/local/lib/python3.13/dist-packages (from langgraph-sdk<0.5.0,>=0.4.6->langgraph<1.3.0,>=1.2.12->langchain) (15.0.1)\n",
            "Requirement already satisfied: anyio<5,>=3.5.0 in /usr/local/lib/python3.13/dist-packages (from langsmith<1.0.0,>=0.14.9->langchain-core) (4.16.0)\n",
            "Requirement already satisfied: distro<2,>=1.7.0 in /usr/local/lib/python3.13/dist-packages (from langsmith<1.0.0,>=0.14.9->langchain-core) (1.9.0)\n",
            "Requirement already satisfied: httpx2<3,>=2 in /usr/local/lib/python3.13/dist-packages (from langsmith<1.0.0,>=0.14.9->langchain-core) (2.16.0)\n",
            "Requirement already satisfied: requests-toolbelt>=1.0.0 in /usr/local/lib/python3.13/dist-packages (from langsmith<1.0.0,>=0.14.9->langchain-core) (1.0.0)\n",
            "Requirement already satisfied: requests>=2.0.0 in /usr/local/lib/python3.13/dist-packages (from langsmith<1.0.0,>=0.14.9->langchain-core) (2.32.4)\n",
            "Requirement already satisfied: sniffio in /usr/local/lib/python3.13/dist-packages (from langsmith<1.0.0,>=0.14.9->langchain-core) (1.3.1)\n",
            "Requirement already satisfied: zstandard>=0.23.0 in /usr/local/lib/python3.13/dist-packages (from langsmith<1.0.0,>=0.14.9->langchain-core) (0.25.0)\n",
            "Requirement already satisfied: idna>=2.8 in /usr/local/lib/python3.13/dist-packages (from anyio<5,>=3.5.0->langsmith<1.0.0,>=0.14.9->langchain-core) (3.20)\n",
            "Requirement already satisfied: httpcore2==2.16.0 in /usr/local/lib/python3.13/dist-packages (from httpx2<3,>=2->langsmith<1.0.0,>=0.14.9->langchain-core) (2.16.0)\n",
            "Requirement already satisfied: truststore>=0.10 in /usr/local/lib/python3.13/dist-packages (from httpx2<3,>=2->langsmith<1.0.0,>=0.14.9->langchain-core) (0.10.5)\n",
            "Requirement already satisfied: h11>=0.16 in /usr/local/lib/python3.13/dist-packages (from httpcore2==2.16.0->httpx2<3,>=2->langsmith<1.0.0,>=0.14.9->langchain-core) (0.16.0)\n",
            "Requirement already satisfied: annotated-types>=0.6.0 in /usr/local/lib/python3.13/dist-packages (from pydantic>=2.7.4->langchain) (0.8.0)\n",
            "Requirement already satisfied: pydantic-core==2.50.2 in /usr/local/lib/python3.13/dist-packages (from pydantic>=2.7.4->langchain) (2.50.2)\n",
            "Requirement already satisfied: typing-inspection>=0.4.4 in /usr/local/lib/python3.13/dist-packages (from pydantic>=2.7.4->langchain) (0.4.4)\n",
            "Requirement already satisfied: groq>=0.30.0 in /usr/local/lib/python3.13/dist-packages (from langchain-groq) (1.7.0)\n",
            "Requirement already satisfied: httpcore==1.* in /usr/local/lib/python3.13/dist-packages (from httpx>=0.23.0->langchain-core) (1.0.9)\n",
            "Requirement already satisfied: jsonpointer>=3.8 in /usr/local/lib/python3.13/dist-packages (from jsonpatch>=1.33.0->langchain-core) (3.8)\n",
            "Requirement already satisfied: charset_normalizer<4,>=2 in /usr/local/lib/python3.13/dist-packages (from requests>=2.0.0->langsmith<1.0.0,>=0.14.9->langchain-core) (3.4.9)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.13/dist-packages (from requests>=2.0.0->langsmith<1.0.0,>=0.14.9->langchain-core) (2.5.0)\n",
            "Downloading langchain-1.5.2-py3-none-any.whl (176 kB)\n",
            "Installing collected packages: langchain\n",
            "  Attempting uninstall: langchain\n",
            "    Found existing installation: langchain 1.4.8\n",
            "    Uninstalling langchain-1.4.8:\n",
            "      Successfully uninstalled langchain-1.4.8\n",
            "Successfully installed langchain-1.5.2\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "kOn2EbGQ3Brp"
      },
      "outputs": [],
      "source": [
        "import os\n",
        "from google.colab import userdata\n",
        "os.environ[\"GROQ_API_KEY\"] = userdata.get(\"GROQ_API_KEY\")   # LangChain reads it from here\n",
        "\n",
        "from langchain_groq import ChatGroq\n",
        "llm = ChatGroq(model=\"openai/gpt-oss-120b\", temperature=0.3)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "cxethZML7CE8",
        "outputId": "4734a692-92e1-4fc6-e871-2224484df845"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Hi Ravi! 😊 Yes, we offer egg‑less versions of all our cakes – plum, chocolate, cupcakes and more. Let me know which one you’d like, and I’ll help you with the details!\n",
            "Your name is Ravi! 😊\n"
          ]
        }
      ],
      "source": [
        "from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder\n",
        "from langchain_core.output_parsers import StrOutputParser\n",
        "\n",
        "SYSTEM = \"\"\"ROLE:   You are the friendly assistant for Sweet Crumbs Home Bakery.\n",
        "FACTS:  Plum cake Rs 500. Chocolate cake Rs 650. Cupcake Rs 80 each.\n",
        "        Orders need 24 hours' notice. All cakes have eggless versions.\n",
        "RULES:  Never promise a delivery time or place. If it isn't in FACTS,\n",
        "        say \"I'll check with the owner.\" Work out totals carefully.\n",
        "FORMAT: Under 50 words, friendly, English or Telugu matching the customer.\"\"\"\n",
        "\n",
        "prompt = ChatPromptTemplate.from_messages([\n",
        "    (\"system\", SYSTEM),\n",
        "    MessagesPlaceholder(\"history\"),          # the chat so far goes here\n",
        "    (\"human\", \"{question}\"),\n",
        "])\n",
        "chain = prompt | llm | StrOutputParser()\n",
        "\n",
        "history = []\n",
        "def ask(question: str) -> str:\n",
        "    answer = chain.invoke({\"history\": history, \"question\": question})\n",
        "    history.extend([(\"human\", question), (\"ai\", answer)])\n",
        "    return answer\n",
        "\n",
        "print(ask(\"Hi, I'm Ravi. Do you make eggless cakes?\"))\n",
        "print(ask(\"What's my name?\"))"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "V7SqEhiD7NCd",
        "outputId": "a234cfa0-9178-44fb-a327-39c3782206aa"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[('human', \"Hi, I'm Ravi. Do you make eggless cakes?\"),\n",
              " ('ai',\n",
              "  'Hi Ravi! 😊 Yes, we offer egg‑less versions of all our cakes – plum, chocolate, cupcakes and more. Let me know which one you’d like, and I’ll help you with the details!'),\n",
              " ('human', \"What's my name?\"),\n",
              " ('ai', 'Your name is Ravi! 😊')]"
            ]
          },
          "metadata": {},
          "execution_count": 5
        }
      ],
      "source": [
        "history"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Xv0m0b6X7U6j",
        "outputId": "27863d2e-bb26-44a4-d6fc-1bf87a20a0b1"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "/content\n",
            "['.config', 'drive', 'sample_data']\n"
          ]
        }
      ],
      "source": [
        "import os\n",
        "\n",
        "print(os.getcwd())\n",
        "print(os.listdir())"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 38
        },
        "id": "3DJRzpL87ix3",
        "outputId": "1d54c954-9f3f-4886-e848-6cb9a02a39d2"
      },
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.HTML object>"
            ],
            "text/html": [
              "\n",
              "     <input type=\"file\" id=\"files-630c5dfd-ebb0-47f9-b368-25bf5d30d2e8\" name=\"files[]\" multiple disabled\n",
              "        style=\"border:none\" />\n",
              "     <output id=\"result-630c5dfd-ebb0-47f9-b368-25bf5d30d2e8\">\n",
              "      Upload widget is only available when the cell has been executed in the\n",
              "      current browser session. Please rerun this cell to enable.\n",
              "      </output>\n",
              "      <script>// Copyright 2017 Google LLC\n",
              "//\n",
              "// Licensed under the Apache License, Version 2.0 (the \"License\");\n",
              "// you may not use this file except in compliance with the License.\n",
              "// You may obtain a copy of the License at\n",
              "//\n",
              "//      http://www.apache.org/licenses/LICENSE-2.0\n",
              "//\n",
              "// Unless required by applicable law or agreed to in writing, software\n",
              "// distributed under the License is distributed on an \"AS IS\" BASIS,\n",
              "// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n",
              "// See the License for the specific language governing permissions and\n",
              "// limitations under the License.\n",
              "\n",
              "/**\n",
              " * @fileoverview Helpers for google.colab Python module.\n",
              " */\n",
              "(function(scope) {\n",
              "function span(text, styleAttributes = {}) {\n",
              "  const element = document.createElement('span');\n",
              "  element.textContent = text;\n",
              "  for (const key of Object.keys(styleAttributes)) {\n",
              "    element.style[key] = styleAttributes[key];\n",
              "  }\n",
              "  return element;\n",
              "}\n",
              "\n",
              "// Max number of bytes which will be uploaded at a time.\n",
              "const MAX_PAYLOAD_SIZE = 100 * 1024;\n",
              "\n",
              "function _uploadFiles(inputId, outputId) {\n",
              "  const steps = uploadFilesStep(inputId, outputId);\n",
              "  const outputElement = document.getElementById(outputId);\n",
              "  // Cache steps on the outputElement to make it available for the next call\n",
              "  // to uploadFilesContinue from Python.\n",
              "  outputElement.steps = steps;\n",
              "\n",
              "  return _uploadFilesContinue(outputId);\n",
              "}\n",
              "\n",
              "// This is roughly an async generator (not supported in the browser yet),\n",
              "// where there are multiple asynchronous steps and the Python side is going\n",
              "// to poll for completion of each step.\n",
              "// This uses a Promise to block the python side on completion of each step,\n",
              "// then passes the result of the previous step as the input to the next step.\n",
              "function _uploadFilesContinue(outputId) {\n",
              "  const outputElement = document.getElementById(outputId);\n",
              "  const steps = outputElement.steps;\n",
              "\n",
              "  const next = steps.next(outputElement.lastPromiseValue);\n",
              "  return Promise.resolve(next.value.promise).then((value) => {\n",
              "    // Cache the last promise value to make it available to the next\n",
              "    // step of the generator.\n",
              "    outputElement.lastPromiseValue = value;\n",
              "    return next.value.response;\n",
              "  });\n",
              "}\n",
              "\n",
              "/**\n",
              " * Generator function which is called between each async step of the upload\n",
              " * process.\n",
              " * @param {string} inputId Element ID of the input file picker element.\n",
              " * @param {string} outputId Element ID of the output display.\n",
              " * @return {!Iterable<!Object>} Iterable of next steps.\n",
              " */\n",
              "function* uploadFilesStep(inputId, outputId) {\n",
              "  const inputElement = document.getElementById(inputId);\n",
              "  inputElement.disabled = false;\n",
              "\n",
              "  const outputElement = document.getElementById(outputId);\n",
              "  outputElement.innerHTML = '';\n",
              "\n",
              "  const pickedPromise = new Promise((resolve) => {\n",
              "    inputElement.addEventListener('change', (e) => {\n",
              "      resolve(e.target.files);\n",
              "    });\n",
              "  });\n",
              "\n",
              "  const cancel = document.createElement('button');\n",
              "  inputElement.parentElement.appendChild(cancel);\n",
              "  cancel.textContent = 'Cancel upload';\n",
              "  const cancelPromise = new Promise((resolve) => {\n",
              "    cancel.onclick = () => {\n",
              "      resolve(null);\n",
              "    };\n",
              "  });\n",
              "\n",
              "  // Wait for the user to pick the files.\n",
              "  const files = yield {\n",
              "    promise: Promise.race([pickedPromise, cancelPromise]),\n",
              "    response: {\n",
              "      action: 'starting',\n",
              "    }\n",
              "  };\n",
              "\n",
              "  cancel.remove();\n",
              "\n",
              "  // Disable the input element since further picks are not allowed.\n",
              "  inputElement.disabled = true;\n",
              "\n",
              "  if (!files) {\n",
              "    return {\n",
              "      response: {\n",
              "        action: 'complete',\n",
              "      }\n",
              "    };\n",
              "  }\n",
              "\n",
              "  for (const file of files) {\n",
              "    const li = document.createElement('li');\n",
              "    li.append(span(file.name, {fontWeight: 'bold'}));\n",
              "    li.append(span(\n",
              "        `(${file.type || 'n/a'}) - ${file.size} bytes, ` +\n",
              "        `last modified: ${\n",
              "            file.lastModifiedDate ? file.lastModifiedDate.toLocaleDateString() :\n",
              "                                    'n/a'} - `));\n",
              "    const percent = span('0% done');\n",
              "    li.appendChild(percent);\n",
              "\n",
              "    outputElement.appendChild(li);\n",
              "\n",
              "    const fileDataPromise = new Promise((resolve) => {\n",
              "      const reader = new FileReader();\n",
              "      reader.onload = (e) => {\n",
              "        resolve(e.target.result);\n",
              "      };\n",
              "      reader.readAsArrayBuffer(file);\n",
              "    });\n",
              "    // Wait for the data to be ready.\n",
              "    let fileData = yield {\n",
              "      promise: fileDataPromise,\n",
              "      response: {\n",
              "        action: 'continue',\n",
              "      }\n",
              "    };\n",
              "\n",
              "    // Use a chunked sending to avoid message size limits. See b/62115660.\n",
              "    let position = 0;\n",
              "    do {\n",
              "      const length = Math.min(fileData.byteLength - position, MAX_PAYLOAD_SIZE);\n",
              "      const chunk = new Uint8Array(fileData, position, length);\n",
              "      position += length;\n",
              "\n",
              "      const base64 = btoa(String.fromCharCode.apply(null, chunk));\n",
              "      yield {\n",
              "        response: {\n",
              "          action: 'append',\n",
              "          file: file.name,\n",
              "          data: base64,\n",
              "        },\n",
              "      };\n",
              "\n",
              "      let percentDone = fileData.byteLength === 0 ?\n",
              "          100 :\n",
              "          Math.round((position / fileData.byteLength) * 100);\n",
              "      percent.textContent = `${percentDone}% done`;\n",
              "\n",
              "    } while (position < fileData.byteLength);\n",
              "  }\n",
              "\n",
              "  // All done.\n",
              "  yield {\n",
              "    response: {\n",
              "      action: 'complete',\n",
              "    }\n",
              "  };\n",
              "}\n",
              "\n",
              "scope.google = scope.google || {};\n",
              "scope.google.colab = scope.google.colab || {};\n",
              "scope.google.colab._files = {\n",
              "  _uploadFiles,\n",
              "  _uploadFilesContinue,\n",
              "};\n",
              "})(self);\n",
              "</script> "
            ]
          },
          "metadata": {}
        }
      ],
      "source": [
        "from google.colab import files\n",
        "\n",
        "uploaded = files.upload()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "TdT52jCK79dW"
      },
      "outputs": [],
      "source": [
        "import csv\n",
        "\n",
        "def run_tests(path: str = \"/day3csv.csv\") -> None:\n",
        "    rows = list(csv.DictReader(open(path)))\n",
        "    passed = 0\n",
        "    for row in rows:\n",
        "        answer = chain.invoke({\"history\": [], \"question\": row[\"question\"]})\n",
        "        ok = row[\"must_include\"].lower() in answer.lower()\n",
        "        passed += ok\n",
        "        print(\"PASS\" if ok else \"FAIL\", \"|\", row[\"question\"], \"→\", answer[:70])\n",
        "    print(f\"\\n{passed}/{len(rows)} passed ({passed / len(rows):.0%})\")\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "run_tests()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "hnGrZ6evs4uX",
        "outputId": "b017c90b-79b7-4de3-a9ac-03a8cfb47224"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "PASS | How much is a plum cake? → A plum cake costs Rs 500. Let me know if you’d like to add anything el\n",
            "FAIL | Do you make eggless cakes? → Yes! All our cakes, including plum, chocolate, and cupcakes, are avail\n",
            "FAIL | Can I get a cake today evening? → I’ll check with the owner and let you know!\n",
            "PASS | Do you deliver to Kakinada? → I'll check with the owner and get back to you soon!\n",
            "PASS | What is the price of 6 cupcakes? → Sure! Six cupcakes would be 6 × ₹80 = **₹480**. Let me know if you’d l\n",
            "\n",
            "3/5 passed (60%)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from langchain.agents import create_agent\n",
        "\n",
        "agent_order = create_agent(\n",
        "    model=llm,\n",
        "    tools=[],\n",
        "    system_prompt=SYSTEM\n",
        ")\n",
        "\n",
        "result_order = agent_order.invoke({\n",
        "    \"messages\": [\n",
        "        {\"role\": \"user\", \"content\": \"Do you make eggless cakes?\"}\n",
        "    ]\n",
        "})\n",
        "\n",
        "print(result_order[\"messages\"][-1].content)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "tX3pATKWxI0s",
        "outputId": "49640e86-a7b5-41b4-a279-88dd522e8dc0"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Yes! All our cakes, including plum, chocolate, and cupcakes, are available in egg‑less versions. Let us know which one you’d like!\n"
          ]
        }
      ]
    }
  ],
  "metadata": {
    "colab": {
      "provenance": [],
      "mount_file_id": "16Hk289eVw9OwuKftmryM9z8RF9AWVjTf",
      "authorship_tag": "ABX9TyN3RUHsDJkiu2RD5+jZwoRH",
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}