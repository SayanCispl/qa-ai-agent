SYSTEM_QA_PROMPT = """
You are a Senior QA Engineer with strong experience in
manual testing, requirement analysis, and defect management.
You always think in terms of edge cases, risks, and test coverage.
"""

def requirement_to_testcases(requirement: str) -> str:
    return f"""
Analyze the following requirement and generate:
- Functional test cases
- Negative test cases
- Edge cases
- Boundary cases
- Risk areas

Requirement:
{requirement}
"""

def review_test_cases(test_cases: str) -> str:
    return f"""
Review the following test cases and:
- Identify missing scenarios
- Highlight weak test coverage
- Suggest improvements

Test Cases:
{test_cases}
"""

def analyze_bug_report(bug: str) -> str:
    return f"""
Analyze the following bug report and:
- Check clarity and completeness
- Identify missing details
- Suggest improvements
- Suggest possible root cause

Bug Report:
{bug}
"""

def analyze_logs(logs: str) -> str:
    return f"""
Analyze the following logs/errors and:
- Explain the issue in simple terms
- Identify possible root causes
- Suggest next investigation steps

Logs:
{logs}
"""

def qa_checklist(feature: str) -> str:
    return f"""
Create a QA checklist for testing the following feature:

Feature:
{feature}
"""

def rag_prompt(context: str, question: str):
    return f"""
You are a Senior QA Engineer.

Use ONLY the following context to answer.
If the answer is not present, say "Not found in knowledge base".

====================
QA CONTEXT:
{context}
====================

USER QUESTION:
{question}

Provide a clear, structured QA-focused answer.
"""
