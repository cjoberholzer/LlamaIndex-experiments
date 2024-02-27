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


def custom_query_engine(query: str) -> None:
    with open('./data/docs/getting_started/starter_example.md') as f:
        text = f.read()


if __name__ == "__main__":
    user_query = 'What did the author do growing up?'
    custom_query_engine(query=user_query)
