# DocumentQA

DocumentQA is a Flask-based application that leverages AI to provide answers to questions based on the content of indexed PDF documents. Utilizing OpenAI's GPT-4o model for generating answers and Meilisearch for document indexing and retrieval, this project offers a robust solution for querying document contents efficiently.

## Features

- **AI-Powered QA**: Uses OpenAI's GPT-4o model to generate answers based on document content.
- **Document Indexing**: Employs Meilisearch for fast and efficient text indexing and retrieval.
- **PDF Text Extraction**: Utilizes PyMuPDF for extracting text from PDF files.

## Requirements

The project requires the following Python packages:

- Flask
- openai
- PyMuPDF
- pdfminer.six
- meilisearch

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/DocumentQA.git
   cd DocumentQA

2. **Create and Activate a Virtual Environment**:
  python -m venv venv
  source venv/bin/activate # On Windows use `venv\Scripts\activate`

3. **Install the Required Packages**:
  pip install -r requirements.txt

4. **Set Up Environment Variables**:
  SECRET_KEY=your_secret_key
  MEILISEARCH_URL=http://127.0.0.1:7700
  OPENAI_API_KEY=your_openai_api_key

5. **Run Meilisearch**:
  - **Download and Install Meilisearch**: https://www.meilisearch.com/docs/learn/what_is_meilisearch/sdks
  - **Start Meilisearch:**: curl -L https://install.meilisearch.com | sh./meilisearch || curl -L https://install.meilisearch.com | sh and ./meilisearch
  - **PDF Text Extraction**: Utilizes PyMuPDF for extracting text from PDF files.

6. **Run the Setup Script for Meilisearch**:
  python chatbot/app/services/setup_meilisearch.py

7. **Run the Flask Application**:
  flask run


## Usage
  - Index a PDF
  Use the /index-pdf endpoint to index a PDF file. Send a POST request with the pdf_filename in the JSON body:

  json
  {
    "pdf_filename": "example.pdf"
  }
  Ask a Question
  Use the /ask-question endpoint to ask a question. Send a POST request with the question in the JSON body:

  json
  {
    "question": "What is Bitcoin?"
  }
  Example Endpoints
  Index PDF:

  http
  POST /index-pdf
  {
    "pdf_filename": "example.pdf"
  }
  Ask Question:

  http
  POST /ask-question
  {
    "question": "What is Bitcoin?"
  }

  ## License
  This project is licensed under the MIT License.
