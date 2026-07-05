"""
Very simple logger setup (no external libraries, just Python's logging).
"""

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger("chatbot_api")
