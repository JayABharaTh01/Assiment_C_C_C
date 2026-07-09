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

# LLM
LLM_PROVIDER = os.getenv("LLM_PROVIDER")
LLM_MODEL = os.getenv("LLM_MODEL")

# API Keys
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Vector Databases
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_ENV = os.getenv("PINECONE_ENV")
PINECONE_INDEX = os.getenv("PINECONE_INDEX")

CHROMA_DB_PATH = os.getenv("CHROMA_DB_PATH")
FAISS_INDEX_PATH = os.getenv("FAISS_INDEX_PATH")

# Retrieval
TOP_K = int(os.getenv("TOP_K"))
SIMILARITY_SEARCH = os.getenv("SIMILARITY_SEARCH")

# Streamlit
STREAMLIT_PORT = int(os.getenv("STREAMLIT_PORT"))

# Logging
LOG_LEVEL = os.getenv("LOG_LEVEL")
LOG_FILE = os.getenv("LOG_FILE")