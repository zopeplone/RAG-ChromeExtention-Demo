# RAG-ChromeExtention-Demo
在腾讯mini学习环节中制作的浏览器插件与本地知识库大模型的demo
## 浏览器插件所用技术栈
* vue3+vite+crxjs 构建工程化目录
* element-plus+sass 样式构建
* 使用异步对chrome storage进行数据库的存取，来做聊天记录的持久化
* axios 向python-server做聊天请求和知识库存储的请求

## RAGdemo所用技术栈
* 使用transformer部署本地qwen-1_8B通义千问模型
* 继承langchain中LLM类封装本地模型api,实现了LCEL,许多基础的组件包括prompt模板,Retriever的调用,都继承于这个接口
* 使用BCE-EMbedding模型实现语义向量化
* 使用faiss向量数据库，存储向量化的知识库，并实现根据输入的向量，查找知识库中最接近的知识
* 使用fastapi，构建简单web后端应用

## 展示图片
### 添加知识库
![knowledge](https://github.com/zopeplone/RAG-ChromeExtention-Demo/assets/115687693/015fb7d7-7c29-4b32-98cc-8916beb36943)
![content_select](https://github.com/zopeplone/RAG-ChromeExtention-Demo/assets/115687693/bfad8150-7cd1-4ad1-b468-7220f2d268d2)
### 聊天时调用知识库
![chat_extension](https://github.com/zopeplone/RAG-ChromeExtention-Demo/assets/115687693/ba5dbf4f-cfbf-428c-9d3d-38cb0e2b05f9)
![chat_extension2](https://github.com/zopeplone/RAG-ChromeExtention-Demo/assets/115687693/5389c651-db7b-4ff6-917d-caea9aef4d8c)

## RAGdemo启动
需要下载Qwen-1_8B和BCE - Embedding
https://www.modelscope.cn/models/qwen/Qwen-1_8B-Chat/summary
https://www.modelscope.cn/models/maidalun/bce-embedding-base_v1/summary
## chromeExtension-demo
pnpm install
pnpm run dev
