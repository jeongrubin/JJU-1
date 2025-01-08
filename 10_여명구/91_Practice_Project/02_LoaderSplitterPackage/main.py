import os

def identify_file_type(file_path):
    # 파일 확장자 추출
    _, file_extension = os.path.splitext(file_path)
    file_extension = file_extension.lower()  # 확장자를 소문자로 변환
    
    # 확장자에 따른 파일 형식 분류
    file_type_mapping = {
        '.pdf': 'PDF',
        '.hwp': 'HWP',
        '.csv': 'CSV',
        '.xlsx': 'Excel',
        '.xls': 'Excel',
        '.txt': 'Text',
        '.json': 'JSON',
        '.py': 'Python',
        '.html': 'HTML',
        '.md': 'Markdown',
    }
    
    file_type = file_type_mapping.get(file_extension, 'Unknown')
    return file_type

# 테스트용 코드
if __name__ == "__main__":
    # 테스트 파일 경로 (하나씩 지정)
    # file_path = "10_여명구/91_Practice_Project/02_LoaderSplitterPackage/data/10.발가락이 닮았다_김동인.txt"  # 여기서 파일 경로를 직접 설정
    file_path = "10_여명구/91_Practice_Project/02_LoaderSplitterPackage/data/인공지능html.html"  # 여기서 파일 경로를 직접 설정
    file_type = identify_file_type(file_path)
    print(f"파일 경로: {file_path}, 파일 종류: {file_type}")
