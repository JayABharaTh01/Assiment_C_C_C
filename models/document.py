"""
document.py

Data model representing a processed document throughout the RAG pipeline.

Author: Jaya Bharath
"""

from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class Document:
    """
    Represents a single document after processing.

    Attributes:
        filename: Name of the file.
        filetype: Extension of the file (.pdf, .csv, etc.).
        content: Cleaned text extracted from the document.
        chunks: List of text chunks.
        metadata: Metadata associated with each chunk.
    """

    filename: str
    filetype: str
    content: str

    chunks: List[str] = field(default_factory=list)

    metadata: List[Dict] = field(default_factory=list)

    def number_of_chunks(self) -> int:
        """
        Returns the total number of chunks.
        """
        return len(self.chunks)

    def add_chunk(self, chunk: str):
        """
        Add a chunk.
        """
        self.chunks.append(chunk)

    def add_metadata(self, meta: Dict):
        """
        Add metadata.
        """
        self.metadata.append(meta)

    def get_chunk(self, index: int):
        """
        Return a chunk.
        """
        return self.chunks[index]

    def get_metadata(self, index: int):
        """
        Return metadata of a chunk.
        """
        return self.metadata[index]

    def to_dict(self):
        """
        Convert Document object into dictionary.
        """
        return {
            "filename": self.filename,
            "filetype": self.filetype,
            "content": self.content,
            "chunks": self.chunks,
            "metadata": self.metadata,
        }

    def __str__(self):
        return (
            f"Document("
            f"filename='{self.filename}', "
            f"type='{self.filetype}', "
            f"chunks={len(self.chunks)})"
        )