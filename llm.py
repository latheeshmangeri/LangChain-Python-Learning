from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
  api_key='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'
  )

response = llm.invoke('Hello, How you doing?')

print(response)