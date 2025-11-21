Patent Search Engine

A Flask-based web application that enables semantic search through patent documents using vector embeddings and Pinecone vector database.

Overview

This project implements a semantic search engine that allows users to query patent documents using natural language. Instead of traditional keyword matching, it uses machine learning embeddings to find the most semantically relevant patent documents based on the user's query.

Features

· Semantic Search: Find patents based on conceptual similarity rather than exact keyword matches
· Web Interface: User-friendly HTML interface for submitting queries
· Vector Database: Uses Pinecone for efficient similarity search
· Fast Embeddings: Leverages BAAI/bge-small-en-v1.5 model for text embeddings
· Document Rendering: Displays patent documents in HTML format

Architecture

Components

1. Flask Web Server: Handles HTTP requests and serves the web interface
2. Embedding Model: BAAI/bge-small-en-v1.5 from HuggingFace for generating text embeddings
3. Pinecone Vector Database: Stores and queries document embeddings
4. Patent Document Storage: JSON file containing patent HTML data

Workflow

1. User submits a query through the web interface
2. Query is converted to vector embeddings using the BGE model
3. Pinecone performs similarity search to find the most relevant patent
4. Corresponding patent document is retrieved from the JSON storage
5. Patent HTML content is rendered and returned to the user

Installation & Setup

Prerequisites

```bash
pip install flask langchain pinecone-client
```

Configuration

1. Pinecone Setup:
   · Sign up for Pinecone at https://pinecone.io
   · Create an index named 'first-index'
   · Replace the API key in the code with your own
2. Patent Data:
   · Ensure patent_files.json exists in the project directory
   · JSON structure should contain patent data with HTML content

Usage

Running the Application

```bash
python app.py
```

The application will:

· Initialize the embedding model
· Connect to Pinecone vector database
· Open the web browser automatically
· Start the Flask server on http://127.0.0.1:5000

API Endpoints

GET /search

· Serves the main search interface

POST /search

· Accepts search queries in JSON or form format
· Returns the most relevant patent document

Query Formats

JSON:

```json
{
  "query": "your search terms"
}
```

Form Data:

```
query=your+search+terms
```

Code Structure

```python
# Key Components:
- Flask app configuration
- Pinecone initialization
- BGE embeddings model setup
- Search route handling
- Document retrieval and rendering
```

Dependencies

· Flask: Web framework
· LangChain: ML model integration
· Pinecone: Vector database
· HuggingFace Transformers: Embedding models

Model Details

· Model: BAAI/bge-small-en-v1.5
· Device: CPU (configurable)
· Normalization: Cosine similarity enabled
· Warmup: Initial query to load model

Security Notes

⚠️ Important: The current code contains hardcoded API credentials. For production use:

· Store API keys in environment variables
· Use proper secret management
· Remove debug mode in production
· Validate and sanitize all user inputs

Potential Enhancements

1. Multiple Results: Return top-k patents instead of just one
2. Pagination: Handle large result sets
3. Caching: Implement response caching for frequent queries
4. Error Handling: Better error messages and edge case handling
5. Authentication: Add user authentication and authorization
6. Deployment: Docker containerization for easy deployment

File Structure

```
project/
├── app.py                 # Main application file
├── templates/
│   └── index.html        # Search interface template
└── patent_files.json     # Patent documents database
```

License

This project is intended for demonstration purposes. Ensure you have proper licensing for the patent data and comply with all relevant terms of service for the APIs and models used.
