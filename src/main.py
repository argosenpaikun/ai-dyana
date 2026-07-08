from config import COLLECTION_NAME
from milvus.document import count_documents

# Temporary test script for Milvus module.
def main():
    count = count_documents(COLLECTION_NAME)
    print(f"Document Count: {count}")

if __name__ == "__main__":
    main()