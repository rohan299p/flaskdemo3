import ai_component.vector_db_con as vector_db_con
from langchain.embeddings.openai import OpenAIEmbeddings
from ai_component.openaiModel import get_response as response

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    # Process user input and generate a response
    user_input = request.form['user_input']
    res = response(user_input, docsearch)
    return {'response': res[0], 'source': res[1]}
@app.route('/save_report', methods=['POST'])
def save_report():
    report = request.data.decode('utf-8')
    with open('./reports/report.txt', 'a') as file:
        file.write(report + '\n')
    return 'Report saved successfully.'

directory_path = './files'
embeddings = OpenAIEmbeddings() #this embeddin
vector_db_con.connect_pinecone() #calling the c
docsearch = vector_db_con.docsearch(directory_path,embeddings)
if __name__== '__ main__':
    app.run()