"""
rag_pipeline.py

Complete RAG pipeline.
"""

from rag.retriever import Retriever

from rag.prompt import PromptBuilder

from rag.generator import Generator


class RAGPipeline:

    def __init__(self):

        self.retriever = Retriever()

        self.prompt_builder = PromptBuilder()

        self.generator = Generator()

    def ask(
        self,
        question
    ):

        retrieved_chunks = self.retriever.retrieve(question)

        prompt = self.prompt_builder.build_prompt(
            question,
            retrieved_chunks
        )

        answer = self.generator.generate(prompt)

        return {
            "question": question,
            "answer": answer,
            "sources": retrieved_chunks
        }