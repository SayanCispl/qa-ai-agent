from agent.qa_agent import QAAIAgent
from rich import print

agent = QAAIAgent()

while True:
    print("\n[bold cyan]QA AI Agent[/bold cyan]")
    print("1. Generate Test Cases from Requirement")
    print("2. Review Existing Test Cases")
    print("3. Analyze Bug Report")
    print("4. Analyze Logs / Errors")
    print("5. Create QA Checklist")
    print("6. Ask QA Question (RAG)")
    print("7. Search QA Memory")
    print("8. Exit")

    choice = input("\nSelect option: ")

    if choice == "1":
        req = input("\nEnter requirement:\n")
        print(agent.generate_test_cases(req))

    elif choice == "2":
        tc = input("\nPaste test cases:\n")
        print(agent.review_test_cases(tc))

    elif choice == "3":
        bug = input("\nPaste bug report:\n")
        print(agent.analyze_bug(bug))

    elif choice == "4":
        logs = input("\nPaste logs/errors:\n")
        print(agent.analyze_logs(logs))

    elif choice == "5":
        feature = input("\nEnter feature name:\n")
        print(agent.create_checklist(feature))

    elif choice == "6":
        question = input("\nAsk your QA question:\n")
        answer = agent.ask_with_rag(question)
        print("\nRAG Answer:\n")
        print(answer)


    elif choice == "7":
        query = input("\nSearch QA memory:\n")
        results = agent.search_memory(query)
        print("\nRelevant past knowledge:")
        for r in results:
            print("-", r)


    elif choice == "8":
        break
