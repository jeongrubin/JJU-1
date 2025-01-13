import os
os.environ["OPENAI_API_KEY"] = ""

os.environ["LANGCHAIN_API_KEY"] = ""
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"
os.environ["LANGCHAIN_PROJECT"] = "test_JJU_YEOMYEONGGU"

from langchain_openai import ChatOpenAI
from langchain_core.prompts import load_prompt

# ======================
# LangChain OpenAI 모델 초기화
# ======================
llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

# ======================
# YAML 파일 경로 및 프롬프트 로드
# ======================
yaml_file_path = r"10_여명구\02_Prompt\person_intro.yaml"
prompt = load_prompt(yaml_file_path, encoding="utf-8")

# ======================
# 프롬프트 생성 및 모델 연결
# ======================
formatted_prompt = prompt.format(name="알버트 아인슈타인")
chain = prompt | llm

# ======================
# 결과 출력
# ======================
result = chain.invoke({"name": "아이작 뉴턴"})
print("Generated Response:")
print(result.content)