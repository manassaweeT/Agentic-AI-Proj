from agents import Runner
from agent import report_agent

def main():
    while True:
        question = input("\nAsk a question (or type 'exit'): ")
        if question.lower() == "exit":
            break
        result = Runner.run_sync(
            report_agent,
            question
        )

        print("\nAnswer:")
        print(result.final_output)

main()

