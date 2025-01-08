"""
csvLoader.py
- CSV 파일을 직접 열어서 파싱하는 로직.
"""

import csv

def load_csv(file_path: str):
    """
    CSV 파일을 열어 csv.reader 또는 pandas 등을 통해 파싱 후 반환.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        csv_content = f.read()
    
    # TODO: csv.reader() 또는 pandas를 통한 파싱
    # lines = csv_content.splitlines()
    # reader = csv.reader(lines)
    pass


if __name__ == "__main__":
    file_path = ""