from langchain.document_loaders import TextLoader

file_path = "10_여명구/91_Practice_Project/02_LoaderSplitterPackage/data/10.발가락이 닮았다_김동인.txt"  # 테스트할 파일 경로

loader = TextLoader(file_path)
documents = loader.load()
print(documents[0].page_content[:100])  # 일부만 출력
# print(len(documents))