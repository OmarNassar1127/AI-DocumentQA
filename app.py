import streamlit as st
import requests

# Load custom CSS
def load_css():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# Function to fetch documents from the backend
def fetch_documents():
    response = requests.get('http://127.0.0.1:5000/get-documents', cookies={"session": st.session_state.get("session_cookie")})
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Failed to fetch documents")
        return []

# Function to interact with the AI backend
def chat_with_ai(prompt, document_id):
    response = requests.post('http://127.0.0.1:5000/ask-question', json={'question': prompt, 'document_id': document_id}, cookies={"session": st.session_state.get("session_cookie")})
    return response.json().get('answer', 'Error: No response from server')

# Function to handle user login
def login(username, password):
    response = requests.post('http://127.0.0.1:5000/login', json={'username': username, 'password': password})
    if response.status_code == 200:
        st.session_state.logged_in = True
        st.session_state.username = username
        st.session_state.session_cookie = response.cookies.get('session')
        st.success("Logged in successfully")
    else:
        st.error("Login failed")

# Function to handle user registration
def register(username, password):
    response = requests.post('http://127.0.0.1:5000/register', json={'username': username, 'password': password})
    if response.status_code == 200:
        st.success("User registered successfully")
    else:
        st.error("User registration failed")

# Streamlit app setup
st.title('AI - talk to your documents')

# User authentication
if 'logged_in' not in st.session_state or not st.session_state.logged_in:
    st.sidebar.title("Login / Register")
    option = st.sidebar.selectbox("Choose an option", ["Login", "Register"])

    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")

    if option == "Login":
        if st.sidebar.button("Login"):
            login(username, password)
    elif option == "Register":
        if st.sidebar.button("Register"):
            register(username, password)
else:
    st.sidebar.write(f"Logged in as {st.session_state.username}")
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.session_state.session_cookie = None

# Fetch and display available documents
if 'logged_in' in st.session_state and st.session_state.logged_in:
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