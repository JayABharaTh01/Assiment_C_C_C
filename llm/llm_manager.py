"""
llm_manager.py

High-level interface for text generation.
"""

from llm.huggingface_llm import HuggingFaceLLM


class LLMManager:

    def __init__(self):

        self.llm = HuggingFaceLLM()

    def ask(self, prompt):

        return self.llm.generate(prompt)