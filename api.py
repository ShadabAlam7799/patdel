from flask import Flask, render_template, request, send_file, render_template_string
import os
import json
from langchain.embeddings import HuggingFaceBgeEmbeddings
import pinecone

app = Flask(__name__)

@app.route('/search', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form['query']
        query_emb = bge_embeddings.embed_query(query)

        query_response = index.query(top_k=1, 
                                     include_values=False, 
                                     include_metadata=True,
                                     vector=query_emb,)
        key = query_response["matches"][0]["metadata"]["file_name"]

        # Load the document
        with open("patent_files.json", 'r') as read_file:
            doc_content = json.load(read_file)
            doc = doc_content["data"][key]["html_data"]

        # Render the document with the title length
        rendered_doc = render_template_string(doc)
        return rendered_doc

    return render_template('index.html')

if __name__ == '__main__':
    pinecone.init(api_key="c9fa65e7-443c-4c12-bea1-0b835c561d9d", environment="gcp-starter")
    index = pinecone.Index('first-index')

    model_name = "BAAI/bge-small-en-v1.5"
    encode_kwargs = {'normalize_embeddings': True} # set True to compute cosine similarity
    device = "cpu"
    bge_embeddings = HuggingFaceBgeEmbeddings(
        model_name=model_name,
        model_kwargs={'device': device},
        encode_kwargs=encode_kwargs
    )
    dummy = bge_embeddings.embed_query("hello world, lets go")

    host = '0.0.0.0'
    port = 5000
    app.run(debug=True, host=host, port=port)
