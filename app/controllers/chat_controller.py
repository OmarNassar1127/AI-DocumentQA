from flask import Blueprint, request, jsonify, session
from app.services.meilisearch_service import search_text, get_documents
from app.services.openai_service import generate_answer, optimize_question
from app.controllers.db_operations import save_message, register_user, authenticate_user
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

chat_bp = Blueprint('chat_bp', __name__)

@chat_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({"error": "Invalid input"}), 400
    try:
        register_user(username, password)
        return jsonify({"message": "User registered successfully"}), 200
    except Exception as e:
        logger.error(f"Error registering user: {e}")
        return jsonify({"error": "User registration failed"}), 500

@chat_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({"error": "Invalid input"}), 400
    user_id = authenticate_user(username, password)
    if user_id:
        session['user_id'] = user_id
        session.permanent = True
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"error": "Invalid username or password"}), 401

@chat_bp.route('/ask-question', methods=['POST'])
def ask_question():
    if 'user_id' not in session:
        return jsonify({"error": "Unauthorized"}), 401
    
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

    save_message(session['user_id'], 'user', question)
    save_message(session['user_id'], 'assistant', answer)
    
    return jsonify({"answer": answer})

@chat_bp.route('/get-documents', methods=['GET'])
def get_docs():
    try:
        documents = get_documents()
        logger.info(f"Documents retrieved: {documents}")
        return jsonify(documents)
    except Exception as e:
        logger.error(f"Error retrieving documents: {e}")
        return jsonify({"error": "Failed to retrieve documents"}), 500