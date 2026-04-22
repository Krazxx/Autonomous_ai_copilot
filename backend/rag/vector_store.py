import chromadb
from rag.embeddings import embed
import uuid

client = chromadb.Client(
    settings=chromadb.config.Settings(
        persist_directory="./chroma_db"
    )
)

collection = client.get_or_create_collection("docs")


def add_document(text):
    vector = embed(text)

    collection.add(
        documents=[text],
        embeddings=[vector],
        ids=[str(uuid.uuid4())]
    )

    client.persist()   # ✅ IMPORTANT FIX


def query(text):
    vector = embed(text)

    results = collection.query(
        query_embeddings=[vector],
        n_results=3
    )

    docs = results.get("documents")

    if docs and len(docs) > 0:
        return docs[0]   # list of docs

    return []