"""
pinecone_store.py

Handles all Pinecone operations.

Author: Jaya Bharath
"""

from typing import List, Dict

from vector_store.index_manager import IndexManager


class PineconeStore:
    """
    Pinecone Vector Store.
    """

    def __init__(self):

        self.index = IndexManager().get_index()

    # ==========================================================
    # Upload Documents
    # ==========================================================

    def upsert_documents(
        self,
        embeddings: List[List[float]],
        chunks: List[str],
        metadata: List[Dict],
    ) -> None:
        """
        Upload document chunks into Pinecone.
        """

        vectors = []

        for embedding, chunk, meta in zip(
            embeddings,
            chunks,
            metadata,
        ):

            vectors.append(
                {
                    "id": meta["chunk_id"],
                    "values": embedding,
                    "metadata": {
                        **meta,
                        "text": chunk,
                    },
                }
            )

        self.index.upsert(vectors=vectors)

        print(f"{len(vectors)} vectors uploaded.")

    # ==========================================================
    # Similarity Search
    # ==========================================================

    def similarity_search(
        self,
        query_embedding: List[float],
        top_k: int,
    ):
        """
        Perform semantic search.
        """

        results = self.index.query(
            vector=query_embedding,
            top_k=top_k,
            include_metadata=True,
        )

        return results.matches