from langchain_openai import ChatOpenAI
from langchain.prompts import load_prompt
from dotenv import load_dotenv
import os

# api key, 다른 것들 불러오기
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
LANGCHAIN_API_KEY = os.getenv("LANGCHAIN_API_KEY")
LANGCHAIN_TRACING_V2 = os.getenv("LANGCHAIN_TRACING_V2")
LANGCHAIN_ENDPOINT = os.getenv("LANGCHAIN_ENDPOINT")
LANGCHAIN_PROJECT = os.getenv("LANGCHAIN_PROJECT")

# llm 설정
llm = ChatOpenAI(
    model='gpt-4o',
    temperature=0,
    max_tokens=None, # 보통 2000개 정도가 적당함
    timeout=None,
    max_retries=2,
)

# yaml 파일 불러오기
prompt_yaml = load_prompt("C:\Users\eys63\Desktop\기타활동\2024\겨울방학\JJU\01-이연승\과제\25_01_09\PROMPTTEMPLATE.yaml", encoding='utf-8')

# chain 생성
chain = prompt_yaml | llm