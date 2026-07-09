"""
pipeline.py

Main data processing pipeline.

Pipeline Flow:

    Read Documents
            │
            ▼
      Clean Documents
            │
            ▼
      Chunk Documents
            │
            ▼
     Extract Metadata
            │
            ▼
     Return Documents

Author: Jaya Bharath
"""

from typing import List

from models.document import Document

from data_pipeline.data_read import DataReader
from data_pipeline.data_cleaning import DataCleaner
from data_pipeline.data_chunking import DataChunker
from data_pipeline.metadata_extraction import MetadataExtractor

from utils.config import (
    CHUNK_SIZE,
    CHUNK_OVERLAP
)


class DataPipeline:
    """
    Complete data processing pipeline.

    Executes the following steps:

        1. Read documents
        2. Clean text
        3. Split into chunks
        4. Generate metadata

    Returns
    -------
    List[Document]
    """

    def __init__(self):

        self.reader = DataReader()

        self.cleaner = DataCleaner()

        self.chunker = DataChunker(
            chunk_size=CHUNK_SIZE,
            overlap=CHUNK_OVERLAP
        )

        self.metadata_extractor = MetadataExtractor()

    # ==========================================================
    # Execute Complete Pipeline
    # ==========================================================

    def run(self) -> List[Document]:
        """
        Execute the complete pipeline.

        Returns
        -------
        List[Document]
        """

        print("=" * 60)
        print("Starting Data Pipeline")
        print("=" * 60)

        # ------------------------------------------------------
        # Step 1 : Read Documents
        # ------------------------------------------------------

        documents = self.reader.read_documents()

        print(f"Documents Read       : {len(documents)}")

        # ------------------------------------------------------
        # Step 2 : Clean Documents
        # ------------------------------------------------------

        documents = self.cleaner.clean_documents(documents)

        print("Documents Cleaned    : Completed")

        # ------------------------------------------------------
        # Step 3 : Chunk Documents
        # ------------------------------------------------------

        documents = self.chunker.chunk_documents(documents)

        total_chunks = sum(
            document.number_of_chunks()
            for document in documents
        )

        print(f"Total Chunks Created : {total_chunks}")

        # ------------------------------------------------------
        # Step 4 : Metadata Extraction
        # ------------------------------------------------------

        documents = self.metadata_extractor.create_metadata(
            documents
        )

        print("Metadata Generated   : Completed")

        print("=" * 60)
        print("Data Pipeline Finished Successfully")
        print("=" * 60)

        return documents