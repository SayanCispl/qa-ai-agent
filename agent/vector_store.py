import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer
import uuid

class QAVectorStore:

    def __init__(self):
        self.client = chromadb.Client(
            Settings(persist_directory="data/knowledge")
        )
        self.collection = self.client.get_or_create_collection(
            name="qa_memory"
        )
        self.embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

    def add_document(self, text: str, metadata: dict = None):
        embedding = self.embedding_model.encode(text).tolist()

        self.collection.add(
            ids=[str(uuid.uuid4())],
            documents=[text],
            embeddings=[embedding],
            metadatas=[metadata or {}]
        )

    def search(self, query: str, top_k: int = 3):
        query_embedding = self.embedding_model.encode(query).tolist()

        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )

        documents = results.get("documents", [[]])[0]

        # Merge into single context block
        return "\n\n".join(documents)

