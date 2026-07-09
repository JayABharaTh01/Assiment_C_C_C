"""
retriever.py

Retrieves the most relevant document chunks from Pinecone.

Flow:
    User Question
            │
            ▼
      Query Embedding
            │
            ▼
      Pinecone Search
            │
            ▼
      Top-K Chunks

Author: Jaya Bharath
"""

from typing import List, Dict

from embeddings.embedding_manager import EmbeddingManager
from vector_store.vector_manager import VectorManager

from utils.config import TOP_K


class Retriever:
    """
    Retrieves relevant document chunks from the vector database.
    """

    def __init__(self):
        """
        Initialize embedding model and vector store.
        """

        self.embedding_manager = EmbeddingManager()
        self.vector_manager = VectorManager()

    # ==========================================================
    # Retrieve Documents
    # ==========================================================

    def retrieve(
        self,
        question: str,
        top_k: int = TOP_K
    ) -> List[Dict]:
        """
        Retrieve the most relevant chunks for a question.

        Parameters
        ----------
        question : str
            User question.

        top_k : int
            Number of chunks to retrieve.

        Returns
        -------
        List[Dict]
            Retrieved chunks with metadata.
        """

        # -----------------------------------------------
        # Generate Query Embedding
        # -----------------------------------------------

        query_embedding = self.embedding_manager.embed_query(
            question
        )

        # -----------------------------------------------
        # Search Pinecone
        # -----------------------------------------------

        results = self.vector_manager.search(
            query_embedding=query_embedding,
            top_k=top_k
        )

        # -----------------------------------------------
        # Format Results
        # -----------------------------------------------

        retrieved_chunks = []

        for match in results:

            retrieved_chunks.append(
                {
                    "id": match.id,
                    "score": float(match.score),
                    "text": match.metadata.get("text", ""),
                    "filename": match.metadata.get("filename", ""),
                    "filetype": match.metadata.get("filetype", ""),
                    "chunk_id": match.metadata.get("chunk_id", ""),
                    "chunk_index": match.metadata.get("chunk_index", 0),
                    "source": match.metadata.get("source", ""),
                    "chunk_length": match.metadata.get("chunk_length", 0),
                }
            )

        return retrieved_chunks