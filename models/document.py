"""
document.py

Represents a processed document throughout the RAG pipeline.

Pipeline:

Read File
    │
    ▼
Clean Text
    │
    ▼
Chunk Text
    │
    ▼
Metadata
    │
    ▼
Embedding

Author: Jaya Bharath
"""

from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class Document:
    """
    Represents a single processed document.
    """

    filename: str
    filetype: str
    content: str

    chunks: List[str] = field(default_factory=list)

    metadata: List[Dict] = field(default_factory=list)

    # ==========================================================
    # Chunk Operations
    # ==========================================================

    def add_chunk(self, chunk: str) -> None:
        """
        Add a chunk.
        """

        self.chunks.append(chunk)

    def add_chunks(self, chunks: List[str]) -> None:
        """
        Add multiple chunks.
        """

        self.chunks.extend(chunks)

    def number_of_chunks(self) -> int:
        """
        Return total number of chunks.
        """

        return len(self.chunks)

    # ==========================================================
    # Metadata Operations
    # ==========================================================

    def add_metadata(self, metadata: Dict) -> None:
        """
        Add metadata.
        """

        self.metadata.append(metadata)

    def add_all_metadata(
        self,
        metadata: List[Dict]
    ) -> None:
        """
        Add multiple metadata entries.
        """

        self.metadata.extend(metadata)

    # ==========================================================
    # Utility
    # ==========================================================

    def clear_chunks(self) -> None:
        """
        Remove all chunks.
        """

        self.chunks.clear()

    def clear_metadata(self) -> None:
        """
        Remove all metadata.
        """

        self.metadata.clear()

    def to_dict(self) -> Dict:
        """
        Convert to dictionary.
        """

        return {
            "filename": self.filename,
            "filetype": self.filetype,
            "content": self.content,
            "chunks": self.chunks,
            "metadata": self.metadata,
        }

    def __repr__(self) -> str:

        return (
            f"Document("
            f"filename='{self.filename}', "
            f"chunks={len(self.chunks)}, "
            f"metadata={len(self.metadata)})"
        )