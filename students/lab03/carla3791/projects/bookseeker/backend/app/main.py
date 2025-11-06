from fastapi import FastAPI
from pydantic import BaseModel
from .db import load_books
from .embeddings import build_index, embed_query

app = FastAPI(title="BookSeeker MVP")

class Query(BaseModel):
    q: str
    k: int = 3

books = load_books()
index, book_embeddings = build_index(books)

@app.post("/search")
def search(query: Query):
    qvec = embed_query(query.q)
    D, I = index.search(qvec, query.k)
    results = []
    for idx in I[0]:
        b = books[idx]
        results.append({"id": b["id"], "title": b["title"], "author": b["author"], "description": b["description"]})
    return {"query": query.q, "results": results}
