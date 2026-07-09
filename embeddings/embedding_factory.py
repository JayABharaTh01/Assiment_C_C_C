"""
embedding_factory.py

Factory class for creating embedding model instances.

This class selects the embedding provider based on
the configuration in the .env file.

Supported Providers:
    - sentence-transformers

Author: Jaya Bharath
"""

from embeddings.huggingface_embedding import HuggingFaceEmbedding
from utils.config import EMBEDDING_PROVIDER


class EmbeddingFactory:
    """
    Factory class for creating embedding model instances.
    """

    @staticmethod
    def get_embedding():
        """
        Returns the configured embedding model.

        Returns
        -------
        BaseEmbedding
            Initialized embedding model.

        Raises
        ------
        ValueError
            If the configured embedding provider is not supported.
        """

        provider = EMBEDDING_PROVIDER.lower().strip()

        if provider == "sentence-transformers":
            return HuggingFaceEmbedding()

        raise ValueError(
            f"Unsupported embedding provider: '{provider}'. "
            "Supported providers: ['sentence-transformers']"
        )