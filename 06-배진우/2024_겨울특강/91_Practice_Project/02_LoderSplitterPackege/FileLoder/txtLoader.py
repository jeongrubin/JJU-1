"""
txtLoader.py
- 일반 텍스트 파일을 직접 열어서 후처리하는 로직.
"""

def load_txt(file_path: str):
    """
    일반 텍스트 파일(.txt)을 열어 가공 후 반환.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        text_content = f.read()
    
    # TODO: 불필요 문자 제거, 토큰화, etc.
    pass
