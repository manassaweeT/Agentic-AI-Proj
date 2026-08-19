from agents import Agent, Runner
from agents.decorators import tool
from search_db import clean, find
from LLM import client

@tool
def get_data(question: str) -> str:
    with open("knowledge_base.txt", "r", encoding="utf-8") as f:
        chunk = f.read()

    question = question.lower().split()
    sen = chunk.lower().split("\n")
    db = clean(sen)
    ques = clean(question)
    result = find(db, ques)

    return str(result)

DB_agent = Agent(
    name="Data Retriever",
    instructions="Expert in information retrieval. Use the get_data tool to search knowledge_base.txt for relevant information. Do not answer the user's question yourself.",
    model="gpt-5-mini",
    tools=[get_data]
)

report_agent = Agent(
    name="Report Generator",
    instructions="""Expert writer and synthesizer. 
    Use the database_searcher tool to retrieve relevant information from the knowledge base. 
    Use the information retrieved from the knowledge base to formulate a clear, concise, and accurate answer to the user's question. 
    Summarize and combine relevant information instead of copying everything.
    Do not invent information that is not contained in the retrieved information.""",
    model="gpt-5-mini",
    tools=[
        DB_agent.as_tool(
            tool_name="database_searcher",
            tool_description="search knowledge database for the relevent description",
        )
    ]
)


# result = Runner.run_sync(
#     report_agent,
#     "What is paracetamol?"
# )

# print(result.final_output)

