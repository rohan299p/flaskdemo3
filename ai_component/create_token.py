from langchain.text_splitter import CharacterTextSplitter 

def chunk_data(page):
    try:
        text_splitter = CharacterTextSplitter(
            separator='\n',
            chunk_size=9000,
            chunk_overlap = 500,
        )
        metadata = [page.metadata] #storing meta data of each page to reuse
        text_chunks = text_splitter.create_documents ([page.page_content],metadatas = metadata)
        #uncomment the below comment to see the token size
        #print(len(text_chunks [e].page_content)
        return text_chunks
    except Exception as e:
        raise Exception(f"Error in chunk data: {str(e)}")