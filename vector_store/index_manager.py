"""
index_manager.py

Handles Pinecone index creation and management.

Author: Jaya Bharath
"""

from pinecone import Pinecone, ServerlessSpec

from utils.config import (
    PINECONE_API_KEY,
    PINECONE_INDEX,
    PINECONE_CLOUD,
    PINECONE_REGION,
)


class IndexManager:
    """
    Manages the Pinecone index.
    """

    def __init__(self):

        self.pc = Pinecone(api_key=PINECONE_API_KEY)

    # ==========================================================
    # Create Index
    # ==========================================================

    def create_index(self, dimension: int):
        """
        Create Pinecone index if it does not exist.
        """

        existing_indexes = self.pc.list_indexes().names()

        if PINECONE_INDEX in existing_indexes:
            print(f"Index '{PINECONE_INDEX}' already exists.")
            return

        self.pc.create_index(
            name=PINECONE_INDEX,
            dimension=dimension,
            metric="cosine",
            spec=ServerlessSpec(
                cloud=PINECONE_CLOUD,
                region=PINECONE_REGION,
            ),
        )

        print(f"Index '{PINECONE_INDEX}' created successfully.")

    # ==========================================================
    # Get Index
    # ==========================================================

    def get_index(self):
        """
        Return Pinecone index instance.
        """

        return self.pc.Index(PINECONE_INDEX)

    # ==========================================================
    # Delete Index
    # ==========================================================

    def delete_index(self):
        """
        Delete Pinecone index.
        """

        existing_indexes = self.pc.list_indexes().names()

        if PINECONE_INDEX in existing_indexes:
            self.pc.delete_index(PINECONE_INDEX)
            print(f"Index '{PINECONE_INDEX}' deleted.")