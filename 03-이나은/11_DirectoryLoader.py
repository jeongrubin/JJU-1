from langchain_community.document_loaders import PythonLoader

loader =  DirectoryLoader(
    './.',
    glob = '**/*.py',
    loader_cls = PythonLoader
)

docs = loader.load()
docs