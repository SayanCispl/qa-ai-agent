TEST_CASE_PROMPT = """
You are a QA engineer.
Generate detailed test cases for the following requirement:

Requirement:
{input}
"""

REVIEW_TEST_CASE_PROMPT = """
Review the following test cases.
Identify gaps, edge cases, and improvements.

Test Cases:
{input}
"""

BUG_ANALYSIS_PROMPT = """
Analyze the following bug report.
Identify root cause, impact, and suggested test scenarios.

Bug Report:
{input}
"""

LOG_ANALYSIS_PROMPT = """
Analyze the following logs/errors and explain the issue.

Logs:
{input}
"""

CHECKLIST_PROMPT = """
Create a QA checklist for the following feature:

Feature:
{input}
"""

RAG_PROMPT = """
You are a QA Assistant.

Use ONLY the context below to answer.
If not found, say: "Not found in QA knowledge."

Context:
{context}

Question:
{question}

Answer:
"""
