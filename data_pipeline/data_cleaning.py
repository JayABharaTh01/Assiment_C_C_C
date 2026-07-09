"""
data_cleaning.py

Cleans extracted document text before chunking.

Responsibilities:
    - Remove extra whitespace
    - Remove unwanted characters
    - Normalize line breaks
    - Clean every Document object

Author: Jaya Bharath
"""

import re
from typing import List

from models.document import Document


class DataCleaner:
    """
    Cleans text extracted from documents.
    """

    def __init__(self):
        pass

    # ==========================================================
    # Clean Single Text
    # ==========================================================

    def clean_text(self, text: str) -> str:
        """
        Clean a single text string.

        Parameters
        ----------
        text : str
            Raw extracted text.

        Returns
        -------
        str
            Cleaned text.
        """

        if not text:
            return ""

        # Normalize line endings
        text = text.replace("\r\n", "\n")
        text = text.replace("\r", "\n")

        # Replace tabs with spaces
        text = text.replace("\t", " ")

        # Remove non-printable characters
        text = re.sub(r"[\x00-\x1F\x7F]", " ", text)

        # Remove multiple spaces
        text = re.sub(r"[ ]{2,}", " ", text)

        # Remove multiple blank lines
        text = re.sub(r"\n{2,}", "\n", text)

        # Remove extra whitespace around lines
        text = "\n".join(
            line.strip()
            for line in text.splitlines()
            if line.strip()
        )

        return text.strip()

    # ==========================================================
    # Clean Documents
    # ==========================================================

    def clean_documents(
        self,
        documents: List[Document]
    ) -> List[Document]:
        """
        Clean all documents.

        Parameters
        ----------
        documents : List[Document]

        Returns
        -------
        List[Document]
        """

        cleaned_documents = []

        for document in documents:

            document.content = self.clean_text(
                document.content
            )

            cleaned_documents.append(document)

        return cleaned_documents