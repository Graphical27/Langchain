from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

chat_template = ChatPromptTemplate.from_messages([
    ('system', "You are a helpful {domain} expert in research papers."),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human', "Explain in simple terms, what is {topic}?"),])


chat_history = []
with open('chat_history.txt') as f:
    chat_history.extend(f.readlines())

print(chat_history)

chat_temp = chat_template.invoke({'chat_history': chat_history, 'domain': 'AI', 'topic': 'Attention Is All You Need'})

print(chat_temp)
