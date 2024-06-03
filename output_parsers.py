from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser, CommaSeparatedListOutputParser, JsonOutputParser
from langchain_core.pydantic_v1 import BaseModel,Field

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
  
print(type(call_string_output_parser()))

def call_list_output_parser():
  prompt = ChatPromptTemplate.from_messages([
    ('system','Generate a list of 10 synonyms for the following word.'
              'Return the results as a comma separated values'),
    ('human','{input}')
  ])
  parser = CommaSeparatedListOutputParser()
  
  chain = prompt | model | parser
  
  return chain.invoke(
    {
      "input": "happy"
    }
  )
  
print(call_list_output_parser())
print(type(call_list_output_parser()))

def call_json_output_parser():
  prompt = ChatPromptTemplate.from_messages([
    ('system','Extract information from the following phrase.\nFormatting Instructions: {format_instructions}'),
    ('human','{phrase}')
  ])
  
  class Person(BaseModel):
    recipe: str = Field(description='The name of Recipe')
    ingredients: list = Field(description='Ingrdients')
  
  parser = JsonOutputParser(pydantic_object=Person)
  
  chain = prompt | model | parser
  
  return chain.invoke(
    {
      'format_instructions': parser.get_format_instructions(),
      "phrase": "The ingredients for a margherita pizza are tomatoes, onions, cheese,basil "
    }
  )
  
print(call_json_output_parser())
  
  