from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.callbacks import get_openai_callback
from models.query import query
from dotenv import load_dotenv

import os

load_dotenv()

def ask_query(knowledgeBase: FAISS, query: query):
    sent_query = query.data
    docs = knowledgeBase.similarity_search(sent_query)
    llm = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"), model = 'gpt-4o-mini')
    print(os.getenv("OPENAI_API_KEY"))
    chain = load_qa_chain(llm, chain_type="stuff")
    with get_openai_callback() as cost:
        response = chain.invoke(input={"question": sent_query, 
                                     "input_documents": docs})
        print(response)
        print(cost)
        print("-------------------------------------------------------------------------")
        print(response["output_text"])
        temp = str(response["output_text"])
        print("-------------------------------------------------------------------------")
        return temp