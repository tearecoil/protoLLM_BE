from PyPDF2 import PdfReader
from fastapi import UploadFile, File, FastAPI
from langchain_text_splitters import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
# from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
# from sub_functions.text_splitter import *

import os

def process_text(text):
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

async def readPDF(file: UploadFile):
    pdf_reader = PdfReader(file.file)
        #store the pdf text in a var
    text = "" 
    #print(len(pdf_reader.pages))    
    for page in pdf_reader.pages:
        text += page.extract_text()
        #create knowledge base object
    knowledgeBase = process_text(text)
    print(knowledgeBase)
    return knowledgeBase
# async def process_pdf(file: UploadFile):
#     print(file.filename)
#     print(file.size)
#     pdf_reader = PdfReader(file.file)
#     print(len(pdf_reader.pages))
#     # print(3)
#     # Process the PDF from URL or local file
#     # pdf = open(file, 'rb')
#     # print(pdf)
#     # print(4)
#     # Extract text from PDF     
#     # print("pages: ", pdf_reader.pages)
#     # # print(5)
#     # #Vấn đề
#     print(len(pdf_reader.pages))
#     for page in range(pdf_reader.numPages):
#         text += pdf_reader.getPage(page).extractText()   
#     file.close()
#     return {"status": "Processing completed"}    