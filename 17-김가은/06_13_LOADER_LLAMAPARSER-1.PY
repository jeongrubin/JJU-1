from langchain_upstage import UpstageLayoutAnalysisLoader
import os

# Upstage API 키 설정
UPSTAGE_API_KEY = ""  # 실제 API 키로 교체

# 파일 경로
file_path = r"C:\Users\PC\전주대학교_인공지능학과\실무인재(겨율특강)\SUB\DATA_ALL\2024년12월 급(상)여 명세표.PDF"

# 문서 로더 설정
loader = UpstageLayoutAnalysisLoader(
    file_path,
    output_type="html",
    split="page",  # 'spilt' 대신 'split'
    use_ocr=True,
    exclude=["header", "footer"],
    api_key=UPSTAGE_API_KEY,
)

# 문서 로드
docs = loader.load()

# 결과 출력
for doc in docs[:3]:
    print(doc)
