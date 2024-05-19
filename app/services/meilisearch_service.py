import meilisearch
import logging
from config.settings import settings

logging.basicConfig(level=logging.DEBUG)
client = meilisearch.Client(settings.MEILISEARCH_URL)

# Create the index and specify the primary key
try:
    index = client.create_index('pdfs', {'primaryKey': 'id'})
    logging.info("Index created successfully with primary key 'id'.")
except meilisearch.errors.MeiliSearchApiError as e:
    if 'index already exists' in str(e):
        logging.info("Index already exists. Proceeding with existing index.")
    else:
        logging.error(f"Error creating index: {e}")
        raise
except Exception as e:
    if 'index already exists' in str(e):
        logging.info("Index already exists. Proceeding with existing index.")
    else:
        logging.error(f"Error creating index: {e}")
        raise

def index_text(text, pdf_id, page_number):
    document = {
        'id': f"{pdf_id}-{page_number}",
        'pdf_id': pdf_id,
        'page_number': page_number,
        'text': text
    }
    logging.debug(f"Indexing document: {document}")
    response = client.index('pdfs').add_documents([document], primary_key='id')
    logging.debug(f"Indexing response: {response}")
    return response

def search_text(query):
    logging.debug(f"Search query: {query}")
    results = client.index('pdfs').search(query)
    logging.debug(f"Search results: {results}")
    hits = []
    for hit in results['hits']:
        hits.append({
            'text': hit['text'],
            'page_number': hit['page_number']
        })
    return hits
