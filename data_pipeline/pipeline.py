"""
pipeline.py

Orchestrates the data pipeline: read -> clean -> chunk.
"""

from .data_read import DataReader
from .data_cleaning import DataCleaner
from .data_chunking import DataChunker


class DataPipeline:
    """
    Main data pipeline that reads, cleans, and chunks documents.
    """

    def __init__(self, data_folder="data",
                 chunk_size=500,
                 overlap=50):
        self.reader = DataReader(data_folder)
        self.cleaner = DataCleaner()
        self.chunker = DataChunker(chunk_size=chunk_size,
                                   overlap=overlap)

    def run(self):
        """
        Execute the full pipeline: read -> clean -> chunk.
        """

        # Step 1: Read all documents
        documents = self.reader.read_all_files()

        # Step 2: Clean documents
        cleaned_docs = self.cleaner.clean_documents(documents)

        # Step 3: Chunk documents
        chunked_docs = self.chunker.chunk_documents(cleaned_docs)

        return chunked_docs
