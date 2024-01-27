from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
llm = Ollama(model="llama2")

output_parser = StrOutputParser()

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are world class technical documentation writer."),
    ("user", "{input}")
])

chain = prompt | llm | output_parser
print(chain.invoke({"input":"how can react help with front end dev?"}))