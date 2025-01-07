from langchain_community.document_loaders import PythonLoader, DirectoryLoader

loader1 =  DirectoryLoader(
    './.',
    glob = '**/*.py',
    loader_cls = PythonLoader
)

docs = loader1.load()
docs