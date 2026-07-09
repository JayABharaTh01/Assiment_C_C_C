from pinecone import Pinecone, ServerlessSpec

from utils.config import (
    PINECONE_API_KEY,
    PINECONE_INDEX,
    PINECONE_CLOUD,
    PINECONE_REGION,
)


class IndexManager:

    def __init__(self):

        self.pc = Pinecone(api_key=PINECONE_API_KEY)

    def create_index(self, dimension):

        indexes = self.pc.list_indexes().names()

        if PINECONE_INDEX not in indexes:

            self.pc.create_index(
                name=PINECONE_INDEX,
                dimension=dimension,
                metric="cosine",
                spec=ServerlessSpec(
                    cloud=PINECONE_CLOUD,
                    region=PINECONE_REGION
                )
            )

            print(f"{PINECONE_INDEX} created.")

        else:

            print(f"{PINECONE_INDEX} already exists.")

    def get_index(self):

        return self.pc.Index(PINECONE_INDEX)

    def delete_index(self):

        self.pc.delete_index(PINECONE_INDEX)