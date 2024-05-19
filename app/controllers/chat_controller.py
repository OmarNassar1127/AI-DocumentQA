from flask import Blueprint, request, jsonify
from app.services.meilisearch_service import search_text
from app.services.openai_service import generate_answer
import logging

chat_bp = Blueprint('chat_bp', __name__)

@chat_bp.route('/ask-question', methods=['POST'])
def ask_question():
    data = request.get_json()
    if not data or 'question' not in data:
        return jsonify({"error": "Invalid input"}), 400

    question = data['question']
    results = search_text(question)
    
    if not results:
        return jsonify({"answer": "No relevant sections found in the document."}), 404
    
    context = " ".join([hit['text'] for hit in results])
    
    answer = generate_answer(question, context, results)
    
    return jsonify({"answer": answer})
