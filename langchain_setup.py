import os
from langchain.llms import OpenAI
from config.settings import settings

# Initialize OpenAI with the API key from settings
llm = OpenAI(model_name="gpt-4o", openai_api_key=settings.OPENAI_API_KEY)

def chat_with_ai(prompt):
    response = llm(prompt)
    return response