from tavily import TavilyClient
import os
from dotenv import load_dotenv
from langchain.tools import tool
load_dotenv()

t_client = TavilyClient(api_key=os.getenv("TAVILI_API_KEY"))

def create_search_tool(researcher_name: str, max_calls: int = 6):
    calls_used = 0

    @tool(description="Search the internet for a query using Tavily.")
    def search_web(q: str) -> str:
        nonlocal calls_used

        if calls_used >= max_calls:
            print(
                f"[{researcher_name}] Search budget exhausted "
                f"({max_calls}/{max_calls})"
            )
            return (
                f"Search budget exhausted ({max_calls} searches). "
                "Stop searching and produce your report using the "
                "evidence collected so far."
            )

        calls_used += 1
        print(
            f"[{researcher_name}] "
            f"Search {calls_used}/{max_calls}: {q}",
            flush=True,
        )

        response = t_client.search(q)
        return str(response)

    return search_web