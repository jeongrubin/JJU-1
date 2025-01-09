import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import load_prompt

def answerfromllm():
    # .env 파일 로드
    load_dotenv()

    # 환경 변수 가져오기
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    LANGCHAIN_API_KEY = os.getenv("LANGCHAIN_API_KEY")
    LANGCHAIN_TRACING_V2 = os.getenv("LANGCHAIN_TRACING_V2")
    LANGCHAIN_ENDPOINT = os.getenv("LANGCHAIN_ENDPOINT")
    LANGCHAIN_PROJECT = os.getenv("LANGCHAIN_PROJECT")

    # LLM 초기화
    llm = ChatOpenAI(
        model="gpt-4o",
        max_tokens=None,
        timeout=None,
        max_retries=1,
        temperature=0,
        api_key=OPENAI_API_KEY
    )

    # YAML 파일 로드
    prompt_yaml = load_prompt(
        "06-배진우/2024_겨울특강/과제/code/2025_01_09/PromptTemplate.yaml",
        encoding="UTF-8"
    )

    # 체인 생성 (PromptTemplate → LLM)
    chain = prompt_yaml | llm

    # 콘솔 입력받아 prompt_yaml에 변수 삽입 (fruit → topic)
    user_topic = input("요약하고 싶은 과학 발견의 주제를 입력하세요: ")
    formatted_prompt = prompt_yaml.format(topic=user_topic)

    # LLM 호출
    response = chain.invoke(formatted_prompt).content

    # 결과 출력
    print(response)

    with open("06-배진우/2024_겨울특강/과제/code/2025_01_09/answerfromllm.txt", "w", encoding="utf-8") as f:
        f.write(response)
    print("answerfromllm.txt 파일이 생성되었습니다.")

if __name__ == "__main__":
    answerfromllm()
