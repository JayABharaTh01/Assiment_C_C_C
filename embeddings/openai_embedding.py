"""
openai_embedding.py

OpenAI embedding implementation.
"""

from openai import OpenAI
from embeddings.base_embedding import BaseEmbedding
from utils.config import (
    OPENAI_API_KEY,
)


class OpenAIEmbedding(BaseEmbedding):

    def __init__(self):

        self.client = OpenAI(api_key=OPENAI_API_KEY)

    def embed_query(self, text):

        response = self.client.embeddings.create(
            model="text-embedding-3-small",
            input=text
        )

        return response.data[0].embedding

    def embed_documents(self, texts):

        response = self.client.embeddings.create(
            model="text-embedding-3-small",
            input=texts
        )

        return [item.embedding for item in response.data]