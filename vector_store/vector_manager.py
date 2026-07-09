"""
vector_manager.py

High-level interface for vector database operations.

Author: Jaya Bharath
"""

from typing import List, Dict

from vector_store.index_manager import IndexManager
from vector_store.pinecone_store import PineconeStore


class VectorManager:
    """
    High-level vector database manager.
    """

    def __init__(self):

        self.index_manager = IndexManager()
        self.vector_store = PineconeStore()

    # ==========================================================
    # Initialize Index
    # ==========================================================

    def initialize(self, embedding_dimension: int):
        """
        Create Pinecone index.
        """

        self.index_manager.create_index(
            embedding_dimension
        )

    # ==========================================================
    # Upload Vectors
    # ==========================================================

    def upload(
        self,
        embeddings: List[List[float]],
        chunks: List[str],
        metadata: List[Dict],
    ):
        """
        Upload vectors to Pinecone.
        """

        self.vector_store.upsert_documents(
            embeddings=embeddings,
            chunks=chunks,
            metadata=metadata,
        )

    # ==========================================================
    # Search
    # ==========================================================

    def search(
        self,
        query_embedding: List[float],
        top_k: int,
    ):
        """
        Perform similarity search.
        """

        return self.vector_store.similarity_search(
            query_embedding=query_embedding,
            top_k=top_k,
        )