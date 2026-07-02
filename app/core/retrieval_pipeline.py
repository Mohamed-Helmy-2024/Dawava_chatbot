"""
Retrieval pipeline.

Loads the existing FAISS indexes + metadata pickle files (built offline
by the notebook) ONE time at import, then exposes search_medicines() and
search_questions() exactly as implemented in the notebook.

No index building happens here - only loading + searching.
"""

import pickle
import numpy as np
import faiss

from app.models.embedding_model import get_embedding
from app.config import (
    MEDICINE_INDEX_PATH,
    MEDICINE_METADATA_PATH,
    QUESTIONS_INDEX_PATH,
    QUESTIONS_METADATA_PATH,
)

# Load medicine index + metadata (notebook cell: faiss.read_index / pickle.load)
medicine_index = faiss.read_index(MEDICINE_INDEX_PATH)

with open(MEDICINE_METADATA_PATH, "rb") as f:
    medicine_metadata = pickle.load(f)
# Load questions index + metadata
questions_index = faiss.read_index(QUESTIONS_INDEX_PATH)

with open(QUESTIONS_METADATA_PATH, "rb") as f:
    questions_metadata = pickle.load(f)


def search_medicines(query, top_k=3):
    """
    Exact logic from the notebook's search_medicines().
    .get() is used instead of direct key access only so it does not
    crash if a column is missing from the metadata file - the search
    logic itself is unchanged.
    """
    query_embedding = get_embedding(query)
    query_embedding = np.array([query_embedding]).astype("float32")
    scores, indices = medicine_index.search(query_embedding, top_k)
    results = []

    for score, idx in zip(scores[0], indices[0]):
        item = medicine_metadata[idx]

        results.append({
            "id": item.get("id"),
            "name_ar": item.get("name_ar"),
            "name_en": item.get("name_en"),
            "scientific_name": item.get("scientific_name"),
            "commerical_name": item.get("commerical_name"),
            "category": item.get("category"),
            "pharmacology": item.get("pharmacology"),
            "indications": item.get("indications"),
            "similar_medicines_ar_names": item.get("similar_medicines_ar_names"),
            "similar_medicines_en_names": item.get("similar_medicines_en_names"),
            "score": float(score)
        })

    return results


def search_questions(query, top_k=3):
    """
    Exact logic from the notebook's search_questions().
    """
    query_embedding = get_embedding(query)
    query_embedding = np.array([query_embedding]).astype("float32")
    scores, indices = questions_index.search(query_embedding, top_k)
    items = []
    for score, idx in zip(scores[0], indices[0]):
        item = questions_metadata[idx]
        item = dict(item)
        item["score"] = float(score)
        items.append(item)

    return items
