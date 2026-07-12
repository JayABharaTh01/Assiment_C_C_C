Customer Complaint Chatbot / RAG-based Assistant
===============================================

Version
-------
- v1.0

Overview
--------
This repository implements a Retrieval-Augmented Generation (RAG) pipeline and a small Streamlit dashboard for exploring retail customer service data (orders, returns, customers, and support tickets). The project is designed as a teaching/prototyping workspace for building tool-using agents that combine retrieval from local data sources with an LLM for grounded responses.

Key capabilities implemented
- RAG pipeline that reads documents, cleans text, chunks documents, extracts metadata, and retrieves relevant chunks for question answering.
- Embedding provider abstraction (supports SentenceTransformers or OpenAI embeddings via configuration).
- LLM provider abstraction (OpenAI by default) and a simple generator wrapper.
- A temporary Streamlit dashboard (`streamlit_ui/app.py`) for exploring metrics and previewing dashboard reference images.

Models and configuration
------------------------
- Embedding model: `sentence-transformers/all-MiniLM-L6-v2` (default in `utils/config.py`).
  - Typical embedding dimension (assumed): 384 (model architecture: MiniLM).
  - Embedding batch size: 32 (configurable via `EMBEDDING_BATCH_SIZE`).
- LLM / Chat model: `gpt-4.1-mini` (configured via `OPENAI_CHAT_MODEL` / `LLM_MODEL`).
- LLM provider: `openai` by default, but the code includes a `huggingface_llm` adapter for alternative providers.
- Chunk size: 500 (configurable via `CHUNK_SIZE` in `utils/config.py`).

Data metrics (current workspace)
--------------------------------
The following metrics were calculated by running the data pipeline on the repository data folder:

Files and raw sizes (bytes):

 - customers.csv: 23,068,710 bytes
 - entity_activity_audit_log.csv: 23,068,686 bytes
 - operations_policies.json: 664,551 bytes
 - orders.csv: 23,068,765 bytes
 - returns.csv: 23,068,823 bytes
 - support_tickets.csv: 23,068,848 bytes

Total raw bytes (all data files combined): 116,008,383 bytes (~110.63 MB)

Pipeline run results (most recent execution):

 - Documents read: 6
 - Total chunks created: 256,845

Estimated embedding storage (assumes 384-d float32 vectors):

 - Estimated bytes for embeddings: 394,513,920 bytes
 - Estimated storage: ~376.24 MB

Notes on "before" and "after":
- "Before" refers to the raw CSV/JSON files listed above.
- "After" is represented by the pipeline's logical output (the total number of chunks) and an estimate of the storage required to persist the embedding vectors for those chunks.

Project working flow
--------------------
1. Read raw files from `data/` using `data_pipeline/data_read.py`.
2. Clean and normalize text via `data_pipeline/data_cleaning.py`.
3. Chunk documents into fixed-size pieces (`CHUNK_SIZE`) in `data_pipeline/data_chunking.py`.
4. Extract metadata for each chunk in `data_pipeline/metadata_extraction.py`.
5. Build or load vector store (vector manager / Pinecone adapter) and index embeddings.
6. Use `rag/retriever.py` to fetch relevant chunks for a query.
7. Build prompt with `rag/prompt.py` and generate an answer with `rag/generator.py` (LLM wrapper).
8. Return a `models/response.Response` object to the caller (and optionally show results in the Streamlit dashboard).

Project structure
-----------------

 - main.py (Streamlit entry for the chatbot UI)
 - README.txt (this file)
 - requirements.txt (project dependencies)
 - .env (runtime configuration)
 - data/ (input CSV/JSON files)
 - data_pipeline/
     - data_read.py
     - data_cleaning.py
     - data_chunking.py
     - metadata_extraction.py
     - pipeline.py
 - embeddings/
     - base_embedding.py
     - huggingface_embedding.py
     - openai_embedding.py
     - embedding_manager.py
 - llm/
     - huggingface_llm.py
     - openai_llm.py
     - llm_manager.py
 - rag/
     - retriever.py
     - prompt.py
     - generator.py
     - rag_pipeline.py
 - vector_store/
     - index_manager.py
     - pinecone_store.py
     - vector_manager.py
 - models/
     - document.py
     - response.py
 - utils/
     - config.py
 - streamlit_ui/
     - app.py
     - styles.css
     - assets/ (place screenshots here to preview in the sidebar)

How to run (development)
------------------------
1. Create a Python virtual environment and install dependencies:

   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt

2. Ensure `.env` has required configuration (API keys, etc.). The project supplies sensible defaults for many options in `utils/config.py`.

3. Run the data pipeline (this will print progress and produce chunk counts):

   python -c "from data_pipeline.pipeline import DataPipeline; dp=DataPipeline(); dp.run()"

4. Start the Streamlit dashboard (temporary UI):

   streamlit run streamlit_ui/app.py --server.port 8502

Notes and caveats
-----------------
- The embedding dimension used above is an assumed typical dimension for `all-MiniLM-L6-v2` (384). If you swap to another embedding model, update the dimension and re-calculate embedding storage estimates.
- The pipeline currently runs in-memory and does not persist chunk files or embeddings unless you wire up the vector store (see `vector_store/`).
- The Streamlit dashboard is a temporary visualization layer for quick inspection. Screenshots can be placed into `streamlit_ui/assets/` to preview reference images.

Changes made in this commit
--------------------------
- Added a temporary Streamlit UI under `streamlit_ui/` with a small dashboard and an image preview sidebar.
- Hardened `utils/config.py` to provide safe defaults when environment variables are missing.
- Added `sitecustomize.py` to ensure the repository root is on the Python path for convenient local imports.
- Updated `requirements.txt` to include `plotly` and `Pillow` for dashboard charts and image previews.

Contact / Next steps
--------------------
- If you want the dashboard to resemble the attached example visuals (large KPI tiles, leaderboards, gradient backgrounds), I can:
  - Add a KPI banner and agent leaderboard view in `streamlit_ui/app.py`.
  - Add persisted vector index export (e.g., an output folder or Pinecone index) so embeddings are saved.
  - Provide a small script to export the chunked text and metadata to JSONL for reproducibility.

Committed to branch: main

-----
Generated/updated by development helper (automated edits)
