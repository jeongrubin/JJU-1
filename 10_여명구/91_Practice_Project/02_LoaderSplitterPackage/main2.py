# 필요한 모듈 설치 주석 추가
# pip install langchain-community[document_loaders]
# pip install pymupdf pypdf pdfminer pdfium

from langchain_community.document_loader import (
    PyPDFLoader,
    PyMuPDFLoader,
    UnstructuredPDFLoader,
    PDFiumLoader,
    PDFMinerLoader,
    HWPLoader,
    CSVLoader,
    ExcelLoader,
    TextLoader,
    JSONLoader,
    MarkdownLoader,
    CodeLoader,
)

class FileLoader:
    def __init__(self, file_path):
        self.file_path = file_path
    
    def load_pdf_pypdf(self):
        """PDF 파일을 PyPDF로 로드"""
        loader = PyPDFLoader(self.file_path)
        return loader.load()

    def load_pdf_pymupdf(self):
        """PDF 파일을 PyMuPDF로 로드"""
        loader = PyMuPDFLoader(self.file_path)
        return loader.load()

    def load_pdf_unstructured(self):
        """PDF 파일을 UnstructuredPDFLoader로 로드"""
        loader = UnstructuredPDFLoader(self.file_path)
        return loader.load()

    def load_pdf_pypdfium2(self):
        """PDF 파일을 PyPDFium2로 로드"""
        loader = PDFiumLoader(self.file_path)
        return loader.load()

    def load_pdf_pdfminer(self):
        """PDF 파일을 PDFMiner로 로드"""
        loader = PDFMinerLoader(self.file_path)
        return loader.load()
    
    def load_hwp(self):
        """HWP 파일 로드"""
        loader = HWPLoader(self.file_path)
        return loader.load()
    
    def load_csv(self):
        """CSV 파일 로드"""
        loader = CSVLoader(self.file_path)
        return loader.load()
    
    def load_excel(self):
        """Excel 파일 로드"""
        loader = ExcelLoader(self.file_path)
        return loader.load()
    
    def load_txt(self):
        """Text 파일 로드"""
        loader = TextLoader(self.file_path)
        return loader.load()
    
    def load_json(self):
        """JSON 파일 로드"""
        loader = JSONLoader(self.file_path)
        return loader.load()
    
    def load_md(self):
        """Markdown 파일 로드"""
        loader = MarkdownLoader(self.file_path)
        return loader.load()
    
    def load_code(self):
        """Code 파일 로드"""
        loader = CodeLoader(self.file_path)
        return loader.load()
    
    def load_file(self):
        """파일 확장자에 따라 적합한 로더 호출"""
        _, ext = os.path.splitext(self.file_path)
        ext = ext.lower()
        
        if ext == ".pdf":
            # PDF 파일은 다섯 가지 방식 중 하나로 로드 (여기선 PyPDF 예시)
            return self.load_pdf_pypdf()
        elif ext == ".hwp":
            return self.load_hwp()
        elif ext == ".csv":
            return self.load_csv()
        elif ext in [".xls", ".xlsx"]:
            return self.load_excel()
        elif ext == ".txt":
            return self.load_txt()
        elif ext == ".json":
            return self.load_json()
        elif ext == ".md":
            return self.load_md()
        elif ext == ".py":
            return self.load_code()
        else:
            raise ValueError(f"Unsupported file type: {ext}")

if __name__ == "__main__":
    # 테스트 파일 경로 (여기서 설정)
    file_path = "10_여명구/91_Practice_Project/02_LoaderSplitterPackage/data/10.발가락이 닮았다_김동인.txt"  # 테스트할 파일 경로
    loader = FileLoader(file_path)
    
    try:
        # 파일을 로드하고 일부 텍스트만 출력
        documents = loader.load_file()
        print("로드된 파일 내용 일부:")
        print(documents[:5])  # 일부만 출력
    except Exception as e:
        print(f"오류 발생: {e}")
