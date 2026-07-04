"""
Chat service - the main entry point used by the controller.
Runs the full pipeline: build memory buffer -> classify -> route ->
retrieve -> generate.
"""

from app.core.chatbot_pipeline import run_chatbot
from app.utils.logger import logger


def handle_chat(query: str, history: list, user_id: str = "", session_id: str = ""):
    logger.info(f"Received query from user_id={user_id} session_id={session_id}: {query}")

    result = run_chatbot(query, history)

    return result
