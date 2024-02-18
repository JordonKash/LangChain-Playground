from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

## grab my openai api key from .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

chat = ChatOpenAI(openai_api_key=api_key)

chat_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a bot that helps people express their accomplishments in working in a team, using less than 10 words {name}."),
        ("human", "Hello, how are you doing?"),
        ("ai", "I'm doing well, thanks!"),
        ("human", "{user_input}"),
    ]
)
messages = chat_template.format_messages(name="Bob", user_input="Jim (born 1958/1959)[2] is an American microprocessor engineer best known for his work at AMD and Apple. He was the lead architect of the AMD K8 microarchitecture[3][4][5] (including the original Athlon 64)[3][6][7] and was involved in designing the Athlon (K7)[5] and Apple A4/A5 processors.[3][8][9][10] He was also the coauthor of the specifications for the x86-64 instruction set[8][11] and HyperTransport interconnect.[3][11][12] From 2012 to 2015 he returned to AMD to work on the AMD K12[13] and Zen microarchitectures.[14][15]")
# From:https://en.wikipedia.org/wiki/Jim_Keller_(engineer)
answer = chat.invoke(messages)

print(answer.content)

