from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate.from_messages([
    ('system',"You are a helpful {domain} expert in research papers."),
    ("topic","Explain in simple terms, what is {topic}?")
])

prompt = chat_template.invoke({
    'domain': 'AI',
    'topic': 'Attention Is All You Need'
})

print(prompt)
