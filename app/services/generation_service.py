"""
Generation service - thin wrapper around the generation pipeline.
"""

from app.core.generation_pipeline import generate_answer

def generate(query, retrieved_context, category):
    return generate_answer(query, retrieved_context, category)
