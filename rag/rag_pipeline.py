"""
rag_pipeline.py

Complete Retrieval-Augmented Generation (RAG) Pipeline.

Pipeline Flow:

User Question
      │
      ▼
Retriever
      │
      ▼
Relevant Chunks
      │
      ▼
Prompt Builder
      │
      ▼
OpenAI Generator
      │
      ▼
Response Model

Author: Jaya Bharath
"""

import time

from rag.retriever import Retriever
from rag.prompt import PromptBuilder
from rag.generator import Generator

from models.response import Response


class RAGPipeline:
    """
    Complete Retrieval-Augmented Generation Pipeline.
    """

    def __init__(self):
        """
        Initialize all RAG components.
        """

        self.retriever = Retriever()

        self.prompt_builder = PromptBuilder()

        self.generator = Generator()

    # ==========================================================
    # Ask Question
    # ==========================================================

    def ask(self, question: str) -> Response:
        """
        Execute the complete RAG pipeline.

        Parameters
        ----------
        question : str
            User question.

        Returns
        -------
        Response
            Final chatbot response.
        """

        start_time = time.perf_counter()

        # ------------------------------------------------------
        # Retrieve Relevant Chunks
        # ------------------------------------------------------

        retrieved_chunks = self.retriever.retrieve(
            question=question
        )

        # ------------------------------------------------------
        # Build Prompt
        # ------------------------------------------------------

        prompt = self.prompt_builder.build_prompt(
            question=question,
            retrieved_chunks=retrieved_chunks
        )

        # ------------------------------------------------------
        # Generate Answer
        # ------------------------------------------------------

        answer = self.generator.generate(
            prompt=prompt
        )

        # ------------------------------------------------------
        # Processing Time
        # ------------------------------------------------------

        processing_time = round(
            time.perf_counter() - start_time,
            2
        )

        # ------------------------------------------------------
        # Build Response
        # ------------------------------------------------------

        response = Response(
            question=question,
            answer=answer,
            sources=retrieved_chunks,
            processing_time=processing_time,
            retrieved_chunks=len(retrieved_chunks)
        )

        return response