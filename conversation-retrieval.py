from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores.faiss import FAISS
from langchain.chains import create_retrieval_chain

def get_documents_from_web(url):
  loader = WebBaseLoader(url)
  docs = loader.load()
  
  splitter = RecursiveCharacterTextSplitter(
    chunk_size = 400,
    chunk_overlap = 20
  )
  
  splitDocs = splitter.split_documents(docs)
  print(len(splitDocs))
  return splitDocs

def create_vector(docs):
  embedding = OpenAIEmbeddings()
  vectorStore = FAISS.from_documents(docs, embedding=embedding)
  return vectorStore

def create_chain(vectorStore):
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
  
  retriever = vectorStore.as_retriever(search_kwargs={'k':3})
  
  retrieval_chain = create_retrieval_chain(
    retriever,
    chain
  )
  return retrieval_chain

def process_chat():
  response = chain.invoke({
    "input": question,
  })
  return response['answer']

if __name__ == '__main__':
  docs = get_documents_from_web('https://python.langchain.com/v0.1/docs/expression_language/')
  vectorStore = create_vector(docs)
  chain = create_chain(vectorStore)
  
  user_input = input("You: ")
  response = process_chat(chain,user_input)
  print("Assisstant: ",response)

