from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
import os
from dotenv import load_dotenv
from src.providers.provider import ollama_model 
load_dotenv()

orchestrator_agent = create_agent(model=ollama_model)
prompt = input("Enter prompt: ")
result = orchestrator_agent.invoke(
    {'messages': [{'role': "user", "content": prompt}]}
)
print(result["messages"][-1].content)