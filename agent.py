import asyncio

from LLM import client

report_agent = client.chat.completions.create(
    name="Report Generator",
    instructions="Expert writer and synthesizer. Uses the provided information snippets to formulate a comprehensive, high-quality answer for the end-user",
    model="gpt-5-mini",
)



