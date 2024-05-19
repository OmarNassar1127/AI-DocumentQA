DocumentQuery AI
DocumentQuery AI is an advanced document querying system that allows users to extract information from indexed PDF documents. By leveraging Flask, MeiliSearch, and OpenAI's GPT-4, it provides precise, context-aware answers to user queries, including page references. This tool is ideal for research and analysis, enhancing document review with intelligent querying capabilities.

Features
Indexes PDF documents for efficient querying.
Uses RAG (Retrieval-Augmented Generation) techniques for precise information extraction.
Provides context-aware answers, including page numbers.
Built with Flask for a robust web interface.
Requirements
The following packages are required to run DocumentQuery AI:

Flask
openai
PyMuPDF
pdfminer.six
meilisearch
These can be installed via the requirements.txt file.

Installation
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/DocumentQueryAI.git
cd DocumentQueryAI
Create and activate a virtual environment:

bash
Copy code
python3 -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`
Install the required packages:

bash
Copy code
pip install -r requirements.txt
Set up environment variables:

Create a .env file in the project root and add the following environment variables:

env
Copy code
SECRET_KEY=your_secret_key
MEILISEARCH_URL=http://127.0.0.1:7700
OPENAI_API_KEY=your_openai_api_key
Start MeiliSearch:

Download and install MeiliSearch from MeiliSearch documentation.

Start MeiliSearch:

bash
Copy code
./meilisearch
Initialize the MeiliSearch index:

Run the setup_meilisearch.py script to create the index and specify the primary key:

bash
Copy code
python chatbot/app/services/setup_meilisearch.py
Usage
Start the Flask server:

bash
Copy code
python chatbot/run.py
Index a PDF document:

Use the /index-pdf endpoint to index a PDF document. Send a POST request with the pdf_filename:

bash
Copy code
curl -X POST http://127.0.0.1:5000/index-pdf -H "Content-Type: application/json" -d '{"pdf_filename": "example.pdf"}'
Ask a question:

Use the /ask-question endpoint to ask a question about the indexed documents. Send a POST request with the question:

bash
Copy code
curl -X POST http://127.0.0.1:5000/ask-question -H "Content-Type: application/json" -d '{"question": "What is Bitcoin?"}'
Project Structure
arduino
Copy code
DocumentQueryAI/
├── chatbot/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── controllers/
│   │   │   ├── chat_controller.py
│   │   │   ├── pdf_controller.py
│   │   ├── services/
│   │   │   ├── meilisearch_service.py
│   │   │   ├── openai_service.py
│   │   │   ├── pdf_service.py
│   │   │   ├── setup_meilisearch.py
│   ├── run.py
├── pdfs/
│   ├── example.pdf
├── requirements.txt
└── README.md
Contributing
Contributions are welcome! Please open an issue or submit a pull request for any changes or improvements.

License
This project is licensed under the MIT License. See the LICENSE file for details.