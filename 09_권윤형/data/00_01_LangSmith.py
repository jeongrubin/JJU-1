# import os

# os.environ['OPENAI_API_KEY'] = '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'
# os.environ['LANGCHAIN_API_KEY'] = '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' # 본인 api
# os.environ['LANGCHAIN_TRACING_V2'] = 'true'
# os.environ['LANGCHAIN_ENDPOINT'] = 'https://api.smith.langchain.com'
# os.environ['LANGCHAIN_PROJECT'] = 'test_JJU_KwonYunHyeong'  # 본인 프로젝트

# from langchain_openai import ChatOpenAI

# llm = ChatOpenAI()

# print(llm.invoke("펩시가 맛있어? 코카콜라가 맛있어?"))

#OPENAI_API_KEY = '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'
LANGCHAIN_TRACING_V2 = True
LANGCHAIN_ENDPOINT="https://api.smith.langchain.com"
LANGCHAIN_API_KEY="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"
LANGCHAIN_PROJECT="test_JJU_KwonYunHyeong"

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    api_key= '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'
)
print(llm.invoke("펩시가 맛있어? 코카콜라가 맛있어?"))