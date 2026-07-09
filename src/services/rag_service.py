from milvus.search import search_documents as vector_search

from bm25.search import search_documents as bm25_search

from llm.prompt import SYSTEM_PROMPT
from llm.generator import generate_answer

from redis_cache.cache import (
    get_cached_answer,
    cache_answer,
)


def ask_question(
    collection_name: str,
    question: str,
):
    cached = get_cached_answer(question)

    if cached is not None:
        print("Redis cache hit.")
        return cached

    print("Redis cache miss.")

    vector_documents = vector_search(
        collection_name=collection_name,
        query=question,
        limit=5,
    )

    bm25_documents = bm25_search(
        query=question,
        limit=5,
    )

    documents = {}

    for document in vector_documents:
        text = document["text"]

        if text not in documents:
            documents[text] = document

    for document in bm25_documents:
        text = document["text"]

        if text not in documents:
            documents[text] = document

    context = "\n\n".join(
        document["text"]
        for document in documents.values()
    )

    prompt = SYSTEM_PROMPT.format(
        context=context,
        question=question,
    )

    answer = generate_answer(prompt)

    response = {
        "answer": answer,
        "sources": list(
            documents.values()
        ),
    }

    cache_answer(
        question=question,
        answer=response,
    )

    return response