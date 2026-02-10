from src.prompts import RAG_PROMPT


class RAGPipeline:
    def __init__(self, vector_store, llm):
        self.vector_store = vector_store
        self.llm = llm

    def answer(self, question: str) -> str:
        """
        RAG Answering with strict grounding.
        - If no context is retrieved, LLM is NOT called.
        - Prevents hallucinations completely.
        """

        # 🔍 Step 1: Retrieve relevant documents
        context_docs = self.vector_store.search(question)

        # 🚨 Step 2: Hard guardrail
        if not context_docs or len(context_docs) == 0:
            return "❌ Not found in QA knowledge."

        # 📚 Step 3: Build grounded context
        context = "\n\n".join(context_docs)

        # 🧠 Step 4: Grounded prompt
        prompt = f"""
You are a QA Assistant.

STRICT RULES:
- Use ONLY the provided context.
- Do NOT use general knowledge.
- If answer is not explicitly present, reply exactly:
"❌ Not found in QA knowledge."

QA CONTEXT:
{context}

QUESTION:
{question}

ANSWER:
"""

        # 🤖 Step 5: Generate grounded response
        return self.llm.generate(prompt)

