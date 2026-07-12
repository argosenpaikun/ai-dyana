from rank_bm25 import BM25Okapi

from bm25.tokenizer import tokenize

_bm25 = None
_documents = []

def build_index(
    documents: list,
):
    global _bm25
    global _documents

    corpus = []
    filtered_docs = []

    for doc in documents:
        tokens = tokenize(doc.get("text", ""))
        
        if tokens:
            corpus.append(tokens)
            filtered_docs.append(doc)

    _documents = filtered_docs

    if not corpus:
        _bm25 = None
        return

    _bm25 = BM25Okapi(corpus)

def get_index():
    return _bm25

def get_documents():
    return _documents