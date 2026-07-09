"""
openai_llm.py

OpenAI LLM implementation.

Author: Jaya Bharath
"""

from openai import OpenAI

from utils.config import (
    OPENAI_API_KEY,
    OPENAI_CHAT_MODEL,
    OPENAI_TEMPERATURE,
    OPENAI_MAX_TOKENS,
)


class OpenAILLM:
    """
    OpenAI Language Model.
    """

    def __init__(self):
        """
        Initialize the OpenAI client.
        """

        self.client = OpenAI(
            api_key=OPENAI_API_KEY
        )

    # ==========================================================
    # Generate Response
    # ==========================================================

    def generate(self, prompt: str) -> str:
        """
        Generate a response from OpenAI.

        Parameters
        ----------
        prompt : str

        Returns
        -------
        str
        """

        response = self.client.chat.completions.create(
            model=OPENAI_CHAT_MODEL,
            temperature=OPENAI_TEMPERATURE,
            max_tokens=OPENAI_MAX_TOKENS,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content.strip()