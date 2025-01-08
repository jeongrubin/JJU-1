"""
HTMLLoader.py
- HTML 파일을 직접 열고, 필요한 라이브러리를 사용해 파싱하는 로직을 담습니다.
"""

# 예: BeautifulSoup 사용 시
# from bs4 import BeautifulSoup

def load_html(file_path: str):
    """
    HTML 파일을 열어서 원하는 대로 파싱/가공 후 반환.
    """
    # 1) 텍스트 모드로 파일 열기
    with open(file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # 2) TODO: BeautifulSoup 등 라이브러리 활용
    # soup = BeautifulSoup(html_content, 'html.parser')
    
    # 3) TODO: 필요 로직 & 후처리
    # return soup
    pass
