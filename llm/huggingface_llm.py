# """
# huggingface_llm.py

# Loads and runs a Hugging Face language model.
# """

# from transformers import pipeline

# from utils.config import (
#     LLM_MODEL,
#     LLM_MAX_NEW_TOKENS,
#     LLM_TEMPERATURE,
#     LLM_DO_SAMPLE
# )


# class HuggingFaceLLM:

#     def __init__(self):

#         print(f"Loading LLM : {LLM_MODEL}")

#         self.generator = pipeline(
#             task="text2text-generation",
#             model=LLM_MODEL
#         )

#     def generate(self, prompt: str):

#         response = self.generator(
#             prompt,
#             max_new_tokens=LLM_MAX_NEW_TOKENS,
#             temperature=LLM_TEMPERATURE,
#             do_sample=LLM_DO_SAMPLE
#         )

#         return response[0]["generated_text"]