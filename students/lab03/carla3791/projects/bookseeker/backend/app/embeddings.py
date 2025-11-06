from sentence_transformers import SentenceTransformer
import numpy as np
import faiss

MODEL_NAME = "all-MiniLM-L6-v2"
_model = None

def load_model():
    global _model
    if _model is None:
        _model = SentenceTransformer(MODEL_NAME)
    return _model

def build_index(books):
    model = load_model()
    texts = [b["description"] for b in books]
    embeddings = model.encode(texts, convert_to_numpy=True)
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)
    return index, embeddings

def embed_query(query):
    model = load_model()
    vec = model.encode([query], convert_to_numpy=True)
    return vec
