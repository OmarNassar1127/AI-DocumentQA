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

def index_text(text, pdf_id, page_number):
    document = {
        'id': f"{pdf_id}-{page_number}",
        'pdf_id': pdf_id,
        'page_number': page_number,
        'text': text
    }
    response = client.index('pdfs').add_documents([document], primary_key='id')
    return response

def search_text(query):
    results = client.index('pdfs').search(query)
    return results['hits']
