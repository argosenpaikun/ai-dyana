from bm25.index import (
    get_index,
    get_documents,
)

from bm25.tokenizer import tokenize

def search_documents(
    query: str,
    limit: int = 5,
):
    bm25 = get_index()

    if bm25 is None:
        return []

    documents = get_documents()

    scores = bm25.get_scores(
        tokenize(query)
    )

    ranked = sorted(
        zip(documents, scores),
        key=lambda x: x[1],
        reverse=True,
    )

    results = []

    for document, score in ranked[:limit]:
        results.append(
            {
                "id": document["id"],
                "text": document["text"],
                "score": float(score),
            }
        )

    return results