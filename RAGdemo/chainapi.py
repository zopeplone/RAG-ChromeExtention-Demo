import sentence_transformers
import uvicorn
from fastapi import FastAPI, Response
from langchain.chains.retrieval_qa.base import RetrievalQA
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pydantic import BaseModel
import uvicorn, json, datetime
import torch
import os
from fastapi.middleware.cors import CORSMiddleware
from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers.generation.utils import GenerationConfig
from langchainRAG.llm_class import MyQwen



app = FastAPI()
model_name = r"./emb/maidalun/bce-embedding-base_v1"
model_kwargs = {'device': 'cpu'}
encode_kwargs = {'normalize_embeddings': False}
embeddings = HuggingFaceEmbeddings(
    model_name=model_name,
    model_kwargs=model_kwargs,
    encode_kwargs=encode_kwargs
)
embeddings.client = sentence_transformers.SentenceTransformer(embeddings.model_name, device='cuda')
# 初始化加载器
text_splitter = RecursiveCharacterTextSplitter(chunk_size=256, chunk_overlap=128)


class Query(BaseModel):
    text: str



@app.post("/ask")
async def chat(query: Query):
    print(query.text)
    llm = MyQwen()
    db = FAISS.load_local('./faiss', embeddings=embeddings, allow_dangerous_deserialization=True)
    retriever = db.as_retriever()
    qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)
    res = qa.invoke(query.text)['result']
    return {"data": res}

@app.post("/addKnowledge")
def addKnowledge(query: Query):
    knowledge = query.text
    split_docs = text_splitter.split_text(knowledge)
    db = FAISS.load_local('./faiss', embeddings=embeddings, allow_dangerous_deserialization=True)
    db.add_texts(split_docs)
    db.save_local("./faiss")

def run_chain_model():
    app.add_middleware(
        CORSMiddleware,
        allow_origins="*",  # 允许访问的源
        allow_credentials=True,  # 支持 cookie
        allow_methods=["*"],  # 允许使用的请求方法
        allow_headers=["*"]  # 允许携带的 Headers
    )
    print('跨域源')
    uvicorn.run(app, host="0.0.0.0", port=7212)
