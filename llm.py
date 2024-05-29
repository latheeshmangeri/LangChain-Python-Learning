from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

llm = ChatOpenAI(
  model="gpt-3.5-turbo",
  temperature=0.7,
  max_tokens=1000,
  verbose=True
)

response = llm.stream('write a poem about AI')

for chunk in response:
  print(chunk.content,end="",flush=True)

#response = llm.stream('write a poem about AI')
#print(response)