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

# Loader 매핑
loader_mapping = {
    "PDF": [load_with_pypdf, load_with_pymupdf, load_with_pypdfium, load_with_pdfminer, load_with_pdfplumber],
    "HWP": [load_with_hwp],
    "CSV": [load_with_csv],
    "Excel": [load_with_excel],
    "Text": [load_with_text],
    "JSON": [load_with_json],
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

if __name__ == "__main__":
    file_path = "/workspaces/JJU-1/04-유상민/250107과제_2/SPRI_AI_Brief_2023년12월호_F.pdf"

    file_type = detect_file_type(file_path)
    print(f"파일 유형: {file_type}")

    try:
        result = load_file(file_path, file_type)
        print("Loader 결과:")
        for i, res in enumerate(result, 1):
            print(f"Loader {i} 결과: {res}")
    except Exception as e:
        print(f"Error 발생: {e}")
