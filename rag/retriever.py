"""
retriever.py

Retrieves the most relevant chunks from Pinecone.
"""

from embeddings.embedding_manager import EmbeddingManager
from vector_store.vector_manager import VectorManager

from utils.config import TOP_K


class Retriever:

    def __init__(self):

        self.embedder = EmbeddingManager()

        self.vector_db = VectorManager()

    def retrieve(
        self,
        query: str,
        top_k: int = TOP_K
    ):

        query_embedding = self.embedder.embed_chunk(query)

        results = self.vector_db.search(
            query_embedding=query_embedding,
            top_k=top_k
        )

        return results