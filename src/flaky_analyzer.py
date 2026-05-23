"""
AI Flaky Test Root Cause Analyzer
---------------------------------

This module detects common flaky automation failures
using AI + semantic reasoning.

Supported:
- Selenium failures
- Playwright failures
- Timeout issues
- Synchronization problems
- Intermittent automation failures
"""

from src.prompts import FLAKY_TEST_PROMPT


class FlakyTestAnalyzer:

    def __init__(self, llm):

        """
        Initialize analyzer with LLM client
        """

        self.llm = llm

    # =====================================================
    # MAIN ANALYZER
    # =====================================================
    def analyze(self, failure_log):

        """
        Analyze flaky automation failure logs
        and generate RCA.
        """

        try:

            # -----------------------------------------
            # BUILD PROMPT
            # -----------------------------------------
            prompt = FLAKY_TEST_PROMPT.format(
                input=failure_log
            )

            # -----------------------------------------
            # GENERATE AI RESPONSE
            # -----------------------------------------
            response = self.llm.generate(prompt)

            # -----------------------------------------
            # RETURN STRUCTURED RESPONSE
            # -----------------------------------------
            return response

        except Exception as e:

            print(
                "Flaky Analyzer Error:",
                e
            )

            return (
                "Failed to analyze flaky "
                "automation issue."
            )