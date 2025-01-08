"""
File Path를 입력 받았을 때 어떤 확장자를 구분해준다.
"""

import os

def sorter_I(file_path):
    _, extension = os.path.splitext(file_path)
    return extension if extension else 'No extension'


