"""
data_read.py

Reads all supported documents from the data folder.

Supported Formats:
- PDF
- CSV
- JSON
- DOCX

Author: Jaya Bharath
"""

from pathlib import Path
import json
import pandas as pd
import fitz  # PyMuPDF
from docx import Document


class DataReader:
    """
    Reads all supported files from the data folder.
    """

    SUPPORTED_EXTENSIONS = {".pdf", ".csv", ".json", ".docx"}

    def __init__(self, data_folder="data"):
        self.data_folder = Path(data_folder)

    # --------------------------------------------------
    # PDF
    # --------------------------------------------------
    def read_pdf(self, filepath):
        text = ""

        with fitz.open(filepath) as pdf:
            for page in pdf:
                text += page.get_text()

        return text

    # --------------------------------------------------
    # CSV
    # --------------------------------------------------
    def read_csv(self, filepath):
        df = pd.read_csv(filepath)

        return df.to_string(index=False)

    # --------------------------------------------------
    # JSON
    # --------------------------------------------------
    def read_json(self, filepath):
        with open(filepath, "r", encoding="utf-8") as file:
            data = json.load(file)

        return json.dumps(data, indent=2)

    # --------------------------------------------------
    # DOCX
    # --------------------------------------------------
    def read_docx(self, filepath):
        doc = Document(filepath)

        text = "\n".join(
            paragraph.text
            for paragraph in doc.paragraphs
        )

        return text

    # --------------------------------------------------
    # Detect File Type
    # --------------------------------------------------
    def read_file(self, filepath):

        extension = filepath.suffix.lower()

        if extension == ".pdf":
            return self.read_pdf(filepath)

        elif extension == ".csv":
            return self.read_csv(filepath)

        elif extension == ".json":
            return self.read_json(filepath)

        elif extension == ".docx":
            return self.read_docx(filepath)

        else:
            raise ValueError(f"Unsupported file: {filepath}")

    # --------------------------------------------------
    # Read Entire data Folder
    # --------------------------------------------------
    def read_all_files(self):

        documents = []

        for file in self.data_folder.iterdir():

            if file.is_file() and file.suffix.lower() in self.SUPPORTED_EXTENSIONS:

                content = self.read_file(file)

                documents.append(
                    {
                        "filename": file.name,
                        "filetype": file.suffix.lower(),
                        "content": content,
                    }
                )

        return documents