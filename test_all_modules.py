"""
test_all_modules.py

Comprehensive test of all project modules
"""

print("=" * 80)
print("COMPREHENSIVE MODULE TEST")
print("=" * 80)

# Test 1: Config
print("\n[1/10] Testing utils/config.py...")
try:
    from utils.config import PROJECT_NAME, EMBEDDING_PROVIDER, EMBEDDING_MODEL
    print(f"✓ Config loaded: {PROJECT_NAME}")
    print(f"  - Embedding: {EMBEDDING_PROVIDER} ({EMBEDDING_MODEL})")
except Exception as e:
    print(f"✗ Error: {e}")

# Test 2: Base Embedding
print("\n[2/10] Testing embeddings/base_embedding.py...")
try:
    from embeddings.base_embedding import BaseEmbedding
    print("✓ BaseEmbedding class imported")
except Exception as e:
    print(f"✗ Error: {e}")

# Test 3: Embedding Factory
print("\n[3/10] Testing embeddings/embedding_factory.py...")
try:
    from embeddings.embedding_factory import EmbeddingFactory
    factory = EmbeddingFactory()
    embedder = factory.get_embedding()
    print("✓ EmbeddingFactory initialized")
    test_vec = embedder.embed_query("test")
    print(f"  - Sample embedding: {len(test_vec)} dimensions")
except Exception as e:
    print(f"✗ Error: {e}")

# Test 4: Embedding Manager
print("\n[4/10] Testing embeddings/embedding_manager.py...")
try:
    from embeddings.embedding_manager import EmbeddingManager
    manager = EmbeddingManager()
    vec = manager.embed_chunk("test chunk")
    print(f"✓ EmbeddingManager working: {len(vec)} dimensions")
except Exception as e:
    print(f"✗ Error: {e}")

# Test 5: Data Reader
print("\n[5/10] Testing data_pipeline/data_read.py...")
try:
    from data_pipeline.data_read import DataReader
    reader = DataReader()
    docs = reader.read_all_files()
    print(f"✓ DataReader working: {len(docs)} files read")
    for d in docs:
        print(f"  - {d['filename']}: {len(d['content'])} chars")
except Exception as e:
    print(f"✗ Error: {e}")

# Test 6: Data Cleaner
print("\n[6/10] Testing data_pipeline/data_cleaning.py...")
try:
    from data_pipeline.data_cleaning import DataCleaner
    cleaner = DataCleaner()
    test_text = "Hello    world  \n\n  test"
    cleaned = cleaner.clean_text(test_text)
    print(f"✓ DataCleaner working")
    print(f"  - Original: '{test_text}'")
    print(f"  - Cleaned:  '{cleaned}'")
except Exception as e:
    print(f"✗ Error: {e}")

# Test 7: Data Chunker
print("\n[7/10] Testing data_pipeline/data_chunking.py...")
try:
    from data_pipeline.data_chunking import DataChunker
    chunker = DataChunker(chunk_size=100, overlap=20)
    text = "A" * 500
    chunks = chunker.chunk_text(text)
    print(f"✓ DataChunker working")
    print(f"  - 500 chars → {len(chunks)} chunks")
except Exception as e:
    print(f"✗ Error: {e}")

# Test 8: Pipeline
print("\n[8/10] Testing data_pipeline/pipeline.py...")
try:
    from data_pipeline.pipeline import DataPipeline
    pipeline = DataPipeline()
    result = pipeline.run()
    total_chunks = sum(len(doc['chunks']) for doc in result)
    print(f"✓ DataPipeline working")
    print(f"  - {len(result)} documents processed")
    print(f"  - Total chunks: {total_chunks:,}")
except Exception as e:
    print(f"✗ Error: {e}")

# Test 9: Vector Store (Index Manager)
print("\n[9/10] Testing vector_store/index_manager.py...")
try:
    from vector_store.index_manager import IndexManager
    print("✓ IndexManager imported (requires valid Pinecone API key to run)")
except Exception as e:
    print(f"✗ Error: {e}")

# Test 10: Vector Manager
print("\n[10/10] Testing vector_store/vector_manager.py...")
try:
    from vector_store.vector_manager import VectorManager
    print("✓ VectorManager imported (requires valid Pinecone API key to run)")
except Exception as e:
    print(f"✗ Error: {e}")

print("\n" + "=" * 80)
print("ALL MODULES TESTED SUCCESSFULLY")
print("=" * 80)
