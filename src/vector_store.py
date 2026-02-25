import os
import uuid
import yaml
import chromadb
from chromadb.config import Settings
from chromadb.utils import embedding_functions


class VectorStore:
    def __init__(self):
        # ✅ Absolute project root path
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        persist_path = os.path.join(base_dir, "chroma_db")

        print("Chroma persist path:", persist_path)

        # ✅ Persistent Chroma client
        self.client = chromadb.Client(
            Settings(
                persist_directory=persist_path,
                is_persistent=True
            )
        )

        # ✅ Embedding function
        self.embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        # ✅ SINGLE collection name (very important)
        self.collection = self.client.get_or_create_collection(
            name="qa_collection",
            embedding_function=self.embedding_function
        )

        print("Collection document count:", self.collection.count())

    # ----------------------------
    # ADD DOCUMENT WITH METADATA
    # ----------------------------
    def add_document(self, document: str, metadata: dict):

        if not metadata:
            metadata = {"source": "unknown"}

        self.collection.add(
            documents=[document],
            metadatas=[metadata],
            ids=[str(uuid.uuid4())]
        )

    # ----------------------------
    # BULK LOAD FROM qa_data FOLDER (Reset Collection)
    # ----------------------------
    def load_documents_from_folder(self, folder_path: str):
        """
        Load all .md files from qa_data folder.
        Clears existing collection before reloading
        to prevent duplicate embeddings.
        """

        print("Loading documents from:", folder_path)

        # 🔥 Step 1: Clear existing collection
        current_count = self.collection.count()
        if current_count > 0:
            print(f"Clearing existing collection ({current_count} documents)...")
            self.collection.delete(where={})
            print("Collection cleared.")

        total_chunks_added = 0

        # 🔥 Step 2: Load all markdown files
        for root, _, files in os.walk(folder_path):
            for file in files:
                if file.endswith(".md"):
                    full_path = os.path.join(root, file)
                    print("Processing:", file)

                    with open(full_path, "r", encoding="utf-8") as f:
                        content = f.read()

                        metadata, body = self._extract_metadata(content)

                        # Add filename into metadata (good practice)
                        metadata["file_name"] = file

                        chunks = self._chunk_text(body)

                        for chunk in chunks:
                            self.add_document(chunk, metadata)
                            total_chunks_added += 1

        # 🔥 Step 3: Final count
        final_count = self.collection.count()
        print(f"Total chunks added: {total_chunks_added}")
        print(f"Final document count in DB: {final_count}")
        print("QA knowledge base successfully refreshed.")

    # ----------------------------
    # SEARCH WITH OPTIONAL FILTER
    # ----------------------------
    def search(self, query: str, top_k: int = 5, where: dict = None):

        print("Searching DB... Total docs:", self.collection.count())

        if where:
            results = self.collection.query(
                query_texts=[query],
                n_results=top_k,
                where=where
            )
        else:
            results = self.collection.query(
                query_texts=[query],
                n_results=top_k
            )

        if results and results.get("documents"):
            return results["documents"][0]

        return []

    # ----------------------------
    # EXTRACT YAML FRONT MATTER
    # ----------------------------
    def _extract_metadata(self, content: str):

        metadata = {}
        body = content

        if content.startswith("---"):
            try:
                parts = content.split("---", 2)
                metadata = yaml.safe_load(parts[1]) or {}
                body = parts[2]
            except Exception as e:
                print("Metadata parsing error:", e)
                metadata = {}

        cleaned_metadata = {}
        for key, value in metadata.items():
            if isinstance(value, (str, int, float, bool)):
                cleaned_metadata[key] = value
            else:
                cleaned_metadata[key] = str(value)

        return cleaned_metadata, body

    # ----------------------------
    # SIMPLE TEXT CHUNKING
    # ----------------------------
    def _chunk_text(self, text: str, chunk_size: int = 800):

        paragraphs = text.split("\n\n")
        chunks = []
        current_chunk = ""

        for para in paragraphs:
            if len(current_chunk) + len(para) < chunk_size:
                current_chunk += para + "\n\n"
            else:
                chunks.append(current_chunk.strip())
                current_chunk = para + "\n\n"

        if current_chunk:
            chunks.append(current_chunk.strip())

        return chunks