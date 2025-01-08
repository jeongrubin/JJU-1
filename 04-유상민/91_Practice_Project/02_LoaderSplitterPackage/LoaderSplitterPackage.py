# 1단계 파일 분류하기
import os

def detect_file_type(file_path):
    """
    주어진 파일 경로에서 확장자를 인식하고 파일 유형을 반환.
    """
    # 파일 확장자만 검사 (경로 유효성 검사 최소화)
    _, file_extension = os.path.splitext(file_path)
    file_extension = file_extension.lower()

    file_types = {
        '.pdf': 'PDF',
        '.csv': 'CSV',
        '.xlsx': 'Excel',
        '.xls': 'Excel',
        '.txt': 'Text',
        '.json': 'JSON',
        '.html': 'HTML',
        '.md': 'Markdown',
        '.hwp': 'HWP',
        '.py': 'py',
    }

    return file_types.get(file_extension, "Unknown File Type")

if __name__ == "__main__":
    # 테스트 경로를 하드코딩
    file_path = "/workspaces/JJU-1/04-유상민/250107과제_2/SPRI_AI_Brief_2023년12월호_F.pdf"

    # 파일 유형 감지
    file_type = detect_file_type(file_path)
    
    # 결과 출력
    print(f"파일 유형: {file_type}")

# ---------------------------------------------------------------------

# 2단계 알맞은 loader탐색하기