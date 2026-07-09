import os
from dotenv import load_dotenv
load_dotenv()
MILVUS_URI = "http://127.0.0.1:19530"
COLLECTION_NAME = "documents"
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
EMBEDDING_DIMENSION = 384
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MONGODB_URI = "mongodb://localhost:27017"
MONGODB_DATABASE = "ai_dyana"