from langchain_community.document_loaders import PythonLoader, DirectoryLoader

loader =  DirectoryLoader(
    './.',
    glob = '**/*.py',
    loader_cls = PythonLoader
)

docs = loader.load()
print(docs)