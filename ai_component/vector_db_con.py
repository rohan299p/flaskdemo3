import pinecone
import ai_component.pinecone_asset as pinecone_asset
from langchain.vectorstores import Pinecone
from ai_component.create_token import chunk_data
from ai_component.load_file import load_files
index_name = 'project1'
dimension = 1536


def connect_pinecone():
    try:
        pinecone.init(
        api_key = pinecone_asset.api_key,
        environment = pinecone_asset.environment
        )
        print("Connected with Pinecone successfully!")
    except Exception as e:
        raise Exception(f'Error while connecting with pinecone {str(e)}).')
    

def docsearch(directory_path,embeddings):
    try:
        content_list = load_files(directory_path) #loading
        document = []
        for content in content_list:
            for page in content:
                document.extend(chunk_data(page))
        # print(document[0])
        if index_name not in pinecone.list_indexes():
            print('Creating the index...')
            pinecone.create_index(index_name,dimension)
            print("Index Created\nIntialising....")
            return Pinecone.from_documents (document, embeddings, index_name = index_name)
        else:
            print('Index already exists\nLoading the index...')
            return Pinecone.from_existing_index(index_name, embeddings)
    except Exception as e:
        raise Exception(f'Error while creating/ fetching data from pinecone {str(e)}).')
