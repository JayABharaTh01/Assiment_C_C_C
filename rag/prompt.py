"""
prompt.py

Builds prompts for the OpenAI LLM.

Responsibilities:
    - Build context from retrieved chunks
    - Generate a structured prompt
    - Prevent hallucinations by restricting answers
      to the provided context

Author: Jaya Bharath
"""

from typing import List, Dict


class PromptBuilder:
    """
    Builds prompts for Retrieval-Augmented Generation (RAG).
    """

    def __init__(self):
        pass

    # ==========================================================
    # Build Context
    # ==========================================================

    def build_context(
        self,
        retrieved_chunks: List[Dict]
    ) -> str:
        """
        Combine retrieved chunks into a single context string.

        Parameters
        ----------
        retrieved_chunks : List[Dict]

        Returns
        -------
        str
        """

        context_parts = []

        for index, chunk in enumerate(retrieved_chunks, start=1):

            context_parts.append(
                f"""
Document {index}
Filename : {chunk['filename']}
Chunk ID : {chunk['chunk_id']}

Content:
{chunk['text']}
"""
            )

        return "\n".join(context_parts)

    # ==========================================================
    # Build Prompt
    # ==========================================================

    def build_prompt(
        self,
        question: str,
        retrieved_chunks: List[Dict]
    ) -> str:
        """
        Build the final prompt for OpenAI.

        Parameters
        ----------
        question : str

        retrieved_chunks : List[Dict]

        Returns
        -------
        str
        """

        context = self.build_context(
            retrieved_chunks
        )

        prompt = f"""
You are an intelligent AI Customer Complaint Assistant.

Your responsibilities:

1. Answer ONLY using the provided context.

2. Do NOT make up information.

3. If the answer is not found in the context, reply exactly:

"I couldn't find relevant information in the knowledge base."

4. Be professional.

5. Keep answers concise and accurate.

6. If multiple documents contain relevant information,
combine them into a single answer.

============================================================
KNOWLEDGE BASE
============================================================

{context}

============================================================
USER QUESTION
============================================================

{question}

============================================================
FINAL ANSWER
============================================================
"""

        return prompt