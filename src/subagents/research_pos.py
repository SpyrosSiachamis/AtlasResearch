from typing import Any, Mapping, cast

from langchain.agents import create_agent
from langchain_core.runnables import RunnableConfig
from providers.provider import ollama_model, google_model
from agent.tools.web_search import create_search_tool
from langgraph.checkpoint.memory import InMemorySaver  
import time
SYSTEM_INSTRUCTION="""
    You are a research assistant agent.
    
    Use web searches strategically to gather evidence for your 10 points.
    Prioritize distinct research dimensions and credible primary sources.
    Do not repeat a search if it substantially overlaps with an earlier query.
    Each search should investigate a new claim, evidence source, or technical dimension.
    You may support multiple points using evidence from the same search.
    Once you have sufficient evidence or exhaust your search budget, stop searching
    and produce your report using the evidence collected so far.
    Include source URLs for factual claims.

    Do not search topics unrelated to the specific topic.
    
    Focus only on supporting the specified topic, do not make comparisons that could support the other point. Explain why you support this argument compared to the latter.
    
    Return your 10-point research when completed.
"""

search_tool = create_search_tool("POSITIVE", max_calls=6)
def call_research_pos(command:str):
    thread_config: RunnableConfig = {"configurable": {"thread_id": "2"}}
    config: RunnableConfig = {
        **thread_config,
        "recursion_limit": 25,
    }
    research_pos = create_agent(
        model=(ollama_model),
        system_prompt=SYSTEM_INSTRUCTION,
        tools=[search_tool],
        checkpointer=InMemorySaver()
    )

    result = research_pos.invoke(
        {"messages": [{"role": "user", "content": command}]},
        config, 
    )
    return result