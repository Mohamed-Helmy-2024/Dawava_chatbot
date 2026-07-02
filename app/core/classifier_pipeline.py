"""
Classifier pipeline.

classify_query() mirrors the notebook's classify_query() function
(cell 28): build the final prompt from the memory buffer +
CLASSIFIER_PROMPT + query, then call generate_text() with
max_tokens=32, thinking=False.

The memory buffer is built once per request by the memory_pipeline
from the history the client sent, and passed in here.
"""

from app.models.classifier_model import generate_text
from app.utils.prompt_builder import build_classifier_prompt
from app.utils.text_cleaner import clean_label
from app.config import CLASSIFIER_MAX_TOKENS


def classify_query(user_query, memory_buffer="No previous memory."):

    final_prompt = build_classifier_prompt(memory_buffer, user_query)
    raw_classification = generate_text(
        final_prompt,
        max_tokens=CLASSIFIER_MAX_TOKENS,
        thinking=False
    )

    return clean_label(raw_classification)
