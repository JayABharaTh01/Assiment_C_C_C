"""
base_embedding.py

Abstract base class for all embedding providers.
"""

from abc import ABC, abstractmethod
from typing import List


class BaseEmbedding(ABC):
    """
    Base interface for embedding models.
    """

    @abstractmethod
    def embed_query(self, text: str) -> List[float]:
        """
        Generate an embedding for a single query.
        """
        pass

    @abstractmethod
    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        """
        Generate embeddings for multiple documents.
        """
        pass