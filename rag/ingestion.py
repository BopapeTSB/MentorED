from rag.chroma_client import collection
from rag.embeddings import create_embedding

def ingest_document(doc_id, text):

    embedding = create_embedding(text)

    collection.add(
        ids=[doc_id],
        documents=[text],
        embeddings=[embedding]
    )
