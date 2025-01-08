# 필요한 모듈 설치 주석 추가
# pip install langchain langchain-community langchain-teddynote pyhwp
# pip install pymupdf pypdf pdfminer pdfium
# pip install unstructured jq networkx
# pip install openpyxl

from langchain_community.document_loaders import (
    PyPDFLoader,
    PyMuPDFLoader,
    UnstructuredPDFLoader,
    PyPDFium2Loader,
    PDFMinerLoader,
    CSVLoader,
    UnstructuredExcelLoader,  # ExcelLoader
    TextLoader,
    JSONLoader,
    WebBaseLoader, # HTMLLoader
    PythonLoader,
)
from langchain_teddynote.document_loaders import HWPLoader
import os


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
        loader = PyPDFium2Loader(self.file_path)
        return loader.load()

    def load_pdf_pdfminer(self):
        """PDF 파일을 PDFMiner로 로드"""
        loader = PDFMinerLoader(self.file_path)
        return loader.load()
    
    def load_hwp(self):
        """HWP 파일 로드 (langchain_teddynote 사용)"""
        loader = HWPLoader(self.file_path)
        return loader.load()
    
    def load_csv(self):
        """CSV 파일 로드"""
        loader = CSVLoader(self.file_path)
        return loader.load()
    
    def load_excel(self):
        """Excel 파일 로드 (UnstructuredExcelLoader 사용)"""
        loader = UnstructuredExcelLoader(self.file_path)
        return loader.load()
    
    def load_txt(self):
        """Text 파일 로드"""
        loader = TextLoader(self.file_path)
        return loader.load()
    
    def load_json(self):
        """JSON 파일 로드"""
        # JSON 파일을 utf-8-sig로 읽어 문자열로 로드
        with open(self.file_path, "r", encoding="utf-8-sig") as f:
            json_content = f.read()
        # jq_schema 정의: 필요한 JSON 필드 추출
        jq_schema = """
        {
            video_id: .video.video_id,
            video_duration: .video.video_duration,
            video_width: .video.video_width,
            video_height: .video.video_height,
            client_info: {
                gender: .video.client_gender,
                age: .video.client_age,
                accessories: .video.client_accessory
            },
            interactions: .video.interactions[].human_event | {
                start_time: .start,
                end_time: .end,
                actions: .actions[].action_discription,
                utterances: .utterances[].utterance_cap
            }
        }
        """
        # JSONLoader를 사용하여 데이터 로드
        loader = JSONLoader(file_path=file_path, jq_schema=jq_schema, text_content=False)
        return loader.load()
    
    # def load_md(self):
    #     """Markdown 파일 로드 (UnstructuredMarkdownLoader 사용)"""
    #     loader = UnstructuredMarkdownLoader(self.file_path)
    #     return loader.load()
    
    def load_html(self):
        """HTML 파일 로드 (WebBaseLoader 사용)"""
        loader = WebBaseLoader(web_path=self.file_path)
        return loader.load()

    def load_code(self):
        """Python Code 파일 로드"""
        loader = PythonLoader(self.file_path)
        return loader.load()
    
    def load_file(self):
        """파일 확장자에 따라 적합한 로더 호출"""
        _, ext = os.path.splitext(self.file_path)
        ext = ext.lower()
        
        if ext == ".pdf":
            # PDF 파일은 PyPDF 방식으로 로드
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
        elif ext == ".html" or ext == ".htm":
            return self.load_html()
        elif ext == ".py":
            return self.load_code()
        else:
            raise ValueError(f"Unsupported file type: {ext}")


if __name__ == "__main__":
    # 테스트 파일 경로 (여기서 설정)
    file_path = "10_여명구/91_Practice_Project/02_LoaderSplitterPackage/data/인공지능html.html"  # 테스트할 파일 경로
    loader = FileLoader(file_path)
    
    try:
        # 파일을 로드하고 일부 텍스트만 출력
        documents = loader.load_file()
        print("로드된 파일 내용 일부:")
        print(documents[:5])  # 일부만 출력
    except Exception as e:
        print(f"오류 발생: {e}")
