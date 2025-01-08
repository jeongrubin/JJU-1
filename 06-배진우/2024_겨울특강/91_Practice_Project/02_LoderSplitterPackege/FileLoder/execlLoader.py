"""
execlLoader.py
- 엑셀 파일을 직접 열어서 파싱하는 로직.
"""

# 예시:
# import openpyxl
# from io import BytesIO

def load_excel(file_path: str):
    """
    Excel 파일(xlsx, xls 등)을 바이너리 모드로 열어 파싱 후 반환.
    """
    with open(file_path, 'rb') as f:
        excel_bytes = f.read()
    
    # TODO: openpyxl, xlrd 등으로 workbook 로드, 시트별 파싱 로직
    pass
