import os
from flask import Blueprint, request, jsonify
from app.services.pdf_service import extract_text
from app.services.meilisearch_service import index_text, delete_all_documents
import logging

pdf_bp = Blueprint('pdf', __name__)

@pdf_bp.route('/index-pdf', methods=['POST'])
def index_pdf():
    data = request.get_json()
    pdf_filename = data.get('pdf_filename')
    
    pdf_path = os.path.join(os.path.dirname(__file__), '..', '..', 'pdfs', pdf_filename)
    pdf_path = os.path.abspath(pdf_path)
    
    logging.debug(f"Extracting text from PDF: {pdf_path}")
    pdf_text = extract_text(pdf_path)
    
    if not pdf_text:
        logging.error(f"Failed to extract text from PDF: {pdf_path}")
        return jsonify({"error": "Failed to extract text from PDF"}), 400

    pdf_id = pdf_filename.split('.')[0]
    
    for page_number, page_text in enumerate(pdf_text):
        index_text(page_text, pdf_id, page_number + 1)
    
    return jsonify({"message": "PDF indexed successfully"}), 200

@pdf_bp.route('/delete-documents', methods=['DELETE'])
def delete_documents():
    try:
        response = delete_all_documents()
        return jsonify({"message": "All documents deleted successfully", "status": response}), 200
    except Exception as e:
        logging.error(f"Error deleting documents: {e}")
        return jsonify({"error": "Failed to delete documents"}), 500