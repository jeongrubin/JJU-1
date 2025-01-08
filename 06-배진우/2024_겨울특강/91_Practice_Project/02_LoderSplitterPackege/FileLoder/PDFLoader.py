"""
PDFLoader.py
- PDF 파일을 직접 열어서 파싱하는 로직.
"""

def load_pdf(file_path: str):
    """
    PDF 파일을 바이너리 모드로 열어 PyPDF2 등으로 텍스트 추출 후 반환.
    """
    # 1) 바이너리 모드로 열기
    with open(file_path, 'rb') as f:
        pdf_bytes = f.read()
    
    # 2) TODO: PyPDF2 or pdfplumber 등 라이브러리를 사용한 파싱/텍스트 추출
    pass