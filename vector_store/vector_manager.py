from vector_store.index_manager import IndexManager
from vector_store.pinecone_store import PineconeStore


class VectorManager:

    def __init__(self):

        self.index_manager = IndexManager()

        self.store = PineconeStore()

    def initialize(self, embedding_dimension):

        self.index_manager.create_index(
            embedding_dimension
        )

    def upload(
        self,
        embeddings,
        chunks,
        metadata
    ):

        self.store.upsert_documents(
            embeddings,
            chunks,
            metadata
        )

    def search(
        self,
        query_embedding,
        top_k=5
    ):

        return self.store.similarity_search(
            query_embedding,
            top_k
        )