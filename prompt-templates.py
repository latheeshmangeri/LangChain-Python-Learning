from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

#Instantiate Model
llm = ChatOpenAI(
  temperature=0.7,
  model='gpt-3.5-turbo-1106'
)

#Prompt Template
prompt = ChatPromptTemplate.from_messages(
  [
    ("system","You are a Brilliant chef. Create a unique recipe based on the following ingredient."),
    ("human","{input}")
  ]
)

prompt = ChatPromptTemplate.from_messages(
  [
    ("system","Generate 10 Synonms for following word. Return response in comma separated values."),
    ("human","{input}")
  ]
)

# Create a LLM Chain
chain = prompt | llm

response = chain.invoke({"input": "Happy"})

print(response.content)
print(type(response.content))