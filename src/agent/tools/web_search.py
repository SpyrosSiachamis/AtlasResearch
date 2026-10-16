from tavily import TavilyClient
import os
from dotenv import load_dotenv
from langchain.tools import tool
load_dotenv()

t_client = TavilyClient(api_key=os.getenv("TAVILI_API_KEY"))

@tool(description="A tool that searches the internet. It takes a parameter q: str where q is the search query. it returns the entire response")
def search_web(q: str):
    print(q)
    response = t_client.search(q)
    return(response)