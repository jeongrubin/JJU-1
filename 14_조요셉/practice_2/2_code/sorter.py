import os
from loader import (
    hwp_loader, csv_loader, unstructured_csv_loader, excel_loader, word_loader,
    unstructured_word_loader, txt_loader, json_loader, python_lodaer,
    html_lodaer, markdown_loader
)
from pdf_loader import (
    py_pdf_loader, py_mu_pdf, py_pdf_mu2loader, pdf_minerloader, pdf_plumber
)
from splitter import (
    charcter_text_splitter, recursive_character_text_splitter, token_text_splitter,
    semanticchunker, python_splitter, markdownheadersplitter, htmlheadersplitter,
    recursivejsonsplitter
)

def load_and_split(file_path):
    """
    Loads a file based on its extension and splits it using appropriate splitters.
    """
    extension = os.path.splitext(file_path)[-1].lower()

    # Dictionary mapping extensions to loader functions
    loader_map = {
        '.hwp': hwp_loader,
        '.csv': csv_loader,
        '.xlsx': excel_loader,
        '.xls': excel_loader,
        '.docx': word_loader,
        '.txt': txt_loader,
        '.json': json_loader,
        '.py': python_lodaer,
        '.html': html_lodaer,
        '.md': markdown_loader,
        '.pdf': py_pdf_loader  # PDF 로더 지정
    }

    # Dictionary mapping extensions to multiple splitter functions
    splitter_map = {
        '.txt': [charcter_text_splitter, token_text_splitter],
        '.docx': [charcter_text_splitter],
        '.csv': [charcter_text_splitter],
        '.hwp': [charcter_text_splitter],
        '.json': [recursivejsonsplitter],
        '.py': [python_splitter],
        '.md': [markdownheadersplitter],
        '.html': [htmlheadersplitter],
        '.pdf': [charcter_text_splitter, token_text_splitter]  # PDF에 일반 스플리터 사용
    }

    if extension not in loader_map:
        raise ValueError(f"Unsupported file extension: {extension}")

    # Load the document using the appropriate loader
    loader = loader_map[extension]
    docs = loader(file_path)

    # PDF 로더가 반환하는 형식을 일반 텍스트 리스트로 변환 (필요할 경우)
    if extension == '.pdf' and isinstance(docs, list):
        docs = ["\n".join(page) if isinstance(page, list) else page for page in docs]

    # Check if the extension has splitters and process each
    if extension in splitter_map:
        splitters = splitter_map[extension]
        split_results = {}

        for splitter in splitters:
            text_splitter = splitter()
            split_docs = text_splitter.create_documents(docs)
            split_results[splitter.__name__] = split_docs

        return split_results
    else:
        # Default to character splitter if no specific splitters are provided
        text_splitter = charcter_text_splitter()
        split_docs = text_splitter.create_documents(docs)
        return {charcter_text_splitter.__name__: split_docs}

# Example usage
if __name__ == "__main__":
    file_path = "example.pdf"  # Replace with actual file path
    try:
        result = load_and_split(file_path)
        print("Split documents by splitter:")
        for splitter_name, docs in result.items():
            print(f"Splitter: {splitter_name}, Documents: {docs}")
    except ValueError as e:
        print("Error:", e)