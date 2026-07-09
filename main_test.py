"""
main_test.py

Test version that shows pipeline without embedding API calls.
"""

from data_pipeline.pipeline import DataPipeline


def main():
    print("=" * 80)
    print("RUNNING DATA PIPELINE TEST")
    print("=" * 80)

    pipeline = DataPipeline()
    documents = pipeline.run()

    print(f"\nTotal documents processed: {len(documents)}\n")

    for i, doc in enumerate(documents, 1):
        print("=" * 80)
        print(f"Document {i}: {doc['filename']}")
        print(f"File Type: {doc['filetype']}")
        print(f"Number of Chunks: {len(doc['chunks'])}")
        print("-" * 80)
        
        # Show first 3 chunks
        for j, chunk in enumerate(doc['chunks'][:3], 1):
            print(f"\nChunk {j}:")
            print(f"  Length: {len(chunk)} chars")
            print(f"  Preview: {chunk[:100]}...")
        
        if len(doc['chunks']) > 3:
            print(f"\n... and {len(doc['chunks']) - 3} more chunks")


if __name__ == "__main__":
    main()
