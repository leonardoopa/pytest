import pytest
import os 
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__))))

from models.user_model import serialize_user

@pytest.mark.usefixtures("test_db")
def test_serialize_user(test_db):
    user = {"id": "123", "name": "John Doe", "email": "john@example.com"}
    serialized = serialize_user(user)
    assert serialized == {"id": "123", "name": "John Doe", "email": "john@example.com"}