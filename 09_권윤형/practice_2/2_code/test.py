import os

FILE_PATH = '/workspaces/JJU/09_권윤형/practice_2/1_usedData/광화사.txt'

_, file_extension = os.path.splitext(FILE_PATH)
print(file_extension)

file_extension = file_extension.lower()
print(file_extension)