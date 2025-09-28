import pytest
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture(scope="session")
def mongo_client():
    """Fixture para criar e fechar a conexão com o MongoDB"""
    client = MongoClient(os.getenv("MONGO_URI"))
    yield client
    client.close()

# @pytest.fixture(scope="function")
# def test_db(mongo_client):
#     """Fixture para fornecer um banco de dados de teste limpo para cada teste"""
#     db = mongo_client["test_burguer_app_db"]
#     db["users"].delete_many({})
#     db["pedidos"].delete_many({})

#     yield db