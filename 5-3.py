from langchain.document_loaders import PyPDFLoader

loader = PyPDFLoader("temp_uploaded_file.pdf")
pages = loader.load_and_split()

print(pages[1])