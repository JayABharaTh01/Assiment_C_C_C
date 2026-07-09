"""
data_chunking.py

Splits cleaned text into chunks.
"""

class DataChunker:

    def __init__(self,
                 chunk_size=500,
                 overlap=50):

        self.chunk_size = chunk_size
        self.overlap = overlap

    def chunk_text(self, text):

        chunks = []

        start = 0

        while start < len(text):

            end = start + self.chunk_size

            chunks.append(text[start:end])

            start += self.chunk_size - self.overlap

        return chunks

    def chunk_documents(self, documents):

        chunked_docs = []

        for doc in documents:

            chunks = self.chunk_text(doc["content"])

            chunked_docs.append(
                {
                    **doc,
                    "chunks": chunks
                }
            )

        return chunked_docs