import os 
import sys
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__))))
from models.user_model import serialize_user




@pytest.mark.parametrize("entrada,esperado", [ 

    ( 

        { 

            "email": "teste@exemplo.com", 

            "name": "Teste", 

            "address": "Rua Exemplo", 

            "role": "admin" 

        }, 

        { 

            "email": "teste@exemplo.com", 

            "name": "Teste", 

            "address": "Rua Exemplo", 

            "role": "admin" 

        } 

    ), 

    ( 

        { 

            "email": "cliente@site.com", 

            "name": "Cliente", 

            "address": "Rua Cliente" 

        }, 

        { 

            "email": "cliente@site.com", 

            "name": "Cliente", 

            "address": "Rua Cliente", 

            "role": "cliente" 

        } 

    ) 

]) 

def test_serialize_user_parametrizado(entrada, esperado): 
    assert serialize_user(entrada) == esperado 

def test_serialize_user_entrada_invalida(): 
    with pytest.raises(AttributeError): 
        serialize_user("isso não é um dicionário")     