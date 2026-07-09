from data_pipeline.pipeline import DataPipeline
from embeddings.embedding_manager import EmbeddingManager
from vector_store.vector_manager import VectorManager


pipeline = DataPipeline()

documents = pipeline.run()

embedder = EmbeddingManager()

manager = VectorManager()

dimension = len(
    embedder.embed_chunk("Hello")
)

manager.initialize(dimension)

for doc_idx, doc in enumerate(documents):

    embeddings = embedder.embed_chunks(
        doc["chunks"]
    )

    # Create metadata for each chunk
    metadata = [
        {
            "chunk_id": f"{doc['filename']}_chunk_{i}",
            "filename": doc["filename"],
            "filetype": doc["filetype"],
            "chunk_index": i
        }
        for i in range(len(doc["chunks"]))
    ]

    manager.upload(
        embeddings,
        doc["chunks"],
        metadata
    )

print("✓ All documents processed and uploaded to vector store!")

print("Completed.")


from rag.rag_pipeline import RAGPipeline


def main():

    chatbot = RAGPipeline()

    while True:

        question = input("\nAsk : ")

        if question.lower() == "exit":
            break

        response = chatbot.ask(question)

        print("\nAnswer\n")

        print(response["answer"])

        print("\nSources\n")

        for source in response["sources"]:

            print(source.metadata["filename"])


if __name__ == "__main__":
    main()