import sentence_transformers
import uvicorn
from fastapi import FastAPI
from langchain.chains.retrieval_qa.base import RetrievalQA
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from pydantic import BaseModel
import uvicorn, json, datetime
import torch
import os
from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers.generation.utils import GenerationConfig
from langchainRAG.llm_class import MyQwen

app = FastAPI()


class Query(BaseModel):
    text: str


path = "Qwen-1_8B-Chat"
tokenizer = AutoTokenizer.from_pretrained(path, revision='master', trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(path, revision='master', device_map="auto", trust_remote_code=True).eval()

# model = AutoModelForCausalLM.from_pretrained(path, device_map="auto", trust_remote_code=True)
# model.generation_config = GenerationConfig.from_pretrained(path)
@app.post("/chat/")
async def chat(query: Query):
    print(query.text)
    response, history = model.chat(tokenizer, query.text, history=None)
    return {"result": response}


def run_chat_model():
    uvicorn.run(app, host="0.0.0.0", port=7211)
