import os

class Config:
    SECRET_KEY= os.environ.get('SECRET_KEY') or 'secret_key_here'
    MEILISEARCH_URL = os.environ.get('MEILISEARCH_URL') or 'http://127.0.0.1:7700'
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY') or 'open_ai_api_key_here'

settings = Config()
