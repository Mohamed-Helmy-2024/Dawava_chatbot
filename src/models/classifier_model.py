"""
Classifier model.
Reuses the same OpenAI client and generate_text() function
for both classification and generation.
"""

from src.models.llm_model import generate_text
__all__ = [
    "generate_text",
]
