import os
import subprocess

os.environ['OPENAI_API_KEY'] = ""

from langchain_teddynote.messages import stream_response
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

template = "{country}의 수도는 어디인가요?"

prompt_template = PromptTemplate(
    template=template,
    input_variables=["country"]
)

print(prompt_template)

prompt = prompt_template.format(country="대한민국")
print(prompt)

prompt = prompt_template.format(country="미국")
print(prompt)

model = ChatOpenAI(
    model="gpt-3.5-turbo",
    max_tokens=2048,
    temperature=0.1
)

prompt = PromptTemplate.from_template("{topic}에 대해 쉽게 설명해주세요.")

chain = prompt | model

input_data = {"topic": "인공지능 모델의 학습 원리"}

output = chain.invoke(input_data)
print(output)
