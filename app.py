import streamlit as st
import requests

# Load custom CSS
def load_css():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# Function to fetch documents from the backend
def fetch_documents():
    response = requests.get('http://127.0.0.1:5000/get-documents')
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Failed to fetch documents")
        return []

# Function to interact with the AI backend
def chat_with_ai(prompt, document_id):
    response = requests.post('http://127.0.0.1:5000/ask-question', json={'question': prompt, 'document_id': document_id})
    return response.json().get('answer', 'Error: No response from server')

# Streamlit app setup
st.title('AI Chatbot with Document Context')

# Fetch and display available documents
document_list = fetch_documents()
if document_list:
    selected_document = st.selectbox("Select Document", document_list)
else:
    st.warning("No documents available")

# Store chat messages in session state
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Input prompt for user question
prompt = st.text_input("Enter your question:")

# Button to send the question
if st.button("Send"):
    if prompt and selected_document:
        # Display the user prompt
        st.session_state.messages.append({'role': 'user', 'content': prompt})
        
        # Get response from the AI
        response = chat_with_ai(prompt, selected_document)
        
        # Display the AI response
        st.session_state.messages.append({'role': 'assistant', 'content': response})

# Display chat messages
st.write('<div class="chat-container">', unsafe_allow_html=True)
for message in st.session_state.messages:
    if message['role'] == 'user':
        st.write(f'<div class="user-message"><b>User:</br> {message["content"]}</div>', unsafe_allow_html=True)
    else:
        st.write(f'<div class="assistant-message"><b>AI:</br> {message["content"]}</div>', unsafe_allow_html=True)
st.write('</div>', unsafe_allow_html=True)