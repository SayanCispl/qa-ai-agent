import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer


class VectorStore:
    def __init__(self, persist_dir="vector_db"):
        self.client = chromadb.Client(
            Settings(persist_directory=persist_dir)
        )

        self.collection = self.client.get_or_create_collection(
            name="qa_knowledge"
        )

        self.embedder = SentenceTransformer("all-MiniLM-L6-v2")

    def add(self, text, metadata=None, doc_id=None):
        embedding = self.embedder.encode(text).tolist()

        self.collection.add(
            documents=[text],
            embeddings=[embedding],
            metadatas=[metadata or {}],
            ids=[doc_id or text[:40]]
        )

    def search(self, query, top_k=5):
        query_embedding = self.embedder.encode(query).tolist()

        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )

        return results.get("documents", [[]])[0]
