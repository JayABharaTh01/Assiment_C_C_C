"""
data_chunking.py

Splits cleaned document text into overlapping chunks.

Pipeline:

Cleaned Document
        │
        ▼
Chunk Text
        │
        ▼
Store Chunks in Document

Author: Jaya Bharath
"""

from typing import List

from models.document import Document


class DataChunker:
    """
    Splits document text into overlapping chunks.
    """

    def __init__(
        self,
        chunk_size: int = 500,
        overlap: int = 50
    ):
        """
        Initialize the chunker.

        Parameters
        ----------
        chunk_size : int
            Maximum characters per chunk.

        overlap : int
            Number of overlapping characters.
        """

        self.chunk_size = chunk_size
        self.overlap = overlap

    # ==========================================================
    # Chunk Single Text
    # ==========================================================

    def chunk_text(self, text: str) -> List[str]:
        """
        Split text into overlapping chunks.

        Parameters
        ----------
        text : str

        Returns
        -------
        List[str]
        """

        if not text.strip():
            return []

        chunks = []

        start = 0
        text_length = len(text)

        while start < text_length:

            end = min(
                start + self.chunk_size,
                text_length
            )

            chunk = text[start:end].strip()

            if chunk:
                chunks.append(chunk)

            if end >= text_length:
                break

            start = end - self.overlap

        return chunks

    # ==========================================================
    # Chunk Documents
    # ==========================================================

    def chunk_documents(
        self,
        documents: List[Document]
    ) -> List[Document]:
        """
        Chunk all documents.

        Parameters
        ----------
        documents : List[Document]

        Returns
        -------
        List[Document]
        """

        processed_documents = []

        for document in documents:

            document.clear_chunks()

            chunks = self.chunk_text(
                document.content
            )

            document.add_chunks(chunks)

            processed_documents.append(document)

        return processed_documents