"""
Retrieval service - thin wrapper around the retrieval pipeline.
"""

from src.core.retrieval_pipeline import search_medicines, search_questions

def retrieve_medicines(query, top_k=3):
    return search_medicines(query, top_k=top_k)

def retrieve_questions(query, top_k=3):
    return search_questions(query, top_k=top_k)
