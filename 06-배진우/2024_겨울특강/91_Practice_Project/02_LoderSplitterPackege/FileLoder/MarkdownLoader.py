"""
MarkdownLoader.py
- Markdown 파일을 직접 열어서 파싱하는 로직.
"""

def load_markdown(file_path: str):
    """
    Markdown 파일을 열어 파싱/가공 후 반환.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # TODO: markdown2, mistune, etc.를 사용한 파싱/HTML 변환/후처리
    pass
