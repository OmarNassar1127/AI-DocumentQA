from flask import Blueprint, request, jsonify
from app.services.meilisearch_service import search_text, get_documents  
from app.services.openai_service import generate_answer, optimize_question
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

chat_bp = Blueprint('chat_bp', __name__)

@chat_bp.route('/ask-question', methods=['POST'])
def ask_question():
    data = request.get_json()
    if not data or 'question' not in data or 'document_id' not in data:
        return jsonify({"error": "Invalid input"}), 400

    question = data['question']
    document_id = data['document_id']
    
    logger.info(f"Original question: {question}")
    
    optimized_question = optimize_question(question)
    
    logger.info(f"Optimized question: {optimized_question}")

    results = search_text(optimized_question, document_id)
    
    if not results:
        return jsonify({"answer": "No relevant sections found in the document."}), 404
    
    context = " ".join([hit['text'] for hit in results])
    
    answer = generate_answer(optimized_question, context, results)
    
    return jsonify({"answer": answer})

@chat_bp.route('/get-documents', methods=['GET'])
def get_docs():
    try:
        documents = get_documents()
        return jsonify(documents)
    except Exception as e:
        return jsonify({"error": "Failed to retrieve documents"}), 500