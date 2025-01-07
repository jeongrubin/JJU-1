from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders import PythonLoader


loader = DirectoryLoader(
    './', glob = '**/*.py', loader_cls = PythonLoader
    )

docs = loader.load()

#print(len(docs))
#print(docs[0].page_content)
print(docs[2])