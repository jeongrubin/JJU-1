"""
JsonLoader.py
- JSON 파일을 직접 열어서 파싱하는 로직.
"""

import json

def load_json(file_path: str):
    """
    JSON 파일을 열어서 파싱 후 파이썬 객체로 반환.
    """
    # 1) 텍스트 모드로 파일 열기
    with open(file_path, 'r', encoding='utf-8') as f:
        json_str = f.read()
    
    # 2) TODO: json.loads() 로 파싱
    # data = json.loads(json_str)
    
    # 3) TODO: 필요 후처리 후 반환
    pass
