import os
from langchain.document_loaders import PyPDFLoader as PyPDFLoaderClass
from langchain.document_loaders import PyMuPDFLoader as PyMuPDFLoaderClass
from langchain_community.document_loaders import PyPDFium2Loader as PyPDFium2LoaderClass
from langchain.document_loaders import PDFMinerLoader as PDFMinerLoaderClass
from langchain_community.document_loaders import PDFPlumberLoader as PDFPlumberLoaderClass
from langchain_teddynote.document_loaders import HWPLoader as HWPLoaderClass
from langchain_community.document_loaders.csv_loader import CSVLoader as CSVLoaderClass
from langchain_community.document_loaders import UnstructuredExcelLoader as UnstructuredExcelLoaderClass
from langchain_community.document_loaders import TextLoader as TextLoaderClass
from langchain_community.document_loaders import JSONLoader as JSONLoaderClass
from bs4 import BeautifulSoup
from langchain.text_splitter import (
    CharacterTextSplitter,
    RecursiveCharacterTextSplitter,
    TokenTextSplitter,
    MarkdownHeaderTextSplitter,
    HTMLHeaderTextSplitter
)

# 1단계: 파일 분류하기
def detect_file_type(file_path):
    _, file_extension = os.path.splitext(file_path)
    file_extension = file_extension.lower()

    file_types = {
        '.pdf': 'PDF',
        '.csv': 'CSV',
        '.xlsx': 'Excel',
        '.xls': 'Excel',
        '.txt': 'Text',
        '.json': 'JSON',
        '.html': 'HTML',
        '.md': 'Markdown',
        '.hwp': 'HWP',
        '.py': 'Python'
    }

    return file_types.get(file_extension, "Unknown File Type")
# --------------------------------------------------------------------------
# 2단계 loader 매핑


# Loader 함수 정의
def load_with_pypdf(file_path):
    loader = PyPDFLoaderClass(file_path)
    docs = loader.load()
    return docs[1].page_content[:1000]

def load_with_pymupdf(file_path):
    loader = PyMuPDFLoaderClass(file_path)
    docs = loader.load()
    return docs[1].page_content[:1000]

def load_with_pypdfium(file_path):
    loader = PyPDFium2LoaderClass(file_path)
    docs = loader.load()
    return docs[1].page_content[:1000]

def load_with_pdfminer(file_path):
    loader = PDFMinerLoaderClass(file_path)
    docs = loader.load()
    return docs[1].page_content[:1000]

def load_with_pdfplumber(file_path):
    loader = PDFPlumberLoaderClass(file_path)
    docs = loader.load()
    return docs[1].page_content[:1000]

def load_with_hwp(file_path):
    loader = HWPLoaderClass(file_path)
    docs = loader.load()
    return docs[0].page_content[:1000]

def load_with_csv(file_path):
    loader = CSVLoaderClass(file_path)
    docs = loader.load()
    return docs[0].page_content[:1000]

def load_with_excel(file_path):
    loader = UnstructuredExcelLoaderClass(file_path)
    docs = loader.load()
    return docs[0].page_content[:1000]

def load_with_text(file_path):
    loader = TextLoaderClass(file_path)
    docs = loader.load()
    return docs[0].page_content[:1000]

def load_with_json(file_path):
    loader = JSONLoaderClass(file_path)
    docs = loader.load()
    return docs[0].page_content[:1000]

def load_with_html(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    soup = BeautifulSoup(html_content, "html.parser")
    sections = []
    for tag in soup.find_all(["h1", "h2", "h3"]):  # 헤더 태그 기준으로 분리
        sections.append(tag.get_text(strip=True))
    return sections

# Loader 매핑
loader_mapping = {
    "PDF": [load_with_pypdf, load_with_pymupdf, load_with_pypdfium, load_with_pdfminer, load_with_pdfplumber],
    "HWP": [load_with_hwp],
    "CSV": [load_with_csv],
    "Excel": [load_with_excel],
    "Text": [load_with_text],
    "JSON": [load_with_json],
    "HTML": [load_with_html],
}

# 3단계: Loader 호출
def load_file(file_path, file_type):
    loaders = loader_mapping.get(file_type)
    if loaders:
        results = []
        for loader in loaders:
            try:
                results.append(loader(file_path))
            except Exception as e:
                results.append(f"Error: {e}")
        return results
    else:
        return f"Error: {file_type}에 적합한 Loader가 없습니다."

# 4단계: TextSplitter 매핑 및 호출 (여러 스플리터 매핑)
splitter_mapping = {
    "PDF": [
        RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=00),
        CharacterTextSplitter(chunk_size=100, chunk_overlap=00),
        TokenTextSplitter(chunk_size=100, chunk_overlap=00)
    ],
    "HWP": [
        RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=00),
        CharacterTextSplitter(chunk_size=100, chunk_overlap=00)
    ],
    "CSV": [
        CharacterTextSplitter(chunk_size=100, chunk_overlap=00)
    ],
    "Excel": [
        CharacterTextSplitter(chunk_size=100, chunk_overlap=00)
    ],
    "Text": [
        RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=00),
        TokenTextSplitter(chunk_size=100, chunk_overlap=00)
    ],
    "JSON": [
        RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=00),
        TokenTextSplitter(chunk_size=100, chunk_overlap=00)
    ],
    # "HTML": [
    #     MarkdownHeaderTextSplitter(headers_to_split=["#", "##", "###"]),
    #     HTMLHeaderTextSplitter()
    # ],
}

def split_texts(file_type, loader_results):
    splitters = splitter_mapping.get(file_type)
    if not splitters:
        raise ValueError(f"{file_type}에 적합한 TextSplitter가 없습니다.")

    split_results = []
    for text in loader_results:
        if isinstance(text, list):  # HTML에서 리스트로 나눠진 경우 처리
            split_results.extend(text)
        elif "Error" not in text:  # 오류가 없는 텍스트만 처리
            for splitter in splitters:  # 여러 스플리터 순차적으로 적용
                split_results.extend(splitter.split_text(text))
    return split_results

if __name__ == "__main__":
    file_path = "/workspaces/JJU-1/04-유상민/250107과제_2/SPRI_AI_Brief_2023년12월호_F.pdf"

    file_type = detect_file_type(file_path)
    print(f"파일 유형: {file_type}")

    try:
        # 3단계: Loader 호출
        loader_results = load_file(file_path, file_type)
        print("Loader 결과:")
        for i, res in enumerate(loader_results, 1):
            print(f"Loader {i} 결과: {res}")

        # 4단계: TextSplitter 호출
        split_results = split_texts(file_type, loader_results)
        print("\nTextSplitter 결과:")
        for i, chunk in enumerate(split_results, 1):
            print(f"Chunk {i}: {chunk}")

    except Exception as e:
        print(f"Error 발생: {e}")
