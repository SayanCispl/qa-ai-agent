"""
Vector Store Module
-------------------
Responsible for:
- Storing QA knowledge in ChromaDB
- Generating embeddings using SentenceTransformer
- Performing semantic search for RAG
"""

import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer


class VectorStore:
    def __init__(self, persist_dir="vector_db"):
        """
                Initialize ChromaDB client and embedding model.

                :param persist_dir: Folder where vector DB will be stored locally
                """

        # Initialize Chroma client with local persistence
        self.client = chromadb.Client(
            Settings(persist_directory=persist_dir)
        )

        # Create or load existing collection
        self.collection = self.client.get_or_create_collection(
            name="qa_knowledge"
        )

        # Load embedding model (lightweight + good for semantic search)
        self.embedder = SentenceTransformer("all-MiniLM-L6-v2")

    def add(self, text, metadata=None, doc_id=None):
        """
                Add a document to the vector store.

                :param text: Text content to embed
                :param metadata: Additional info (type=bug/test_case/etc.)
                :param doc_id: Unique ID for document
                """

        # Convert text into vector embedding
        embedding = self.embedder.encode(text).tolist()

        # Store in ChromaDB
        self.collection.add(
            documents=[text],
            embeddings=[embedding],
            metadatas=[metadata or {}],
            ids=[doc_id or text[:40]]
        )

    def search(self, query, top_k=5):
        """
                Perform semantic similarity search.

                :param query: User question
                :param top_k: Number of similar documents to retrieve
                :return: List of relevant documents
                """

        # Convert query into embedding
        query_embedding = self.embedder.encode(query).tolist()
        # Query ChromaDB
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )
        # Return list of matching documents
        return results.get("documents", [[]])[0]
