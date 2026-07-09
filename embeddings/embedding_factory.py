"""
embedding_factory.py

Returns the configured embedding provider.
"""

from embeddings.openai_embedding import OpenAIEmbedding


class EmbeddingFactory:

    @staticmethod
    def get_embedding():
        # OpenAI is the only supported embedding provider
        return OpenAIEmbedding()