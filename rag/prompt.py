"""
prompt.py

Creates prompts for the LLM.
"""


class PromptBuilder:

    def build_prompt(
        self,
        question,
        retrieved_chunks
    ):

        context = ""

        for chunk in retrieved_chunks:

            context += chunk.metadata["text"]

            context += "\n\n"

        prompt = f"""
You are an intelligent customer complaint assistant.

Use ONLY the context below to answer the user's question.

If the answer is not available, respond:

"I couldn't find relevant information."

Context:

{context}

Question:

{question}

Answer:
"""

        return prompt