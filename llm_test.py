from llm.llm_manager import LLMManager


llm = LLMManager()

response = llm.ask(
    "Explain what is Artificial Intelligence in 100 words."
)

print(response)