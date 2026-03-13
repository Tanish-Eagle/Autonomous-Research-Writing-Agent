from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_core.documents import Document

def ingest_text(text: str, source: str = "webpage"):
    # Split text into chunks
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)

    chunks = splitter.split_text(text)

    docs = [Document(page_content=chunk, metadata={"source": source}) for chunk in chunks]

    # Embeddings

    embeddings = OpenAIEmbeddings()

    # Vector store (persistent)

    vectordb = Chroma(collection_name="research_store", embedding_function=embeddings, persist_directory="./chroma_db")

    vectordb.add_documents(docs)

    print(f"Stored {len(docs)} chunks in vector database")

