#!/usr/bin/env python3
from dotenv import load_dotenv
from langchain.chains import RetrievalQA
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.vectorstores import Chroma
from langchain.llms import GPT4All, LlamaCpp
import os
import argparse
import json
from colorama import Fore , Style

import time

load_dotenv()

embeddings_model_name = os.environ.get("EMBEDDINGS_MODEL_NAME")
persist_directory = os.environ.get('PERSIST_DIRECTORY')

model_type = os.environ.get('MODEL_TYPE')
model_path = os.environ.get('MODEL_PATH')
model_n_ctx = os.environ.get('MODEL_N_CTX')
model_n_batch = int(os.environ.get('MODEL_N_BATCH',8))
target_source_chunks = int(os.environ.get('TARGET_SOURCE_CHUNKS',4))

from constants import CHROMA_SETTINGS

# def main():
#     args = parse_arguments()
#     embeddings = HuggingFaceEmbeddings(model_name=embeddings_model_name)
#     db = Chroma(persist_directory=persist_directory, embedding_function=embeddings, client_settings=CHROMA_SETTINGS)
#     retriever = db.as_retriever(search_kwargs={"k": target_source_chunks})
#     callbacks = [] if args.mute_stream else [StreamingStdOutCallbackHandler()]
#     match model_type:
#         case "LlamaCpp":
#             llm = LlamaCpp(model_path=model_path, max_tokens=model_n_ctx, n_batch=model_n_batch, callbacks=callbacks, verbose=False)
#         case "GPT4All":
#             llm = GPT4All(model=model_path, max_tokens=model_n_ctx, backend='gptj', n_batch=model_n_batch, callbacks=callbacks, verbose=False)
#             #llm = GPT4All(model=model_path)
#         case _default:
#             raise Exception(f"Model type {model_type} is not supported. Please choose one of the following: LlamaCpp, GPT4All")
        
#     qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever, return_source_documents= not args.hide_source)
#     while True:
#         query = input("\nEnter a query: ")
#         if query == "exit":
#             break
#         if query.strip() == "":
#             continue
#         start = time.time()
#         res = qa(query)
#         answer, docs = res['result'], [] if args.hide_source else res['source_documents']
#         end = time.time()
#         print("\n\n> Question:")
#         print(query)
#         print(f"\n> Answer (took {round(end - start, 2)} s.):")
#         print(answer)
#         for document in docs:
#             print("\n> " + document.metadata["source"] + ":")
#             print(document.page_content)
def main():
    embeddings = HuggingFaceEmbeddings(model_name=embeddings_model_name)
    db = Chroma(persist_directory=persist_directory, embedding_function=embeddings, client_settings=CHROMA_SETTINGS)
    retriever = db.as_retriever(search_kwargs={"k": target_source_chunks})
    callbacks = [StreamingStdOutCallbackHandler()]
    llm = GPT4All(model=model_path, max_tokens=model_n_ctx, backend='gptj', n_batch=model_n_batch, callbacks=callbacks, verbose=False)
    if llm==None:
        return "Model not downloaded", 400    
    qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever, return_source_documents=True)
    query = input(">Enter your query: ")
    if query!=None and query!="":
        res = qa(query)
        answer, docs = res['result'], res['source_documents']
        
        source_data =[]
        for document in docs:
             source_data.append({"name":document.metadata["source"]})
        print( Fore.GREEN+Style.BRIGHT+answer+Fore.RESET)
        # return jsonify(query=query,answer=answer,source=source_data)
    return "Empty Query",400

def parse_arguments():
    parser = argparse.ArgumentParser(description='privateGPT: Ask questions to your documents without an internet connection, '
                                                 'using the power of LLMs.')
    parser.add_argument("--hide-source", "-S", action='store_true',
                        help='Use this flag to disable printing of source documents used for answers.')

    parser.add_argument("--mute-stream", "-M",
                        action='store_true',
                        help='Use this flag to disable the streaming StdOut callback for LLMs.')

    return parser.parse_args()


if __name__ == "__main__":
    main()