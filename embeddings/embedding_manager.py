"""
embedding_manager.py

High-level embedding manager.
"""

from embeddings.embedding_factory import EmbeddingFactory


class EmbeddingManager:

    def __init__(self):

        self.embedding_model = EmbeddingFactory.get_embedding()

    def embed_chunk(self, chunk):

        return self.embedding_model.embed_query(chunk)

    def embed_chunks(self, chunks):

        return self.embedding_model.embed_documents(chunks)