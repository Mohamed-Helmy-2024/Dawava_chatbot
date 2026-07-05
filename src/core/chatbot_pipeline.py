"""
Chatbot pipeline.

Combines the other pipelines in the order shown in the architecture
diagram, with memory now coming straight from the request (no database,
no user_id/session_id):

  0. Build a memory buffer from the history sent with the request
  2. Classify query (Qwen3-1.7B, using the memory buffer - cell 28)
  4. Route + retrieve (medicine index for 'drug', questions index for
     'medical', no retrieval for 'general')
  5. Generate final answer (Qwen3-1.7B, using the memory buffer - cells 43-45)
"""

from src.core.classifier_pipeline import classify_query
from src.core.retrieval_pipeline import search_medicines, search_questions
from src.core.generation_pipeline import generate_answer
from src.core.memory_pipeline import build_memory_buffer


def run_chatbot(query, history):
    memory_buffer = build_memory_buffer(history)
    classification = classify_query(query, memory_buffer = memory_buffer)
    if classification == "drug":
        retrieved_context = search_medicines(query, top_k=3)
    elif classification == "medical":
        retrieved_context = search_questions(query, top_k=3)
    else:  # general -> no retrieval needed
        retrieved_context = []

    answer = generate_answer(
        query=query,
        retrieved_context=retrieved_context,
        category=classification,
        memory_summary=memory_buffer
    )

    return {
        # "classification": classification,
        # "retrieved_context": retrieved_context,
        "answer": answer
    }
