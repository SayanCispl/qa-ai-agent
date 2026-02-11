"""
QA AI Agent Core Module
-----------------------

This module acts as the central controller of the application.

Responsibilities:
- Initialize all core components (Vector Store, LLM, RAG)
- Handle direct LLM-based QA tasks
- Handle RAG-based knowledge retrieval
- Provide clean interface for main.py

This keeps main.py simple and maintains separation of concerns.
"""

from src.vector_store import VectorStore
from src.ollama_client import OllamaClient
from src.rag import RAGPipeline
# Prompt templates for structured QA tasks
from src.prompts import (
    TEST_CASE_PROMPT,
    REVIEW_TEST_CASE_PROMPT,
    BUG_ANALYSIS_PROMPT,
    LOG_ANALYSIS_PROMPT,
    CHECKLIST_PROMPT
)


class QAAIAgent:
    """
       Main QA AI Agent class.

       This class orchestrates:
       - Direct LLM-based generation tasks
       - RAG-based contextual question answering
       - Semantic search over QA memory
       """
    def __init__(self):
        """
               Initialize all core components.

               Components:
               - VectorStore → Handles QA knowledge storage & retrieval
               - OllamaClient → Sends prompts to local LLM
               - RAGPipeline → Handles context injection before answering
               """

        # Initialize vector database
        self.vector_store = VectorStore()
        # Initialize local LLM client (Ollama)
        self.llm = OllamaClient()
        # Initialize RAG pipeline with vector store + LLM
        self.rag = RAGPipeline(self.vector_store, self.llm)
        # =====================================================
        # DIRECT LLM TASKS (No RAG)
        # =====================================================

    def generate_test_cases(self, requirement):
        """
                Generate detailed test cases from a requirement.

                Flow:
                1. Inject requirement into structured prompt template
                2. Send prompt to LLM
                3. Return generated test cases
                """
        prompt = TEST_CASE_PROMPT.format(input=requirement)
        return self.llm.generate(prompt)

    def review_test_cases(self, test_cases):
        """
                Review existing test cases.

                Flow:
                1. Insert test cases into review prompt
                2. LLM analyzes gaps, missing edge cases, improvements
                """
        prompt = REVIEW_TEST_CASE_PROMPT.format(input=test_cases)
        return self.llm.generate(prompt)

    def analyze_bug(self, bug_report):
        """
               Analyze a bug report.

               LLM typically:
               - Identifies possible root cause
               - Suggests regression scenarios
               - Recommends additional tests
               """
        prompt = BUG_ANALYSIS_PROMPT.format(input=bug_report)
        return self.llm.generate(prompt)

    def analyze_logs(self, logs):
        """
                Analyze logs or error messages.

                Useful for:
                - Root cause hints
                - Failure pattern detection
                - Suggested debugging approach
                """
        prompt = LOG_ANALYSIS_PROMPT.format(input=logs)
        return self.llm.generate(prompt)

    def create_checklist(self, feature):
        """
               Generate QA checklist for a feature.

               Typically includes:
               - Functional coverage
               - Edge cases
               - Negative scenarios
               - Non-functional considerations
               """
        prompt = CHECKLIST_PROMPT.format(input=feature)
        return self.llm.generate(prompt)

    # =====================================================
    # RAG-BASED TASKS (Context-Aware)
    # =====================================================

    def ask_with_rag(self, question):
        """
                Ask a question using Retrieval-Augmented Generation.

                Flow:
                1. Search vector DB for relevant QA knowledge
                2. If nothing found → block hallucination
                3. Inject retrieved context into LLM prompt
                4. Return grounded answer
                """

        return self.rag.answer(question)

    def search_memory(self, query):
        """
                Perform direct semantic search in QA knowledge base.

                This does NOT call LLM.
                It only returns matching stored documents.

                Useful for:
                - Exploring stored QA docs
                - Debugging RAG behavior
                """
        return self.vector_store.search(query)
