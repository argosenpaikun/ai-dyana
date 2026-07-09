from rank_bm25 import BM25Okapi

from bm25.tokenizer import tokenize

_bm25 = None
_documents = []

def build_index(
    documents: list,
):
    global _bm25
    global _documents

    _documents = documents

    corpus = [
        tokenize(
            document["text"]
        )
        for document in documents
    ]

    _bm25 = BM25Okapi(corpus)

def get_index():
    return _bm25

def get_documents():
    return _documents