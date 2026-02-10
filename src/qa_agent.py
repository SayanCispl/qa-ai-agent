from src.vector_store import VectorStore
from src.ollama_client import OllamaClient
from src.rag import RAGPipeline
from src.prompts import (
    TEST_CASE_PROMPT,
    REVIEW_TEST_CASE_PROMPT,
    BUG_ANALYSIS_PROMPT,
    LOG_ANALYSIS_PROMPT,
    CHECKLIST_PROMPT
)


class QAAIAgent:
    def __init__(self):
        self.vector_store = VectorStore()
        self.llm = OllamaClient()
        self.rag = RAGPipeline(self.vector_store, self.llm)

    def generate_test_cases(self, requirement):
        prompt = TEST_CASE_PROMPT.format(input=requirement)
        return self.llm.generate(prompt)

    def review_test_cases(self, test_cases):
        prompt = REVIEW_TEST_CASE_PROMPT.format(input=test_cases)
        return self.llm.generate(prompt)

    def analyze_bug(self, bug_report):
        prompt = BUG_ANALYSIS_PROMPT.format(input=bug_report)
        return self.llm.generate(prompt)

    def analyze_logs(self, logs):
        prompt = LOG_ANALYSIS_PROMPT.format(input=logs)
        return self.llm.generate(prompt)

    def create_checklist(self, feature):
        prompt = CHECKLIST_PROMPT.format(input=feature)
        return self.llm.generate(prompt)

    def ask_with_rag(self, question):
        return self.rag.answer(question)

    def search_memory(self, query):
        return self.vector_store.search(query)
