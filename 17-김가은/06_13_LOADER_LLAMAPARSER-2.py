import os
import nest_asyncio

LLAMA_CLOUD_API_KEY = ""
nest_asyncio.apply()

from llama_parse import LlamaParse
from llama_index.core import SimpleDirectoryReader

# LlamaParse 설정
parser = LlamaParse(
    result_type="markdown",  # "markdown" 또는 "text" 사용 가능
    num_workers=8,  # worker 수 (기본값: 4)
    verbose=True,
    language="ko",
    api_key=LLAMA_CLOUD_API_KEY,
)

# 파일 경로 설정 (문자열로 지정)
file_path = r"C:\Users\PC\전주대학교_인공지능학과\실무인재(겨율특강)\SUB\DATA_ALL\2024년12월 급(상)여 명세표.PDF"

# 파일 존재 여부 확인
if not os.path.exists(file_path):
    raise FileNotFoundError(f"파일이 존재하지 않습니다: {file_path}")

# SimpleDirectoryReader를 사용하여 파일 파싱
file_extractor = {".pdf": parser}

# 문서 로드
documents = SimpleDirectoryReader(
    input_files=[file_path],
    file_extractor=file_extractor,
).load_data()

# 문서 개수 확인
print(f"총 문서 개수: {len(documents)}")

# 문서 내용 출력
for doc in documents[:3]:  # 처음 3개의 문서 출력
    print(doc)
