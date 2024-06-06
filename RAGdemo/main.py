from langchainRAG.chainapi import run_chain_model
from langchainRAG.chatapi import run_chat_model
from threading import Thread


def main():
    chat_thread = Thread(target=run_chat_model)
    chat_thread.start()
    chain_thread = Thread(target=run_chain_model)
    chain_thread.start()


if __name__ == '__main__':
    main()
