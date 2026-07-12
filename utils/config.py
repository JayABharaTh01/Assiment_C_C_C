import os
from dotenv import load_dotenv

load_dotenv()


def _get_env(name, default=None):
    value = os.getenv(name, default)
    if value is None:
        return default
    return value


def _get_int_env(name, default=0):
    value = _get_env(name, default)
    try:
        return int(value)
    except (TypeError, ValueError):
        return int(default)


def _get_float_env(name, default=0.0):
    value = _get_env(name, default)
    try:
        return float(value)
    except (TypeError, ValueError):
        return float(default)


# Project
PROJECT_NAME = _get_env("PROJECT_NAME", "Customer Complaint Chatbot")
ENVIRONMENT = _get_env("ENVIRONMENT", "development")
DEBUG = _get_env("DEBUG", "False") == "True"

# Data
DATA_FOLDER = _get_env("DATA_FOLDER", "data")
SUPPORTED_EXTENSIONS = [
    ext.strip() for ext in _get_env("SUPPORTED_EXTENSIONS", ".pdf,.csv,.json,.docx").split(",") if ext.strip()
]

# Chunking
CHUNK_SIZE = _get_int_env("CHUNK_SIZE", 500)
CHUNK_OVERLAP = _get_int_env("CHUNK_OVERLAP", 50)

# Embedding
EMBEDDING_PROVIDER = _get_env("EMBEDDING_PROVIDER", "sentence-transformers")
EMBEDDING_MODEL = _get_env("EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2")
EMBEDDING_DEVICE = _get_env("EMBEDDING_DEVICE", "cpu")
EMBEDDING_BATCH_SIZE = _get_int_env("EMBEDDING_BATCH_SIZE", 32)
NORMALIZE_EMBEDDINGS = _get_env("NORMALIZE_EMBEDDINGS", "True") == "True"

# ==========================================================
# OpenAI LLM
# ==========================================================

OPENAI_CHAT_MODEL = _get_env("OPENAI_CHAT_MODEL", "gpt-4.1-mini")
OPENAI_TEMPERATURE = _get_float_env("OPENAI_TEMPERATURE", 0.2)
OPENAI_MAX_TOKENS = _get_int_env("OPENAI_MAX_TOKENS", 512)

# API Keys
OPENAI_API_KEY = _get_env("OPENAI_API_KEY")

# Vector Databases
# Pinecone

PINECONE_API_KEY = _get_env("PINECONE_API_KEY")
PINECONE_INDEX = _get_env("PINECONE_INDEX", "customer-complaints")
PINECONE_CLOUD = _get_env("PINECONE_CLOUD", "aws")
PINECONE_REGION = _get_env("PINECONE_REGION", "us-east-1")


# Retrieval
TOP_K = _get_int_env("TOP_K", 5)
SIMILARITY_SEARCH = _get_env("SIMILARITY_SEARCH", "cosine")

# Streamlit
STREAMLIT_PORT = _get_int_env("STREAMLIT_PORT", 8501)

# Logging
LOG_LEVEL = _get_env("LOG_LEVEL", "INFO")
LOG_FILE = _get_env("LOG_FILE", "app.log")

# LLM
LLM_PROVIDER = _get_env("LLM_PROVIDER", "openai")
LLM_MODEL = _get_env("LLM_MODEL", OPENAI_CHAT_MODEL)
LLM_MAX_NEW_TOKENS = _get_int_env("LLM_MAX_NEW_TOKENS", 512)
LLM_TEMPERATURE = _get_float_env("LLM_TEMPERATURE", OPENAI_TEMPERATURE)
LLM_DO_SAMPLE = _get_env("LLM_DO_SAMPLE", "False") == "True"