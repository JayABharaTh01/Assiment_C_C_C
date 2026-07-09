"""
llm_manager.py

High-level interface for interacting with the LLM.

Author: Jaya Bharath
"""

from llm.openai_llm import OpenAILLM


class LLMManager:
    """
    High-level LLM Manager.
    """

    def __init__(self):
        """
        Initialize the configured language model.
        """

        self.llm = OpenAILLM()

    # ==========================================================
    # Ask LLM
    # ==========================================================

    def ask(self, prompt: str) -> str:
        """
        Send a prompt to the language model.

        Parameters
        ----------
        prompt : str

        Returns
        -------
        str
        """

        return self.llm.generate(prompt)