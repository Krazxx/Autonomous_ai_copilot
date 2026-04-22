from rag.vector_store import query

def retrieve_context(question):

    docs = query(question)
    print("RETRIEVED DOCS:", docs)

    if not docs:
        return ""   

    return "\n".join(docs)[:2000]   