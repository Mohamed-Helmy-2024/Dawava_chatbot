"""
Central configuration.
All values here are exactly what was used in the notebook
(model names, file names, top_k) — nothing new added.
"""

import os
import os
from dotenv import load_dotenv

load_dotenv()

# Paths (same files produced by the notebook's embedding phase)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

MEDICINE_INDEX_PATH = os.path.join(DATA_DIR, "medicines.index")
MEDICINE_METADATA_PATH = os.path.join(DATA_DIR, "medicines_metadata.pkl")

QUESTIONS_INDEX_PATH = os.path.join(DATA_DIR, "questions.index")
QUESTIONS_METADATA_PATH = os.path.join(DATA_DIR, "questions_metadata.pkl")

# Models (same names used in the notebook)
EMBEDDING_MODEL_NAME = "./AI/models/bge-m3"
LLM_MODEL_NAME = "./AI/models/Qwen3-4B"

# DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

# Retrieval / generation defaults (same defaults used in the notebook)
TOP_K_MEDICINE = 3
TOP_K_QUESTIONS = 3

CLASSIFIER_MAX_TOKENS = 32
GENERATION_MAX_TOKENS = 512

# Chat memory buffer (no database - history is sent by the client with
# each request; this only controls how many recent messages are used)
MEMORY_BUFFER_LIMIT = 20
COHERE_API_KEY = os.getenv("COHERE_API_KEY")
# OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
  # Replace with your actual OpenAI API key