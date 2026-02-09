🧪 QA AI Agent
Offline AI-Powered QA Assistant with RAG using Ollama & ChromaDB
An open-source, fully local QA AI Agent designed to assist QA Engineers and Test Automation teams by generating, analyzing, storing, and retrieving QA knowledge using Retrieval-Augmented Generation (RAG).
✅ No OpenAI API
✅ No paid services
✅ Runs fully offline
✅ Uses open-source LLMs

🚀 Key Features
🤖 Local LLM via Ollama (LLaMA 3 / Mistral)
🧠 RAG (Retrieval-Augmented Generation)
📦 Vector Database (ChromaDB)
🔍 Semantic search for QA knowledge
🧪 Test case review & generation
🐞 Bug analysis
📄 Log analysis
📋 QA checklist creation
🔐 Hallucination-safe answers (context enforced)

Architecture Flow
User Input (QA Question)
        ↓
Vector Database (ChromaDB)
        ↓
Relevant QA Context (Semantic Search)
        ↓
Context Injection (RAG Prompt)
        ↓
Local LLM (Ollama - LLaMA3)
        ↓
Final Grounded QA Answer


Project Structure
qa-ai-agent/
│
├── agent/
│   ├── qa_agent.py          # Core QA agent logic
│   ├── ollama_client.py     # Ollama LLM client
│   ├── vector_store.py      # ChromaDB vector operations
│   ├── prompts.py           # System & RAG prompts
│
├── .env                     # Environment variables
├── main.py                  # CLI entry point
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation

Core Components Explained
1️⃣ Ollama (Local LLM Engine)
Runs open-source LLMs locally
No API keys required
Example models:
a. llama3
b. mistral

2️⃣ ChromaDB (Vector Database)
Stores QA knowledge as embeddings
Enables semantic similarity search
Fully local & lightweight

3️⃣ RAG Layer (Context Injection)
Retrieves relevant QA data
Injects it into LLM prompts
Prevents hallucinations
Ensures project-specific answers

RAG Prompt Strategy
The agent only answers using retrieved context:
If the answer is not present in the context,
respond with: "Not found in knowledge base"
This makes the agent QA-safe and reliable.

🛠️ Installation
1️⃣ Install Ollama
brew install ollama
brew services start ollama
Verify:
ollama --version
Pull model:
ollama pull llama3

2️⃣ Setup Python Environment
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

3️⃣ Run the Agent
python main.py
🧪 Example RAG Question
What login-related issues were found earlier?
✔ Searches QA memory
✔ Injects real bug/test/log context
✔ Produces grounded answer


Why This Project Is Special =>
| Feature      | Cloud AI | This Project |
| ------------ | -------- | ------------ |
| Offline      | ❌        | ✅            |
| Free         | ❌        | ✅            |
| Private Data | ❌        | ✅            |
| RAG          | ⚠️        | ✅            |
| QA-Specific  | ❌        | ✅            |

🧭 Roadmap
📂 Upload Jira tickets / PRDs / logs (PDF, TXT)
🌐 Web UI using FastAPI
🧠 Auto-learning from test execution results
📊 Confidence score per answer
🧪 CI/CD pipeline integration
🔄 Multi-project vector isolation

🤝 Contributing
Contributions are welcome!
Feel free to:
Add new QA tools
Improve prompts
Enhance RAG logic
Add UI layers

📜 License
MIT License – Free to use, modify, and distribute.

🙌 Author
Sayan Koley
QA Automation | AI in Testing | Open Source
