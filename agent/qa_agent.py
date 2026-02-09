from agent.ollama_client import ask_llm
from agent.prompts import *
from agent.vector_store import QAVectorStore

class QAAIAgent:

    def __init__(self):
        self.memory = QAVectorStore()

    def generate_test_cases(self, requirement: str):
        self.memory.add_document(
            requirement,
            metadata={"type": "requirement"}
        )
        return ask_llm(SYSTEM_QA_PROMPT, requirement_to_testcases(requirement))

    def review_test_cases(self, test_cases: str):
        self.memory.add_document(
            test_cases,
            metadata={"type": "test_cases"}
        )
        return ask_llm(SYSTEM_QA_PROMPT, review_test_cases(test_cases))

    def analyze_bug(self, bug: str):
        self.memory.add_document(
            bug,
            metadata={"type": "bug"}
        )
        return ask_llm(SYSTEM_QA_PROMPT, analyze_bug_report(bug))

    def analyze_logs(self, logs: str):
        self.memory.add_document(
            logs,
            metadata={"type": "logs"}
        )
        return ask_llm(SYSTEM_QA_PROMPT, analyze_logs(logs))

    def search_memory(self, query: str):
        return self.memory.search(query)

    def ask_with_rag(self, question: str):
        context = self.memory.search(question)

        if not context.strip():
            return "No relevant QA knowledge found."

        prompt = rag_prompt(context, question)
        return ask_llm(SYSTEM_QA_PROMPT, prompt)

