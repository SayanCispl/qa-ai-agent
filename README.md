# 🧠 QA AI Agent

### 🚀 Offline AI-Powered QA Engineering Platform using RAG, Ollama, FastAPI & ChromaDB

---

## 🔥 AI-Powered QA Intelligence Platform

### ⚡ Fully Offline • Private • Open Source • Enterprise Ready

An advanced AI-driven QA Engineering platform built specifically for:

✅ QA Engineers
✅ SDETs
✅ Automation Engineers
✅ API Testers
✅ Performance Testers
✅ DevOps & Release Teams

Powered by:

🧠 Retrieval-Augmented Generation (RAG)
📦 ChromaDB Vector Search
🤖 Ollama Local LLMs
📊 Confidence Score Engine
🌐 FastAPI APIs
📘 Swagger Documentation
📈 Streamlit Dashboard
🧪 AI Flaky Test RCA

---

# 📸 Project Preview

---

## 🧠 RAG Architecture Workflow

---

## 📦 Vector Database Architecture

---

## ⚙️ Complete System Design

---

# ✨ Core Features

## 🤖 AI-Powered QA Assistant

* AI Test Case Generation
* AI Bug Analysis
* AI Log Analysis
* AI QA Checklist Creation
* AI Root Cause Analysis
* AI Automation Failure Detection

## 🧠 RAG + Semantic Search

* ChromaDB Vector Search
* Sentence Transformer Embeddings
* Semantic Similarity Retrieval
* Context-Aware QA Answers
* Hallucination Prevention
* Confidence Score Engine

## 🌐 Modern Backend Stack

* FastAPI REST APIs
* Swagger/OpenAPI Docs
* Streamlit Dashboard
* Rich CLI UI
* JSON Structured Logging
* Modular Architecture

## 🧪 QA Engineering Focus

* Selenium Failure RCA
* Playwright RCA
* API Failure Analysis
* Payment Failure Scenarios
* Flaky Automation Detection
* Retry Mechanism Validation

---

# 🏗️ Enterprise System Architecture

```text
                    ┌──────────────────────┐
                    │     Streamlit UI     │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │      FastAPI API     │
                    └──────────┬───────────┘
                               │
                ┌──────────────┼──────────────┐
                ▼                             ▼
      ┌─────────────────┐         ┌─────────────────┐
      │   QA AI Agent   │         │  Swagger Docs   │
      └────────┬────────┘         └─────────────────┘
               │
     ┌─────────┼─────────┐
     ▼                   ▼
┌──────────────┐   ┌──────────────┐
│  RAG Engine  │   │ Ollama LLM  │
└──────┬───────┘   └──────────────┘
       │
       ▼
┌──────────────────────────┐
│     ChromaDB Vector DB   │
└──────────┬───────────────┘
           ▼
┌──────────────────────────┐
│ SentenceTransformer Emb. │
└──────────────────────────┘
```

---

# 🚀 Tech Stack


| Layer                | Technology            |
| -------------------- | --------------------- |
| Programming Language | Python                |
| Local LLM Engine     | Ollama                |
| Supported Models     | LLaMA3 / Mistral      |
| Vector Database      | ChromaDB              |
| Embeddings           | SentenceTransformers  |
| Backend APIs         | FastAPI               |
| API Documentation    | Swagger/OpenAPI       |
| Frontend Dashboard   | Streamlit             |
| UI Framework         | Rich                  |
| AI Architecture      | RAG                   |
| Logging              | Python Logging + JSON |
| Metadata             | YAML                  |

---

# 📂 Project Structure

```bash
qa-ai-agent/
│
├── api.py
├── run.py
├── streamlit_app.py
│
├── chroma_db/
│
├── logs/
│
├── data/
│   └── qa_data/
│
├── src/
│   ├── main.py
│   ├── qa_agent.py
│   ├── rag.py
│   ├── vector_store.py
│   ├── ollama_client.py
│   ├── prompts.py
│   └── flaky_analyzer.py
│
├── requirements.txt
└── README.md
```

---

# 🧠 Core Components Explained

## 1️⃣ Ollama (Local LLM Engine)

Runs open-source LLMs completely offline.

### Supported Models

* llama3
* mistral

### Benefits

✅ No API Keys
✅ Fully Offline
✅ Faster Local Inference
✅ Secure & Private
✅ Enterprise Friendly

---

## 2️⃣ ChromaDB (Vector Database)

Stores QA knowledge as vector embeddings.

### Responsibilities

* Semantic Search
* Similarity Matching
* Persistent QA Memory
* Context Retrieval
* RAG Support

---

## 3️⃣ RAG (Retrieval-Augmented Generation)

Retrieves relevant QA knowledge before generating answers.

### Advantages

✅ Hallucination Reduction
✅ Context-Aware Responses
✅ Higher Accuracy
✅ Grounded AI Answers

---

## 4️⃣ Confidence Score Engine 📊

Every AI response includes a semantic confidence score.

### Formula

```python
confidence = (1 - distance) * 100
```

### Benefits

✅ Measures Retrieval Accuracy
✅ Improves AI Trustworthiness
✅ Useful for Enterprise QA
✅ Helps Validate Responses

---

## 5️⃣ AI Flaky Test RCA 🧪

Intelligent flaky automation analysis engine.

### Detects Issues Like

* TimeoutException
* ElementClickInterceptedException
* StaleElementReferenceException
* Synchronization Failures
* DOM Rendering Delays
* Spinner Overlay Issues
* Hardcoded Sleep Problems

---

# 🌐 FastAPI + Swagger Integration

Production-ready backend APIs.

### Features

✅ REST APIs
✅ JSON Responses
✅ Swagger Documentation
✅ OpenAPI Support
✅ Frontend Integration Ready

### Swagger Docs

```text
http://127.0.0.1:8000/docs
```

---

# 📊 Streamlit Dashboard

Interactive AI dashboard for QA Engineers.

### Dashboard Features

* RAG QA Search
* Test Case Generation
* AI Bug Analysis
* AI Log Analysis
* Confidence Visualization
* Flaky Test RCA

---

# 🛠️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/qa-ai-agent.git

cd qa-ai-agent
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv .venv
```

---

## 3️⃣ Activate Environment

### macOS/Linux

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

---

## 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 5️⃣ Install Ollama

```bash
brew install ollama
```

---

## 6️⃣ Start Ollama

```bash
ollama serve
```

---

## 7️⃣ Pull LLM Model

```bash
ollama pull mistral
```

---

## 8️⃣ Load QA Embeddings

```bash
python data/load_qa_data.py
```

---

## ▶️ Run CLI Application

```bash
python run.py
```

---

## 🌐 Run FastAPI Backend

```bash
uvicorn api:app --reload
```

---

## 📊 Run Streamlit Dashboard

```bash
streamlit run streamlit_app.py
```

---

# 🧪 Example QA Queries

```text
Explain the payment gateway timeout production incident.

Generate negative test cases for checkout flow.

Analyze this Selenium flaky automation failure.

Why did duplicate payment happen during retry?

Create regression checklist for authentication module.
```

---

# 🎯 Real-World QA Use Cases


| Domain      | Use Case                       |
| ----------- | ------------------------------ |
| Banking     | Payment Failure RCA            |
| FinTech     | Duplicate Transaction Analysis |
| E-Commerce  | Checkout Failure Debugging     |
| Automation  | Flaky Selenium RCA             |
| API Testing | Webhook Failure Analysis       |
| Performance | Timeout Root Cause Analysis    |
| DevOps      | Log Failure Investigation      |

---

# 📊 Why This Project Matters


| Feature          | Cloud AI | QA AI Agent |
| ---------------- | -------- | ----------- |
| Offline Support  | ❌       | ✅          |
| Free to Use      | ❌       | ✅          |
| Local LLM        | ❌       | ✅          |
| Private Data     | ❌       | ✅          |
| RAG Architecture | ⚠️     | ✅          |
| Confidence Score | ❌       | ✅          |
| QA-Specific AI   | ❌       | ✅          |
| Flaky Test RCA   | ❌       | ✅          |

---

# 🌟 Enterprise Vision

* AI Failure Triage
* Multi-Agent QA Systems
* Autonomous Bug Clustering
* Selenium Integration
* Playwright Integration
* Allure Report Analysis
* AI QA Analytics Platform
* CI/CD Failure Intelligence

---

# 🧭 Future Roadmap

* 📂 PDF/Jira Upload Support
* 🧠 Self-Learning QA Engine
* 🧪 AI Test Script Generation
* 🐳 Docker Deployment
* 📊 Advanced Observability
* 🔄 Multi-Project Isolation
* 📈 Historical RCA Tracking
* ☁️ Kubernetes Deployment

---

# 🤝 Contributing

Contributions are welcome!

### You can contribute by:

* Improving RAG Retrieval
* Enhancing Prompt Engineering
* Optimizing Embeddings
* Building UI Features
* Adding QA Utilities
* Improving AI RCA Logic

---

# 📜 License

MIT License

Free to use, modify, and distribute.

---

# 👨‍💻 Author

# Sayan Koley

### QA Automation Engineer • AI in Testing • Open Source Enthusiast

---

# ⭐ Support the Project

If you found this project useful:

⭐ Star the repository
🍴 Fork the project
🐛 Raise issues
🧠 Contribute ideas

---

# 🚀 Vision

### Building the Future of AI-Powered QA Engineering

🔥 Offline AI
🔥 Local LLMs
🔥 Intelligent Testing
🔥 Enterprise QA Automation
