"""
base_embedding.py

Abstract base class for all embedding providers.

This interface ensures that every embedding model
implements the same methods, allowing the rest of
the application to remain independent of the
underlying embedding provider.

Author: Jaya Bharath
"""

from abc import ABC, abstractmethod
from typing import List


class BaseEmbedding(ABC):
    """
    Abstract base class for embedding models.
    """

    @abstractmethod
    def load_model(self) -> None:
        """
        Load the embedding model.
        """
        pass

    @abstractmethod
    def embed_query(self, text: str) -> List[float]:
        """
        Generate an embedding for a single query.

        Parameters
        ----------
        text : str
            Input query.

        Returns
        -------
        List[float]
            Query embedding.
        """
        pass

    @abstractmethod
    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        """
        Generate embeddings for multiple documents.

        Parameters
        ----------
        texts : List[str]
            List of document chunks.

        Returns
        -------
        List[List[float]]
            List of embedding vectors.
        """
        pass

    @abstractmethod
    def embedding_dimension(self) -> int:
        """
        Return the embedding dimension of the model.

        Returns
        -------
        int
            Embedding vector dimension.
        """
        pass