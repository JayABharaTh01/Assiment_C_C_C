from vector_store.index_manager import IndexManager


class PineconeStore:

    def __init__(self):

        self.index = IndexManager().get_index()

    def upsert_documents(
        self,
        embeddings,
        chunks,
        metadata
    ):

        vectors = []

        for i in range(len(chunks)):

            vectors.append(
                {
                    "id": metadata[i]["chunk_id"],
                    "values": embeddings[i],
                    "metadata": {
                        "text": chunks[i],
                        **metadata[i]
                    }
                }
            )

        self.index.upsert(vectors=vectors)

        print("Documents uploaded.")

    def similarity_search(
        self,
        query_embedding,
        top_k=5
    ):

        results = self.index.query(
            vector=query_embedding,
            top_k=top_k,
            include_metadata=True
        )

        return results.matches