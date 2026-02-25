class RAGPipeline:
    def __init__(self, vector_store, llm):
        self.vector_store = vector_store
        self.llm = llm

    def answer(self, question: str, metadata_filter: dict = None):
        """
        Retrieve relevant documents using metadata filter (optional)
        """

        print("Metadata filter:", metadata_filter)

        context_docs = self.vector_store.search(
            query=question,
            top_k=3,
            where=metadata_filter
        )

        print("Retrieved docs:", context_docs)

        if not context_docs:
            return "No relevant QA knowledge found."

        context = "\n\n".join(context_docs)

        prompt = f"""
You are a QA expert assistant.

Use the following context to answer the question.

Context:
{context}

Question:
{question}

Answer:
"""

        return self.llm.generate(prompt)
