from typing import Union, Annotated
from PyPDF2 import PdfReader
from fastapi import FastAPI, File, UploadFile
from main_functions import read_pdf, ask_query
from services import storage_backend
from models.query import query
from models.current_user import current_user
from pydantic import BaseModel
from langchain_community.vectorstores import FAISS

import PyPDF2

app = FastAPI()
knowledge_base: FAISS
cur_user: current_user

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/setuser")
def set_username(user: current_user):
    global cur_user
    cur_user = user
    # print(cur_user)
 
@app.post("/uploadfile")
async def upload(file: UploadFile = File(...)):
    global knowledge_base
    try:
        # print(file.filename)
        # print(file.size)
        contents = file.file.read()
        # print(1)
        with open(file.filename, 'wb') as f:
            f.write(contents)
            # print(f)
        # print(2)
        knowledge_base = await read_pdf.readPDF(file)
        # print("FROM MAIN")
        # print(knowledge_base)
        # read_pdf.readPDF(file)
        #Save the file to Firebase
        storage_backend.sendPDF(cur_user.name, file.filename)
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()
    # return {"message": f"Successfully uploaded {file.filename}"}
    return {"message": f"Successfully uploaded"}

@app.post("/askquery")
def sendquery(sendquery: query):
    global knowledge_base
    print("FROM ASK QUERY")
    print(knowledge_base)
    if knowledge_base:
        print(1)
        response = ask_query.ask_query(knowledge_base, sendquery)
        print (response)
        return {"message": response}
        # print(sendquery)
        # print(sendquery.name)
        # print(sendquery.data)
    else:
        print("null knowledge base")

@app.post("/multifile")
async def multifille(files: list[UploadFile]):
    for file in files:
        print(len(file))
    return{"state": 200} 