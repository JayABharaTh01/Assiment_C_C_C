"""
huggingface_embedding.py

Embedding model using Sentence Transformers.
"""

from sentence_transformers import SentenceTransformer
from embeddings.base_embedding import BaseEmbedding
from utils.config import (
    EMBEDDING_MODEL,
    EMBEDDING_DEVICE,
    NORMALIZE_EMBEDDINGS,
)


class HuggingFaceEmbedding(BaseEmbedding):

    def __init__(self):

        print(f"Loading Hugging Face model: {EMBEDDING_MODEL}")

        self.model = SentenceTransformer(
            EMBEDDING_MODEL,
            device=EMBEDDING_DEVICE
        )

    def embed_query(self, text):

        embedding = self.model.encode(
            text,
            normalize_embeddings=NORMALIZE_EMBEDDINGS
        )

        return embedding.tolist()

    def embed_documents(self, texts):

        embeddings = self.model.encode(
            texts,
            batch_size=32,
            normalize_embeddings=NORMALIZE_EMBEDDINGS,
            show_progress_bar=True
        )

        return embeddings.tolist()