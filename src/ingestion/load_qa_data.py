import os
from src.vector_store import VectorStore

if __name__ == "__main__":
    print("Initializing Vector Store...")
    vs = VectorStore()

    # Go one level UP from src to project root
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    qa_data_path = os.path.join(base_dir, "qa_data")

    print("Loading from path:", qa_data_path)

    vs.load_documents_from_folder(qa_data_path)

    print("Total documents in collection:",
          vs.collection.count())

    print("✅ All documents loaded successfully into ChromaDB!")
