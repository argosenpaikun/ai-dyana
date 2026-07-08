from milvus.collection import (
    create_collection,
    list_collections,
    describe_collection,
    drop_collection
)

from milvus.document import (
    insert_document,
    count_documents,
    delete_document
)

from milvus.search import search_documents

COLLECTION_NAME = "demo_collection"

def test_create_collection():
    print("\n=== TEST CREATE COLLECTION ===")
    create_collection(COLLECTION_NAME)

def test_list_collection():
    print("\n=== TEST LIST COLLECTION ===")
    list_collections()

def test_describe_collection():
    print("\n=== TEST DESCRIBE COLLECTION ===")
    describe_collection(COLLECTION_NAME)

def test_insert_document():
    print("\n=== TEST INSERT DOCUMENT ===")

    documents = [
        "Milvus is an open source vector database",
        "Artificial Intelligence enables machines to learn from data.",
        "Kubernetes manages containerized applications."
    ]

    inserted_ids = []
    for doc in documents:
        result = insert_document(
            collection_name=COLLECTION_NAME,
            text=doc
        )
        inserted_ids.extend(result["ids"])

    print("Inserted IDs:", inserted_ids)
    return inserted_ids
    
def test_count_documents():
    print("\n=== TEST COUNT DOCUMENTS ===")
    count = count_documents(
        collection_name=COLLECTION_NAME
    )

    print(f"Total documents: {count}")

def test_search_document():
    print("\n=== TEST SEARCH DOCUMENT ===")
    query = "What is a vector database?"

    results = search_documents(
        collection_name=COLLECTION_NAME,
        query=query,
        limit=3,
    )

    for result in results:
        print("-----------------------")
        print("ID:", result["id"])
        print("Score:", result["score"])
        print("Text:", result["text"])

def test_delete_document(document_id):
    print("\n=== TEST DELETE DOCUMENT ===")
    delete_document(
        collection_name=COLLECTION_NAME,
        document_id=document_id
    )

def test_drop_collection():
    print("\n=== TEST DROP COLLECTION ===")

    drop_collection(
        collection_name=COLLECTION_NAME
    )

def main():
    try:

        # 1. Create collection
        test_create_collection()

        # 2. List collections
        test_list_collection()

        # 3. Describe collection
        test_describe_collection()

        # 4. Insert documents
        ids = test_insert_document()

        # 5. Count documents
        test_count_documents()

        # 6. Search documents
        test_search_document()

        # 7. Delete first document
        if ids:
            test_delete_document(ids[0])

        # 8. Count after deletion
        test_count_documents()

        # 9. Remove collection
        # Uncomment if you want cleanup
        test_drop_collection()
        
    except Exception as e:
        print("\nERROR OCCURED")
        print(e)

if __name__ == "__main__":
    main()