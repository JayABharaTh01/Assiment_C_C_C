"""
metadata_extraction.py

Creates metadata for every chunk in each document.

Responsibilities:
    - Generate unique chunk IDs
    - Create metadata for Pinecone
    - Attach metadata to Document objects

Author: Jaya Bharath
"""

from pathlib import Path
from typing import List

from models.document import Document


class MetadataExtractor:
    """
    Generates metadata for every chunk of every document.
    """

    def __init__(self):
        pass

    # ==========================================================
    # Create Metadata for One Document
    # ==========================================================

    def create_document_metadata(
        self,
        document: Document
    ) -> Document:
        """
        Generate metadata for a single document.

        Parameters
        ----------
        document : Document

        Returns
        -------
        Document
        """

        metadata = []

        for index, chunk in enumerate(document.chunks):

            chunk_id = f"{Path(document.filename).stem}_chunk_{index}"

            metadata.append(
                {
                    "chunk_id": chunk_id,
                    "chunk_index": index,
                    "filename": document.filename,
                    "filetype": document.filetype,
                    "source": str(Path("data") / document.filename),
                    "chunk_length": len(chunk),
                    "text": chunk
                }
            )

        document.metadata = metadata

        return document

    # ==========================================================
    # Create Metadata for All Documents
    # ==========================================================

    def create_metadata(
        self,
        documents: List[Document]
    ) -> List[Document]:
        """
        Generate metadata for all documents.

        Parameters
        ----------
        documents : List[Document]

        Returns
        -------
        List[Document]
        """

        processed_documents = []

        for document in documents:

            processed_documents.append(
                self.create_document_metadata(document)
            )

        return processed_documents