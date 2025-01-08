"""
hwpLoader.py
- 한글(HWP) 파일을 직접 열어서 파싱하는 로직.
- pyhwp, olefile 등을 사용할 수 있습니다.
"""

def load_hwp(file_path: str):
    """
    HWP 파일을 바이너리 모드로 열어 필요한 정보 추출 후 반환.
    """
    with open(file_path, 'rb') as f:
        hwp_bytes = f.read()
    
    # TODO: pyhwp, olefile 등을 통한 파싱 & 후처리
    pass
