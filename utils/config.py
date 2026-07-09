import os
from dotenv import load_dotenv

load_dotenv()

# Project
PROJECT_NAME = os.getenv("PROJECT_NAME")
ENVIRONMENT = os.getenv("ENVIRONMENT")
DEBUG = os.getenv("DEBUG") == "True"

# Data
DATA_FOLDER = os.getenv("DATA_FOLDER")
SUPPORTED_EXTENSIONS = os.getenv("SUPPORTED_EXTENSIONS").split(",")

# Chunking
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE"))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP"))

# Embedding
EMBEDDING_PROVIDER = os.getenv("EMBEDDING_PROVIDER")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL")
EMBEDDING_DEVICE = os.getenv("EMBEDDING_DEVICE", "cpu")
EMBEDDING_BATCH_SIZE = int(os.getenv("EMBEDDING_BATCH_SIZE", "32"))
NORMALIZE_EMBEDDINGS = os.getenv("NORMALIZE_EMBEDDINGS", "True") == "True"

# LLM
LLM_PROVIDER = os.getenv("LLM_PROVIDER")
LLM_MODEL = os.getenv("LLM_MODEL")

# API Keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Vector Databases
# Pinecone

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_INDEX = os.getenv("PINECONE_INDEX")
PINECONE_CLOUD = os.getenv("PINECONE_CLOUD")
PINECONE_REGION = os.getenv("PINECONE_REGION")


# Retrieval
TOP_K = int(os.getenv("TOP_K"))
SIMILARITY_SEARCH = os.getenv("SIMILARITY_SEARCH")

# Streamlit
STREAMLIT_PORT = int(os.getenv("STREAMLIT_PORT"))

# Logging
LOG_LEVEL = os.getenv("LOG_LEVEL")
LOG_FILE = os.getenv("LOG_FILE")

# LLM

LLM_PROVIDER = os.getenv("LLM_PROVIDER")

LLM_MODEL = os.getenv("LLM_MODEL")

LLM_MAX_NEW_TOKENS = int(os.getenv("LLM_MAX_NEW_TOKENS"))

LLM_TEMPERATURE = float(os.getenv("LLM_TEMPERATURE"))

LLM_DO_SAMPLE = os.getenv("LLM_DO_SAMPLE") == "True"