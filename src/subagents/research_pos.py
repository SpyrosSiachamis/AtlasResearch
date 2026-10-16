from langchain.agents import create_agent
from langchain_core.runnables import RunnableConfig
from providers.provider import ollama_model, google_model
from agent.tools.web_search import search_web
from langgraph.checkpoint.memory import InMemorySaver  

SYSTEM_INSTRUCTION="""
    You are a research assistant agent.
    
    Always use your web search tool when looking for positive points.
    Always search separately for each point.

    Your goal state is to formulate 10 positive points for the specified topic.

    Do not search topics unrelated to the specific topic.
    
    Focus only on supporting the specified topic, do not make comparisons that could support the other point. Explain why you support this argument compared to the latter.
    
    Return your 10-point research when completed.
"""
provider = input(f"Choose Provider: {1} for Ollama, {2} for Google")

thread_config: RunnableConfig = {"configurable": {"thread_id": "1"}}
research_pos = create_agent(
    model=(ollama_model if provider == 0 else google_model),
    system_prompt=SYSTEM_INSTRUCTION,
    tools=[search_web],
    checkpointer=InMemorySaver()
)
print(f"Chosen Provider: {'Ollama' if int(provider) == 0 else 'Google'}")
prompt = input("Enter research topic: ")



for chunk in research_pos.stream(
    {"messages": [{"role": "user", "content": prompt}]},
    thread_config,
    stream_mode="updates",
):
    for node, update in chunk.items():
        for msg in update["messages"]:
            msg.pretty_print()
# print(result["messages"][-1].text)