from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv
import os

## grab my openai api key from .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

chat = ChatOpenAI(openai_api_key=api_key)

messages = [
    SystemMessage(content="You give answers that do not exceed 7 words."),
    SystemMessage(content="If someone asks you about the population of a place, tell them you only know the population of New York City."),
    HumanMessage(content="What is the population of San Fransico?"),
]

answer = chat.invoke(messages)

print(answer.content)

