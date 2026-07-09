"""
huggingface_embedding.py

Sentence Transformer embedding implementation.

Author: Jaya Bharath
"""

from typing import List

from sentence_transformers import SentenceTransformer

from embeddings.base_embedding import BaseEmbedding

from utils.config import (
    EMBEDDING_MODEL,
    EMBEDDING_DEVICE,
    EMBEDDING_BATCH_SIZE,
    NORMALIZE_EMBEDDINGS,
)


class HuggingFaceEmbedding(BaseEmbedding):
    """
    Sentence Transformer embedding model.
    """

    def __init__(self):
        self.model = None
        self.load_model()

    # ==========================================================
    # Load Model
    # ==========================================================

    def load_model(self) -> None:
        """
        Load the Sentence Transformer model.
        """

        print(f"Loading Embedding Model : {EMBEDDING_MODEL}")

        self.model = SentenceTransformer(
            EMBEDDING_MODEL,
            device=EMBEDDING_DEVICE
        )

        print("Embedding Model Loaded Successfully.")

    # ==========================================================
    # Embed Query
    # ==========================================================

    def embed_query(self, text: str) -> List[float]:
        """
        Generate embedding for a user query.
        """

        embedding = self.model.encode(
            text,
            normalize_embeddings=NORMALIZE_EMBEDDINGS,
            convert_to_numpy=True
        )

        return embedding.tolist()

    # ==========================================================
    # Embed Documents
    # ==========================================================

    def embed_documents(
        self,
        texts: List[str]
    ) -> List[List[float]]:
        """
        Generate embeddings for multiple document chunks.
        """

        embeddings = self.model.encode(
            texts,
            batch_size=EMBEDDING_BATCH_SIZE,
            normalize_embeddings=NORMALIZE_EMBEDDINGS,
            convert_to_numpy=True,
            show_progress_bar=True
        )

        return embeddings.tolist()

    # ==========================================================
    # Embedding Dimension
    # ==========================================================

    def embedding_dimension(self) -> int:
        """
        Return embedding dimension.
        """

        return self.model.get_sentence_embedding_dimension()