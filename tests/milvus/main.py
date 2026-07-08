from pymilvus import utility, connections

def connect_db():
    connections.connect(
        alias="default",
        host="localhost",
        port="19530"
    )

    print("Connected to Milvus successfully")

def list_collections():
    connections.connect(
        alias="default",
        hosts="localhost",
        port="19530"
    )
    print(utility.list_collections())

if __name__ == "__main__":
    connect_db()