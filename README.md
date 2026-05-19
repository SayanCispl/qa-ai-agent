<div align="center">

# 🧪 QA AI Agent

### 🚀 Offline AI-Powered QA Assistant using RAG, Ollama & ChromaDB

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/Ollama-Local%20LLM-black?style=for-the-badge" />
  <img src="https://img.shields.io/badge/RAG-ChromaDB-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" />
  <img src="https://img.shields.io/badge/AI-QA%20Automation-red?style=for-the-badge" />
</p>

---

### 🔥 Fully Local • Private • Offline • Open Source

An advanced AI-powered QA Assistant built specifically for QA Engineers and SDETs using **Retrieval-Augmented Generation (RAG)** architecture.

💯 No OpenAI API
🔒 100% Offline
🧠 Local LLMs via Ollama
📦 ChromaDB Vector Search
📊 Confidence Score Enabled

</div>

---

# ✨ Key Features

<table>
<tr>
<td width="50%">

---

# 🏗️ System Architecture

<div align="center">

```text
                  ┌──────────────────────┐
                  │      User Query      │
                  └──────────┬───────────┘
                             ↓
                  ┌──────────────────────┐
                  │      main.py CLI     │
                  └──────────┬───────────┘
                             ↓
                  ┌──────────────────────┐
                  │      qa_agent.py     │
                  └──────────┬───────────┘
                             ↓
                  ┌──────────────────────┐
                  │ ChromaDB Vector Store│
                  └──────────┬───────────┘
                             ↓
                  ┌──────────────────────┐
                  │ Semantic QA Retrieval│
                  └──────────┬───────────┘
                             ↓
                  ┌──────────────────────┐
                  │   RAG Prompt Builder │
                  └──────────┬───────────┘
                             ↓
                  ┌──────────────────────┐
                  │ Ollama (LLaMA3 LLM) │
                  └──────────┬───────────┘
                             ↓
                  ┌──────────────────────┐
                  │ Grounded QA Response │
                  │ + Confidence Score   │
                  └──────────────────────┘
```

</div>

---

# 📸 Project Preview

## 🧠 RAG Workflow

<p align="center">
  <img width="1200" alt="RAG" src="https://github.com/user-attachments/assets/3a591340-68aa-48a6-81be-3e89774811f6" />
</p>

---

## 📦 Vector Database Architecture

<p align="center">
  <img width="948" alt="VectorDB" src="https://github.com/user-attachments/assets/3f8460ea-47e1-4027-9214-4fe401788fe3" />
</p>

---

## ⚙️ Project Architecture

<p align="center">
  <img width="1100" alt="Project Architecture" src="https://github.com/user-attachments/assets/69f8d6cd-d981-4c9f-a273-eb2765dd1968" />
</p>

---

# 🚀 Tech Stack


| Layer           | Technology                |
| --------------- | ------------------------- |
| LLM Engine      | Ollama                    |
| Models          | LLaMA3 / Mistral          |
| Vector Database | ChromaDB                  |
| Embeddings      | Sentence Transformers     |
| Backend         | Python                    |
| Architecture    | RAG                       |
| Search          | Semantic Similarity       |
| Memory          | Persistent Vector Storage |

---

# 📂 Project Structure

```bash
qa-ai-agent/
│
├── agent/
│   ├── qa_agent.py
│   ├── ollama_client.py
│   ├── vector_store.py
│   ├── prompts.py
│
├── chroma_db/
├── .env
├── main.py
├── requirements.txt
└── README.md
```

---

# 🧠 Core Components

# 1️⃣ Ollama (Local LLM Engine)

Runs open-source Large Language Models completely offline.

### Supported Models

- llama3
- mistral

### Benefits

✅ No API Keys
✅ Fully Offline
✅ Faster Local Inference
✅ Privacy Friendly

---

# 2️⃣ ChromaDB (Vector Database)

Stores QA knowledge as vector embeddings.

### Responsibilities

- Semantic Search
- QA Context Retrieval
- Persistent Memory
- Similarity Matching

---

# 3️⃣ RAG Layer

Retrieves relevant QA context and injects it into prompts.

### Advantages

- Prevents Hallucinations
- Produces Grounded Answers
- Improves Accuracy
- Context-Aware Responses

---

# 4️⃣ Confidence Score Engine 📊

The system now includes a **Confidence Score Mechanism** to evaluate response reliability based on semantic similarity retrieval.

### Example

```text
Answer Confidence: 92%
```

### Benefits

- Helps validate AI responses
- Indicates retrieval relevance
- Improves trustworthiness
- Useful for enterprise QA workflows

---

# 🔐 Hallucination Safety

The assistant only answers using retrieved QA context.

If no relevant context is found:

```text
"Not found in knowledge base"
```

This ensures:

- Reliable Answers
- Reduced Hallucinations
- Enterprise Safety
- QA Accuracy

---

# 🛠️ Installation

# 1️⃣ Install Ollama

## macOS

```bash
brew install ollama
brew services start ollama
```

## Verify

```bash
ollama --version
```

## Pull Model

```bash
ollama pull llama3
```

---

# 2️⃣ Setup Python Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

# 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 4️⃣ Run the Agent

```bash
python main.py
```

---

# 🧪 Example QA Queries

```text
What login-related bugs were reported earlier?

Generate negative test cases for payment module.

Analyze this automation failure log.

Create a regression checklist for authentication.

Why did the checkout test fail yesterday?
```

---

# 📊 Why This Project Matters


| Feature          | Cloud AI | QA AI Agent |
| ---------------- | -------- | ----------- |
| Offline Support  | ❌       | ✅          |
| Free to Use      | ❌       | ✅          |
| Private Data     | ❌       | ✅          |
| RAG Architecture | ⚠️     | ✅          |
| QA-Specific      | ❌       | ✅          |
| Confidence Score | ❌       | ✅          |
| Local LLM        | ❌       | ✅          |

---

# 🌟 Enterprise Vision

- Multi-Agent QA Reasoning
- AI Failure Triage
- Selenium Integration
- Playwright Integration
- Jira Integration
- Autonomous Bug Clustering
- QA Analytics Dashboard
- AI Test Review Board

---

# 🧭 Future Roadmap

- 📂 PDF / Jira / Log Upload Support
- 🌐 FastAPI Web Dashboard
- 🧠 Auto-Learning from Test Results
- 📊 Advanced Confidence Metrics
- 🔄 Multi-Project Isolation
- 🧪 CI/CD Integration
- 🐳 Docker Deployment
- 📈 AI Observability

---

# 🤝 Contributing

Contributions are welcome!

You can help by:

- Improving Retrieval Logic
- Enhancing Prompt Engineering
- Optimizing Semantic Search
- Building UI Components
- Adding QA Utilities

---

# 📜 License

MIT License

Free to use, modify, and distribute.

---

# 👨‍💻 Author

<div align="center">

## Sayan Koley

### QA Automation Engineer • AI in Testing • Open Source Enthusiast

</div>

---

# ⭐ Support

If you found this project useful:

⭐ Star the repository
🍴 Fork the project
🐛 Raise issues
🧠 Contribute ideas

---

<div align="center">

# 🔥 Vision

### Building the Future of Offline AI for QA Engineering

</div>
