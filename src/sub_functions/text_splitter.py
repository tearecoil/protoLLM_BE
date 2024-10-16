from langchain_text_splitters import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

import os

def process_text(text):
    #split text into chunks
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size = 1500,
        chunk_overlap = 50,
        length_function = len
    )
    chunks = text_splitter.split_text(text)

    #convert chunks to embeddings
    embeddings = OpenAIEmbeddings(openai_api_key = os.environ.get('OPENAI_API_KEY'))
    knowledge_base = FAISS.from_texts(chunks, embeddings)
    return knowledge_base