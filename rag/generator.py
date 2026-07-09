"""
generator.py

Generates answers using the LLM.
"""

from llm.llm_manager import LLMManager


class Generator:

    def __init__(self):

        self.llm = LLMManager()

    def generate(
        self,
        prompt
    ):

        return self.llm.ask(prompt)