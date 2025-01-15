"""
csvLoader.py
- CSV 파일을 직접 열어서 파싱하는 로직.
"""

from langchain_community.document_loaders.csv_loader import CSVLoader

def load_csv(file_path: str):
    # CSV 로더 생성
    loader = CSVLoader(file_path=file_path)

    # 데이터 로드
    docs = loader.load()
    return docs

if __name__ == "__main__":
    file_path = "/workspaces/JJU-1/06-배진우/2024_겨울특강/91_Practice_Project/02_LoderSplitterPackege/FileLoder/data/서울2019년기상정보.csv"
    print(load_csv(file_path))