from rag.chroma_client import collection
from rag.embeddings import create_embedding

def retrieve_documents(query):


    embedding = create_embedding(query)

    results = collection.query(
        query_embeddings=[embedding],
        n_results=3
    )

    return results["documents"][0]
