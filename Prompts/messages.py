from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")


messages = [
    SystemMessage(content="You are a helpful assistant that provides information about research papers."),
    HumanMessage(content="What is the main contribution of the paper 'Attention Is All You Need'?"),
    ]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))
print(result.content)