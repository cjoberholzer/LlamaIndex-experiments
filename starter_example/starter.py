import dotenv
import os
from llama_index.core import (VectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage)

"""
Setup
"""
dotenv.load_dotenv('../.env')
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

# logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
# logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

"""
Code starts
"""

PERSIST_DIR = './data/storage'


def llama_index_starter(query: str):
    # check if storage already exists
    if not os.path.exists(PERSIST_DIR):
        print('Building index from scratch')
        # Load the documents and create the index
        documents = SimpleDirectoryReader('data').load_data()
        index = VectorStoreIndex.from_documents(documents)
        # Save the index to disk
        index.storage_context.persist(persist_dir=PERSIST_DIR)
    else:
        print('Loading index from storage')
        # Load the index from disk
        storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
        index = load_index_from_storage(storage_context)

    # Query the index
    query_engine = index.as_query_engine(steaming=True)
    response = query_engine.query(query)
    response.print_response_stream()
    print(response)


if __name__ == "__main__":
    query = 'What did the author do growing up?'
    llama_index_starter(query=query)

