import json
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parents[1] / "data" / "books.json"

def load_books():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)
