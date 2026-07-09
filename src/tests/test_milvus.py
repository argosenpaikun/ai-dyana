import unittest
import time

from milvus.collection import (
    create_collection,
    list_collections,
    drop_collection
)

from milvus.document import (
    insert_document,
    count_documents,
    delete_document
)

from milvus.search import search_documents

COLLECTION_NAME = "demo_collection"

class TestMilvus(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        Runs once before all tests
        """
        try:
            drop_collection(COLLECTION_NAME)
        except Exception:
            pass

        create_collection(COLLECTION_NAME)


    @classmethod
    def tearDownClass(cls):
        """
        Runs once after all tests
        """
        try:
            drop_collection(COLLECTION_NAME)
        except Exception:
            pass

    def test_01_collection_exists(self):
        collections = list_collections()

        self.assertIn(
            COLLECTION_NAME,
            collections
        )

    def test_02_insert_document(self):
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

        self.assertEqual(len(inserted_ids), 3)
        self.__class__.ids = inserted_ids
        
    def test_03_count_documents(self):
        count = count_documents(
            collection_name=COLLECTION_NAME
        )

        self.assertEqual(count, 3)

    def test_04_search_document(self):
        query = "What is a vector database?"

        results = search_documents(
            collection_name=COLLECTION_NAME,
            query=query,
            limit=3,
        )

        self.assertGreater(len(results), 0)
        self.assertIn("text", results[0])
        self.assertIn("score", results[0])

    def test_05_delete_document(self):
        deleted_id = self.ids[0]

        delete_document(
            collection_name=COLLECTION_NAME,
            document_id=deleted_id
        )
        time.sleep(2)

        results = search_documents(
            collection_name=COLLECTION_NAME,
            query="Milvus vector database",
            limit=5
        )

        results_ids = [
            result["id"]
            for result in results
        ]
        
        self.assertNotIn(deleted_id, results_ids)

if __name__ == "__main__":
    unittest.main(verbosity=2)