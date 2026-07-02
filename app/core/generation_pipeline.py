"""
Generation pipeline.

generate_answer() mirrors the notebook's final generation cell
(cells 43-45): build the prompt (RAG prompt with the memory buffer for
medical/drug, simple prompt for general), apply the chat template, and
call model.generate() through generate_text().
"""

from app.models.llm_model import generate_text
from app.utils.prompt_builder import build_prompt, build_general_prompt
from app.config import GENERATION_MAX_TOKENS


def generate_answer(query, retrieved_context, category, memory_summary="No previous memory."):
    if category == "general":
        prompt = build_general_prompt(query, memory_summary=memory_summary)
    else:
        prompt = build_prompt(
            query=query,
            retrieved_context=retrieved_context,
            memory_summary=memory_summary,
            category=category
        )

    response = generate_text(
        prompt,
        max_tokens=GENERATION_MAX_TOKENS,
        thinking=False
    )

    return response
