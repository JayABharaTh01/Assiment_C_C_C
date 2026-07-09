"""
embedding_factory.py

Returns the configured embedding provider.
"""

from utils.config import EMBEDDING_PROVIDER
from embeddings.huggingface_embedding import HuggingFaceEmbedding


class EmbeddingFactory:

    @staticmethod
    def get_embedding():
        provider = EMBEDDING_PROVIDER.lower()
        
        if provider == "sentence-transformers":
            return HuggingFaceEmbedding()
        else:
            raise ValueError(
                f"Unsupported embedding provider: {provider}. "
                f"Use 'sentence-transformers'"
            )