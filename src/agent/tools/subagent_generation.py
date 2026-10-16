from langchain.tools import tool
from subagents.research_pos import call_research_pos
from subagents.research_neg import call_research_neg

@tool(description="A positive research subagent. Its goal is to formulate 10 reasons on why the research topic is good.")
async def generate_positive_research_agent(command: str):
    return call_research_pos(command)

@tool(description="A negative research subagent. Its goal is to formulate 10 counter arguments on why the research topic is not good.")
async def generate_negative_research_agent(command: str):
    return call_research_neg(command)