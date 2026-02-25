import os
import logging
from logging.handlers import RotatingFileHandler
from pythonjsonlogger import jsonlogger
from dotenv import load_dotenv
from rich import print
from src.qa_agent import QAAIAgent


# ----------------------------
# Load Environment Variables
# ----------------------------
load_dotenv()

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
DEBUG_MODE = os.getenv("DEBUG", "false").lower() == "true"


# ----------------------------
# Ensure logs directory exists
# ----------------------------
os.makedirs("logs", exist_ok=True)


# ----------------------------
# Configure Logging
# ----------------------------
logger = logging.getLogger("qa_ai_agent")
logger.setLevel(LOG_LEVEL)

# JSON Formatter
json_formatter = jsonlogger.JsonFormatter(
    "%(asctime)s %(levelname)s %(name)s %(message)s"
)

# File Handler (rotating log)
file_handler = RotatingFileHandler(
    "logs/app.log",
    maxBytes=5 * 1024 * 1024,
    backupCount=3
)
file_handler.setFormatter(json_formatter)

# Console Handler (clean human-readable)
console_handler = logging.StreamHandler()
console_handler.setFormatter(
    logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
)

logger.addHandler(file_handler)
logger.addHandler(console_handler)


# ----------------------------
# Safe Execution Wrapper
# ----------------------------
def safe_execute(func):
    try:
        return func()
    except Exception as e:
        logger.exception("Unhandled exception occurred")
        print("\n[bold red]An unexpected error occurred. Check logs/app.log[/bold red]")


# ----------------------------
# Main CLI Runner
# ----------------------------
def run():
    logger.info("QA AI Agent started", extra={"debug_mode": DEBUG_MODE})

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
            safe_execute(lambda: print(
                agent.generate_test_cases(input("\nEnter requirement:\n"))
            ))

        elif choice == "2":
            safe_execute(lambda: print(
                agent.review_test_cases(input("\nPaste test cases:\n"))
            ))

        elif choice == "3":
            safe_execute(lambda: print(
                agent.analyze_bug(input("\nPaste bug report:\n"))
            ))

        elif choice == "4":
            safe_execute(lambda: print(
                agent.analyze_logs(input("\nPaste logs/errors:\n"))
            ))

        elif choice == "5":
            safe_execute(lambda: print(
                agent.create_checklist(input("\nEnter feature name:\n"))
            ))

        elif choice == "6":
            def handle_rag():
                question = input("\nAsk your QA question:\n")

                logger.info(
                    "RAG query received",
                    extra={
                        "query": question,
                        "debug_mode": DEBUG_MODE
                    }
                )

                answer = agent.ask_with_rag(question)

                print("\n[bold green]RAG Answer:[/bold green]\n")
                print(answer)

            safe_execute(handle_rag)

        elif choice == "7":
            def handle_memory():
                query = input("\nSearch QA memory:\n")

                logger.info(
                    "Memory search",
                    extra={
                        "query": query,
                        "debug_mode": DEBUG_MODE
                    }
                )

                results = agent.search_memory(query)

                print("\n[bold yellow]Relevant past knowledge:[/bold yellow]")
                for r in results:
                    print("-", r)

            safe_execute(handle_memory)

        elif choice == "8":
            logger.info("QA AI Agent stopped")
            print("\n[bold red]Exiting QA AI Agent...[/bold red]")
            break

        else:
            print("\n[red]Invalid option. Please try again.[/red]")