# DocumentQA

DocumentQA is a Flask-based application that leverages AI to provide answers to questions based on the content of indexed PDF documents. Utilizing OpenAI's GPT-4 model for generating answers and Meilisearch for document indexing and retrieval, this project offers a robust solution for querying document contents efficiently.

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
