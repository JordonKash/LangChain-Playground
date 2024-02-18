from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

## grab my openai api key from .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

chat = ChatOpenAI(openai_api_key=api_key)

answer = chat.invoke("What is the population of San Fransico?")
print(answer.content)

