from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

model = ChatOpenAI(
  model_name="gpt-3.5-turbo-1106",
  temperature=0.7
)


def call_string_output_parser():
  prompt = ChatPromptTemplate.from_messages(
    [
      ('system','Tell me a joke about following subject'),
      ('human','{input}')
    ]
  )

  parser = StrOutputParser()
  
  chain = prompt | model | parser

  return chain.invoke({
    'input': 'dog'
  })
  
print(call_string_output_parser())