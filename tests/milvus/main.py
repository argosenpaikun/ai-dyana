from pymilvus import (
    MilvusClient,
    FieldSchema,
    CollectionSchema,
    DataType
)

MILVUS_URI = "http://localhost:19530"
COLLECTION_NAME = "demo_collection"

def connect_milvus():
    """Connect to Milvus database"""
    try:
        client = MilvusClient(
            uri=MILVUS_URI
        )

        print("Connected to Milvus")
        return client
    except Exception as e:
        print(f"Milvus connection failed: {e}")
        return None
    
def list_collections(client):
    """List existing collections."""
    collections = client.list_collections()

    print("Existing Collections:")
    print(collections)

    return collections

def create_collection(client):
    """Create Milvus collection."""
    if client.has_collection(COLLECTION_NAME):
        print(f"Collection {COLLECTION_NAME} already exists")
        return 
    
    schema = MilvusClient.create_schema(
        auto_id=False,
        enable_dynamic_field=False
    )

    schema.add_field(
        field_name="id", 
        datatype=DataType.INT64,
        is_primary=True
    )

    schema.add_field(
        field_name="embedding",
        datatype=DataType.FLOAT_VECTOR,
        dim=4
    )

    client.create_collection(
        collection_name=COLLECTION_NAME,
        schema=schema
    )
    
    print(f"Collection {COLLECTION_NAME} created")

def create_index(client):
    """Create vector index"""
    index_params = client.prepare_index_params()

    index_params.add_index(
        field_name="embedding",
        index_type="AUTOINDEX",
        metric_type="L2"
    )

    client.create_index(
        collection_name=COLLECTION_NAME,
        index_params=index_params
    )

def insert_data(client):
    """Insert vector data"""
    data = [
        {
            "id": 1,
            "embedding": [
                0.1,
                0.2,
                0.3,
                0.4
            ]
        },
        {
            "id": 2,
            "embedding": [
                0.5,
                0.6,
                0.7,
                0.8
            ]
        },
        {
            "id": 3,
            "embedding": [
                0.9,
                1.0,
                1.1,
                1.2
            ]
        }
    ]

    result = client.insert(
        collection_name=COLLECTION_NAME,
        data=data
    )

    # Ensure data is persisted
    client.flush(
        collection_name=COLLECTION_NAME
    )

    print(f"Insert completed: {result}")

def search_vector(client):
    """Perform vector similarity search"""
    
    results = client.search(
        collection_name=COLLECTION_NAME,
        data=[
            [
                0.1,
                0.2,
                0.3,
                0.4
            ]
        ],
        anns_field="embedding",
        search_params={
            "metric_type": "L2",
            "params": {
                "nprobe": 10
            }
        },
        limit=3,
        output_fields=[
            "id"
        ]
    )

    print("Search Result:")
    for hits in results:
        for hit in hits:
            print(
                f"ID: {hit['id']}, "
                f"Distance: {hit['distance']}"
            )

def delete_collection(client):
    """Delete collection"""
    if client.has_collection(COLLECTION_NAME):
        client.drop_collection(
            COLLECTION_NAME
        )
        print(f"Collection {COLLECTION_NAME} deleted")
    
def main():
    print("=== Milvus Database Test ===")

    # Connect
    client = connect_milvus()

    if client is None:
        return
    
    # Delete collections
    delete_collection(client)
    
    # List collections
    list_collections(client)

    # Create collection
    create_collection(client)

    # Insert vectors
    insert_data(client)

    create_index(client)

    client.load_collection(
        collection_name=COLLECTION_NAME
    )

    # Search vectors
    search_vector(client)

    # Show collections
    list_collections(client)

    # Delete collections
    delete_collection(client)

    print("=== Milvus Test Completed ===")

if __name__ == "__main__":
    main()