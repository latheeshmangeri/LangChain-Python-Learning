from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def get_documents_from_web(url):
  loader = WebBaseLoader(url)
  docs = loader.load()
  
  splitter = RecursiveCharacterTextSplitter(
    chunk_size = 200,
    chunk_overlap = 20
  )
  
  splitDocs = splitter.split_documents(docs)
  print(len(splitDocs))
  return splitDocs

docs = get_documents_from_web('https://python.langchain.com/v0.1/docs/expression_language/')

model = ChatOpenAI(
  model_name="gpt-3.5-turbo-16k",
  temperature=0.7
)

prompt = ChatPromptTemplate.from_template(
  """
  Answer the user's question:
  Context: {context}
  Question: {input}
  """
)

chain = create_stuff_documents_chain(
  llm=model,
  prompt=prompt
)

response = chain.invoke({
  "input": "What is LCEL?",
  "context": docs
})

print(response)

