from sentence_transformers import SentenceTransformer
from config import EMBEDDING_MODEL

_model = None

def get_embedding_model():
    """
    Load and return the embedding model.
    """
    global _model
    if _model is None:
        print(f"Loading embedding model: {EMBEDDING_MODEL}...")
        _model = SentenceTransformer(EMBEDDING_MODEL)
        print("Embedding model loaded successfully.")
    return _model

def generate_embedding(text: str):
    """
    Generate an embedding from text.
    """
    model = get_embedding_model()
    embedding = model.encode(
        text,
        normalize_embeddings=True,
    )
    return embedding.tolist()