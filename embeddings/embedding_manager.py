"""
embedding_manager.py

High-level embedding manager.

This class serves as the interface between the
application and the embedding model.

Responsibilities:
    - Load the embedding model
    - Generate embeddings for queries
    - Generate embeddings for document chunks
    - Return embedding dimensions

Author: Jaya Bharath
"""

from typing import List

from embeddings.embedding_factory import EmbeddingFactory


class EmbeddingManager:
    """
    High-level interface for embedding operations.
    """

    def __init__(self):
        """
        Initialize the configured embedding model.
        """
        self.embedding_model = EmbeddingFactory.get_embedding()

    # ==========================================================
    # Embed Query
    # ==========================================================

    def embed_query(self, query: str) -> List[float]:
        """
        Generate an embedding for a user query.

        Parameters
        ----------
        query : str
            User question.

        Returns
        -------
        List[float]
            Query embedding.
        """

        return self.embedding_model.embed_query(query)

    # ==========================================================
    # Embed Documents
    # ==========================================================

    def embed_documents(
        self,
        documents: List[str]
    ) -> List[List[float]]:
        """
        Generate embeddings for multiple document chunks.

        Parameters
        ----------
        documents : List[str]
            List of document chunks.

        Returns
        -------
        List[List[float]]
            Embedding vectors.
        """

        return self.embedding_model.embed_documents(documents)

    # ==========================================================
    # Embed Single Chunk
    # ==========================================================

    def embed_chunk(self, chunk: str) -> List[float]:
        """
        Generate an embedding for a single chunk.

        Parameters
        ----------
        chunk : str
            Document chunk.

        Returns
        -------
        List[float]
            Embedding vector.
        """

        return self.embed_query(chunk)

    # ==========================================================
    # Embed Multiple Chunks
    # ==========================================================

    def embed_chunks(
        self,
        chunks: List[str]
    ) -> List[List[float]]:
        """
        Generate embeddings for multiple chunks.

        Parameters
        ----------
        chunks : List[str]

        Returns
        -------
        List[List[float]]
            Embedding vectors.
        """

        return self.embed_documents(chunks)

    # ==========================================================
    # Get Embedding Dimension
    # ==========================================================

    def get_embedding_dimension(self) -> int:
        """
        Returns the embedding dimension of the loaded model.

        Returns
        -------
        int
            Embedding dimension.
        """

        return self.embedding_model.embedding_dimension()