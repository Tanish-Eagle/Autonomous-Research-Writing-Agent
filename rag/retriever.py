from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

def get_relevant_docs(query: str):
    embeddings = OpenAIEmbeddings()

    vectordb = Chroma(collection_name="research_store", embedding_function=embeddings, persist_directory="./chroma_db")

    retriever = vectordb.as_retriever(search_kwargs={"k": 4})

    docs = retriever.invoke(query)

    return docs