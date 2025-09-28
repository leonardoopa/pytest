import pytest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.user_model import serialize_user


def test_serialize_user_completo():
    """Test serialization of a complete user object."""
    user = {
        "address": "123 Main St",
        "name": "John Doe",
        "email": "john@example.com",
        "role": "user",
    }
    resultado = serialize_user(user)

    esperado = {
        "address": "123 Main St",
        "name": "John Doe",
        "email": "john@example.com",
        "role": "user",
    }

    assert resultado == esperado


def test_serialize_user_string():
    with pytest.raises(AttributeError):
        serialize_user("string de teste")


def test_serialize_user_dict_none():
    user = {"email": None, "name": None, "address": None, "role": None}
    resultado = serialize_user(user)
    esperado = {"email": None, "name": None, "address": None, "role": None}
