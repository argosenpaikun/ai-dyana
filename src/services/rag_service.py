from milvus.search import search_documents
from llm.prompt import SYSTEM_PROMPT
from llm.generator import generate_answer

def ask_question(
        collection_name: str,
        question: str
):
    documents = search_documents(
        collection_name=collection_name,
        query=question,
        limit=5
    )

    context = "\n\n".join(
        doc["text"]
        for doc in documents
    )

    prompt = SYSTEM_PROMPT.format(
        context=context,
        question=question
    )

    answer = generate_answer(prompt)

    return {
        "answer": answer,
        "sources": documents
    }