from langchain.chat_models import init_chat_model
from langchain_ollama import ChatOllama
import os
from dotenv import load_dotenv


load_dotenv()

google_model = init_chat_model("google_genai:gemini-3.5-flash-lite")
ollama_model = ChatOllama(
    model="qwen3.5:4b",
    base_url="http://100.103.8.27:11434",
    temperature=0,
    num_ctx=8192
)