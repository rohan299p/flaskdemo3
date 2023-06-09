import os
from langchain.document_loaders import PyPDFLoader

def read_pdf(file_path): #reading files
    try:
        loader = PyPDFLoader(file_path)
        pages = loader.load_and_split()
        return pages
    except Exception as e:
        raise Exception(f"Error in reading PDF file: {str(e)}")

def load_files(directory_path): #reading the whole directory
    pdf_files = [file for file in os.listdir(directory_path) if file.endswith('.pdf')]
    content_list = []
    for pdf_file in pdf_files:
        file_path = os.path.join(directory_path,pdf_file)
        content = read_pdf(file_path)
        content_list.append(content)
    return content_list