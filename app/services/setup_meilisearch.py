import meilisearch
from config.settings import settings

client = meilisearch.Client(settings.MEILISEARCH_URL)

try:
    index = client.create_index('pdfs', {'primaryKey': 'id'})
    print("Index created successfully with primary key 'id'.")
except meilisearch.errors.MeiliSearchApiError as e:
    if 'index already exists' in str(e):
        print("Index already exists. Proceeding with existing index.")
    else:
        print(f"Error creating index: {e}")
        raise
except Exception as e:
    if 'index already exists' in str(e):
        print("Index already exists. Proceeding with existing index.")
    else:
        print(f"Error creating index: {e}")
        raise
