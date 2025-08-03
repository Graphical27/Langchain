from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")


chat_history = [
    SystemMessage(content="You are a helpful Chat Bot."),
    
]
while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(user_input))
    if user_input.lower() == 'exit':
        print("Exiting the chatbot. Goodbye!")
        break
    response = model.invoke(chat_history)
    chat_history.append(AIMessage(response.content))
    print(response.content)

print(chat_history)