import openai
import os
import ai_component.open_ai_key as open_ai_key
os.environ['OPENAI_ API_ KEY'] = open_ai_key.mykey
from create_logs import log
def get_response(input,docsearch_index): #function to connect wiht openai
    try:
        docs = docsearch_index.similarity_search(input,k=2)
        #uncomment the below comment to see the meta data associated the similar results
        #print(docs[e])
        source = {}
        extracted_result = ''
        for doc in docs:
            extracted_result+=doc.page_content[:]
            if doc.metadata['source'] in source:
                source[doc.metadata['source' ]].append(doc.metadata['page'])
            else:
                source[doc.metadata['source' ]]=[doc.metadata['page']]
        #print(source)
        
        prompt = f"""
        You are an AI assistant. Answer the user queries using only the below information delimited in triple
        Information: ```{extracted_result}```
        """
        messages= [
            {'role':'system','content':prompt},
            {'role':'user','content':input}
        ]
        chat = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages = messages,
            n=3
        )
        chat['source'] = source
        print(chat)
        log(input,chat) #saving the log
        # reply = chat.choices[0].message.content
        answers = []
        for ans in chat.choices:
            answers.append(ans.message.content)
        return [answers,chat['source']]
    except Exception as e:
        raise Exception(f'Error while loading get_response {str(e)}')