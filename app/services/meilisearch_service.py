import meilisearch
from config.settings import settings

client = meilisearch.Client(settings.MEILISEARCH_URL)

try:
    index = client.get_index('pdfs')
    print("Index 'pdfs' already exists. Proceeding with existing index.")
except meilisearch.errors.MeiliSearchApiError:
    index = client.create_index('pdfs', {'primaryKey': 'id'})
    print("Index 'pdfs' created successfully with primary key 'id'.")

try:
    index.update_filterable_attributes(['pdf_id'])
    print("Updated filterable attributes to include 'pdf_id'.")
except Exception as e:
    print(f"Error updating filterable attributes: {e}")
    raise

def index_text(text, pdf_id, page_number):
    document = {
        'id': f"{pdf_id}-{page_number}",
        'pdf_id': pdf_id,
        'page_number': page_number,
        'text': text
    }
    response = index.add_documents([document])
    return response

def search_text(query, document_id):
    results = index.search(query, {
        'filter': f'pdf_id = "{document_id}"'
    })
    return results['hits']

def delete_all_documents():
    response = index.delete_all_documents()
    return response
