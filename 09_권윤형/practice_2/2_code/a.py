from langchain_community.document_loaders import PyPDFLoader, PyMuPDFLoader, PyPDFium2Loader, PDFMinerLoader, PDFPlumberLoader
from langchain.document_loaders import CSVLoader
from langchain_teddynote.document_loaders import HWPLoader
from langchain_community.document_loaders import UnstructuredExcelLoader
from langchain_community.document_loaders import TextLoader

def load_pdf(FILE_PATH):
    # 각 로더 초기화
    loader_pypdf = PyPDFLoader(FILE_PATH)
    loader_pymupdf = PyMuPDFLoader(FILE_PATH)
    loader_pypdfium2 = PyPDFium2Loader(FILE_PATH)
    loader_pdfminer = PDFMinerLoader(FILE_PATH)
    loader_plumber = PDFPlumberLoader(FILE_PATH)

    # 각 로더로 PDF 파일을 로드
    docs_pypdf = loader_pypdf.load()
    docs_pymupdf = loader_pymupdf.load()
    docs_pypdfium2 = loader_pypdfium2.load()
    docs_pdfminer = loader_pdfminer.load()
    docs_plumber = loader_plumber.load()

    # 결과를 딕셔너리로 반환
    return {
        'PyPDFLoader': docs_pypdf,
        'PyMuPDFLoader': docs_pymupdf,
        'PyPDFium2Loader': docs_pypdfium2,
        'PDFMinerLoader': docs_pdfminer,
        'PDFPlumber': docs_plumber
    }

def load_hwp(FILE_PATH):
    loader_hwp = HWPLoader(FILE_PATH)
    docs_hwp = loader_hwp.load()
    return docs_hwp

def load_csv(FILE_PATH):
    loader_csv = CSVLoader(FILE_PATH)
    docs_csv = loader_csv.load()
    return docs_csv

def load_excel(FILE_PATH):
    loader_excel = UnstructuredExcelLoader(FILE_PATH)
    docs_excel = loader_excel.load()
    return docs_excel

def load_txt(FILE_PATH):
    loader_txt = TextLoader(FILE_PATH)
    docs_txt = loader_txt.load()
    return docs_txt


def load_txt(FILE_PATH):
    loader_txt = TextLoader(FILE_PATH)
    docs_txt = loader_txt.load()
    return docs_txt

def load_txt(FILE_PATH):
    loader_txt = TextLoader(FILE_PATH)
    docs_txt = loader_txt.load()
    return docs_txt


def load_file(file_path):
    _, file_extension = os.path.splitext(file_path)
    file_extension = file_extension.lower()

    # Mapping file extensions to loader functions
    loaders = {
        '.pdf': load_pdf,
        '.hwp': load_hwp,
        '.csv': load_csv,
        '.xlsx': load_excel,
        '.txt': load_txt,
        '.json': load_json,
        '.md': load_md,
        '.html': load_html,
    }

    if file_extension in loaders:
        return loaders[file_extension](file_path)
    else:
        raise ValueError(f"Unsupported file type: {file_extension}")

# Example usage
file_path = "example.pdf"  # Replace with your file path
try:
    content = load_file(file_path)
    print(content)
except ValueError as e:
    print(e)